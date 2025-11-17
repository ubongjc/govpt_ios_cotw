//
//  HierarchicalMapView.swift
//  Government Promises Tracker
//
//  Created by Claude Code
//

import SwiftUI
import MapKit

struct HierarchicalMapView: View {
    @StateObject private var viewModel = MapViewModel()
    @EnvironmentObject var database: DatabaseManager
    @AppStorage("defaultRegionId") private var defaultRegionId: String?

    var body: some View {
        NavigationStack {
            ZStack {
                Map(position: $viewModel.cameraPosition, selection: $viewModel.selectedRegionId) {
                    // Draw region markers
                    ForEach(viewModel.visibleRegions) { region in
                        if let lat = region.latitude, let lon = region.longitude {
                            Annotation(region.name, coordinate: CLLocationCoordinate2D(latitude: lat, longitude: lon)) {
                                RegionMarker(
                                    region: region,
                                    electionStatus: viewModel.getElectionStatus(region),
                                    onTap: {
                                        viewModel.selectRegion(region)
                                    }
                                )
                            }
                        }
                    }
                }
                .mapStyle(.standard(elevation: .realistic, pointsOfInterest: .excludingAll))
                .mapControls {
                    // No default controls - we handle everything custom
                }
                .ignoresSafeArea(edges: .top)
                .onChange(of: viewModel.selectedRegionId) { oldValue, newValue in
                    if newValue != nil {
                        viewModel.zoomIntoSelection()
                    }
                }

                // Custom boundary overlay drawn with Core Graphics
                MapBoundaryOverlay(
                    regions: viewModel.visibleRegions.filter { $0.boundaryCoordinates != nil },
                    cameraPosition: viewModel.cameraPosition
                )
                .allowsHitTesting(false)

                // Breadcrumb navigation
                VStack {
                    if !viewModel.navigationPath.isEmpty {
                        ScrollView(.horizontal, showsIndicators: false) {
                            HStack(spacing: 8) {
                                Button {
                                    viewModel.navigateToWorld()
                                } label: {
                                    Text("🌍 World")
                                        .font(.caption)
                                        .padding(.horizontal, 12)
                                        .padding(.vertical, 6)
                                        .background(Color.blue.opacity(0.2))
                                        .cornerRadius(8)
                                }

                                ForEach(viewModel.navigationPath.indices, id: \.self) { index in
                                    Image(systemName: "chevron.right")
                                        .font(.caption2)
                                        .foregroundColor(.secondary)

                                    Button {
                                        viewModel.navigateBack(to: index)
                                    } label: {
                                        Text(viewModel.navigationPath[index].name)
                                            .font(.caption)
                                            .padding(.horizontal, 12)
                                            .padding(.vertical, 6)
                                            .background(index == viewModel.navigationPath.count - 1 ? Color.blue : Color.blue.opacity(0.2))
                                            .foregroundColor(index == viewModel.navigationPath.count - 1 ? .white : .primary)
                                            .cornerRadius(8)
                                    }
                                }
                            }
                            .padding(.horizontal)
                        }
                        .padding(.top, 8)
                        .background(Color(.systemBackground).opacity(0.95))
                    }

                    Spacer()

                    // Region details panel
                    if let selected = viewModel.selectedRegion {
                        RegionDetailPanel(
                            region: selected,
                            officeholder: viewModel.currentOfficeholder,
                            promisesCount: viewModel.promisesCount,
                            onClose: { viewModel.selectedRegionId = nil },
                            onSetDefault: {
                                defaultRegionId = selected.regionId
                                viewModel.showingMessage = "Set as default region"
                            },
                            onViewPromises: {
                                viewModel.showingCountryView = true
                            }
                        )
                    }
                }
            }
            .navigationTitle(viewModel.currentRegion?.name ?? "GPT")
            .navigationBarTitleDisplayMode(.large)
            .sheet(isPresented: $viewModel.showingCountryView) {
                if let region = viewModel.selectedRegion {
                    CountryView(region: region)
                        .environmentObject(database)
                }
            }
            .overlay {
                if let message = viewModel.showingMessage {
                    VStack {
                        Spacer()
                        Text(message)
                            .padding()
                            .background(Color.black.opacity(0.8))
                            .foregroundColor(.white)
                            .cornerRadius(10)
                            .padding()
                    }
                    .transition(.move(edge: .bottom).combined(with: .opacity))
                    .animation(.easeInOut, value: viewModel.showingMessage)
                    .onAppear {
                        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                            viewModel.showingMessage = nil
                        }
                    }
                }
            }
            .onAppear {
                viewModel.database = database
                viewModel.loadInitialRegion(defaultRegionId: defaultRegionId)
            }
        }
    }
}

enum ElectionStatus {
    case upcoming       // Yellow - election within 6 months
    case noElection     // Blue - no active election
    case nonDemocratic  // Grey - non-democratic system
}

