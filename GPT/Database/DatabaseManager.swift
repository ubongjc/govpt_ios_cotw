//
//  DatabaseManager.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import Foundation
import GRDB
import Combine

class DatabaseManager: ObservableObject {
    static let shared = DatabaseManager()

    private var dbQueue: DatabaseQueue!

    @Published var isInitialized = false

    private init() {
        setupDatabase()
    }

    private func setupDatabase() {
        do {
            let fileManager = FileManager.default
            let documentsPath = try fileManager.url(
                for: .documentDirectory,
                in: .userDomainMask,
                appropriateFor: nil,
                create: true
            )
            let dbPath = documentsPath.appendingPathComponent("gpt.sqlite")

            dbQueue = try DatabaseQueue(path: dbPath.path)

            var migrator = DatabaseMigrator()

            // Migration v1: Create base tables
            migrator.registerMigration("v1") { db in
                try db.create(table: "region") { t in
                    t.column("regionId", .text).primaryKey()
                    t.column("type", .text).notNull()
                    t.column("isoCode", .text).notNull()
                    t.column("name", .text).notNull()
                    t.column("parentRegionId", .text)
                    t.column("shapeRef", .text)
                    t.column("latitude", .double)
                    t.column("longitude", .double)
                    t.column("boundingBoxJSON", .text)
                    // Add these columns in v1 for fresh installs
                    t.column("nextElection", .datetime)
                    t.column("electionSystem", .text)
                }

                try db.create(table: "officeholder") { t in
                    t.column("personId", .text).primaryKey()
                    t.column("name", .text).notNull()
                    t.column("title", .text).notNull()
                    t.column("regionId", .text).notNull()
                        .references("region", onDelete: .cascade)
                    t.column("partyName", .text)
                    t.column("partyURL", .text)
                    t.column("startDate", .datetime)
                    t.column("endDate", .datetime)
                    t.column("officialSiteURL", .text)
                    t.column("photoURL", .text)
                }

                try db.create(table: "promise") { t in
                    t.column("promiseId", .text).primaryKey()
                    t.column("personId", .text).notNull()
                        .references("officeholder", onDelete: .cascade)
                    t.column("regionId", .text).notNull()
                        .references("region", onDelete: .cascade)
                    t.column("dateMade", .datetime).notNull()
                    t.column("context", .text).notNull()
                    t.column("quoteExact", .text).notNull()
                    t.column("summary", .text).notNull()
                    t.column("tagsJSON", .text).notNull()
                    t.column("dueBy", .datetime)
                    t.column("sourcePrimary", .text).notNull()
                    t.column("sourceType", .text).notNull()
                    t.column("policyTagsJSON", .text)
                    t.column("effectInputsJSON", .text)
                }

                try db.create(table: "evidence") { t in
                    t.column("evidenceId", .text).primaryKey()
                    t.column("promiseId", .text).notNull()
                        .references("promise", onDelete: .cascade)
                    t.column("date", .datetime).notNull()
                    t.column("actionType", .text).notNull()
                    t.column("resultValue", .text)
                    t.column("sourcePrimary", .text).notNull()
                    t.column("notes", .text)
                }

                try db.create(table: "status_snapshot") { t in
                    t.column("snapshotId", .text).primaryKey()
                    t.column("promiseId", .text).notNull()
                        .references("promise", onDelete: .cascade)
                    t.column("status", .text).notNull()
                    t.column("score", .double).notNull()
                    t.column("computedAt", .datetime).notNull()
                    t.column("explanation", .text).notNull()
                }

                try db.create(table: "industry") { t in
                    t.column("industryId", .text).primaryKey()
                    t.column("code", .text).notNull()
                    t.column("name", .text).notNull()
                }

                try db.create(table: "policy_tag") { t in
                    t.column("tag", .text).primaryKey()
                    t.column("description", .text)
                }

                try db.create(table: "policy_tag_industry") { t in
                    t.column("tag", .text).notNull()
                        .references("policy_tag", onDelete: .cascade)
                    t.column("industryId", .text).notNull()
                        .references("industry", onDelete: .cascade)
                    t.column("weight", .double).notNull().defaults(to: 1.0)
                    t.primaryKey(["tag", "industryId"])
                }

                try db.create(table: "promise_industry_impact") { t in
                    t.column("promiseId", .text).notNull()
                        .references("promise", onDelete: .cascade)
                    t.column("industryId", .text).notNull()
                        .references("industry", onDelete: .cascade)
                    t.column("direction", .integer).notNull()
                    t.column("impactClass", .text).notNull()
                    t.column("pctLow", .double).notNull()
                    t.column("pctHigh", .double).notNull()
                    t.column("confidence", .double).notNull()
                    t.column("rationale", .text)
                    t.primaryKey(["promiseId", "industryId"])
                }
            }

            // Migration v2: Add election fields
            migrator.registerMigration("v2") { db in
                // Check if columns exist before trying to add them
                let columns = try db.columns(in: "region").map { $0.name }

                if !columns.contains("nextElection") {
                    try db.alter(table: "region") { t in
                        t.add(column: "nextElection", .datetime)
                    }
                }

                if !columns.contains("electionSystem") {
                    try db.alter(table: "region") { t in
                        t.add(column: "electionSystem", .text)
                    }
                }
            }

            // Migration v3: Create FTS5 virtual tables
            migrator.registerMigration("v3") { db in
                // Check if FTS tables already exist
                let ftsRegionsExists = try db.tableExists("fts_regions")
                let ftsPromisesExists = try db.tableExists("fts_promises")

                if !ftsRegionsExists {
                    try db.execute(sql: """
                        CREATE VIRTUAL TABLE fts_regions USING fts5(
                            regionId UNINDEXED,
                            name,
                            isoCode,
                            type,
                            content='region',
                            content_rowid='rowid'
                        )
                    """)

                    // Triggers to keep FTS in sync
                    try db.execute(sql: """
                        CREATE TRIGGER region_ai AFTER INSERT ON region BEGIN
                            INSERT INTO fts_regions(regionId, name, isoCode, type)
                            VALUES (new.regionId, new.name, new.isoCode, new.type);
                        END
                    """)

                    try db.execute(sql: """
                        CREATE TRIGGER region_ad AFTER DELETE ON region BEGIN
                            DELETE FROM fts_regions WHERE regionId = old.regionId;
                        END
                    """)

                    try db.execute(sql: """
                        CREATE TRIGGER region_au AFTER UPDATE ON region BEGIN
                            UPDATE fts_regions
                            SET name = new.name, isoCode = new.isoCode, type = new.type
                            WHERE regionId = new.regionId;
                        END
                    """)
                }

                if !ftsPromisesExists {
                    try db.execute(sql: """
                        CREATE VIRTUAL TABLE fts_promises USING fts5(
                            promiseId UNINDEXED,
                            summary,
                            quoteExact,
                            tags,
                            personName,
                            regionName,
                            content='promise'
                        )
                    """)
                }
            }

            // Migration v4: Fix region schema for databases with missing columns
            migrator.registerMigration("v4") { db in
                // Check if the region table exists and is missing columns
                if try db.tableExists("region") {
                    let columns = try db.columns(in: "region").map { $0.name }

                    if !columns.contains("nextElection") || !columns.contains("electionSystem") {
                        NSLog("⚠️ Region table missing required columns, recreating...")

                        // For simplicity, just drop and recreate since we'll reload seed data anyway
                        try db.drop(table: "region")

                        // Recreate with all columns
                        try db.create(table: "region") { t in
                            t.column("regionId", .text).primaryKey()
                            t.column("type", .text).notNull()
                            t.column("isoCode", .text).notNull()
                            t.column("name", .text).notNull()
                            t.column("parentRegionId", .text)
                            t.column("shapeRef", .text)
                            t.column("latitude", .double)
                            t.column("longitude", .double)
                            t.column("boundingBoxJSON", .text)
                            t.column("nextElection", .datetime)
                            t.column("electionSystem", .text)
                        }

                        NSLog("✅ Region table recreated with new schema")
                    }
                }
            }

            // Migration v5: Add company table for stocks/ETFs/mutual funds
            migrator.registerMigration("v5") { db in
                let tableExists = try db.tableExists("company")
                if !tableExists {
                    try db.create(table: "company") { t in
                        t.column("companyId", .text).primaryKey()
                        t.column("ticker", .text).notNull()
                        t.column("name", .text).notNull()
                        t.column("securityType", .text).notNull()
                        t.column("industryId", .text).notNull()
                            .references("industry", onDelete: .cascade)
                        t.column("exchange", .text)
                        t.column("description", .text)
                    }
                    NSLog("✅ Created company table")
                }
            }

            // Migration v6: Add promise_company_impact table to link companies to specific impacts
            migrator.registerMigration("v6") { db in
                let tableExists = try db.tableExists("promise_company_impact")
                if !tableExists {
                    try db.create(table: "promise_company_impact") { t in
                        t.column("promiseId", .text).notNull()
                        t.column("industryId", .text).notNull()
                        t.column("companyId", .text).notNull()
                            .references("company", onDelete: .cascade)
                        t.column("relevance", .double) // 0.0 to 1.0 score of how relevant this company is
                        t.column("rationale", .text) // Why this company is specifically affected

                        t.foreignKey(["promiseId", "industryId"], references: "promise_industry_impact", onDelete: .cascade)
                        t.primaryKey(["promiseId", "industryId", "companyId"])
                    }
                    NSLog("✅ Created promise_company_impact table")
                }
            }

            try migrator.migrate(dbQueue)

            NSLog("🔄 Migrations complete, loading seed data...")

            // Load seed data
            do {
                try loadSeedData()
                NSLog("✅ Seed data loaded successfully")
            } catch {
                NSLog("❌ Seed data loading error: \(error)")
            }

            DispatchQueue.main.async {
                self.isInitialized = true
                NSLog("✅ Database initialized")
            }

        } catch {
            NSLog("❌ Database setup error: \(error)")
            NSLog("Error details: \(error.localizedDescription)")
        }
    }

