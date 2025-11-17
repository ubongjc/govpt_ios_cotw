//
//  InteractiveMapView.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI
import MapKit

struct InteractiveMapView: View {
    @StateObject private var viewModel = InteractiveMapViewModel()
    @EnvironmentObject var database: DatabaseManager
    @AppStorage("defaultRegionId") private var defaultRegionId: String?
    @State private var hasLoadedInitialData = false

    var body: some View {
        NavigationStack {
            ZStack {
                Map(position: $viewModel.cameraPosition, interactionModes: .all) {
                    ForEach(viewModel.visibleRegions) { region in
                        if let lat = region.latitude, let lon = region.longitude {
                            Annotation(region.name, coordinate: CLLocationCoordinate2D(latitude: lat, longitude: lon)) {
                                Button {
                                    viewModel.selectRegion(region)
                                } label: {
                                    VStack(spacing: 4) {
                                        ZStack {
                                            if region.type == .country {
                                                // Country flag emoji
                                                Text(countryFlagEmoji(for: region.isoCode))
                                                    .font(.system(size: markerSize(for: region.type) * 0.9))
                                            } else {
                                                // Other region types use colored circles
                                                Circle()
                                                    .fill(viewModel.electionStatusColor(for: region))
                                                    .frame(width: markerSize(for: region.type), height: markerSize(for: region.type))
                                                    .shadow(radius: 3)

                                                Image(systemName: iconName(for: region.type))
                                                    .font(.system(size: markerSize(for: region.type) * 0.5))
                                                    .foregroundColor(.white)
                                            }
                                        }
                                        .shadow(radius: 4)

                                        // Neon glowing solid dot election status indicator at the base
                                        if region.type == .country {
                                            ZStack {
                                                // Outer glow layers
                                                Circle()
                                                    .fill(viewModel.electionStatusColor(for: region).opacity(0.3))
                                                    .frame(width: 20, height: 20)
                                                    .blur(radius: 8)

                                                Circle()
                                                    .fill(viewModel.electionStatusColor(for: region).opacity(0.5))
                                                    .frame(width: 16, height: 16)
                                                    .blur(radius: 6)

                                                // Core bright dot
                                                Circle()
                                                    .fill(
                                                        RadialGradient(
                                                            colors: [
                                                                .white,
                                                                viewModel.electionStatusColor(for: region)
                                                            ],
                                                            center: .center,
                                                            startRadius: 0,
                                                            endRadius: 6
                                                        )
                                                    )
                                                    .frame(width: 10, height: 10)
                                                    .shadow(color: viewModel.electionStatusColor(for: region), radius: 8, x: 0, y: 0)
                                                    .shadow(color: viewModel.electionStatusColor(for: region), radius: 4, x: 0, y: 0)
                                                    .shadow(color: viewModel.electionStatusColor(for: region).opacity(0.8), radius: 2, x: 0, y: 0)
                                            }
                                        }

                                        Text(region.name)
                                            .font(.caption2)
                                            .fontWeight(.semibold)
                                            .foregroundColor(.primary)
                                            .padding(.horizontal, 6)
                                            .padding(.vertical, 2)
                                            .background(
                                                Capsule()
                                                    .fill(.ultraThinMaterial)
                                            )
                                            .shadow(radius: 1)
                                    }
                                }
                                .buttonStyle(.plain)
                            }
                            .tag(region.regionId)
                        }
                    }
                }
                .mapStyle(.standard(elevation: .realistic, pointsOfInterest: .excludingAll))
                .mapControls {
                    MapCompass()
                    MapScaleView()
                }


                // Breadcrumb navigation overlay
                VStack(spacing: 0) {
                    if !viewModel.navigationPath.isEmpty {
                        HStack(spacing: 8) {
                            Button {
                                viewModel.navigateToWorld()
                            } label: {
                                HStack(spacing: 4) {
                                    Image(systemName: "globe")
                                    Text("World")
                                }
                                .font(.caption)
                                .padding(.horizontal, 10)
                                .padding(.vertical, 6)
                                .background(Color.blue.opacity(0.15))
                                .cornerRadius(8)
                            }

                            ForEach(Array(viewModel.navigationPath.enumerated()), id: \.offset) { index, region in
                                Image(systemName: "chevron.right")
                                    .font(.caption2)
                                    .foregroundColor(.secondary)

                                Button {
                                    viewModel.navigateBack(to: index)
                                } label: {
                                    Text(region.name)
                                        .font(.caption)
                                        .padding(.horizontal, 10)
                                        .padding(.vertical, 6)
                                        .background(index == viewModel.navigationPath.count - 1 ? Color.blue : Color.blue.opacity(0.15))
                                        .foregroundColor(index == viewModel.navigationPath.count - 1 ? .white : .primary)
                                        .cornerRadius(8)
                                }
                            }

                            Spacer()
                        }
                        .padding()
                        .background(Color(.systemBackground).opacity(0.95))
                        .shadow(radius: 2)
                    }

                    Spacer()

                    // Bottom controls: Default Region (left) and Filter (right)
                    HStack(alignment: .bottom) {
                        // Go to Default Region Button - Bottom Left
                        if let defaultId = defaultRegionId {
                            VStack(alignment: .leading, spacing: 4) {
                                Button(action: {
                                    withAnimation(.spring()) {
                                        viewModel.navigateToRegion(regionId: defaultId)
                                    }
                                }) {
                                    Image(systemName: "star.fill")
                                        .font(.title2)
                                        .foregroundColor(.yellow)
                                        .padding(8)
                                        .background(
                                            Circle()
                                                .fill(.ultraThinMaterial)
                                                .shadow(radius: 2)
                                        )
                                }
                            }
                            .padding(.leading, 16)
                            .padding(.bottom, 8)
                        }

                        Spacer()

                        // Collapsible Election Status Filter - Bottom Right
                        VStack(alignment: .trailing, spacing: 4) {
                            if viewModel.showFilterLegend {
                                VStack(alignment: .leading, spacing: 8) {
                                    Text("Filter by Status")
                                        .font(.caption)
                                        .fontWeight(.semibold)
                                        .foregroundColor(.secondary)

                                    Button(action: { viewModel.toggleFilter(.upcoming) }) {
                                        HStack(spacing: 6) {
                                            Image(systemName: viewModel.activeFilters.contains(.upcoming) ? "checkmark.circle.fill" : "circle")
                                                .foregroundColor(.yellow)
                                            Circle()
                                                .fill(Color.yellow)
                                                .frame(width: 10, height: 10)
                                                .shadow(color: .yellow, radius: 4)
                                            Text("Within 6 months")
                                                .font(.caption2)
                                                .foregroundColor(.primary)
                                        }
                                    }

                                    Button(action: { viewModel.toggleFilter(.noElection) }) {
                                        HStack(spacing: 6) {
                                            Image(systemName: viewModel.activeFilters.contains(.noElection) ? "checkmark.circle.fill" : "circle")
                                                .foregroundColor(.blue)
                                            Circle()
                                                .fill(Color.blue)
                                                .frame(width: 10, height: 10)
                                                .shadow(color: .blue, radius: 4)
                                            Text("No active election")
                                                .font(.caption2)
                                                .foregroundColor(.primary)
                                        }
                                    }

                                    Button(action: { viewModel.toggleFilter(.nonDemocratic) }) {
                                        HStack(spacing: 6) {
                                            Image(systemName: viewModel.activeFilters.contains(.nonDemocratic) ? "checkmark.circle.fill" : "circle")
                                                .foregroundColor(.gray)
                                            Circle()
                                                .fill(Color.gray)
                                                .frame(width: 10, height: 10)
                                                .shadow(color: .gray, radius: 4)
                                            Text("Non-democratic")
                                                .font(.caption2)
                                                .foregroundColor(.primary)
                                        }
                                    }
                                }
                                .padding(10)
                                .background(
                                    RoundedRectangle(cornerRadius: 10)
                                        .fill(.ultraThinMaterial)
                                        .shadow(radius: 2)
                                )
                                .transition(.move(edge: .trailing).combined(with: .opacity))
                            }

                            // Toggle button
                            Button(action: {
                                withAnimation(.spring()) {
                                    viewModel.showFilterLegend.toggle()
                                }
                            }) {
                                Image(systemName: viewModel.showFilterLegend ? "xmark.circle.fill" : "line.3.horizontal.decrease.circle.fill")
                                    .font(.title2)
                                    .foregroundColor(.blue)
                                    .padding(8)
                                    .background(
                                        Circle()
                                            .fill(.ultraThinMaterial)
                                            .shadow(radius: 2)
                                    )
                            }
                        }
                        .padding(.trailing, 16)
                        .padding(.bottom, 8)
                    }

                    // Region detail panel
                    if let selected = viewModel.selectedRegion {
                        RegionInfoPanel(
                            region: selected,
                            officeholder: viewModel.currentOfficeholder,
                            promisesCount: viewModel.promisesCount,
                            onClose: {
                                viewModel.selectedRegion = nil
                            },
                            onSetDefault: {
                                defaultRegionId = selected.regionId
                                viewModel.showMessage("Set as default region")
                            },
                            onViewDetails: {
                                viewModel.showingDetailView = true
                            }
                        )
                        .transition(.move(edge: .bottom).combined(with: .opacity))
                        .animation(.spring(), value: viewModel.selectedRegion != nil)
                    }
                }
            }
            .navigationTitle(viewModel.currentLevelTitle)
            .navigationBarTitleDisplayMode(.large)
            .sheet(isPresented: $viewModel.showingDetailView) {
                if let region = viewModel.selectedRegion, region.type == .country {
                    CountryView(region: region)
                }
            }
            .overlay {
                if let message = viewModel.messageText {
                    VStack {
                        Spacer()
                        Text(message)
                            .padding()
                            .background(Color.black.opacity(0.8))
                            .foregroundColor(.white)
                            .cornerRadius(10)
                            .padding(.bottom, 60)
                    }
                    .transition(.move(edge: .bottom).combined(with: .opacity))
                }
            }
            .onAppear {
                viewModel.database = database
                if !hasLoadedInitialData {
                    viewModel.loadInitialData(defaultRegionId: defaultRegionId)
                    hasLoadedInitialData = true
                }
            }
        }
    }

