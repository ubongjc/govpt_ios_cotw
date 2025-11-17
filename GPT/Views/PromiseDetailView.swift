//
//  PromiseDetailView.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI
import SafariServices

struct PromiseDetailView: View {
    let promise: Promise
    @EnvironmentObject var database: DatabaseManager
    @State private var officeholder: Officeholder?
    @State private var evidence: [Evidence] = []
    @State private var statusSnapshot: StatusSnapshot?
    @State private var impacts: [(PromiseIndustryImpact, Industry)] = []
    @State private var showSourceURL: String?
    @State private var showMarketDisclaimer = false

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 24) {
                summarySection
                quoteSection
                statusSection
                if !impacts.isEmpty {
                    marketImpactSection
                }
                contextSection
                evidenceSection
                sourceSection
            }
            .padding()
        }
        .navigationTitle("Promise Detail")
        .navigationBarTitleDisplayMode(.inline)
        .sheet(isPresented: Binding(
            get: { showSourceURL != nil },
            set: { if !$0 { showSourceURL = nil } }
        )) {
            if let urlString = showSourceURL, let url = URL(string: urlString) {
                SafariView(url: url)
            }
        }
        .sheet(isPresented: $showMarketDisclaimer) {
            MarketDisclaimerView()
        }
        .onAppear {
            loadData()
        }
    }

    private var summarySection: some View {
        VStack(alignment: .leading, spacing: 8) {
            if let status = statusSnapshot {
                StatusChip(status: status.status)
            }
            Text(promise.summary)
                .font(.title2)
                .fontWeight(.bold)

            if let officeholder = officeholder {
                HStack {
                    Image(systemName: "person.fill")
                        .foregroundStyle(.secondary)
                    Text(officeholder.name)
                        .font(.subheadline)
                    Text("•")
                        .foregroundStyle(.secondary)
                    Text(promise.dateMade, format: .dateTime.month().day().year())
                        .font(.subheadline)
                }
                .foregroundStyle(.secondary)
            }

            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 8) {
                    ForEach(promise.tags, id: \.self) { tag in
                        Text(tag)
                            .font(.caption)
                            .padding(.horizontal, 10)
                            .padding(.vertical, 5)
                            .background(Color.blue.opacity(0.1))
                            .foregroundStyle(.blue)
                            .cornerRadius(12)
                    }
                }
            }
        }
    }

    private var quoteSection: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Exact Quote")
                .font(.headline)
                .foregroundStyle(.secondary)

            Text("\"")
                .font(.title)
                .foregroundStyle(.blue)
            + Text(promise.quoteExact)
                .font(.body)
            + Text("\"")
                .font(.title)
                .foregroundStyle(.blue)
        }
        .padding()
        .background(Color.blue.opacity(0.05))
        .cornerRadius(12)
    }

    private var statusSection: some View {
        Group {
            if let status = statusSnapshot {
                VStack(alignment: .leading, spacing: 12) {
                    HStack {
                        Text("Status")
                            .font(.headline)
                        Spacer()
                        ProgressBar(score: status.score)
                            .frame(width: 100)
                    }

                    Text(status.explanation)
                        .font(.subheadline)
                        .foregroundStyle(.secondary)

                    HStack {
                        Text("Last updated:")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                        Text(status.computedAt, format: .dateTime.month().day().year())
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }
                .padding()
                .background(Color(.systemGray6))
                .cornerRadius(12)
            }
        }
    }

    private var marketImpactSection: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                Text("Market Impact")
                    .font(.headline)
                Spacer()
                Button {
                    showMarketDisclaimer = true
                } label: {
                    Image(systemName: "info.circle")
                        .foregroundStyle(.blue)
                }
            }

            Text("Industries potentially affected if this promise is fulfilled:")
                .font(.caption)
                .foregroundStyle(.secondary)

            ForEach(impacts, id: \.0.industryId) { (impact, industry) in
                MarketImpactCard(promiseId: promise.promiseId, impact: impact, industry: industry)
            }

            DisclaimerText()
        }
        .padding()
        .background(Color.orange.opacity(0.05))
        .cornerRadius(12)
    }

    private var contextSection: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Context")
                .font(.headline)
            Text(promise.context)
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
        .padding()
        .background(Color(.systemGray6))
        .cornerRadius(12)
    }

    private var evidenceSection: some View {
        Group {
            if !evidence.isEmpty {
                VStack(alignment: .leading, spacing: 12) {
                    Text("Evidence")
                        .font(.headline)

                    ForEach(evidence, id: \.evidenceId) { item in
                        EvidenceCard(evidence: item, onTapSource: { url in
                            showSourceURL = url
                        })
                    }
                }
            }
        }
    }

    private var sourceSection: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Primary Source")
                .font(.headline)

            Button {
                showSourceURL = promise.sourcePrimary
            } label: {
                HStack {
                    VStack(alignment: .leading, spacing: 4) {
                        Text(sourceTypeText(promise.sourceType))
                            .font(.caption)
                            .foregroundStyle(.secondary)
                        Text(promise.sourcePrimary)
                            .font(.subheadline)
                            .lineLimit(2)
                    }
                    Spacer()
                    Image(systemName: "arrow.up.right.square")
                        .foregroundStyle(.blue)
                }
                .padding()
                .background(Color(.systemGray6))
                .cornerRadius(12)
            }
            .buttonStyle(.plain)

            ShareLink(item: promise.sourcePrimary) {
                HStack {
                    Image(systemName: "square.and.arrow.up")
                    Text("Share Source")
                }
                .frame(maxWidth: .infinity)
                .padding()
                .background(Color.blue.opacity(0.1))
                .foregroundStyle(.blue)
                .cornerRadius(12)
            }
        }
    }

    private func loadData() {
        do {
            officeholder = try database.fetchOfficeholder(byId: promise.personId)
            evidence = try database.fetchEvidence(forPromise: promise.promiseId)
            statusSnapshot = try database.fetchStatusSnapshot(forPromise: promise.promiseId)
            impacts = try database.fetchImpacts(forPromise: promise.promiseId)
        } catch {
            print("Error loading promise details: \(error)")
        }
    }

    private func sourceTypeText(_ type: Promise.SourceType) -> String {
        switch type {
        case .manifestoPDF: return "Campaign Manifesto PDF"
        case .officialSite: return "Official Website"
        case .officialVideo: return "Official Video"
        case .officialSocial: return "Official Social Media"
        case .officialStatement: return "Official Statement"
        case .govRelease: return "Government Release"
        case .legalGazette: return "Legal Gazette"
        }
    }
}

