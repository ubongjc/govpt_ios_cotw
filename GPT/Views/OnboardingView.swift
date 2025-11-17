//
//  OnboardingView.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI

struct OnboardingView: View {
    @AppStorage("hasCompletedOnboarding") private var hasCompletedOnboarding = false
    @State private var currentPage = 0
    @EnvironmentObject var database: DatabaseManager
    @StateObject private var notificationManager = NotificationManager.shared

    var body: some View {
        ZStack {
            // Background gradient
            LinearGradient(
                colors: [.blue.opacity(0.3), .purple.opacity(0.3)],
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
            .ignoresSafeArea()

            VStack(spacing: 0) {
                // Page indicator
                HStack(spacing: 8) {
                    ForEach(0..<3) { index in
                        Circle()
                            .fill(index == currentPage ? Color.blue : Color.gray.opacity(0.3))
                            .frame(width: 8, height: 8)
                    }
                }
                .padding(.top, 24)

                // Content pages
                TabView(selection: $currentPage) {
                    WelcomePage()
                        .tag(0)

                    FeaturesPage()
                        .tag(1)

                    NotificationsPage(
                        notificationManager: notificationManager,
                        onComplete: {
                            hasCompletedOnboarding = true
                        }
                    )
                    .tag(2)
                }
                .tabViewStyle(.page(indexDisplayMode: .never))

                // Navigation buttons
                HStack {
                    if currentPage > 0 {
                        Button(action: { withAnimation { currentPage -= 1 } }) {
                            Text("Back")
                                .foregroundColor(.blue)
                                .padding(.horizontal, 24)
                                .padding(.vertical, 12)
                        }
                    }

                    Spacer()

                    if currentPage < 2 {
                        Button(action: { withAnimation { currentPage += 1 } }) {
                            Text("Next")
                                .fontWeight(.semibold)
                                .foregroundColor(.white)
                                .padding(.horizontal, 32)
                                .padding(.vertical, 12)
                                .background(Color.blue)
                                .cornerRadius(12)
                        }
                    }
                }
                .padding(.horizontal, 24)
                .padding(.bottom, 32)
            }
        }
    }
}

struct WelcomePage: View {
    var body: some View {
        VStack(spacing: 32) {
            Spacer()

            Image(systemName: "globe.americas.fill")
                .font(.system(size: 100))
                .foregroundStyle(
                    LinearGradient(
                        colors: [.blue, .purple],
                        startPoint: .topLeading,
                        endPoint: .bottomTrailing
                    )
                )

            VStack(spacing: 16) {
                Text("Welcome to")
                    .font(.title2)
                    .foregroundColor(.secondary)

                Text("Global Promises Tracker")
                    .font(.system(size: 36, weight: .bold))
                    .multilineTextAlignment(.center)
                    .fixedSize(horizontal: false, vertical: true)

                Text("Track political promises and hold leaders accountable worldwide")
                    .font(.body)
                    .foregroundColor(.secondary)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 32)
            }

            Spacer()
        }
        .padding()
    }
}

struct FeaturesPage: View {
    var body: some View {
        VStack(spacing: 32) {
            Spacer()

            Text("Key Features")
                .font(.system(size: 32, weight: .bold))

            VStack(spacing: 24) {
                FeatureRow(
                    icon: "map.fill",
                    title: "Interactive Map",
                    description: "Explore regions worldwide and drill down from continents to cities"
                )

                FeatureRow(
                    icon: "checklist",
                    title: "Promise Tracking",
                    description: "Monitor campaign promises with status updates and evidence"
                )

                FeatureRow(
                    icon: "chart.line.uptrend.xyaxis",
                    title: "Market Impact",
                    description: "See how promises affect industries and markets"
                )

                FeatureRow(
                    icon: "calendar.badge.clock",
                    title: "Election Alerts",
                    description: "Get notified about upcoming elections in your region"
                )
            }
            .padding(.horizontal, 32)

            Spacer()
        }
        .padding()
    }
}

struct FeatureRow: View {
    let icon: String
    let title: String
    let description: String

    var body: some View {
        HStack(alignment: .top, spacing: 16) {
            Image(systemName: icon)
                .font(.title)
                .foregroundColor(.blue)
                .frame(width: 40)

            VStack(alignment: .leading, spacing: 4) {
                Text(title)
                    .font(.headline)

                Text(description)
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .fixedSize(horizontal: false, vertical: true)
            }
        }
    }
}

struct NotificationsPage: View {
    @ObservedObject var notificationManager: NotificationManager
    let onComplete: () -> Void
    @State private var showingComplete = false

    var body: some View {
        VStack(spacing: 32) {
            Spacer()

            Image(systemName: "bell.badge.fill")
                .font(.system(size: 80))
                .foregroundColor(.blue)

            VStack(spacing: 16) {
                Text("Stay Informed")
                    .font(.system(size: 32, weight: .bold))

                Text("Get notified about upcoming elections in regions you follow")
                    .font(.body)
                    .foregroundColor(.secondary)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 32)
            }

            VStack(spacing: 16) {
                Button(action: {
                    Task {
                        let granted = await notificationManager.requestAuthorization()
                        if granted {
                            showingComplete = true
                            DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
                                onComplete()
                            }
                        }
                    }
                }) {
                    HStack {
                        Image(systemName: "bell.fill")
                        Text("Enable Notifications")
                    }
                    .font(.headline)
                    .foregroundColor(.white)
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 16)
                    .background(Color.blue)
                    .cornerRadius(12)
                }
                .padding(.horizontal, 32)

                Button(action: {
                    showingComplete = true
                    DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
                        onComplete()
                    }
                }) {
                    Text("Skip for Now")
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                }
            }

            if showingComplete {
                HStack {
                    Image(systemName: "checkmark.circle.fill")
                        .foregroundColor(.green)
                    Text("Getting Started...")
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                }
                .transition(.scale.combined(with: .opacity))
            }

            Spacer()
        }
        .padding()
        .animation(.easeInOut, value: showingComplete)
    }
}