    private func loadSeedData() throws {
        // Check if data already exists - check multiple tables to ensure complete data
        let (regionCount, officeholderCount, promiseCount) = try dbQueue.read { db in
            (try Region.fetchCount(db),
             try Officeholder.fetchCount(db),
             try Promise.fetchCount(db))
        }

        // We should have at least 150 regions, 90 officeholders, and 14 promises for complete world data with Ford
        let hasCompleteData = regionCount >= 150 && officeholderCount >= 90 && promiseCount >= 14

        if hasCompleteData {
            NSLog("✅ Database has complete data (\(regionCount) regions, \(officeholderCount) officeholders, \(promiseCount) promises) - skipping seed data load")
            return // Data already loaded
        }

        if regionCount > 0 || officeholderCount > 0 || promiseCount > 0 {
            NSLog("⚠️ Incomplete data detected (\(regionCount) regions, \(officeholderCount) officeholders, \(promiseCount) promises)")
            NSLog("🔄 Clearing incomplete data and reloading...")

            // Clear all existing data
            try dbQueue.write { db in
                try db.execute(sql: "DELETE FROM evidence")
                try db.execute(sql: "DELETE FROM status_snapshot")
                if try db.tableExists("promise_company_impact") {
                    try db.execute(sql: "DELETE FROM promise_company_impact")
                }
                try db.execute(sql: "DELETE FROM promise_industry_impact")
                try db.execute(sql: "DELETE FROM policy_tag_industry")
                try db.execute(sql: "DELETE FROM policy_tag")
                if try db.tableExists("company") {
                    try db.execute(sql: "DELETE FROM company")
                }
                try db.execute(sql: "DELETE FROM industry")
                try db.execute(sql: "DELETE FROM promise")
                try db.execute(sql: "DELETE FROM officeholder")
                try db.execute(sql: "DELETE FROM region")
                NSLog("✅ Cleared all incomplete data")
            }
        }

        NSLog("📥 Loading seed data (database is empty)...")

        // Load seed JSON
        guard let seedURL = Bundle.main.url(forResource: "seed_data", withExtension: "json") else {
            NSLog("❌ Could not find seed_data.json in bundle")
            NSLog("Bundle path: \(Bundle.main.bundlePath)")
            throw NSError(domain: "DatabaseManager", code: 1, userInfo: [NSLocalizedDescriptionKey: "seed_data.json not found in bundle"])
        }

        NSLog("✅ Found seed_data.json at: \(seedURL.path)")

        let seedData = try Data(contentsOf: seedURL)

        NSLog("✅ Read \(seedData.count) bytes from seed_data.json")

        let decoder = JSONDecoder()

        // Custom date decoder that handles multiple formats
        let dateFormatter = ISO8601DateFormatter()
        dateFormatter.formatOptions = [.withInternetDateTime, .withFractionalSeconds]

        decoder.dateDecodingStrategy = .custom { decoder in
            let container = try decoder.singleValueContainer()
            let dateString = try container.decode(String.self)

            // Try ISO8601 with fractional seconds
            if let date = dateFormatter.date(from: dateString) {
                return date
            }

            // Try ISO8601 without fractional seconds
            dateFormatter.formatOptions = [.withInternetDateTime]
            if let date = dateFormatter.date(from: dateString) {
                return date
            }

            // Try basic datetime format
            let basicFormatter = DateFormatter()
            basicFormatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ss'Z'"
            basicFormatter.timeZone = TimeZone(secondsFromGMT: 0)
            if let date = basicFormatter.date(from: dateString) {
                return date
            }

            // Try date-only format (e.g., "2024-07-02")
            let dateOnlyFormatter = DateFormatter()
            dateOnlyFormatter.dateFormat = "yyyy-MM-dd"
            dateOnlyFormatter.timeZone = TimeZone(secondsFromGMT: 0)
            if let date = dateOnlyFormatter.date(from: dateString) {
                return date
            }

            throw DecodingError.dataCorruptedError(in: container, debugDescription: "Cannot decode date string: \(dateString)")
        }

        let seedJSON: SeedData
        do {
            seedJSON = try decoder.decode(SeedData.self, from: seedData)
            NSLog("✅ Successfully decoded seed data")
        } catch {
            NSLog("❌ Could not decode seed_data.json")
            NSLog("❌ Decoding error: \(error)")
            if let decodingError = error as? DecodingError {
                switch decodingError {
                case .keyNotFound(let key, let context):
                    NSLog("Missing key: \(key.stringValue) at \(context.codingPath)")
                case .typeMismatch(let type, let context):
                    NSLog("Type mismatch for type \(type) at \(context.codingPath)")
                case .valueNotFound(let type, let context):
                    NSLog("Value not found for type \(type) at \(context.codingPath)")
                case .dataCorrupted(let context):
                    NSLog("Data corrupted at \(context.codingPath): \(context.debugDescription)")
                @unknown default:
                    NSLog("Unknown decoding error")
                }
            }
            throw error
        }

        NSLog("✅ Decoded seed data: \(seedJSON.regions.count) regions, \(seedJSON.officeholders.count) officeholders")

        try dbQueue.write { db in
            // Insert regions
            NSLog("📝 Inserting \(seedJSON.regions.count) regions...")
            for (index, region) in seedJSON.regions.enumerated() {
                do {
                    try region.insert(db)
                } catch {
                    NSLog("❌ Failed to insert region #\(index): \(region.regionId)")
                    NSLog("   Error: \(error)")
                    throw error
                }
            }
            NSLog("✅ Inserted \(seedJSON.regions.count) regions")

            // Insert officeholders
            NSLog("📝 Inserting \(seedJSON.officeholders.count) officeholders...")
            var skippedOfficeholders = 0
            for (index, officeholder) in seedJSON.officeholders.enumerated() {
                do {
                    try officeholder.insert(db)
                } catch {
                    // Skip officeholders with invalid foreign keys (missing regions)
                    NSLog("⚠️ Skipping officeholder #\(index): \(officeholder.personId) - region '\(officeholder.regionId)' not found")
                    skippedOfficeholders += 1
                    continue
                }
            }
            let insertedOfficeholders = seedJSON.officeholders.count - skippedOfficeholders
            NSLog("✅ Inserted \(insertedOfficeholders) officeholders (skipped \(skippedOfficeholders) with invalid regions)")

            // Insert promises
            NSLog("📝 Inserting \(seedJSON.promises.count) promises...")
            var skippedPromises = 0
            for (index, promise) in seedJSON.promises.enumerated() {
                do {
                    try promise.insert(db)
                } catch {
                    // Skip promises with invalid foreign keys
                    NSLog("⚠️ Skipping promise #\(index): \(promise.promiseId) - invalid personId or regionId")
                    skippedPromises += 1
                    continue
                }
            }
            let insertedPromises = seedJSON.promises.count - skippedPromises
            NSLog("✅ Inserted \(insertedPromises) promises (skipped \(skippedPromises) with invalid references)")

            // Insert evidence
            var skippedEvidence = 0
            for evidence in seedJSON.evidence {
                do {
                    try evidence.insert(db)
                } catch {
                    skippedEvidence += 1
                }
            }
            if skippedEvidence > 0 {
                NSLog("⚠️ Skipped \(skippedEvidence) evidence records with invalid references")
            }

            // Insert status snapshots
            var skippedSnapshots = 0
            for snapshot in seedJSON.statusSnapshots {
                do {
                    try snapshot.insert(db)
                } catch {
                    skippedSnapshots += 1
                }
            }
            if skippedSnapshots > 0 {
                NSLog("⚠️ Skipped \(skippedSnapshots) status snapshots with invalid references")
            }

            // Insert industries
            for industry in seedJSON.industries {
                try industry.insert(db)
            }

            // Insert companies (if present in seed data)
            if let companies = seedJSON.companies {
                var skippedCompanies = 0
                for company in companies {
                    do {
                        try company.insert(db)
                    } catch {
                        skippedCompanies += 1
                    }
                }
                if skippedCompanies > 0 {
                    NSLog("⚠️ Skipped \(skippedCompanies) companies with invalid industry references")
                }
                NSLog("✅ Inserted \(companies.count - skippedCompanies) companies")
            }

            // Insert policy tags
            for tag in seedJSON.policyTags {
                try tag.insert(db)
            }

            // Insert policy tag industries
            var skippedPTI = 0
            for pti in seedJSON.policyTagIndustries {
                do {
                    try pti.insert(db)
                } catch {
                    skippedPTI += 1
                }
            }
            if skippedPTI > 0 {
                NSLog("⚠️ Skipped \(skippedPTI) policy tag industries with invalid references")
            }

            // Insert impacts
            var skippedImpacts = 0
            for impact in seedJSON.promiseIndustryImpacts {
                do {
                    try impact.insert(db)
                } catch {
                    skippedImpacts += 1
                }
            }
            if skippedImpacts > 0 {
                NSLog("⚠️ Skipped \(skippedImpacts) promise industry impacts with invalid references")
            }

            // Insert promise company impacts (if present in seed data)
            if let companyImpacts = seedJSON.promiseCompanyImpacts {
                var skippedCompanyImpacts = 0
                for companyImpact in companyImpacts {
                    do {
                        try companyImpact.insert(db)
                    } catch {
                        skippedCompanyImpacts += 1
                    }
                }
                if skippedCompanyImpacts > 0 {
                    NSLog("⚠️ Skipped \(skippedCompanyImpacts) promise company impacts with invalid references")
                }
                NSLog("✅ Inserted \(companyImpacts.count - skippedCompanyImpacts) promise company impacts")
            }
        }
    }

