//
//  Promise.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import Foundation
import GRDB

struct Promise: Codable, FetchableRecord, PersistableRecord {
    var promiseId: String
    var personId: String
    var regionId: String
    var dateMade: Date
    var context: String
    var quoteExact: String
    var summary: String
    var tagsJSON: String
    var dueBy: Date?
    var sourcePrimary: String
    var sourceType: SourceType
    var policyTagsJSON: String?
    var effectInputsJSON: String?

    enum SourceType: String, Codable, DatabaseValueConvertible {
        case manifestoPDF = "manifesto_pdf"
        case officialSite = "official_site"
        case officialVideo = "official_video"
        case officialSocial = "official_social"
        case officialStatement = "official_statement"
        case govRelease = "gov_release"
        case legalGazette = "legal_gazette"
    }

    static let databaseTableName = "promise"

    enum Columns {
        static let promiseId = Column(CodingKeys.promiseId)
        static let personId = Column(CodingKeys.personId)
        static let regionId = Column(CodingKeys.regionId)
        static let dateMade = Column(CodingKeys.dateMade)
        static let context = Column(CodingKeys.context)
        static let quoteExact = Column(CodingKeys.quoteExact)
        static let summary = Column(CodingKeys.summary)
        static let tagsJSON = Column(CodingKeys.tagsJSON)
        static let dueBy = Column(CodingKeys.dueBy)
        static let sourcePrimary = Column(CodingKeys.sourcePrimary)
        static let sourceType = Column(CodingKeys.sourceType)
        static let policyTagsJSON = Column(CodingKeys.policyTagsJSON)
        static let effectInputsJSON = Column(CodingKeys.effectInputsJSON)
    }

    var tags: [String] {
        get {
            (try? JSONDecoder().decode([String].self, from: Data(tagsJSON.utf8))) ?? []
        }
    }

    var policyTags: [String]? {
        get {
            guard let json = policyTagsJSON else { return nil }
            return try? JSONDecoder().decode([String].self, from: Data(json.utf8))
        }
    }

    var officeholder: QueryInterfaceRequest<Officeholder> {
        Officeholder.filter(Officeholder.Columns.personId == personId)
    }

    var region: QueryInterfaceRequest<Region> {
        Region.filter(Region.Columns.regionId == regionId)
    }

    var evidences: QueryInterfaceRequest<Evidence> {
        Evidence.filter(Evidence.Columns.promiseId == promiseId)
    }

    var statusSnapshot: QueryInterfaceRequest<StatusSnapshot> {
        StatusSnapshot.filter(StatusSnapshot.Columns.promiseId == promiseId)
    }
}

struct PolicyEffectInputs: Codable {
    var intensity: Double
    var budget: Double
    var timing: Double
    var jurisdiction: Double
    var execution: Double

    var score: Double {
        (intensity + budget + timing + jurisdiction + execution) / 5.0
    }
}
