//
//  PromiseCompanyImpact.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import Foundation
import GRDB

struct PromiseCompanyImpact: Codable, FetchableRecord, PersistableRecord {
    var promiseId: String  // References promise_industry_impact
    var industryId: String  // References promise_industry_impact
    var companyId: String
    var relevance: Double?  // 0.0 to 1.0 score
    var rationale: String?  // Why this company is specifically affected

    static let databaseTableName = "promise_company_impact"

    enum Columns {
        static let promiseId = Column(CodingKeys.promiseId)
        static let industryId = Column(CodingKeys.industryId)
        static let companyId = Column(CodingKeys.companyId)
        static let relevance = Column(CodingKeys.relevance)
        static let rationale = Column(CodingKeys.rationale)
    }

    // Relationship to company
    var company: QueryInterfaceRequest<Company> {
        Company.filter(Company.Columns.companyId == companyId)
    }

    // Relationship to impact
    var promiseIndustryImpact: QueryInterfaceRequest<PromiseIndustryImpact> {
        PromiseIndustryImpact.filter(
            PromiseIndustryImpact.Columns.promiseId == promiseId &&
            PromiseIndustryImpact.Columns.industryId == industryId
        )
    }
}