    // MARK: - Query Methods

    func fetchRegions(ofType type: Region.RegionType? = nil, parentId: String? = nil) throws -> [Region] {
        try dbQueue.read { db in
            var request = Region.all()
            if let type = type {
                request = request.filter(Region.Columns.type == type)
            }
            if let parentId = parentId {
                request = request.filter(Region.Columns.parentRegionId == parentId)
            }
            return try request.fetchAll(db)
        }
    }

    func fetchOfficeholder(byId id: String) throws -> Officeholder? {
        try dbQueue.read { db in
            try Officeholder.filter(Officeholder.Columns.personId == id).fetchOne(db)
        }
    }

    func fetchCurrentOfficeholders(inRegion regionId: String) throws -> [Officeholder] {
        try dbQueue.read { db in
            try Officeholder
                .filter(Officeholder.Columns.regionId == regionId)
                .filter(Officeholder.Columns.endDate == nil)
                .fetchAll(db)
        }
    }

    func fetchPromises(forPerson personId: String) throws -> [Promise] {
        try dbQueue.read { db in
            try Promise
                .filter(Promise.Columns.personId == personId)
                .order(Promise.Columns.dateMade.desc)
                .fetchAll(db)
        }
    }

    func fetchPromise(byId id: String) throws -> Promise? {
        try dbQueue.read { db in
            try Promise.filter(Promise.Columns.promiseId == id).fetchOne(db)
        }
    }

