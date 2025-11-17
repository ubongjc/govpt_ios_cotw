//
//  MapBoundaryOverlay.swift
//  Government Promises Tracker
//
//  Custom overlay for drawing region boundaries on the map
//

import SwiftUI
import MapKit

/// A custom view that draws region boundaries as lines over the map
struct MapBoundaryOverlay: UIViewRepresentable {
    let regions: [Region]
    let cameraPosition: MapCameraPosition

    func makeUIView(context: Context) -> BoundaryDrawingView {
        let view = BoundaryDrawingView()
        view.backgroundColor = .clear
        view.isUserInteractionEnabled = false
        return view
    }

    func updateUIView(_ uiView: BoundaryDrawingView, context: Context) {
        uiView.regions = regions
        uiView.cameraPosition = cameraPosition
        uiView.setNeedsDisplay()
    }
}

/// UIView subclass that handles the actual drawing of boundaries
class BoundaryDrawingView: UIView {
    var regions: [Region] = []
    var cameraPosition: MapCameraPosition = .automatic

    private var currentMapRegion: MKCoordinateRegion? {
        // Extract MKCoordinateRegion from MapCameraPosition using Mirror reflection
        let mirror = Mirror(reflecting: cameraPosition)
        for child in mirror.children {
            if let region = child.value as? MKCoordinateRegion {
                return region
            }
        }
        return nil
    }

    override func draw(_ rect: CGRect) {
        super.draw(rect)

        guard let context = UIGraphicsGetCurrentContext(),
              let mapRegion = currentMapRegion else { return }

        let center = mapRegion.center
        let span = mapRegion.span

        // Set drawing properties
        context.setStrokeColor(UIColor.orange.cgColor)
        context.setLineWidth(2.0)
        context.setAlpha(0.8)

        // Draw each region's boundary
        for region in regions {
            guard let coordinates = region.boundaryCoordinates, coordinates.count >= 3 else {
                continue
            }

            // Convert first coordinate to screen point
            if let firstPoint = convertCoordinateToPoint(coordinates[0], center: center, span: span, viewSize: rect.size) {
                context.move(to: firstPoint)

                // Draw lines to subsequent points
                for coordinate in coordinates.dropFirst() {
                    if let point = convertCoordinateToPoint(coordinate, center: center, span: span, viewSize: rect.size) {
                        context.addLine(to: point)
                    }
                }

                // Close the path
                context.addLine(to: firstPoint)
                context.strokePath()
            }
        }
    }

    /// Converts a geographic coordinate to a screen point
    private func convertCoordinateToPoint(_ coordinate: CLLocationCoordinate2D, center: CLLocationCoordinate2D, span: MKCoordinateSpan, viewSize: CGSize) -> CGPoint? {
        // Calculate relative position from center
        let deltaLat = coordinate.latitude - center.latitude
        let deltaLon = coordinate.longitude - center.longitude

        // Convert to screen coordinates
        // Normalize to -0.5 to 0.5 range, then scale to view size
        let x = (deltaLon / span.longitudeDelta + 0.5) * viewSize.width
        let y = (-deltaLat / span.latitudeDelta + 0.5) * viewSize.height

        // Check if point is visible in current view
        guard x >= -100 && x <= viewSize.width + 100 &&
              y >= -100 && y <= viewSize.height + 100 else {
            return nil
        }

        return CGPoint(x: x, y: y)
    }
}