struct ProgressBar: View {
    let score: Double

    private var color: Color {
        if score >= 0.7 { return .green }
        else if score >= 0.3 { return .orange }
        else { return .red }
    }

    var body: some View {
        VStack(alignment: .trailing, spacing: 4) {
            GeometryReader { geometry in
                ZStack(alignment: .leading) {
                    Rectangle()
                        .fill(Color(.systemGray5))
                        .frame(height: 8)
                        .cornerRadius(4)

                    Rectangle()
                        .fill(color)
                        .frame(width: geometry.size.width * score, height: 8)
                        .cornerRadius(4)
                }
            }
            .frame(height: 8)

            Text("\(Int(score * 100))%")
                .font(.caption2)
                .foregroundStyle(.secondary)
        }
    }
}

struct EvidenceCard: View {
    let evidence: Evidence
    let onTapSource: (String) -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Image(systemName: actionIcon)
                    .foregroundStyle(.green)
                Text(actionText)
                    .font(.subheadline)
                    .fontWeight(.medium)
                Spacer()
                Text(evidence.date, format: .dateTime.month().day().year())
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }

            if let notes = evidence.notes {
                Text(notes)
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }

            Button {
                onTapSource(evidence.sourcePrimary)
            } label: {
                HStack {
                    Image(systemName: "link")
                        .font(.caption)
                    Text("View Source")
                        .font(.caption)
                    Spacer()
                    Image(systemName: "arrow.up.right")
                        .font(.caption)
                }
                .foregroundStyle(.blue)
            }
        }
        .padding()
        .background(Color.green.opacity(0.05))
        .cornerRadius(8)
    }

    private var actionIcon: String {
        switch evidence.actionType {
        case .billPassed: return "doc.text.fill"
        case .budgetLine: return "dollarsign.circle.fill"
        case .executiveOrder: return "signature"
        case .programLaunched: return "sparkles"
        case .regulationPublished: return "book.fill"
        case .publicDataMetric: return "chart.bar.fill"
        }
    }

    private var actionText: String {
        switch evidence.actionType {
        case .billPassed: return "Bill Passed"
        case .budgetLine: return "Budget Line Item"
        case .executiveOrder: return "Executive Order"
        case .programLaunched: return "Program Launched"
        case .regulationPublished: return "Regulation Published"
        case .publicDataMetric: return "Public Data / Metric"
        }
    }
}