    func fetchEvidence(forPromise promiseId: String) throws -> [Evidence] {
        try dbQueue.read { db in
            try Evidence
                .filter(Evidence.Columns.promiseId == promiseId)
                .order(Evidence.Columns.date.desc)
                .fetchAll(db)
        }
    }

    func fetchStatusSnapshot(forPromise promiseId: String) throws -> StatusSnapshot? {
        try dbQueue.read { db in
            try StatusSnapshot
                .filter(StatusSnapshot.Columns.promiseId == promiseId)
                .order(StatusSnapshot.Columns.computedAt.desc)
                .fetchOne(db)
        }
    }

    func fetchImpacts(forPromise promiseId: String) throws -> [(PromiseIndustryImpact, Industry)] {
        try dbQueue.read { db in
            let impacts = try PromiseIndustryImpact
                .filter(PromiseIndustryImpact.Columns.promiseId == promiseId)
                .fetchAll(db)

            return try impacts.compactMap { impact in
                guard let industry = try Industry
                    .filter(Industry.Columns.industryId == impact.industryId)
                    .fetchOne(db) else {
                    return nil
                }
                return (impact, industry)
            }
        }
    }

    func fetchCompanies(forPromiseId promiseId: String, industryId: String) throws -> [(PromiseCompanyImpact, Company)] {
        try dbQueue.read { db in
            let companyImpacts = try PromiseCompanyImpact
                .filter(PromiseCompanyImpact.Columns.promiseId == promiseId &&
                       PromiseCompanyImpact.Columns.industryId == industryId)
                .fetchAll(db)

            return try companyImpacts.compactMap { companyImpact in
                guard let company = try Company
                    .filter(Company.Columns.companyId == companyImpact.companyId)
                    .fetchOne(db) else {
                    return nil
                }
                return (companyImpact, company)
            }
        }
    }

