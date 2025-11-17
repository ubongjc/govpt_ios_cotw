//
//  SearchView.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI

struct SearchView: View {
    @StateObject private var searchService = SearchService()
    @EnvironmentObject var database: DatabaseManager
    @State private var showingFilters = false

    var body: some View {
        NavigationStack {
            VStack(spacing: 0) {
                searchBar

                if searchService.isSearching {
                    ProgressView()
                        .padding()
                } else if searchService.searchQuery.isEmpty {
                    emptySearchState
                } else if searchService.searchResults.isEmpty {
                    noResultsState
                } else {
                    searchResultsList
                }
            }
            .navigationTitle("Search")
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button {
                        showingFilters = true
                    } label: {
                        Image(systemName: "line.3.horizontal.decrease.circle")
                            .font(.title3)
                    }
                }
            }
            .sheet(isPresented: $showingFilters) {
                FilterSheet(searchService: searchService)
                    .presentationDetents([.height(300)])
            }
        }
    }

    private var searchBar: some View {
        HStack {
            Image(systemName: "magnifyingglass")
                .foregroundStyle(.secondary)
            TextField("Search regions, promises, leaders, or companies...", text: $searchService.searchQuery)
                .textFieldStyle(.plain)
                .autocorrectionDisabled()

            if !searchService.searchQuery.isEmpty {
                Button {
                    searchService.searchQuery = ""
                } label: {
                    Image(systemName: "xmark.circle.fill")
                        .foregroundStyle(.secondary)
                }
            }
        }
        .padding()
        .background(Color(.systemGray6))
        .cornerRadius(12)
        .padding()
    }

    private var emptySearchState: some View {
        VStack(spacing: 16) {
            Image(systemName: "magnifyingglass")
                .font(.system(size: 60))
                .foregroundStyle(.secondary)
            Text("Search GPT")
                .font(.title2)
                .fontWeight(.bold)
            Text("Find promises, regions, and leaders")
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)

            VStack(alignment: .leading, spacing: 12) {
                SuggestionRow(icon: "map", text: "Try searching for a country")
                SuggestionRow(icon: "person.fill", text: "Search for a leader's name")
                SuggestionRow(icon: "doc.text", text: "Look up specific promises")
            }
            .padding()
        }
        .padding()
    }

    private var noResultsState: some View {
        VStack(spacing: 16) {
            Image(systemName: "magnifyingglass")
                .font(.system(size: 60))
                .foregroundStyle(.secondary)
            Text("No Results")
                .font(.title2)
                .fontWeight(.bold)
            Text("Try a different search term")
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
        .padding()
    }

    private var searchResultsList: some View {
        ScrollView {
            LazyVStack(alignment: .leading, spacing: 20) {
                if !searchService.searchResults.regions.isEmpty {
                    sectionHeader("Regions", count: searchService.searchResults.regions.count)
                    ForEach(searchService.searchResults.regions, id: \.regionId) { region in
                        NavigationLink {
                            if region.type == .country {
                                CountryView(region: region)
                            } else {
                                RegionResultView(region: region)
                            }
                        } label: {
                            RegionResultCard(region: region)
                        }
                        .buttonStyle(.plain)
                    }
                }

                if !searchService.searchResults.officeholders.isEmpty {
                    sectionHeader("Leaders", count: searchService.searchResults.officeholders.count)
                    ForEach(searchService.searchResults.officeholders, id: \.personId) { officeholder in
                        NavigationLink {
                            if let region = database.fetchRegion(id: officeholder.regionId),
                               region.type == .country {
                                CountryView(region: region)
                            } else {
                                OfficeholderDetailView(officeholder: officeholder)
                            }
                        } label: {
                            OfficeholderResultCard(officeholder: officeholder)
                        }
                        .buttonStyle(.plain)
                    }
                }

                if !searchService.searchResults.companies.isEmpty {
                    sectionHeader("Companies", count: searchService.searchResults.companies.count)
                    ForEach(searchService.searchResults.companies, id: \.companyId) { company in
                        CompanyCard(company: company)
                    }
                }

                if !searchService.searchResults.promises.isEmpty {
                    sectionHeader("Promises", count: searchService.searchResults.promises.count)
                    ForEach(searchService.searchResults.promises, id: \.promiseId) { promise in
                        NavigationLink {
                            PromiseDetailView(promise: promise)
                        } label: {
                            SearchPromiseCard(promise: promise)
                        }
                        .buttonStyle(.plain)
                    }
                }
            }
            .padding()
        }
    }

    private func sectionHeader(_ title: String, count: Int) -> some View {
        HStack {
            Text(title)
                .font(.headline)
            Text("(\(count))")
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
    }
}

struct SuggestionRow: View {
    let icon: String
    let text: String

    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: icon)
                .foregroundStyle(.blue)
                .frame(width: 24)
            Text(text)
                .font(.subheadline)
            Spacer()
        }
    }
}

