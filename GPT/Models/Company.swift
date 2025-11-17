//
//  Company.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import Foundation
import GRDB

struct Company: Codable, FetchableRecord, PersistableRecord, Identifiable {
    var companyId: String
    var ticker: String
    var name: String
    var securityType: SecurityType
    var industryId: String
    var exchange: String?
    var description: String?

    var id: String { companyId }

    enum SecurityType: String, Codable, DatabaseValueConvertible {
        case stock = "Stock"
        case etf = "ETF"
        case mutualFund = "Mutual Fund"
        case index = "Index"
    }

    static let databaseTableName = "company"

    enum Columns {
        static let companyId = Column(CodingKeys.companyId)
        static let ticker = Column(CodingKeys.ticker)
        static let name = Column(CodingKeys.name)
        static let securityType = Column(CodingKeys.securityType)
        static let industryId = Column(CodingKeys.industryId)
        static let exchange = Column(CodingKeys.exchange)
        static let description = Column(CodingKeys.description)
    }

    var industry: QueryInterfaceRequest<Industry> {
        Industry.filter(Industry.Columns.industryId == industryId)
    }
}