struct MarketImpactCard: View {
    let promiseId: String
    let impact: PromiseIndustryImpact
    let industry: Industry

    @EnvironmentObject var db: DatabaseManager
    @State private var companies: [(PromiseCompanyImpact, Company)] = []

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Text(industry.name)
                    .font(.subheadline)
                    .fontWeight(.medium)
                Spacer()
                DirectionIndicator(direction: impact.direction)
            }

            HStack {
                ImpactClassBadge(impactClass: impact.impactClass)
                Text("\(Int(impact.pctLow * 100))% to \(Int(impact.pctHigh * 100))%")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                Spacer()
                ConfidenceBadge(confidence: impact.confidence)
            }

            if let rationale = impact.rationale {
                Text(rationale)
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .fixedSize(horizontal: false, vertical: true)
            }

            if !companies.isEmpty {
                Divider()
                    .padding(.vertical, 4)

                Text("Affected Companies")
                    .font(.caption)
                    .fontWeight(.semibold)
                    .foregroundStyle(.secondary)

                ForEach(companies, id: \.1.companyId) { (companyImpact, company) in
                    HStack {
                        Text(company.ticker)
                            .font(.caption)
                            .fontWeight(.medium)
                            .padding(.horizontal, 6)
                            .padding(.vertical, 2)
                            .background(Color.blue.opacity(0.15))
                            .foregroundStyle(.blue)
                            .cornerRadius(4)

                        Text(company.name)
                            .font(.caption)
                            .foregroundStyle(.secondary)

                        Spacer()

                        Text(company.securityType.rawValue)
                            .font(.caption2)
                            .foregroundStyle(.secondary)
                    }
                }
            }

            Text(industry.code)
                .font(.caption2)
                .foregroundStyle(.secondary)
        }
        .padding()
        .background(Color(.systemGray6))
        .cornerRadius(8)
        .onAppear {
            loadCompanies()
        }
    }

    private func loadCompanies() {
        do {
            companies = try db.fetchCompanies(forPromiseId: promiseId, industryId: industry.industryId)
        } catch {
            print("Error fetching companies for \(promiseId) and \(industry.industryId): \(error)")
        }
    }
}

struct DirectionIndicator: View {
    let direction: Int

    var body: some View {
        Image(systemName: direction > 0 ? "arrow.up.circle.fill" : direction < 0 ? "arrow.down.circle.fill" : "minus.circle.fill")
            .foregroundStyle(direction > 0 ? .green : direction < 0 ? .red : .gray)
    }
}

struct ImpactClassBadge: View {
    let impactClass: PromiseIndustryImpact.ImpactClass

    private var color: Color {
        switch impactClass {
        case .minor: return .gray
        case .moderate: return .blue
        case .meaningful: return .cyan
        case .significant: return .orange
        case .transformational: return .purple
        }
    }

    var body: some View {
        Text(impactClass.rawValue.capitalized)
            .font(.caption2)
            .fontWeight(.medium)
            .padding(.horizontal, 8)
            .padding(.vertical, 4)
            .background(color.opacity(0.2))
            .foregroundStyle(color)
            .cornerRadius(6)
    }
}

