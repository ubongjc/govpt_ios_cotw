//
//  Region.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import Foundation
import GRDB
import CoreLocation

struct Region: Codable, FetchableRecord, PersistableRecord, Identifiable {
    var id: String { regionId }
    var regionId: String
    var type: RegionType
    var isoCode: String
    var name: String
    var parentRegionId: String?
    var shapeRef: String?
    var latitude: Double?
    var longitude: Double?
    var boundingBoxJSON: String?
    var nextElection: Date?
    var electionSystem: String?

    // Helper to decode boundary coordinates from JSON
    var boundaryCoordinates: [CLLocationCoordinate2D]? {
        guard let json = boundingBoxJSON,
              let data = json.data(using: .utf8),
              let coords = try? JSONDecoder().decode([[Double]].self, from: data) else {
            return nil
        }

        return coords.compactMap { coord -> CLLocationCoordinate2D? in
            guard coord.count == 2 else { return nil }
            return CLLocationCoordinate2D(latitude: coord[0], longitude: coord[1])
        }
    }

    enum RegionType: String, Codable, DatabaseValueConvertible {
        case continent
        case country
        case state
        case province
        case city
    }

    static let databaseTableName = "region"

    enum Columns {
        static let regionId = Column(CodingKeys.regionId)
        static let type = Column(CodingKeys.type)
        static let isoCode = Column(CodingKeys.isoCode)
        static let name = Column(CodingKeys.name)
        static let parentRegionId = Column(CodingKeys.parentRegionId)
        static let shapeRef = Column(CodingKeys.shapeRef)
        static let latitude = Column(CodingKeys.latitude)
        static let longitude = Column(CodingKeys.longitude)
        static let boundingBoxJSON = Column(CodingKeys.boundingBoxJSON)
        static let nextElection = Column(CodingKeys.nextElection)
        static let electionSystem = Column(CodingKeys.electionSystem)
    }

    var parent: QueryInterfaceRequest<Region> {
        guard let parentRegionId = parentRegionId else {
            return Region.none()
        }
        return Region.filter(Columns.regionId == parentRegionId)
    }

    var children: QueryInterfaceRequest<Region> {
        Region.filter(Columns.parentRegionId == regionId)
    }
}
