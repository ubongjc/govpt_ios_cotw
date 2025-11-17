//
//  ContentView.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI

struct ContentView: View {
    @EnvironmentObject var database: DatabaseManager
    @State private var selectedTab = 0

    var body: some View {
        TabView(selection: $selectedTab) {
            InteractiveMapView()
                .tabItem {
                    Label("Map", systemImage: "map")
                }
                .tag(0)

            SearchView()
                .tabItem {
                    Label("Search", systemImage: "magnifyingglass")
                }
                .tag(1)

            MarketsView()
                .tabItem {
                    Label("Markets", systemImage: "chart.line.uptrend.xyaxis")
                }
                .tag(2)

            SettingsView()
                .tabItem {
                    Label("Settings", systemImage: "gearshape.fill")
                }
                .tag(3)
        }
    }
}

#Preview {
    ContentView()
        .environmentObject(DatabaseManager.shared)
}
