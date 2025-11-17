//
//  PromisesListView.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI

struct PromisesListView: View {
    let officeholder: Officeholder
    @EnvironmentObject var database: DatabaseManager
    @State private var promises: [Promise] = []
    @State private var statusSnapshots: [String: StatusSnapshot] = [:]
    @State private var selectedTag: String?
    @State private var selectedStatus: StatusSnapshot.PromiseStatus?
    @State private var showFilters = false

    private var allTags: [String] {
        Array(Set(promises.flatMap { $0.tags })).sorted()
    }

    private var filteredPromises: [Promise] {
        promises.filter { promise in
            let tagMatch = selectedTag == nil || promise.tags.contains(selectedTag!)
            let statusMatch: Bool
            if let selectedStatus = selectedStatus {
                statusMatch = statusSnapshots[promise.promiseId]?.status == selectedStatus
            } else {
                statusMatch = true
            }
            return tagMatch && statusMatch
        }
    }

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                headerSection

                filterSection

                if filteredPromises.isEmpty {
                    emptyState
                } else {
                    promisesList
                }
            }
            .padding()
        }
        .navigationTitle("Promises")
        .navigationBarTitleDisplayMode(.large)
        .toolbar {
            ToolbarItem(placement: .topBarTrailing) {
                Button {
                    showFilters.toggle()
                } label: {
                    Image(systemName: "line.3.horizontal.decrease.circle")
                }
            }
        }
        .sheet(isPresented: $showFilters) {
            FiltersView(
                selectedTag: $selectedTag,
                selectedStatus: $selectedStatus,
                availableTags: allTags
            )
        }
        .onAppear {
            loadPromises()
        }
    }

    private var headerSection: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("\(officeholder.name)")
                .font(.title2)
                .fontWeight(.bold)
            Text("\(promises.count) promises tracked")
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
    }

    private var filterSection: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 8) {
                if selectedTag != nil || selectedStatus != nil {
                    Button {
                        selectedTag = nil
                        selectedStatus = nil
                    } label: {
                        HStack {
                            Image(systemName: "xmark.circle.fill")
                            Text("Clear")
                        }
                        .padding(.horizontal, 12)
                        .padding(.vertical, 6)
                        .background(Color.red.opacity(0.2))
                        .foregroundStyle(.red)
                        .cornerRadius(16)
                    }
                }

                if let tag = selectedTag {
                    FilterChip(text: tag, isActive: true)
                }

                if let status = selectedStatus {
                    FilterChip(text: status.rawValue.capitalized, isActive: true)
                }
            }
        }
    }

    private var promisesList: some View {
        LazyVStack(spacing: 12) {
            ForEach(filteredPromises, id: \.promiseId) { promise in
                NavigationLink {
                    PromiseDetailView(promise: promise)
                } label: {
                    PromiseCard(
                        promise: promise,
                        status: statusSnapshots[promise.promiseId]
                    )
                }
                .buttonStyle(.plain)
            }
        }
    }

    private var emptyState: some View {
        VStack(spacing: 12) {
            Image(systemName: "doc.text.magnifyingglass")
                .font(.system(size: 48))
                .foregroundStyle(.secondary)
            Text("No promises match your filters")
                .font(.headline)
            Text("Try adjusting your filters")
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
        .frame(maxWidth: .infinity)
        .padding(.top, 60)
    }

    private func loadPromises() {
        do {
            promises = try database.fetchPromises(forPerson: officeholder.personId)

            for promise in promises {
                if let snapshot = try database.fetchStatusSnapshot(forPromise: promise.promiseId) {
                    statusSnapshots[promise.promiseId] = snapshot
                }
            }
        } catch {
            print("Error loading promises: \(error)")
        }
    }
}

