//
//  Officeholder.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import Foundation
import GRDB

struct Officeholder: Codable, FetchableRecord, PersistableRecord {
    var personId: String
    var name: String
    var title: String
    var regionId: String
    var partyName: String?
    var partyURL: String?
    var startDate: Date?
    var endDate: Date?
    var officialSiteURL: String?
    var photoURL: String?

    static let databaseTableName = "officeholder"

    enum Columns {
        static let personId = Column(CodingKeys.personId)
        static let name = Column(CodingKeys.name)
        static let title = Column(CodingKeys.title)
        static let regionId = Column(CodingKeys.regionId)
        static let partyName = Column(CodingKeys.partyName)
        static let partyURL = Column(CodingKeys.partyURL)
        static let startDate = Column(CodingKeys.startDate)
        static let endDate = Column(CodingKeys.endDate)
        static let officialSiteURL = Column(CodingKeys.officialSiteURL)
        static let photoURL = Column(CodingKeys.photoURL)
    }

    var region: QueryInterfaceRequest<Region> {
        Region.filter(Region.Columns.regionId == regionId)
    }

    var promises: QueryInterfaceRequest<Promise> {
        Promise.filter(Promise.Columns.personId == personId)
    }

    var isCurrent: Bool {
        endDate == nil
    }
}
