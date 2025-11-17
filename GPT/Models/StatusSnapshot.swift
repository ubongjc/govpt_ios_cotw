//
//  StatusSnapshot.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import Foundation
import GRDB

struct StatusSnapshot: Codable, FetchableRecord, PersistableRecord {
    var snapshotId: String
    var promiseId: String
    var status: PromiseStatus
    var score: Double
    var computedAt: Date
    var explanation: String

    enum PromiseStatus: String, Codable, DatabaseValueConvertible {
        case kept
        case inProgress = "in_progress"
        case broken
        case stalled
        case obsolete
    }

    static let databaseTableName = "status_snapshot"

    enum Columns {
        static let snapshotId = Column(CodingKeys.snapshotId)
        static let promiseId = Column(CodingKeys.promiseId)
        static let status = Column(CodingKeys.status)
        static let score = Column(CodingKeys.score)
        static let computedAt = Column(CodingKeys.computedAt)
        static let explanation = Column(CodingKeys.explanation)
    }

    var promise: QueryInterfaceRequest<Promise> {
        Promise.filter(Promise.Columns.promiseId == promiseId)
    }
}
