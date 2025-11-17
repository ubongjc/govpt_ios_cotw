//
//  GeoService.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import Foundation
import MapKit

class GeoService: ObservableObject {
    @Published var selectedRegion: Region?
    @Published var mapRegion = MKCoordinateRegion(
        center: CLLocationCoordinate2D(latitude: 45.0, longitude: -95.0),
        span: MKCoordinateSpan(latitudeDelta: 80, longitudeDelta: 80)
    )

    private let database = DatabaseManager.shared

    func selectRegion(_ region: Region) {
        selectedRegion = region

        if let lat = region.latitude, let lon = region.longitude {
            let span: MKCoordinateSpan
            switch region.type {
            case .continent:
                span = MKCoordinateSpan(latitudeDelta: 60, longitudeDelta: 60)
            case .country:
                span = MKCoordinateSpan(latitudeDelta: 20, longitudeDelta: 20)
            case .state, .province:
                span = MKCoordinateSpan(latitudeDelta: 5, longitudeDelta: 5)
            case .city:
                span = MKCoordinateSpan(latitudeDelta: 0.5, longitudeDelta: 0.5)
            }

            mapRegion = MKCoordinateRegion(
                center: CLLocationCoordinate2D(latitude: lat, longitude: lon),
                span: span
            )
        }
    }

    func fetchChildren(of region: Region) -> [Region] {
        do {
            return try database.fetchRegions(parentId: region.regionId)
        } catch {
            print("Error fetching children: \(error)")
            return []
        }
    }

    func fetchContinents() -> [Region] {
        do {
            return try database.fetchRegions(ofType: .continent)
        } catch {
            print("Error fetching continents: \(error)")
            return []
        }
    }
}