    private func markerSize(for type: Region.RegionType) -> CGFloat {
        switch type {
        case .continent: return 44
        case .country: return 36
        case .state, .province: return 30
        case .city: return 24
        }
    }

    private func iconName(for type: Region.RegionType) -> String {
        switch type {
        case .continent: return "globe"
        case .country: return "flag.fill"
        case .state, .province: return "mappin.circle.fill"
        case .city: return "building.2.fill"
        }
    }

    private func countryFlagEmoji(for isoCode: String) -> String {
        let base: UInt32 = 127397
        var flag = ""
        for scalar in isoCode.uppercased().unicodeScalars {
            if let scalarValue = UnicodeScalar(base + scalar.value) {
                flag.append(String(scalarValue))
            }
        }
        return flag.isEmpty ? "🏴" : flag
    }
}

struct RegionInfoPanel: View {
    let region: Region
    let officeholder: Officeholder?
    let promisesCount: Int
    let onClose: () -> Void
    let onSetDefault: () -> Void
    let onViewDetails: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            // Header with close button
            HStack {
                VStack(alignment: .leading, spacing: 4) {
                    Text(region.name)
                        .font(.title2)
                        .fontWeight(.bold)

                    Text(region.type.rawValue.capitalized)
                        .font(.caption)
                        .foregroundColor(.secondary)
                }

                Spacer()

                Button(action: onClose) {
                    Image(systemName: "xmark.circle.fill")
                        .font(.title2)
                        .foregroundColor(.secondary)
                }
            }