    func searchRegions(query: String) throws -> [Region] {
        try dbQueue.read { db in
            let sql = """
                SELECT region.* FROM region
                JOIN fts_regions ON region.regionId = fts_regions.regionId
                WHERE fts_regions MATCH ?
                ORDER BY rank
                LIMIT 20
            """
            return try Region.fetchAll(db, sql: sql, arguments: [query])
        }
    }

    func searchPromises(query: String) throws -> [Promise] {
        try dbQueue.read { db in
            let sql = """
                SELECT promise.* FROM promise
                JOIN fts_promises ON promise.promiseId = fts_promises.promiseId
                WHERE fts_promises MATCH ?
                ORDER BY rank
                LIMIT 50
            """
            return try Promise.fetchAll(db, sql: sql, arguments: [query])
        }
    }

    func searchOfficeholders(query: String) throws -> [Officeholder] {
        try dbQueue.read { db in
            let pattern = "%\(query)%"
            return try Officeholder
                .filter(Officeholder.Columns.name.like(pattern) ||
                       Officeholder.Columns.title.like(pattern) ||
                       Officeholder.Columns.partyName.like(pattern))
                .order(Officeholder.Columns.name)
                .limit(50)
                .fetchAll(db)
        }
    }

    func searchCompanies(query: String) throws -> [Company] {
        try dbQueue.read { db in
            let pattern = "%\(query)%"
            return try Company
                .filter(Company.Columns.name.like(pattern) ||
                       Company.Columns.ticker.like(pattern) ||
                       Company.Columns.description.like(pattern))
                .order(Company.Columns.name)
                .limit(50)
                .fetchAll(db)
        }
    }