struct RegionResultCard: View {
    let region: Region

    var body: some View {
        HStack {
            Image(systemName: regionIcon)
                .font(.title2)
                .foregroundStyle(.blue)
                .frame(width: 40)

            VStack(alignment: .leading, spacing: 4) {
                Text(region.name)
                    .font(.headline)
                    .foregroundStyle(.primary)
                HStack {
                    Text(region.type.rawValue.capitalized)
                        .font(.caption)
                    Text("•")
                        .font(.caption)
                    Text(region.isoCode)
                        .font(.caption)
                }
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

    private var regionIcon: String {
        switch region.type {
        case .continent: return "globe"
        case .country: return "flag.fill"
        case .state, .province: return "map.fill"
        case .city: return "building.2.fill"
        }
    }
}

struct SearchPromiseCard: View {
    let promise: Promise
    @EnvironmentObject var database: DatabaseManager
    @State private var officeholder: Officeholder?

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text(promise.summary)
                .font(.headline)
                .foregroundStyle(.primary)

            if let officeholder = officeholder {
                HStack {
                    Image(systemName: "person.fill")
                        .font(.caption)
                    Text(officeholder.name)
                        .font(.caption)
                }
                .foregroundStyle(.secondary)
            }

            Text(promise.quoteExact)
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .lineLimit(2)

            HStack {
                ForEach(promise.tags.prefix(2), id: \.self) { tag in
                    Text(tag)
                        .font(.caption2)
                        .padding(.horizontal, 6)
                        .padding(.vertical, 3)
                        .background(Color.blue.opacity(0.1))
                        .foregroundStyle(.blue)
                        .cornerRadius(6)
                }
            }
        }
        .padding()
        .background(Color(.systemGray6))
        .cornerRadius(12)
        .onAppear {
            loadOfficeholder()
        }
    }

    private func loadOfficeholder() {
        do {
            officeholder = try database.fetchOfficeholder(byId: promise.personId)
        } catch {
            print("Error loading officeholder: \(error)")
        }
    }
}

struct OfficeholderResultCard: View {
    let officeholder: Officeholder
    @EnvironmentObject var database: DatabaseManager
    @State private var region: Region?