            // Officeholder info
            if let officeholder = officeholder {
                VStack(alignment: .leading, spacing: 8) {
                    HStack {
                        Image(systemName: "person.circle.fill")
                            .foregroundColor(.blue)
                            .font(.title3)

                        VStack(alignment: .leading, spacing: 2) {
                            Text(officeholder.name)
                                .font(.headline)
                            Text(officeholder.title)
                                .font(.subheadline)
                                .foregroundColor(.secondary)
                        }
                    }

                    if let party = officeholder.partyName {
                        Text(party)
                            .font(.caption)
                            .padding(.horizontal, 8)
                            .padding(.vertical, 4)
                            .background(Color.blue.opacity(0.15))
                            .cornerRadius(6)
                    }
                }
            }

            // Promises count
            if promisesCount > 0 {
                HStack {
                    Image(systemName: "checkmark.seal.fill")
                        .foregroundColor(.green)
                    Text("\(promisesCount) tracked \(promisesCount == 1 ? "promise" : "promises")")
                        .font(.subheadline)
                }
            }

            // Upcoming election info
            if let nextElection = region.nextElection, nextElection >= Date() {
                VStack(alignment: .leading, spacing: 6) {
                    HStack(spacing: 8) {
                        Image(systemName: "calendar.badge.exclamationmark")
                            .foregroundColor(.yellow)
                            .font(.title3)

                        VStack(alignment: .leading, spacing: 2) {
                            Text("Upcoming Election")
                                .font(.headline)
                                .foregroundColor(.primary)
                            Text(nextElection, format: .dateTime.month(.wide).day().year())
                                .font(.subheadline)
                                .foregroundColor(.secondary)
                        }
                    }
                }
                .padding(12)
                .background(Color.yellow.opacity(0.15))
                .cornerRadius(10)
            }

