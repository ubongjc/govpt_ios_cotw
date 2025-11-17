//
//  MarketsView.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI

struct MarketsView: View {
    @EnvironmentObject var database: DatabaseManager
    @State private var allImpacts: [(PromiseIndustryImpact, Industry, Promise, Officeholder)] = []
    @State private var groupedByIndustry: [String: [(PromiseIndustryImpact, Industry, Promise, Officeholder)]] = [:]
    @State private var selectedFilter: FilterOption = .all
    @State private var isLoading = true
    @State private var showFilters = false

    // Advanced filters
    @State private var selectedPositions: Set<String> = []
    @State private var selectedCountries: Set<String> = []
    @State private var selectedIndustries: Set<String> = []

    enum FilterOption: String, CaseIterable {
        case all = "All"
        case benefits = "Benefits"
        case risks = "Risks"
        case high = "High Impact"
    }

    var body: some View {
        NavigationStack {
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
            .navigationTitle("Market Impacts")
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button {
                        showFilters.toggle()
                    } label: {
                        HStack(spacing: 4) {
                            Image(systemName: "line.3.horizontal.decrease.circle")
                            if hasActiveFilters {
                                Circle()
                                    .fill(.blue)
                                    .frame(width: 8, height: 8)
                            }
                        }
                    }
                }
            }
            .sheet(isPresented: $showFilters) {
                AdvancedFiltersView(
                    allImpacts: allImpacts,
                    selectedPositions: $selectedPositions,
                    selectedCountries: $selectedCountries,
                    selectedIndustries: $selectedIndustries
                )
            }
            .onAppear {
                loadImpacts()
            }
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
            Text("Market impact predictions will appear here")
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
        }
        .padding()
    }

    private var impactsList: some View {
        ScrollView {
            LazyVStack(alignment: .leading, spacing: 20) {
                Text("Policy promises may impact these industries and companies")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                    .padding(.horizontal)

                ForEach(Array(groupedFilteredImpacts.keys.sorted()), id: \.self) { industryName in
                    if let impacts = groupedFilteredImpacts[industryName] {
                        IndustryGroupCard(
                            industryName: industryName,
                            impacts: impacts,
                            database: database
                        )
                    }
                }
            }
            .padding(.vertical)
        }
    }

    private var hasActiveFilters: Bool {
        !selectedPositions.isEmpty || !selectedCountries.isEmpty || !selectedIndustries.isEmpty
    }

    private var filteredImpacts: [(PromiseIndustryImpact, Industry, Promise, Officeholder)] {
        var impacts = allImpacts

        // Apply basic filter
        switch selectedFilter {
        case .all:
            break
        case .benefits:
            impacts = impacts.filter { $0.0.direction > 0 }
        case .risks:
            impacts = impacts.filter { $0.0.direction < 0 }
        case .high:
            impacts = impacts.filter {
                $0.0.impactClass == .significant || $0.0.impactClass == .transformational
            }
        }

        // Apply advanced filters
        if !selectedPositions.isEmpty {
            impacts = impacts.filter { selectedPositions.contains($0.3.title) }
        }

        if !selectedCountries.isEmpty {
            impacts = impacts.filter { selectedCountries.contains($0.3.regionId) }
        }

        if !selectedIndustries.isEmpty {
            impacts = impacts.filter { selectedIndustries.contains($0.1.name) }
        }

        return impacts
    }

    private var groupedFilteredImpacts: [String: [(PromiseIndustryImpact, Industry, Promise, Officeholder)]] {
        Dictionary(grouping: filteredImpacts) { $0.1.name }
    }

    private func loadImpacts() {
        isLoading = true
        do {
            allImpacts = try database.fetchAllIndustryImpacts()
            groupedByIndustry = Dictionary(grouping: allImpacts) { $0.1.name }
        } catch {
            print("Error loading market impacts: \(error)")
        }
        isLoading = false
    }
}

