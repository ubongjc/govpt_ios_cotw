//
//  NotificationManager.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import Foundation
import UserNotifications

@MainActor
class NotificationManager: ObservableObject {
    static let shared = NotificationManager()

    @Published var authorizationStatus: UNAuthorizationStatus = .notDetermined

    private let center = UNUserNotificationCenter.current()

    private init() {
        Task {
            await checkAuthorizationStatus()
        }
    }

    /// Request notification permissions from the user
    func requestAuthorization() async -> Bool {
        do {
            let granted = try await center.requestAuthorization(options: [.alert, .badge, .sound])
            await checkAuthorizationStatus()
            return granted
        } catch {
            print("Error requesting notification authorization: \(error)")
            return false
        }
    }

    /// Check current authorization status
    func checkAuthorizationStatus() async {
        let settings = await center.notificationSettings()
        authorizationStatus = settings.authorizationStatus
    }

    /// Schedule election reminder notifications for a region
    func scheduleElectionReminders(for region: Region) async {
        guard let electionDate = region.nextElection else { return }

        // Cancel any existing notifications for this region
        await cancelElectionReminders(for: region.regionId)

        let now = Date()
        let calendar = Calendar.current

        // Schedule notifications at different intervals
        let intervals: [(days: Int, title: String, identifier: String)] = [
            (7, "Election in 1 week", "election_1week"),
            (1, "Election tomorrow", "election_1day"),
            (0, "Election today", "election_today")
        ]

        for interval in intervals {
            guard let triggerDate = calendar.date(byAdding: .day, value: -interval.days, to: electionDate),
                  triggerDate > now else { continue }

            let content = UNMutableNotificationContent()
            content.title = interval.title
            content.body = "\(region.name) election on \(electionDate.formatted(date: .abbreviated, time: .omitted))"
            content.sound = .default
            content.categoryIdentifier = "ELECTION_REMINDER"
            content.userInfo = [
                "regionId": region.regionId,
                "regionName": region.name,
                "electionDate": electionDate.timeIntervalSince1970
            ]

            let components = calendar.dateComponents([.year, .month, .day, .hour, .minute], from: triggerDate)
            let trigger = UNCalendarNotificationTrigger(dateMatching: components, repeats: false)

            let identifier = "\(interval.identifier)_\(region.regionId)"
            let request = UNNotificationRequest(identifier: identifier, content: content, trigger: trigger)

            do {
                try await center.add(request)
                print("Scheduled \(interval.title) notification for \(region.name) at \(triggerDate)")
            } catch {
                print("Error scheduling notification: \(error)")
            }
        }
    }

    /// Schedule reminders for all regions with upcoming elections
    func scheduleAllElectionReminders(regions: [Region]) async {
        for region in regions {
            if region.nextElection != nil {
                await scheduleElectionReminders(for: region)
            }
        }
    }

    /// Cancel election reminders for a specific region
    func cancelElectionReminders(for regionId: String) async {
        let identifiers = [
            "election_1week_\(regionId)",
            "election_1day_\(regionId)",
            "election_today_\(regionId)"
        ]
        center.removePendingNotificationRequests(withIdentifiers: identifiers)
    }

    /// Cancel all election reminders
    func cancelAllElectionReminders() {
        center.removeAllPendingNotificationRequests()
    }

    /// Get all pending notification requests (for debugging)
    func getPendingNotifications() async -> [UNNotificationRequest] {
        return await center.pendingNotificationRequests()
    }
}
