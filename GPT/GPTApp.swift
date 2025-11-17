//
//  GPTApp.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI

@main
struct GPTApp: App {
    @StateObject private var database = DatabaseManager.shared
    @AppStorage("hasCompletedOnboarding") private var hasCompletedOnboarding = false

    var body: some Scene {
        WindowGroup {
            if database.isInitialized {
                if hasCompletedOnboarding {
                    ContentView()
                        .environmentObject(database)
                } else {
                    OnboardingView()
                        .environmentObject(database)
                }
            } else {
                LoadingView()
            }
        }
    }
}

struct LoadingView: View {
    var body: some View {
        ZStack {
            Color.blue.opacity(0.1)
                .ignoresSafeArea()

            VStack(spacing: 24) {
                ProgressView()
                    .scaleEffect(1.5)
                    .tint(.blue)

                Text("Global Promises Tracker")
                    .font(.largeTitle)
                    .fontWeight(.bold)
                    .multilineTextAlignment(.center)

                Text("Loading data...")
                    .font(.subheadline)
                    .foregroundColor(.secondary)
            }
            .padding()
        }
    }
}