struct IndustryGroupCard: View {
    let industryName: String
    let impacts: [(PromiseIndustryImpact, Industry, Promise, Officeholder)]
    let database: DatabaseManager

    @State private var isExpanded = false
    @State private var companies: [Company] = []

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Button {
                withAnimation {
                    isExpanded.toggle()
                }
            } label: {
                HStack {
                    VStack(alignment: .leading, spacing: 4) {
                        Text(industryName)
                            .font(.headline)
                            .foregroundStyle(.primary)

                        HStack(spacing: 12) {
                            let benefitCount = impacts.filter { $0.0.direction > 0 }.count
                            let riskCount = impacts.filter { $0.0.direction < 0 }.count

                            if benefitCount > 0 {
                                HStack(spacing: 4) {
                                    Image(systemName: "arrow.up.circle.fill")
                                        .font(.caption)
                                        .foregroundStyle(.green)
                                    Text("\(benefitCount) benefit\(benefitCount == 1 ? "" : "s")")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                }
                            }

                            if riskCount > 0 {
                                HStack(spacing: 4) {
                                    Image(systemName: "arrow.down.circle.fill")
                                        .font(.caption)
                                        .foregroundStyle(.red)
                                    Text("\(riskCount) risk\(riskCount == 1 ? "" : "s")")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                }
                            }
                        }
                    }

                    Spacer()

                    Image(systemName: isExpanded ? "chevron.up" : "chevron.down")
                        .foregroundStyle(.secondary)
                }
            }
            .buttonStyle(.plain)

            if isExpanded {
                Divider()
                    .padding(.vertical, 4)

                // Companies section
                if !companies.isEmpty {
                    VStack(alignment: .leading, spacing: 8) {
                        HStack {
                            Image(systemName: "building.2.fill")
                                .font(.caption)
                                .foregroundStyle(.blue)
                            Text("Related Companies & Securities")
                                .font(.subheadline)
                                .fontWeight(.semibold)
                        }
                        .padding(.bottom, 4)

                        ForEach(companies) { company in
                            CompanyCard(company: company)
                        }
                    }
                    .padding(.bottom, 8)

                    Divider()
                        .padding(.vertical, 4)
                }

                ForEach(Array(impacts.enumerated()), id: \.offset) { index, item in
                    let (impact, industry, promise, officeholder) = item
                    NavigationLink {
                        PromiseDetailView(promise: promise)
                    } label: {
                        MarketImpactDetailCard(
                            impact: impact,
                            industry: industry,
                            promise: promise,
                            officeholder: officeholder
                        )
                    }
                    .buttonStyle(.plain)
                }
            }
        }
        .padding()
        .background(Color(.systemGray6))
        .cornerRadius(12)
        .padding(.horizontal)
        .onAppear {
            loadCompanies()
        }
        .onChange(of: isExpanded) { _, expanded in
            if expanded {
                loadCompanies()
            }
        }
    }

    private func loadCompanies() {
        guard let firstImpact = impacts.first else { return }
        let industryId = firstImpact.1.industryId

        do {
            companies = try database.fetchCompanies(forIndustry: industryId)
        } catch {
            print("Error loading companies for industry \(industryId): \(error)")
        }
    }
}

struct CompanyCard: View {
    let company: Company

    var body: some View {
        HStack(spacing: 12) {
            // Security type icon
            ZStack {
                Circle()
                    .fill(securityTypeColor.opacity(0.2))
                    .frame(width: 40, height: 40)

                Image(systemName: securityTypeIcon)
                    .font(.caption)
                    .foregroundStyle(securityTypeColor)
            }

            VStack(alignment: .leading, spacing: 4) {
                HStack {
                    Text(company.ticker)
                        .font(.headline)
                        .fontWeight(.bold)

                    if let exchange = company.exchange {
                        Text("• \(exchange)")
                            .font(.caption2)
                            .foregroundStyle(.secondary)
                    }
                }

                Text(company.name)
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                    .lineLimit(1)

                HStack(spacing: 4) {
                    Image(systemName: "chart.line.uptrend.xyaxis")
                        .font(.caption2)
                    Text(company.securityType.rawValue)
                        .font(.caption2)
                }
                .foregroundStyle(.blue)
            }

            Spacer()

            Image(systemName: "chevron.right")
                .font(.caption)
                .foregroundStyle(.secondary)
        }
        .padding(12)
        .background(Color(.systemBackground))
        .cornerRadius(8)
    }

