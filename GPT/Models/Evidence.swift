//
//  Evidence.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import Foundation
import GRDB

struct Evidence: Codable, FetchableRecord, PersistableRecord {
    var evidenceId: String
    var promiseId: String
    var date: Date
    var actionType: ActionType
    var resultValue: String?
    var sourcePrimary: String
    var notes: String?

    enum ActionType: String, Codable, DatabaseValueConvertible {
        case billPassed = "bill_passed"
        case budgetLine = "budget_line"
        case executiveOrder = "executive_order"
        case programLaunched = "program_launched"
        case regulationPublished = "regulation_published"
        case publicDataMetric = "public_data_metric"
    }

    static let databaseTableName = "evidence"

    enum Columns {
        static let evidenceId = Column(CodingKeys.evidenceId)
        static let promiseId = Column(CodingKeys.promiseId)
        static let date = Column(CodingKeys.date)
        static let actionType = Column(CodingKeys.actionType)
        static let resultValue = Column(CodingKeys.resultValue)
        static let sourcePrimary = Column(CodingKeys.sourcePrimary)
        static let notes = Column(CodingKeys.notes)
    }

    var promise: QueryInterfaceRequest<Promise> {
        Promise.filter(Promise.Columns.promiseId == promiseId)
    }
}