    // MARK: - Map View Helpers

    func fetchRegion(id: String) -> Region? {
        try? dbQueue.read { db in
            try Region.fetchOne(db, key: id)
        }
    }

    func fetchContinents() -> [Region] {
        (try? dbQueue.read { db in
            try Region.filter(Region.Columns.type == Region.RegionType.continent.rawValue)
                .order(Region.Columns.name)
                .fetchAll(db)
        }) ?? []
    }

    func fetchChildren(of region: Region) -> [Region] {
        (try? dbQueue.read { db in
            try Region.filter(Region.Columns.parentRegionId == region.regionId)
                .order(Region.Columns.name)
                .fetchAll(db)
        }) ?? []
    }

    func fetchCurrentOfficeholder(for region: Region) -> Officeholder? {
        try? dbQueue.read { db in
            try Officeholder
                .filter(Officeholder.Columns.regionId == region.regionId)
                .filter(Officeholder.Columns.endDate == nil)
                .order(Officeholder.Columns.startDate.desc)
                .fetchOne(db)
        }
    }

    func fetchPromisesCount(for region: Region) -> Int {
        (try? dbQueue.read { db in
            try Promise.filter(Promise.Columns.regionId == region.regionId)
                .fetchCount(db)
        }) ?? 0
    }

    func fetchNextElectionDate(for region: Region) -> Date? {
        // Return the nextElection date directly from the region
        return region.nextElection
    }