    private var securityTypeIcon: String {
        switch company.securityType {
        case .stock:
            return "chart.line.uptrend.xyaxis"
        case .etf:
            return "chart.bar.xaxis"
        case .mutualFund:
            return "chart.pie.fill"
        case .index:
            return "list.bullet.rectangle"
        }
    }

    private var securityTypeColor: Color {
        switch company.securityType {
        case .stock:
            return .blue
        case .etf:
            return .green
        case .mutualFund:
            return .orange
        case .index:
            return .purple
        }
    }
}

struct MarketImpactDetailCard: View {
    let impact: PromiseIndustryImpact
    let industry: Industry
    let promise: Promise
    let officeholder: Officeholder

    private func countryName(for regionId: String) -> String {
        let countryNames: [String: String] = [
            "cnt:us": "United States",
            "cnt:ca": "Canada",
            "cnt:gb": "United Kingdom",
            "cnt:fr": "France",
            "cnt:de": "Germany",
            "cnt:it": "Italy",
            "cnt:ng": "Nigeria",
            "cnt:in": "India",
            "cnt:au": "Australia",
            "cnt:ar": "Argentina",
            "cnt:eg": "Egypt"
        ]
        return countryNames[regionId] ?? regionId
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack(alignment: .top) {
                Image(systemName: impact.direction > 0 ? "arrow.up.circle.fill" : "arrow.down.circle.fill")
                    .foregroundStyle(impact.direction > 0 ? .green : .red)
                    .font(.title3)

                VStack(alignment: .leading, spacing: 4) {
                    HStack {
                        Text(impact.direction > 0 ? "Potential Benefit" : "Potential Risk")
                            .font(.subheadline)
                            .fontWeight(.semibold)
                            .foregroundStyle(impact.direction > 0 ? .green : .red)

                        Spacer()

                        ConfidenceBadge(confidence: impact.confidence)
                    }

                    HStack(spacing: 6) {
                        ImpactClassBadge(impactClass: impact.impactClass)
                        Text("\(Int(impact.pctLow * 100))% to \(Int(impact.pctHigh * 100))%")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }
            }

            Text(promise.summary)
                .font(.callout)
                .foregroundStyle(.primary)
                .lineLimit(2)

            HStack {
                Image(systemName: "person.fill")
                    .font(.caption2)
                Text(officeholder.name)
                    .font(.caption)
                    .fontWeight(.medium)
                Text("•")
                    .font(.caption)
                Text(officeholder.title)
                    .font(.caption)
                Text("•")
                    .font(.caption)
                Text(countryName(for: officeholder.regionId))
                    .font(.caption)
            }
            .foregroundStyle(.secondary)

            if let rationale = impact.rationale {
                Text(rationale)
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .lineLimit(3)
                    .padding(.top, 4)
            }
        }
        .padding()
        .background(Color(.systemBackground))
        .cornerRadius(8)
    }
}

