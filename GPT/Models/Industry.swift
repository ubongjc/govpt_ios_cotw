//
//  Industry.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import Foundation
import GRDB

struct Industry: Codable, FetchableRecord, PersistableRecord {
    var industryId: String
    var code: String
    var name: String

    static let databaseTableName = "industry"

    enum Columns {
        static let industryId = Column(CodingKeys.industryId)
        static let code = Column(CodingKeys.code)
        static let name = Column(CodingKeys.name)
    }
}

struct PolicyTag: Codable, FetchableRecord, PersistableRecord {
    var tag: String
    var description: String?

    static let databaseTableName = "policy_tag"

    enum Columns {
        static let tag = Column(CodingKeys.tag)
        static let description = Column(CodingKeys.description)
    }
}

struct PolicyTagIndustry: Codable, FetchableRecord, PersistableRecord {
    var tag: String
    var industryId: String
    var weight: Double

    static let databaseTableName = "policy_tag_industry"

    enum Columns {
        static let tag = Column(CodingKeys.tag)
        static let industryId = Column(CodingKeys.industryId)
        static let weight = Column(CodingKeys.weight)
    }
}

struct PromiseIndustryImpact: Codable, FetchableRecord, PersistableRecord {
    var promiseId: String
    var industryId: String
    var direction: Int
    var impactClass: ImpactClass
    var pctLow: Double
    var pctHigh: Double
    var confidence: Double
    var rationale: String?

    enum ImpactClass: String, Codable, DatabaseValueConvertible {
        case minor
        case moderate
        case meaningful
        case significant
        case transformational
    }

    static let databaseTableName = "promise_industry_impact"

    enum Columns {
        static let promiseId = Column(CodingKeys.promiseId)
        static let industryId = Column(CodingKeys.industryId)
        static let direction = Column(CodingKeys.direction)
        static let impactClass = Column(CodingKeys.impactClass)
        static let pctLow = Column(CodingKeys.pctLow)
        static let pctHigh = Column(CodingKeys.pctHigh)
        static let confidence = Column(CodingKeys.confidence)
        static let rationale = Column(CodingKeys.rationale)
    }

    var promise: QueryInterfaceRequest<Promise> {
        Promise.filter(Promise.Columns.promiseId == promiseId)
    }

    var industry: QueryInterfaceRequest<Industry> {
        Industry.filter(Industry.Columns.industryId == industryId)
    }
}