    // MARK: - Database Reset Method

    func resetDatabase() {
        NSLog("🔄 Manual database reset requested...")
        do {
            // Clear all existing data
            try dbQueue.write { db in
                try db.execute(sql: "DELETE FROM evidence")
                try db.execute(sql: "DELETE FROM status_snapshot")
                try db.execute(sql: "DELETE FROM promise_industry_impact")
                try db.execute(sql: "DELETE FROM policy_tag_industry")
                try db.execute(sql: "DELETE FROM policy_tag")
                try db.execute(sql: "DELETE FROM industry")
                try db.execute(sql: "DELETE FROM promise")
                try db.execute(sql: "DELETE FROM officeholder")
                try db.execute(sql: "DELETE FROM region")
                NSLog("✅ Cleared all data")
            }

            // Reload seed data
            try loadSeedData()
            NSLog("✅ Database reset complete")

            DispatchQueue.main.async {
                self.isInitialized = false
                self.isInitialized = true  // Trigger UI refresh
            }
        } catch {
            NSLog("❌ Database reset error: \(error)")
        }
    }

    // MARK: - Industry Impact Helpers

    func fetchIndustryImpacts(for officeholder: Officeholder) throws -> [(PromiseIndustryImpact, Industry, Promise)] {
        try dbQueue.read { db in
            let sql = """
                SELECT pii.*, i.*, p.*
                FROM promise_industry_impact pii
                JOIN industry i ON pii.industryId = i.industryId
                JOIN promise p ON pii.promiseId = p.promiseId
                WHERE p.personId = ?
                ORDER BY ABS(pii.direction * (pii.pctHigh + pii.pctLow) / 2) DESC
            """

            let rows = try Row.fetchAll(db, sql: sql, arguments: [officeholder.personId])
            return try rows.map { row in
                let impact = try PromiseIndustryImpact(row: row)
                let industry = try Industry(row: row)
                let promise = try Promise(row: row)
                return (impact, industry, promise)
            }
        }
    }