struct AdvancedFiltersView: View {
    let allImpacts: [(PromiseIndustryImpact, Industry, Promise, Officeholder)]
    @Binding var selectedPositions: Set<String>
    @Binding var selectedCountries: Set<String>
    @Binding var selectedIndustries: Set<String>
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 24) {
                    // Position filters
                    FilterSection(
                        title: "Position Type",
                        icon: "person.badge.shield.checkmark",
                        options: availablePositions,
                        selected: $selectedPositions
                    )

                    Divider()

                    // Country filters
                    FilterSection(
                        title: "Country",
                        icon: "flag",
                        options: availableCountries,
                        selected: $selectedCountries
                    )

                    Divider()

                    // Industry filters
                    FilterSection(
                        title: "Industry",
                        icon: "building.2",
                        options: availableIndustries,
                        selected: $selectedIndustries
                    )
                }
                .padding()
            }
            .navigationTitle("Filters")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    Button("Clear All") {
                        selectedPositions.removeAll()
                        selectedCountries.removeAll()
                        selectedIndustries.removeAll()
                    }
                    .disabled(selectedPositions.isEmpty && selectedCountries.isEmpty && selectedIndustries.isEmpty)
                }
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Done") {
                        dismiss()
                    }
                    .fontWeight(.semibold)
                }
            }
        }
    }

    private var availablePositions: [String] {
        Array(Set(allImpacts.map { $0.3.title })).sorted()
    }

    private var availableCountries: [String] {
        Array(Set(allImpacts.map { $0.3.regionId })).sorted()
    }

    private var availableIndustries: [String] {
        Array(Set(allImpacts.map { $0.1.name })).sorted()
    }
}

struct FilterSection: View {
    let title: String
    let icon: String
    let options: [String]
    @Binding var selected: Set<String>

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                Image(systemName: icon)
                    .foregroundStyle(.blue)
                Text(title)
                    .font(.headline)
            }

            FlowLayout(spacing: 8) {
                ForEach(options, id: \.self) { option in
                    Button {
                        if selected.contains(option) {
                            selected.remove(option)
                        } else {
                            selected.insert(option)
                        }
                    } label: {
                        Text(displayName(for: option))
                            .font(.subheadline)
                            .padding(.horizontal, 12)
                            .padding(.vertical, 6)
                            .background(selected.contains(option) ? Color.blue : Color(.systemGray6))
                            .foregroundStyle(selected.contains(option) ? .white : .primary)
                            .cornerRadius(16)
                    }
                }
            }
        }
    }

    private func displayName(for value: String) -> String {
        // Convert regionId to readable name
        if value.hasPrefix("cnt:") {
            let countryCode = value.replacingOccurrences(of: "cnt:", with: "")
            let countryNames: [String: String] = [
                "us": "United States",
                "ca": "Canada",
                "fr": "France",
                "uk": "United Kingdom",
                "de": "Germany"
            ]
            return countryNames[countryCode] ?? value
        }
        return value
    }
}

// Simple flow layout for filter chips
struct FlowLayout: Layout {
    var spacing: CGFloat = 8

    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        let result = FlowResult(in: proposal.replacingUnspecifiedDimensions().width, subviews: subviews, spacing: spacing)
        return result.size
    }

    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        let result = FlowResult(in: bounds.width, subviews: subviews, spacing: spacing)
        for (index, subview) in subviews.enumerated() {
            subview.place(at: CGPoint(x: bounds.minX + result.positions[index].x, y: bounds.minY + result.positions[index].y), proposal: .unspecified)
        }
    }

    struct FlowResult {
        var size: CGSize = .zero
        var positions: [CGPoint] = []

        init(in maxWidth: CGFloat, subviews: Subviews, spacing: CGFloat) {
            var currentX: CGFloat = 0
            var currentY: CGFloat = 0
            var lineHeight: CGFloat = 0

            for subview in subviews {
                let size = subview.sizeThatFits(.unspecified)

                if currentX + size.width > maxWidth && currentX > 0 {
                    currentX = 0
                    currentY += lineHeight + spacing
                    lineHeight = 0
                }

                positions.append(CGPoint(x: currentX, y: currentY))
                currentX += size.width + spacing
                lineHeight = max(lineHeight, size.height)
            }

            self.size = CGSize(width: maxWidth, height: currentY + lineHeight)
        }
    }
}

#Preview {
    MarketsView()
        .environmentObject(DatabaseManager.shared)
}