            // Action buttons
            HStack(spacing: 12) {
                Button(action: onSetDefault) {
                    Label("Set Default", systemImage: "star.fill")
                        .font(.footnote)
                        .padding(.horizontal, 12)
                        .padding(.vertical, 8)
                        .background(Color.blue.opacity(0.15))
                        .foregroundColor(.blue)
                        .cornerRadius(8)
                }

                if promisesCount > 0 {
                    Button(action: onViewDetails) {
                        Label("View Details", systemImage: "arrow.right.circle.fill")
                            .font(.footnote)
                            .padding(.horizontal, 12)
                            .padding(.vertical, 8)
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(8)
                    }
                }
            }
        }
        .padding()
        .background(
            RoundedRectangle(cornerRadius: 16)
                .fill(Color(.systemBackground))
                .shadow(radius: 10)
        )
        .padding()
    }
}

enum ElectionStatusFilter: Hashable {
    case upcoming
    case noElection
    case nonDemocratic
}

@MainActor
class InteractiveMapViewModel: ObservableObject {
    @Published var cameraPosition: MapCameraPosition = .region(MKCoordinateRegion(
        center: CLLocationCoordinate2D(latitude: 20, longitude: 10),
        span: MKCoordinateSpan(latitudeDelta: 180, longitudeDelta: 360)
    ))
    @Published var visibleRegions: [Region] = []
    @Published var navigationPath: [Region] = []
    @Published var selectedRegion: Region?
    @Published var currentOfficeholder: Officeholder?
    @Published var promisesCount: Int = 0
    @Published var showingDetailView = false
    @Published var messageText: String?
    @Published var activeFilters: Set<ElectionStatusFilter> = []
    @Published var showFilterLegend = false

    private var allRegions: [Region] = []
    var database: DatabaseManager?

    var currentLevelTitle: String {
        if let last = navigationPath.last {
            return last.name
        }
        return "GPT"
    }

    func loadInitialData(defaultRegionId: String?) {
        if let defaultId = defaultRegionId,
           let defaultRegion = database?.fetchRegion(id: defaultId) {
            // Build path to default region
            buildPathToRegion(defaultRegion)
            // Add the default region itself to the path
            navigationPath.append(defaultRegion)
            // Load children of the default region
            let children = database?.fetchChildren(of: defaultRegion) ?? []
            allRegions = children
            applyFilters()
            // Animate directly to the default region
            animateToRegion(defaultRegion)
        } else {
            loadContinents()
        }
    }

    func loadContinents() {
        allRegions = database?.fetchContinents() ?? []
        applyFilters()
        navigationPath = []
        animateToWorld()
    }

    func toggleFilter(_ filter: ElectionStatusFilter) {
        if activeFilters.contains(filter) {
            activeFilters.remove(filter)
        } else {
            activeFilters.insert(filter)
        }
        applyFilters()
    }

    func applyFilters() {
        if activeFilters.isEmpty {
            visibleRegions = allRegions
        } else {
            visibleRegions = allRegions.filter { region in
                let status = getElectionStatus(region)
                return activeFilters.contains(status)
            }
        }
    }

    func getElectionStatus(_ region: Region) -> ElectionStatusFilter {
        if region.electionSystem == "non-democratic" {
            return .nonDemocratic
        }

        guard let nextElection = region.nextElection else {
            return .noElection
        }

        let now = Date()
        let calendar = Calendar.current

        // Get date components for today and election date (ignoring time)
        let todayComponents = calendar.dateComponents([.year, .month, .day], from: now)
        let electionComponents = calendar.dateComponents([.year, .month, .day], from: nextElection)

        // Check if election is on the same day as today (regardless of time)
        let isToday = todayComponents.year == electionComponents.year &&
                      todayComponents.month == electionComponents.month &&
                      todayComponents.day == electionComponents.day

        // Check if election is today or in the future
        if isToday || nextElection > now {
            let sixMonthsFromNow = calendar.date(byAdding: .month, value: 6, to: now) ?? now
            if nextElection <= sixMonthsFromNow {
                return .upcoming
            }
        }

        return .noElection
    }