    func fetchAllIndustryImpacts() throws -> [(PromiseIndustryImpact, Industry, Promise, Officeholder)] {
        try dbQueue.read { db in
            let sql = """
                SELECT pii.*, i.*, p.*, o.*
                FROM promise_industry_impact pii
                JOIN industry i ON pii.industryId = i.industryId
                JOIN promise p ON pii.promiseId = p.promiseId
                JOIN officeholder o ON p.personId = o.personId
                ORDER BY ABS(pii.direction * (pii.pctHigh + pii.pctLow) / 2) DESC
            """

            let rows = try Row.fetchAll(db, sql: sql)
            return try rows.map { row in
                let impact = try PromiseIndustryImpact(row: row)
                let industry = try Industry(row: row)
                let promise = try Promise(row: row)
                let officeholder = try Officeholder(row: row)
                return (impact, industry, promise, officeholder)
            }
        }
    }

    func fetchIndustriesWithImpacts() throws -> [Industry] {
        try dbQueue.read { db in
            let sql = """
                SELECT DISTINCT i.*
                FROM industry i
                JOIN promise_industry_impact pii ON i.industryId = pii.industryId
                ORDER BY i.name
            """
            return try Industry.fetchAll(db, sql: sql)
        }
    }

    // MARK: - Company Queries

    func fetchCompanies(forIndustry industryId: String) throws -> [Company] {
        try dbQueue.read { db in
            try Company
                .filter(Company.Columns.industryId == industryId)
                .order(Company.Columns.name)
                .fetchAll(db)
        }
    }

    func fetchAllCompanies() throws -> [Company] {
        try dbQueue.read { db in
            try Company.order(Company.Columns.name).fetchAll(db)
        }
    }

    func fetchCompanyImpacts(forPromise promiseId: String, industry industryId: String) throws -> [(PromiseCompanyImpact, Company)] {
        try dbQueue.read { db in
            let sql = """
                SELECT pci.*, c.*
                FROM promise_company_impact pci
                JOIN company c ON pci.companyId = c.companyId
                WHERE pci.promiseId = ? AND pci.industryId = ?
                ORDER BY pci.relevance DESC, c.name
                """

            var results: [(PromiseCompanyImpact, Company)] = []
            let rows = try Row.fetchAll(db, sql: sql, arguments: [promiseId, industryId])

            for row in rows {
                let impact = try PromiseCompanyImpact(row: row)
                let company = try Company(row: row)
                results.append((impact, company))
            }

            return results
        }
    }

    // MARK: - Statistics Helpers

    func fetchAllOfficeholdersCount() -> Int {
        (try? dbQueue.read { db in
            try Officeholder.fetchCount(db)
        }) ?? 0
    }

    func fetchAllPromisesCount() -> Int {
        (try? dbQueue.read { db in
            try Promise.fetchCount(db)
        }) ?? 0
    }
}

// MARK: - Seed Data Structure

struct SeedData: Codable {
    var regions: [Region]
    var officeholders: [Officeholder]
    var promises: [Promise]
    var evidence: [Evidence]
    var statusSnapshots: [StatusSnapshot]
    var industries: [Industry]
    var policyTags: [PolicyTag]
    var policyTagIndustries: [PolicyTagIndustry]
    var promiseIndustryImpacts: [PromiseIndustryImpact]
    var companies: [Company]?  // Optional for backward compatibility
    var promiseCompanyImpacts: [PromiseCompanyImpact]?  // Optional for backward compatibility
}
