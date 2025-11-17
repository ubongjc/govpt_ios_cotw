//
//  HomeMapView.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI
import MapKit

struct HomeMapView: View {
    @StateObject private var geoService = GeoService()
    @EnvironmentObject var database: DatabaseManager
    @State private var continents: [Region] = []
    @State private var countries: [Region] = []
    @State private var selectedContinent: Region?
    @State private var selectedCountry: Region?
    @State private var showCountriesList = false

    var body: some View {
        NavigationStack {
            ZStack {
                Map(position: .constant(.region(geoService.mapRegion))) {
                    ForEach(continents, id: \.regionId) { continent in
                        if let lat = continent.latitude, let lon = continent.longitude {
                            Annotation(continent.name, coordinate: CLLocationCoordinate2D(latitude: lat, longitude: lon)) {
                                VStack {
                                    Image(systemName: "globe")
                                        .font(.title)
                                        .foregroundStyle(.blue)
                                        .padding(8)
                                        .background(Circle().fill(.white))
                                        .shadow(radius: 4)
                                    Text(continent.name)
                                        .font(.caption)
                                        .fontWeight(.medium)
                                        .padding(4)
                                        .background(Capsule().fill(.white))
                                        .shadow(radius: 2)
                                }
                                .onTapGesture {
                                    drillIntoRegion(continent)
                                }
                            }
                        }
                    }
                }
                .mapStyle(.standard(elevation: .realistic))
                .ignoresSafeArea(edges: .top)

                VStack {
                    Spacer()

                    if !continents.isEmpty {
                        VStack(alignment: .leading, spacing: 12) {
                            Text("Select a Region")
                                .font(.headline)

                            ScrollView(.horizontal, showsIndicators: false) {
                                HStack(spacing: 12) {
                                    ForEach(continents, id: \.regionId) { continent in
                                        Button {
                                            drillIntoRegion(continent)
                                        } label: {
                                            VStack {
                                                Image(systemName: "globe")
                                                    .font(.title2)
                                                Text(continent.name)
                                                    .font(.caption)
                                            }
                                            .frame(width: 100, height: 80)
                                            .background(Color.white)
                                            .cornerRadius(12)
                                            .shadow(radius: 4)
                                        }
                                        .buttonStyle(.plain)
                                    }
                                }
                                .padding(.horizontal)
                            }
                        }
                        .padding()
                        .background(Color(.systemBackground).opacity(0.95))
                        .cornerRadius(16)
                        .padding()
                    }
                }
            }
            .navigationTitle("Government Promises")
            .navigationBarTitleDisplayMode(.large)
            .sheet(item: $selectedCountry) { country in
                CountryView(region: country)
            }
            .sheet(isPresented: $showCountriesList) {
                CountriesListView(
                    continent: selectedContinent,
                    countries: countries,
                    onSelectCountry: { country in
                        selectedCountry = country
                        showCountriesList = false
                    }
                )
            }
            .onAppear {
                loadContinents()
            }
        }
    }

    private func loadContinents() {
        continents = geoService.fetchContinents()
    }

    private func drillIntoRegion(_ region: Region) {
        let children = geoService.fetchChildren(of: region)

        if !children.isEmpty {
            selectedContinent = region
            countries = children
            showCountriesList = true
        }
    }
}

struct CountriesListView: View {
    let continent: Region?
    let countries: [Region]
    let onSelectCountry: (Region) -> Void
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            List(countries, id: \.regionId) { country in
                Button {
                    onSelectCountry(country)
                } label: {
                    HStack {
                        Image(systemName: "flag.fill")
                            .foregroundStyle(.blue)
                        VStack(alignment: .leading) {
                            Text(country.name)
                                .font(.headline)
                            Text(country.isoCode)
                                .font(.caption)
                                .foregroundStyle(.secondary)
                        }
                    }
                }
            }
            .navigationTitle(continent?.name ?? "Countries")
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Done") {
                        dismiss()
                    }
                }
            }
        }
    }
}

#Preview {
    HomeMapView()
        .environmentObject(DatabaseManager.shared)
}