    var body: some View {
        HStack {
            Image(systemName: "person.circle.fill")
                .font(.title)
                .foregroundStyle(.blue)
                .frame(width: 40)

            VStack(alignment: .leading, spacing: 4) {
                Text(officeholder.name)
                    .font(.headline)
                    .foregroundStyle(.primary)

                Text(officeholder.title)
                    .font(.subheadline)
                    .foregroundStyle(.secondary)

                if let regionName = region?.name {
                    HStack {
                        Image(systemName: "mappin.circle")
                            .font(.caption2)
                        Text(regionName)
                            .font(.caption)
                    }
                    .foregroundStyle(.secondary)
                }

                if let party = officeholder.partyName {
                    Text(party)
                        .font(.caption2)
                        .padding(.horizontal, 6)
                        .padding(.vertical, 2)
                        .background(Color.blue.opacity(0.1))
                        .foregroundStyle(.blue)
                        .cornerRadius(4)
                }
            }

            Spacer()

            Image(systemName: "chevron.right")
                .foregroundStyle(.secondary)
        }
        .padding()
        .background(Color(.systemGray6))
        .cornerRadius(12)
        .onAppear {
            region = database.fetchRegion(id: officeholder.regionId)
        }
    }
}

struct OfficeholderDetailView: View {
    let officeholder: Officeholder
    @EnvironmentObject var database: DatabaseManager
    @State private var region: Region?
    @State private var promises: [Promise] = []
    @State private var industryImpacts: [(PromiseIndustryImpact, Industry, Promise)] = []

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                HStack {
                    Image(systemName: "person.circle.fill")
                        .font(.largeTitle)
                        .foregroundStyle(.blue)
                    VStack(alignment: .leading) {
                        Text(officeholder.name)
                            .font(.title2)
                            .fontWeight(.bold)
                        Text(officeholder.title)
                            .font(.subheadline)
                            .foregroundStyle(.secondary)
                    }
                }

                if let region = region {
                    VStack(alignment: .leading, spacing: 8) {
                        Text("Region")
                            .font(.headline)
                        NavigationLink {
                            if region.type == .country {
                                CountryView(region: region)
                            } else {
                                RegionResultView(region: region)
                            }
                        } label: {
                            HStack {
                                Image(systemName: "map.fill")
                                Text(region.name)
                                Spacer()
                                Image(systemName: "chevron.right")
                            }
                            .padding()
                            .background(Color(.systemGray6))
                            .cornerRadius(12)
                        }
                    }
                }

                if let party = officeholder.partyName {
                    VStack(alignment: .leading, spacing: 8) {
                        Text("Political Party")
                            .font(.headline)
                        Text(party)
                            .padding()
                            .frame(maxWidth: .infinity, alignment: .leading)
                            .background(Color(.systemGray6))
                            .cornerRadius(12)
                    }
                }

                if !industryImpacts.isEmpty {
                    VStack(alignment: .leading, spacing: 12) {
                        HStack {
                            Image(systemName: "chart.line.uptrend.xyaxis")
                                .foregroundStyle(.green)
                            Text("Market Impact Predictions")
                                .font(.headline)
                        }

                        Text("Industries & companies that may be affected by \(officeholder.name)'s promises")
                            .font(.caption)
                            .foregroundStyle(.secondary)

                        ForEach(Array(industryImpacts.prefix(10).enumerated()), id: \.offset) { index, item in
                            let (impact, industry, promise) = item
                            NavigationLink {
                                PromiseDetailView(promise: promise)
                            } label: {
                                LeaderIndustryImpactCard(impact: impact, industry: industry, promise: promise)
                            }
                            .buttonStyle(.plain)
                        }
                    }
                    .padding(.top, 8)
                }

                if !promises.isEmpty {
                    VStack(alignment: .leading, spacing: 12) {
                        Text("Promises (\(promises.count))")
                            .font(.headline)

                        ForEach(promises.prefix(5), id: \.promiseId) { promise in
                            NavigationLink {
                                PromiseDetailView(promise: promise)
                            } label: {
                                Text(promise.summary)
                                    .font(.subheadline)
                                    .padding()
                                    .frame(maxWidth: .infinity, alignment: .leading)
                                    .background(Color(.systemGray6))
                                    .cornerRadius(12)
                            }
                            .buttonStyle(.plain)
                        }
                    }
                }
            }
            .padding()
        }
        .navigationTitle(officeholder.name)
        .navigationBarTitleDisplayMode(.large)
        .onAppear {
            region = database.fetchRegion(id: officeholder.regionId)
            loadPromises()
            loadIndustryImpacts()
        }
    }

    private func loadPromises() {
        do {
            promises = try database.fetchPromises(forPerson: officeholder.personId)
        } catch {
            print("Error loading promises: \(error)")
        }
    }

    private func loadIndustryImpacts() {
        do {
            industryImpacts = try database.fetchIndustryImpacts(for: officeholder)
        } catch {
            print("Error loading industry impacts: \(error)")
        }
    }
}

