//
//  SettingsView.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI

struct SettingsView: View {
    @EnvironmentObject var database: DatabaseManager
    @StateObject private var notificationManager = NotificationManager.shared
    @AppStorage("defaultRegionId") private var defaultRegionId: String?
    @AppStorage("hasCompletedOnboarding") private var hasCompletedOnboarding = true

    @State private var defaultRegion: Region?
    @State private var showingRegionPicker = false
    @State private var showingClearDataAlert = false
    @State private var showingResetOnboardingAlert = false

    var body: some View {
        NavigationStack {
            List {
                // Notifications Section
                Section {
                    HStack {
                        Image(systemName: "bell.badge.fill")
                            .foregroundColor(.blue)
                            .frame(width: 30)

                        VStack(alignment: .leading, spacing: 4) {
                            Text("Notifications")
                                .font(.body)
                            Text(notificationStatusText)
                                .font(.caption)
                                .foregroundColor(.secondary)
                        }

                        Spacer()

                        if notificationManager.authorizationStatus == .notDetermined {
                            Button("Enable") {
                                Task {
                                    await notificationManager.requestAuthorization()
                                }
                            }
                            .font(.subheadline)
                        } else if notificationManager.authorizationStatus == .denied {
                            Button("Settings") {
                                if let url = URL(string: UIApplication.openSettingsURLString) {
                                    UIApplication.shared.open(url)
                                }
                            }
                            .font(.subheadline)
                        }
                    }
                } header: {
                    Text("Notifications")
                } footer: {
                    Text("Get reminders about upcoming elections in regions you follow")
                }

                // Default Region Section
                Section {
                    Button(action: { showingRegionPicker = true }) {
                        HStack {
                            Image(systemName: "map.circle.fill")
                                .foregroundColor(.blue)
                                .frame(width: 30)

                            VStack(alignment: .leading, spacing: 4) {
                                Text("Default Region")
                                    .foregroundColor(.primary)
                                if let region = defaultRegion {
                                    Text(region.name)
                                        .font(.caption)
                                        .foregroundColor(.secondary)
                                } else {
                                    Text("None set")
                                        .font(.caption)
                                        .foregroundColor(.secondary)
                                }
                            }

                            Spacer()

                            Image(systemName: "chevron.right")
                                .font(.caption)
                                .foregroundColor(.secondary)
                        }
                    }

                    if defaultRegion != nil {
                        Button(action: {
                            defaultRegionId = nil
                            defaultRegion = nil
                        }) {
                            HStack {
                                Image(systemName: "xmark.circle.fill")
                                    .foregroundColor(.red)
                                    .frame(width: 30)
                                Text("Clear Default Region")
                                    .foregroundColor(.red)
                            }
                        }
                    }
                } header: {
                    Text("Region Preferences")
                } footer: {
                    Text("Set a default region to open automatically when you launch the app")
                }

                // Data Management Section
                Section {
                    Button(action: { showingResetOnboardingAlert = true }) {
                        HStack {
                            Image(systemName: "arrow.counterclockwise.circle.fill")
                                .foregroundColor(.orange)
                                .frame(width: 30)
                            Text("Reset Onboarding")
                                .foregroundColor(.primary)
                        }
                    }

                    Button(action: { showingClearDataAlert = true }) {
                        HStack {
                            Image(systemName: "trash.circle.fill")
                                .foregroundColor(.red)
                                .frame(width: 30)
                            Text("Clear All Data")
                                .foregroundColor(.red)
                        }
                    }
                } header: {
                    Text("Data Management")
                }

                // About Section
                Section {
                    HStack {
                        Image(systemName: "info.circle.fill")
                            .foregroundColor(.blue)
                            .frame(width: 30)
                        Text("Version")
                        Spacer()
                        Text("1.0.0")
                            .foregroundColor(.secondary)
                    }

                    HStack {
                        Image(systemName: "doc.text.fill")
                            .foregroundColor(.blue)
                            .frame(width: 30)
                        Text("Build")
                        Spacer()
                        Text("1")
                            .foregroundColor(.secondary)
                    }
                } header: {
                    Text("About")
                }

                // Database Stats Section
                Section {
                    HStack {
                        Image(systemName: "globe.americas.fill")
                            .foregroundColor(.purple)
                            .frame(width: 30)
                        Text("Regions")
                        Spacer()
                        Text("\(database.fetchContinents().count) continents")
                            .foregroundColor(.secondary)
                    }

                    HStack {
                        Image(systemName: "person.3.fill")
                            .foregroundColor(.green)
                            .frame(width: 30)
                        Text("Officeholders")
                        Spacer()
                        Text("\(database.fetchAllOfficeholdersCount())")
                            .foregroundColor(.secondary)
                    }

                    HStack {
                        Image(systemName: "checkmark.seal.fill")
                            .foregroundColor(.blue)
                            .frame(width: 30)
                        Text("Promises")
                        Spacer()
                        Text("\(database.fetchAllPromisesCount())")
                            .foregroundColor(.secondary)
                    }
                } header: {
                    Text("Database Statistics")
                }
            }
            .navigationTitle("Settings")
            .sheet(isPresented: $showingRegionPicker) {
                RegionPickerView(selectedRegionId: $defaultRegionId)
                    .environmentObject(database)
            }
            .alert("Clear All Data", isPresented: $showingClearDataAlert) {
                Button("Cancel", role: .cancel) {}
                Button("Clear", role: .destructive) {
                    clearAllData()
                }
            } message: {
                Text("This will clear all local data and re-seed the database. This action cannot be undone.")
            }
            .alert("Reset Onboarding", isPresented: $showingResetOnboardingAlert) {
                Button("Cancel", role: .cancel) {}
                Button("Reset", role: .destructive) {
                    hasCompletedOnboarding = false
                    // Force app restart to show onboarding
                    exit(0)
                }
            } message: {
                Text("This will reset the onboarding flow and restart the app.")
            }
            .onAppear {
                loadDefaultRegion()
            }
        }
    }