struct ConfidenceBadge: View {
    let confidence: Double

    private var confidenceLevel: String {
        if confidence >= 0.7 { return "High" }
        else if confidence >= 0.4 { return "Medium" }
        else { return "Low" }
    }

    private var color: Color {
        if confidence >= 0.7 { return .green }
        else if confidence >= 0.4 { return .orange }
        else { return .red }
    }

    var body: some View {
        HStack(spacing: 4) {
            Circle()
                .fill(color)
                .frame(width: 6, height: 6)
            Text("\(confidenceLevel)")
                .font(.caption2)
        }
        .foregroundStyle(.secondary)
    }
}

struct DisclaimerText: View {
    var body: some View {
        Text("This feature is informational only and not financial advice. Markets move for many reasons. Do your own research.")
            .font(.caption2)
            .foregroundStyle(.secondary)
            .italic()
            .padding(.top, 4)
    }
}

struct MarketDisclaimerView: View {
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 20) {
                    Text("About Market Impact")
                        .font(.title2)
                        .fontWeight(.bold)

                    Text("This feature maps government promises to industries that may be affected if those promises are fulfilled.")
                        .font(.body)

                    VStack(alignment: .leading, spacing: 12) {
                        Text("What you see:")
                            .font(.headline)

                        BulletPoint(text: "Direction: Whether the policy would likely favor (↑) or disadvantage (↓) the industry")
                        BulletPoint(text: "Impact Range: A policy-sensitivity band (not a price forecast)")
                        BulletPoint(text: "Confidence: How certain the mapping is based on policy intensity, budget, timing, jurisdiction, and execution likelihood")
                        BulletPoint(text: "Rationale: A brief explanation of the connection")
                    }

                    Text("Important Disclaimer")
                        .font(.headline)
                        .foregroundStyle(.red)

                    Text("This is NOT financial advice. Markets are influenced by countless factors including macroeconomics, global events, liquidity, valuations, and more. Representative tickers and ETFs (when shown) are examples only, not recommendations. Always do your own research and consult with a financial advisor before making investment decisions.")
                        .font(.subheadline)
                        .foregroundStyle(.secondary)

                    VStack(alignment: .leading, spacing: 12) {
                        Text("How it works:")
                            .font(.headline)

                        BulletPoint(text: "Each promise is tagged with policy levers (e.g., 'infrastructure', 'green_subsidies')")
                        BulletPoint(text: "We maintain a curated mapping of policies to industry sectors")
                        BulletPoint(text: "Impact ranges are computed using policy intensity, budget scale, timing, jurisdiction, and execution likelihood")
                        BulletPoint(text: "All mappings are auditable and based on publicly available information")
                    }
                }
                .padding()
            }
            .navigationTitle("Market Impact")
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
}

struct BulletPoint: View {
    let text: String

    var body: some View {
        HStack(alignment: .top, spacing: 8) {
            Text("•")
                .font(.body)
            Text(text)
                .font(.subheadline)
        }
    }
}

struct SafariView: UIViewControllerRepresentable {
    let url: URL

    func makeUIViewController(context: Context) -> SFSafariViewController {
        SFSafariViewController(url: url)
    }

    func updateUIViewController(_ uiViewController: SFSafariViewController, context: Context) {}
}

#Preview {
    NavigationStack {
        PromiseDetailView(promise: Promise(
            promiseId: "pr:ca:taxcut",
            personId: "p:carney",
            regionId: "cnt:can",
            dateMade: Date(),
            context: "Campaign platform PDF",
            quoteExact: "We will cut taxes for the middle class.",
            summary: "Cut middle-class taxes",
            tagsJSON: "[\"taxes\",\"economy\"]",
            dueBy: nil,
            sourcePrimary: "https://liberal.ca/plan",
            sourceType: .manifestoPDF,
            policyTagsJSON: nil,
            effectInputsJSON: nil
        ))
        .environmentObject(DatabaseManager.shared)
    }
}
