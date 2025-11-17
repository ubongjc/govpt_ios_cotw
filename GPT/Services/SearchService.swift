//
//  SearchService.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import Foundation
import Combine

enum SearchFilter: String, CaseIterable {
    case regions = "Regions"
    case leaders = "Leaders"
    case promises = "Promises"
    case companies = "Companies"
}

class SearchService: ObservableObject {
    @Published var searchQuery: String = ""
    @Published var searchResults: SearchResults = SearchResults()
    @Published var isSearching = false
    @Published var activeFilters: Set<SearchFilter> = Set(SearchFilter.allCases)

    private var cancellables = Set<AnyCancellable>()
    private let database = DatabaseManager.shared

    init() {
        $searchQuery
            .debounce(for: .milliseconds(300), scheduler: DispatchQueue.main)
            .removeDuplicates()
            .sink { [weak self] query in
                self?.performSearch(query: query)
            }
            .store(in: &cancellables)
    }

    func toggleFilter(_ filter: SearchFilter) {
        if activeFilters.contains(filter) {
            activeFilters.remove(filter)
        } else {
            activeFilters.insert(filter)
        }
        // Re-run search with new filters
        performSearch(query: searchQuery)
    }

    private func performSearch(query: String) {
        guard !query.isEmpty else {
            searchResults = SearchResults()
            return
        }

        isSearching = true

        DispatchQueue.global(qos: .userInitiated).async { [weak self] in
            guard let self = self else { return }

            do {
                let regions = self.activeFilters.contains(.regions) ? try self.database.searchRegions(query: query) : []
                let promises = self.activeFilters.contains(.promises) ? try self.database.searchPromises(query: query) : []
                let officeholders = self.activeFilters.contains(.leaders) ? try self.database.searchOfficeholders(query: query) : []
                let companies = self.activeFilters.contains(.companies) ? try self.database.searchCompanies(query: query) : []

                DispatchQueue.main.async {
                    self.searchResults = SearchResults(
                        regions: regions,
                        promises: promises,
                        officeholders: officeholders,
                        companies: companies
                    )
                    self.isSearching = false
                }
            } catch {
                print("Search error: \(error)")
                DispatchQueue.main.async {
                    self.isSearching = false
                }
            }
        }
    }
}

struct SearchResults {
    var regions: [Region] = []
    var promises: [Promise] = []
    var officeholders: [Officeholder] = []
    var companies: [Company] = []

    var isEmpty: Bool {
        regions.isEmpty && promises.isEmpty && officeholders.isEmpty && companies.isEmpty
    }
}