struct RegionMarker: View {
    let region: Region
    let electionStatus: ElectionStatus
    let onTap: () -> Void

    var body: some View {
        VStack(spacing: 4) {
            // Main marker
            ZStack {
                if region.type == .country {
                    // Country flag emoji
                    let _ = print("🚨 DEBUG: Showing flag for country: \(region.name), ISO: \(region.isoCode), Flag: \(countryFlag)")
                    Text(countryFlag)
                        .font(.system(size: markerSize * 0.9))
                } else {
                    let _ = print("⚠️ DEBUG: NOT a country - Region: \(region.name), Type: \(region.type)")
                    // Other region types use colored circles
                    Circle()
                        .fill(markerColor)
                        .frame(width: markerSize, height: markerSize)

                    Image(systemName: iconName)
                        .font(.caption)
                        .foregroundColor(.white)
                }
            }
            .shadow(radius: 4)

            // Glassy election status indicator at the base
            if region.nextElection != nil {
                Circle()
                    .fill(electionIndicatorColor.opacity(0.3))
                    .frame(width: 16, height: 16)
                    .background(
                        Circle()
                            .fill(.ultraThinMaterial)
                            .frame(width: 16, height: 16)
                    )
                    .overlay(
                        Circle()
                            .stroke(electionIndicatorColor, lineWidth: 2)
                            .frame(width: 16, height: 16)
                    )
                    .shadow(color: electionIndicatorColor.opacity(0.5), radius: 4)
            }

            Text(region.name)
                .font(.caption2)
                .fontWeight(.medium)
                .padding(4)
                .background(Capsule().fill(.white.opacity(0.9)))
                .shadow(radius: 2)
        }
        .onTapGesture(perform: onTap)
    }

    private var countryFlag: String {
        // Map ISO codes to flag emojis
        let isoCode = region.isoCode.uppercased()
        let base: UInt32 = 127397
        var flag = ""
        for scalar in isoCode.unicodeScalars {
            if let scalarValue = UnicodeScalar(base + scalar.value) {
                flag.append(String(scalarValue))
            }
        }
        return flag.isEmpty ? "🏴" : flag
    }

    private var markerColor: Color {
        switch region.type {
        case .country:
            return .blue
        case .continent:
            return .purple
        case .state, .province:
            return .indigo
        case .city:
            return .teal
        }
    }

    private var electionIndicatorColor: Color {
        switch electionStatus {
        case .upcoming:
            return .yellow
        case .noElection:
            return .blue
        case .nonDemocratic:
            return .gray
        }
    }

    private var iconName: String {
        switch region.type {
        case .continent:
            return "globe"
        case .country:
            return "flag.fill"
        case .state, .province:
            return "mappin.circle.fill"
        case .city:
            return "building.2.fill"
        }
    }

    private var markerSize: CGFloat {
        switch region.type {
        case .continent:
            return 40
        case .country:
            return 32
        case .state, .province:
            return 28
        case .city:
            return 24
        }
    }
}

