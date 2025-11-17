// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "GovPT",
    platforms: [
        .iOS(.v17)
    ],
    products: [
        .library(
            name: "GovPT",
            targets: ["GovPT"])
    ],
    dependencies: [
        .package(url: "https://github.com/groue/GRDB.swift.git", from: "6.0.0")
    ],
    targets: [
        .target(
            name: "GovPT",
            dependencies: [
                .product(name: "GRDB", package: "GRDB.swift")
            ]
        )
    ]
)