    func selectRegion(_ region: Region) {
        selectedRegion = region
        loadRegionDetails(region)

        // Zoom to the selected region first
        animateToRegion(region)

        // Check if has children, then drill down
        let children = database?.fetchChildren(of: region) ?? []
        if !children.isEmpty {
            // Has children, prepare for drill down with longer delay
            DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
                self.drillInto(region, children: children)
            }
        }
    }

    func drillInto(_ region: Region, children: [Region]) {
        navigationPath.append(region)
        allRegions = children
        applyFilters()
        animateToRegion(region)
    }

    func navigateToWorld() {
        selectedRegion = nil
        loadContinents()
    }

    func navigateBack(to index: Int) {
        guard index < navigationPath.count else { return }

        selectedRegion = nil
        let targetRegion = navigationPath[index]
        navigationPath = Array(navigationPath.prefix(index + 1))

        let children = database?.fetchChildren(of: targetRegion) ?? []
        allRegions = children
        applyFilters()
        animateToRegion(targetRegion)
    }

    func navigateToRegion(regionId: String) {
        guard let region = database?.fetchRegion(id: regionId) else { return }

        selectedRegion = nil
        // Build path to the region
        buildPathToRegion(region)
        // Add the region itself to the path
        navigationPath.append(region)
        // Load children of the region
        let children = database?.fetchChildren(of: region) ?? []
        allRegions = children
        applyFilters()
        // Animate to the region
        animateToRegion(region)
    }

    func loadRegionDetails(_ region: Region) {
        currentOfficeholder = database?.fetchCurrentOfficeholder(for: region)
        promisesCount = database?.fetchPromisesCount(for: region) ?? 0
    }

    func electionStatusColor(for region: Region) -> Color {
        if region.electionSystem == "non-democratic" {
            return Color.gray
        }

        guard let nextElection = region.nextElection else {
            return Color.blue
        }

        let now = Date()
        let calendar = Calendar.current

        // Get date components for today and election date (ignoring time)
        let todayComponents = calendar.dateComponents([.year, .month, .day], from: now)
        let electionComponents = calendar.dateComponents([.year, .month, .day], from: nextElection)

        // Check if election is on the same day as today (regardless of time)
        let isToday = todayComponents.year == electionComponents.year &&
                      todayComponents.month == electionComponents.month &&
                      todayComponents.day == electionComponents.day

        // Check if election is today or in the future
        if isToday || nextElection > now {
            let sixMonthsFromNow = calendar.date(byAdding: .month, value: 6, to: now) ?? now
            if nextElection <= sixMonthsFromNow {
                // Election is today or within 6 months - yellow
                return Color.yellow
            }
        }

        // Election has passed or is more than 6 months away - blue
        return Color.blue
    }

    func hasUpcomingElection(_ region: Region) -> Bool {
        guard let nextElection = database?.fetchNextElectionDate(for: region) else {
            return false
        }
        let sixMonthsFromNow = Calendar.current.date(byAdding: .month, value: 6, to: Date()) ?? Date()
        return nextElection <= sixMonthsFromNow && nextElection >= Date()
    }

    func showMessage(_ text: String) {
        messageText = text
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            self.messageText = nil
        }
    }

    private func animateToWorld() {
        withAnimation(.easeInOut(duration: 1.0)) {
            cameraPosition = .region(MKCoordinateRegion(
                center: CLLocationCoordinate2D(latitude: 20, longitude: 10),
                span: MKCoordinateSpan(latitudeDelta: 180, longitudeDelta: 360)
            ))
        }
    }

    private func animateToRegion(_ region: Region) {
        guard let lat = region.latitude, let lon = region.longitude else { return }

        let span: MKCoordinateSpan
        switch region.type {
        case .continent:
            span = MKCoordinateSpan(latitudeDelta: 40, longitudeDelta: 40)
        case .country:
            span = MKCoordinateSpan(latitudeDelta: 10, longitudeDelta: 10)
        case .state, .province:
            span = MKCoordinateSpan(latitudeDelta: 3, longitudeDelta: 3)
        case .city:
            span = MKCoordinateSpan(latitudeDelta: 0.3, longitudeDelta: 0.3)
        }

        withAnimation(.easeInOut(duration: 1.0)) {
            cameraPosition = .region(MKCoordinateRegion(
                center: CLLocationCoordinate2D(latitude: lat, longitude: lon),
                span: span
            ))
        }
    }

    private func buildPathToRegion(_ region: Region) {
        var path: [Region] = []
        var current: Region? = region

        while let parentId = current?.parentRegionId,
              let parent = database?.fetchRegion(id: parentId) {
            path.insert(parent, at: 0)
            current = parent
        }

        navigationPath = path
    }
}