struct RegionDetailPanel: View {
    let region: Region
    let officeholder: Officeholder?
    let promisesCount: Int
    let onClose: () -> Void
    let onSetDefault: () -> Void
    let onViewPromises: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            HStack {
                VStack(alignment: .leading, spacing: 8) {
                    Text(region.name)
                        .font(.title2)
                        .fontWeight(.bold)

                    if let officeholder = officeholder {
                        HStack {
                            Image(systemName: "person.circle.fill")
                                .foregroundColor(.blue)
                            VStack(alignment: .leading) {
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
                                .background(Color.blue.opacity(0.2))
                                .cornerRadius(4)
                        }
                    }

                    if promisesCount > 0 {
                        HStack {
                            Image(systemName: "checkmark.circle.fill")
                                .foregroundColor(.green)
                            Text("\(promisesCount) tracked promises")
                                .font(.subheadline)
                                .foregroundColor(.secondary)
                        }
                    }
                }

                Spacer()

                Button(action: onClose) {
                    Image(systemName: "xmark.circle.fill")
                        .font(.title2)
                        .foregroundColor(.secondary)
                }
            }

            HStack(spacing: 12) {
                Button(action: onSetDefault) {
                    Label("Set as Default", systemImage: "star.fill")
                        .font(.caption)
                        .padding(.horizontal, 12)
                        .padding(.vertical, 8)
                        .background(Color.blue.opacity(0.2))
                        .cornerRadius(8)
                }

                if promisesCount > 0 {
                    Button(action: onViewPromises) {
                        Label("View Promises", systemImage: "list.bullet")
                            .font(.caption)
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
        .background(Color(.systemBackground).opacity(0.95))
        .cornerRadius(16)
        .shadow(radius: 8)
        .padding()
    }
}

@MainActor
class MapViewModel: ObservableObject {
    @Published var cameraPosition: MapCameraPosition = .region(MKCoordinateRegion(
        center: CLLocationCoordinate2D(latitude: 20, longitude: 0),
        span: MKCoordinateSpan(latitudeDelta: 120, longitudeDelta: 120)
    ))
    @Published var visibleRegions: [Region] = []
    @Published var navigationPath: [Region] = []
    @Published var selectedRegionId: String?
    @Published var selectedRegion: Region?
    @Published var currentRegion: Region?
    @Published var currentOfficeholder: Officeholder?
    @Published var promisesCount: Int = 0
    @Published var showingCountryView = false
    @Published var showingMessage: String?

    var database: DatabaseManager?

    func loadInitialRegion(defaultRegionId: String?) {
        if let defaultId = defaultRegionId,
           let defaultRegion = database?.fetchRegion(id: defaultId) {
            // Navigate to default region
            buildPath(to: defaultRegion)
            loadRegionData(defaultRegion)
        } else {
            // Load world view (continents)
            loadContinents()
        }
    }

    func loadContinents() {
        guard let db = database else { return }
        visibleRegions = db.fetchContinents()
        currentRegion = nil
        navigationPath = []
        cameraPosition = .region(MKCoordinateRegion(
            center: CLLocationCoordinate2D(latitude: 20, longitude: 0),
            span: MKCoordinateSpan(latitudeDelta: 120, longitudeDelta: 120)
        ))
    }

    func selectRegion(_ region: Region) {
        selectedRegion = region
        selectedRegionId = region.regionId
        loadRegionDetails(region)
    }

    func zoomIntoSelection() {
        guard let region = selectedRegion else { return }

        // Load children if available
        let children = database?.fetchChildren(of: region) ?? []

        if !children.isEmpty {
            // Has children, drill down
            navigationPath.append(region)
            visibleRegions = children
            currentRegion = region

            // Animate to region
            if let lat = region.latitude, let lon = region.longitude {
                withAnimation(.easeInOut(duration: 1.0)) {
                    cameraPosition = .region(MKCoordinateRegion(
                        center: CLLocationCoordinate2D(latitude: lat, longitude: lon),
                        span: spanForRegionType(region.type)
                    ))
                }
            }
        }
    }

    func navigateToWorld() {
        selectedRegionId = nil
        selectedRegion = nil
        loadContinents()
    }

    func navigateBack(to index: Int) {
        guard index < navigationPath.count else { return }

        let targetRegion = navigationPath[index]
        navigationPath = Array(navigationPath.prefix(index))

        loadRegionData(targetRegion)
    }

    func loadRegionData(_ region: Region) {
        let children = database?.fetchChildren(of: region) ?? []
        visibleRegions = children
        currentRegion = region

        if let lat = region.latitude, let lon = region.longitude {
            withAnimation(.easeInOut(duration: 1.0)) {
                cameraPosition = .region(MKCoordinateRegion(
                    center: CLLocationCoordinate2D(latitude: lat, longitude: lon),
                    span: spanForRegionType(region.type)
                ))
            }
        }
    }

    func loadRegionDetails(_ region: Region) {
        currentOfficeholder = database?.fetchCurrentOfficeholder(for: region)
        promisesCount = database?.fetchPromisesCount(for: region) ?? 0
    }

    func getElectionStatus(_ region: Region) -> ElectionStatus {
        // Check election system first
        if region.electionSystem == "non-democratic" {
            return .nonDemocratic
        }

        // For democratic regions, check if election is within 6 months
        if let nextElectionDate = region.nextElection {
            let now = Date()
            let sixMonthsFromNow = Calendar.current.date(byAdding: .month, value: 6, to: now) ?? now

            if nextElectionDate > now && nextElectionDate <= sixMonthsFromNow {
                // Election within 6 months
                return .upcoming
            }
        }

        // Democratic region with no upcoming election within 6 months
        return .noElection
    }

    func hasUpcomingElection(_ region: Region) -> Bool {
        return getElectionStatus(region) == .upcoming
    }

    private func buildPath(to region: Region) {
        // Build navigation path from world to region
        var path: [Region] = []
        var current: Region? = region

        while let parent = current?.parentRegionId,
              let parentRegion = database?.fetchRegion(id: parent) {
            path.insert(parentRegion, at: 0)
            current = parentRegion
        }

        navigationPath = path
    }

    private func spanForRegionType(_ type: Region.RegionType) -> MKCoordinateSpan {
        switch type {
        case .continent:
            return MKCoordinateSpan(latitudeDelta: 40, longitudeDelta: 40)
        case .country:
            return MKCoordinateSpan(latitudeDelta: 10, longitudeDelta: 10)
        case .state, .province:
            return MKCoordinateSpan(latitudeDelta: 3, longitudeDelta: 3)
        case .city:
            return MKCoordinateSpan(latitudeDelta: 0.5, longitudeDelta: 0.5)
        }
    }
}
