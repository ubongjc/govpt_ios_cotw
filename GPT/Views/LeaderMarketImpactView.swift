//
//  LeaderMarketImpactView.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI

struct LeaderMarketImpactView: View {
    let officeholder: Officeholder
    @EnvironmentObject var database: DatabaseManager
    @State private var impacts: [(PromiseIndustryImpact, Industry, Promise)] = []
    @State private var isLoading = true
    @State private var selectedFilter: FilterOption = .all

    enum FilterOption: String, CaseIterable {
        case all = "All"
        case benefits = "Benefits"
        case risks = "Risks"
    }

    var body: some View {
        VStack(spacing: 0) {
            filterBar

            if isLoading {
                ProgressView()
                    .padding()
            } else if filteredImpacts.isEmpty {
                emptyState
            } else {
                impactsList
            }
        }
        .navigationTitle("\(officeholder.name)'s Market Impact")
        .navigationBarTitleDisplayMode(.large)
        .onAppear {
            loadImpacts()
        }
    }

    private var filterBar: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 12) {
                ForEach(FilterOption.allCases, id: \.self) { option in
                    Button {
                        selectedFilter = option
                    } label: {
                        Text(option.rawValue)
                            .font(.subheadline)
                            .fontWeight(selectedFilter == option ? .semibold : .regular)
                            .padding(.horizontal, 16)
                            .padding(.vertical, 8)
                            .background(selectedFilter == option ? Color.blue : Color(.systemGray6))
                            .foregroundStyle(selectedFilter == option ? .white : .primary)
                            .cornerRadius(20)
                    }
                }
            }
            .padding()
        }
        .background(Color(.systemBackground))
    }

    private var emptyState: some View {
        VStack(spacing: 16) {
            Image(systemName: "chart.line.uptrend.xyaxis")
                .font(.system(size: 60))
                .foregroundStyle(.secondary)
            Text("No Market Data")
                .font(.title2)
                .fontWeight(.bold)
            Text("No market impact predictions available for \(officeholder.name)")
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
        }
        .padding()
    }

    private var impactsList: some View {
        ScrollView {
            LazyVStack(alignment: .leading, spacing: 16) {
                Text("\(officeholder.name)'s promises may impact these industries")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                    .padding(.horizontal)

                summaryCard

                ForEach(Array(filteredImpacts.enumerated()), id: \.offset) { index, item in
                    let (impact, industry, promise) = item
                    NavigationLink {
                        PromiseDetailView(promise: promise)
                    } label: {
                        LeaderIndustryImpactCard(
                            impact: impact,
                            industry: industry,
                            promise: promise
                        )
                    }
                    .buttonStyle(.plain)
                    .padding(.horizontal)
                }
            }
            .padding(.vertical)
        }
    }

    private var summaryCard: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Summary")
                .font(.headline)

            HStack(spacing: 20) {
                VStack {
                    Text("\(benefitCount)")
                        .font(.title)
                        .fontWeight(.bold)
                        .foregroundStyle(.green)
                    Text("Benefits")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                .frame(maxWidth: .infinity)

                Divider()

                VStack {
                    Text("\(riskCount)")
                        .font(.title)
                        .fontWeight(.bold)
                        .foregroundStyle(.red)
                    Text("Risks")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                .frame(maxWidth: .infinity)

                Divider()

                VStack {
                    Text("\(impacts.count)")
                        .font(.title)
                        .fontWeight(.bold)
                        .foregroundStyle(.blue)
                    Text("Total")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                .frame(maxWidth: .infinity)
            }
            .frame(height: 60)
        }
        .padding()
        .background(Color(.systemGray6))
        .cornerRadius(12)
        .padding(.horizontal)
    }

    private var filteredImpacts: [(PromiseIndustryImpact, Industry, Promise)] {
        switch selectedFilter {
        case .all:
            return impacts
        case .benefits:
            return impacts.filter { $0.0.direction > 0 }
        case .risks:
            return impacts.filter { $0.0.direction < 0 }
        }
    }

    private var benefitCount: Int {
        impacts.filter { $0.0.direction > 0 }.count
    }

    private var riskCount: Int {
        impacts.filter { $0.0.direction < 0 }.count
    }

    private func loadImpacts() {
        isLoading = true
        do {
            impacts = try database.fetchIndustryImpacts(for: officeholder)
        } catch {
            print("Error loading market impacts: \(error)")
        }
        isLoading = false
    }
}

#Preview {
    NavigationStack {
        LeaderMarketImpactView(
            officeholder: Officeholder(
                personId: "p:donald_trump",
                name: "Donald Trump",
                title: "President",
                regionId: "cnt:us",
                partyName: "Republican",
                partyURL: nil,
                startDate: Date(),
                endDate: nil,
                officialSiteURL: nil,
                photoURL: nil
            )
        )
        .environmentObject(DatabaseManager.shared)
    }
}
