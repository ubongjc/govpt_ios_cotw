//
//  CountryView.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI

struct CountryView: View {
    let region: Region
    @Environment(\.dismiss) private var dismiss
    @EnvironmentObject var database: DatabaseManager
    @State private var officeholders: [Officeholder] = []
    @State private var selectedOfficeholder: Officeholder?

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 20) {
                    headerSection

                    if let current = officeholders.first {
                        leaderCard(current)
                    }

                    if let officeholder = officeholders.first {
                        NavigationLink {
                            PromisesListView(officeholder: officeholder)
                        } label: {
                            HStack {
                                VStack(alignment: .leading) {
                                    Text("View All Promises")
                                        .font(.headline)
                                    Text("See what \(officeholder.name) has committed to")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                }
                                Spacer()
                                Image(systemName: "chevron.right")
                                    .foregroundStyle(.secondary)
                            }
                            .padding()
                            .background(Color(.systemGray6))
                            .cornerRadius(12)
                        }
                        .buttonStyle(.plain)
                        .padding(.horizontal)

                        NavigationLink {
                            LeaderMarketImpactView(officeholder: officeholder)
                        } label: {
                            HStack {
                                Image(systemName: "chart.line.uptrend.xyaxis")
                                    .font(.title3)
                                    .foregroundStyle(.green)
                                VStack(alignment: .leading) {
                                    Text("Market Impact Analysis")
                                        .font(.headline)
                                    Text("Industries & stocks affected by \(officeholder.name)'s policies")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                }
                                Spacer()
                                Image(systemName: "chevron.right")
                                    .foregroundStyle(.secondary)
                            }
                            .padding()
                            .background(Color.green.opacity(0.1))
                            .cornerRadius(12)
                        }
                        .buttonStyle(.plain)
                        .padding(.horizontal)
                    }
                }
            }
            .navigationTitle(region.name)
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button {
                        dismiss()
                    } label: {
                        Image(systemName: "xmark.circle.fill")
                            .foregroundStyle(.secondary)
                    }
                }
            }
            .onAppear {
                loadOfficeholders()
            }
        }
    }

    private var headerSection: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Image(systemName: "flag.fill")
                    .font(.title)
                    .foregroundStyle(.blue)
                Text(region.name)
                    .font(.title2)
                    .fontWeight(.bold)
            }
            Text(region.isoCode)
                .font(.caption)
                .foregroundStyle(.secondary)
        }
        .padding()
    }

    private func leaderCard(_ officeholder: Officeholder) -> some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                VStack(alignment: .leading, spacing: 4) {
                    Text("Current Leader")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    Text(officeholder.name)
                        .font(.title3)
                        .fontWeight(.bold)
                    Text(officeholder.title)
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                }
                Spacer()
            }

            if let party = officeholder.partyName {
                HStack {
                    Image(systemName: "person.3.fill")
                        .foregroundStyle(.blue)
                    Text(party)
                        .font(.subheadline)
                }
            }

            if let startDate = officeholder.startDate {
                HStack {
                    Image(systemName: "calendar")
                        .foregroundStyle(.blue)
                    Text("In office since \(startDate, format: .dateTime.month().day().year())")
                        .font(.subheadline)
                }
            }

            if let url = officeholder.officialSiteURL {
                Link(destination: URL(string: url)!) {
                    HStack {
                        Image(systemName: "link")
                        Text("Official Website")
                        Spacer()
                        Image(systemName: "arrow.up.right")
                    }
                    .font(.subheadline)
                    .foregroundStyle(.blue)
                }
            }
        }
        .padding()
        .background(Color(.systemGray6))
        .cornerRadius(16)
        .padding(.horizontal)
    }

    private func loadOfficeholders() {
        do {
            officeholders = try database.fetchCurrentOfficeholders(inRegion: region.regionId)
        } catch {
            print("Error loading officeholders: \(error)")
        }
    }
}

#Preview {
    CountryView(region: Region(
        regionId: "cnt:can",
        type: .country,
        isoCode: "CA",
        name: "Canada",
        parentRegionId: "cont:na",
        shapeRef: nil,
        latitude: 56.1304,
        longitude: -106.3468,
        boundingBoxJSON: nil
    ))
    .environmentObject(DatabaseManager.shared)
}