struct PromiseCard: View {
    let promise: Promise
    let status: StatusSnapshot?

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                Text(promise.summary)
                    .font(.headline)
                    .foregroundStyle(.primary)
                Spacer()
                if let status = status {
                    StatusChip(status: status.status)
                }
            }

            Text(promise.quoteExact)
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .lineLimit(3)

            HStack {
                Image(systemName: "calendar")
                    .font(.caption)
                Text(promise.dateMade, format: .dateTime.month().day().year())
                    .font(.caption)

                Spacer()

                ForEach(promise.tags.prefix(3), id: \.self) { tag in
                    Text(tag)
                        .font(.caption2)
                        .padding(.horizontal, 8)
                        .padding(.vertical, 4)
                        .background(Color.blue.opacity(0.1))
                        .foregroundStyle(.blue)
                        .cornerRadius(8)
                }
            }
            .foregroundStyle(.secondary)
        }
        .padding()
        .background(Color(.systemGray6))
        .cornerRadius(12)
    }
}

struct StatusChip: View {
    let status: StatusSnapshot.PromiseStatus

    private var color: Color {
        switch status {
        case .kept: return .green
        case .inProgress: return .orange
        case .broken: return .red
        case .stalled: return .gray
        case .obsolete: return .purple
        }
    }

    var body: some View {
        Text(statusText)
            .font(.caption)
            .fontWeight(.medium)
            .padding(.horizontal, 10)
            .padding(.vertical, 5)
            .background(color.opacity(0.2))
            .foregroundStyle(color)
            .cornerRadius(12)
    }

    private var statusText: String {
        switch status {
        case .kept: return "Kept"
        case .inProgress: return "In Progress"
        case .broken: return "Broken"
        case .stalled: return "Stalled"
        case .obsolete: return "Obsolete"
        }
    }
}

struct FilterChip: View {
    let text: String
    let isActive: Bool

    var body: some View {
        Text(text)
            .font(.subheadline)
            .padding(.horizontal, 12)
            .padding(.vertical, 6)
            .background(isActive ? Color.blue : Color(.systemGray5))
            .foregroundStyle(isActive ? .white : .primary)
            .cornerRadius(16)
    }
}

struct FiltersView: View {
    @Environment(\.dismiss) private var dismiss
    @Binding var selectedTag: String?
    @Binding var selectedStatus: StatusSnapshot.PromiseStatus?
    let availableTags: [String]

    var body: some View {
        NavigationStack {
            Form {
                Section("Filter by Tag") {
                    ForEach(availableTags, id: \.self) { tag in
                        Button {
                            selectedTag = selectedTag == tag ? nil : tag
                            dismiss()
                        } label: {
                            HStack {
                                Text(tag)
                                Spacer()
                                if selectedTag == tag {
                                    Image(systemName: "checkmark")
                                        .foregroundStyle(.blue)
                                }
                            }
                        }
                        .foregroundStyle(.primary)
                    }
                }

                Section("Filter by Status") {
                    ForEach([
                        StatusSnapshot.PromiseStatus.kept,
                        .inProgress,
                        .broken,
                        .stalled,
                        .obsolete
                    ], id: \.self) { status in
                        Button {
                            selectedStatus = selectedStatus == status ? nil : status
                            dismiss()
                        } label: {
                            HStack {
                                Text(statusText(status))
                                Spacer()
                                if selectedStatus == status {
                                    Image(systemName: "checkmark")
                                        .foregroundStyle(.blue)
                                }
                            }
                        }
                        .foregroundStyle(.primary)
                    }
                }

                Section {
                    Button("Clear All Filters") {
                        selectedTag = nil
                        selectedStatus = nil
                        dismiss()
                    }
                    .foregroundStyle(.red)
                }
            }
            .navigationTitle("Filters")
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

    private func statusText(_ status: StatusSnapshot.PromiseStatus) -> String {
        switch status {
        case .kept: return "Kept"
        case .inProgress: return "In Progress"
        case .broken: return "Broken"
        case .stalled: return "Stalled"
        case .obsolete: return "Obsolete"
        }
    }
}

#Preview {
    NavigationStack {
        PromisesListView(officeholder: Officeholder(
            personId: "p:carney",
            name: "Mark Carney",
            title: "Prime Minister of Canada",
            regionId: "cnt:can",
            partyName: "Liberal Party of Canada",
            partyURL: "https://liberal.ca",
            startDate: Date(),
            endDate: nil,
            officialSiteURL: "https://www.pm.gc.ca/en",
            photoURL: nil
        ))
        .environmentObject(DatabaseManager.shared)
    }
}