struct LeaderIndustryImpactCard: View {
    let impact: PromiseIndustryImpact
    let industry: Industry
    let promise: Promise

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Image(systemName: impact.direction > 0 ? "arrow.up.circle.fill" : "arrow.down.circle.fill")
                    .foregroundStyle(impact.direction > 0 ? .green : .red)
                    .font(.title2)

                VStack(alignment: .leading, spacing: 4) {
                    Text(industry.name)
                        .font(.headline)
                        .foregroundStyle(.primary)

                    HStack(spacing: 6) {
                        ImpactClassBadge(impactClass: impact.impactClass)
                        Text("\(Int(impact.pctLow * 100))% to \(Int(impact.pctHigh * 100))%")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }

                Spacer()

                VStack(alignment: .trailing) {
                    Text(impact.direction > 0 ? "Benefit" : "Risk")
                        .font(.caption)
                        .fontWeight(.semibold)
                        .foregroundStyle(impact.direction > 0 ? .green : .red)

                    ConfidenceBadge(confidence: impact.confidence)
                }
            }

            Text(promise.summary)
                .font(.caption)
                .foregroundStyle(.secondary)
                .lineLimit(2)
        }
        .padding()
        .background(Color(.systemGray6))
        .cornerRadius(12)
    }
}

struct RegionResultView: View {
    let region: Region
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                HStack {
                    Image(systemName: "map.fill")
                        .font(.title)
                        .foregroundStyle(.blue)
                    VStack(alignment: .leading) {
                        Text(region.name)
                            .font(.title2)
                            .fontWeight(.bold)
                        Text(region.type.rawValue.capitalized)
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }

                if let lat = region.latitude, let lon = region.longitude {
                    VStack(alignment: .leading, spacing: 8) {
                        Text("Location")
                            .font(.headline)
                        Text("Latitude: \(lat, specifier: "%.4f")")
                            .font(.subheadline)
                            .foregroundStyle(.secondary)
                        Text("Longitude: \(lon, specifier: "%.4f")")
                            .font(.subheadline)
                            .foregroundStyle(.secondary)
                    }
                    .padding()
                    .background(Color(.systemGray6))
                    .cornerRadius(12)
                }
            }
            .padding()
        }
        .navigationTitle(region.name)
        .navigationBarTitleDisplayMode(.large)
    }
}

struct FilterSheet: View {
    @ObservedObject var searchService: SearchService
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            List {
                Section {
                    ForEach(SearchFilter.allCases, id: \.self) { filter in
                        Button {
                            searchService.toggleFilter(filter)
                        } label: {
                            HStack {
                                Image(systemName: iconFor(filter))
                                    .foregroundStyle(colorFor(filter))
                                    .frame(width: 30)

                                Text(filter.rawValue)
                                    .foregroundStyle(.primary)

                                Spacer()

                                if searchService.activeFilters.contains(filter) {
                                    Image(systemName: "checkmark")
                                        .foregroundStyle(.blue)
                                }
                            }
                        }
                    }
                } header: {
                    Text("Filter Results")
                } footer: {
                    Text("Select which types of results to show in your search")
                }
            }
            .navigationTitle("Search Filters")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Done") {
                        dismiss()
                    }
                }
            }
        }
    }

    private func iconFor(_ filter: SearchFilter) -> String {
        switch filter {
        case .regions: return "map.fill"
        case .leaders: return "person.fill"
        case .promises: return "doc.text.fill"
        case .companies: return "building.2.fill"
        }
    }

    private func colorFor(_ filter: SearchFilter) -> Color {
        switch filter {
        case .regions: return .blue
        case .leaders: return .purple
        case .promises: return .green
        case .companies: return .orange
        }
    }
}

#Preview {
    SearchView()
        .environmentObject(DatabaseManager.shared)
}
