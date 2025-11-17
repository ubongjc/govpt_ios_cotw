// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "GPT",
    platforms: [
        .iOS(.v17)
    ],
    products: [
        .library(
            name: "GPT",
            targets: ["GPT"])
    ],
    dependencies: [
        .package(url: "https://github.com/groue/GRDB.swift.git", from: "6.0.0")
    ],
    targets: [
        .target(
            name: "GPT",
            dependencies: [
                .product(name: "GRDB", package: "GRDB.swift")
            ]
        )
    ]
)