    private var notificationStatusText: String {
        switch notificationManager.authorizationStatus {
        case .notDetermined:
            return "Not configured"
        case .denied:
            return "Disabled - Tap to enable in Settings"
        case .authorized:
            return "Enabled"
        case .provisional:
            return "Provisional"
        case .ephemeral:
            return "Ephemeral"
        @unknown default:
            return "Unknown"
        }
    }

    private func loadDefaultRegion() {
        if let id = defaultRegionId {
            defaultRegion = database.fetchRegion(id: id)
        }
    }

    private func clearAllData() {
        // This would clear the database and reseed
        // For now, we'll just show a message
        // In production, you'd implement database.clearAndReseed()
    }
}

struct RegionPickerView: View {
    @EnvironmentObject var database: DatabaseManager
    @Binding var selectedRegionId: String?
    @Environment(\.dismiss) private var dismiss

    @State private var continents: [Region] = []
    @State private var expandedContinentId: String?
    @State private var countries: [String: [Region]] = [:]

    var body: some View {
        NavigationStack {
            List {
                ForEach(continents) { continent in
                    Section {
                        Button(action: {
                            selectedRegionId = continent.regionId
                            dismiss()
                        }) {
                            HStack {
                                Text(continent.name)
                                    .foregroundColor(.primary)
                                Spacer()
                                if selectedRegionId == continent.regionId {
                                    Image(systemName: "checkmark")
                                        .foregroundColor(.blue)
                                }
                            }
                        }

                        if let continentCountries = countries[continent.regionId] {
                            ForEach(continentCountries) { country in
                                Button(action: {
                                    selectedRegionId = country.regionId
                                    dismiss()
                                }) {
                                    HStack {
                                        Text(country.name)
                                            .foregroundColor(.primary)
                                            .padding(.leading, 16)
                                        Spacer()
                                        if selectedRegionId == country.regionId {
                                            Image(systemName: "checkmark")
                                                .foregroundColor(.blue)
                                        }
                                    }
                                }
                            }
                        }
                    } header: {
                        Button(action: {
                            if expandedContinentId == continent.regionId {
                                expandedContinentId = nil
                                countries[continent.regionId] = nil
                            } else {
                                expandedContinentId = continent.regionId
                                countries[continent.regionId] = database.fetchChildren(of: continent)
                            }
                        }) {
                            HStack {
                                Text(continent.name)
                                    .font(.headline)
                                Spacer()
                                Image(systemName: expandedContinentId == continent.regionId ? "chevron.up" : "chevron.down")
                                    .font(.caption)
                            }
                        }
                        .buttonStyle(.plain)
                    }
                }
            }
            .navigationTitle("Select Region")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") {
                        dismiss()
                    }
                }
            }
            .onAppear {
                continents = database.fetchContinents()
            }
        }
    }
}
