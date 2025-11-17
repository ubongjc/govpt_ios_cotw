# Government Promises Tracker (GPT)

A sleek iOS app that lets anyone drill down from a world map → continent → country → state/province → city and see official promises from the current officeholder, with verifiable primary-source proof and a transparent fulfillment score.

## Features

### Core Functionality
- **Interactive Map Navigation**: Drill down from continents to countries to see current leaders
- **Promise Tracking**: View all promises made by government officials with exact quotes
- **Primary Source Verification**: Every promise links to official sources (government sites, campaign PDFs, official videos)
- **Status Tracking**: See fulfillment status (Kept, In Progress, Broken, Stalled, Obsolete) with evidence
- **Full-Text Search**: Fast, offline search across regions, promises, and leaders using SQLite FTS5
- **Market Impact Analysis**: See which industries may be affected by policy promises

### Technology Stack
- **Swift 5.10+** with **SwiftUI**
- **MapKit** for interactive maps
- **GRDB.swift** for SQLite database with FTS5 full-text search
- **Combine** for reactive programming
- **iOS 17+** minimum deployment target

## Project Structure

```
GPT/
├── Models/              # Data models (Region, Officeholder, Promise, etc.)
├── Views/               # SwiftUI views
│   ├── HomeMapView.swift
│   ├── CountryView.swift
│   ├── PromisesListView.swift
│   ├── PromiseDetailView.swift
│   └── SearchView.swift
├── Services/            # Business logic services
│   ├── SearchService.swift
│   └── GeoService.swift
├── Database/            # Database manager and migrations
│   └── DatabaseManager.swift
├── Resources/           # Seed data and assets
│   └── seed_data.json
└── Assets.xcassets/     # App icons and colors
```

## Current Seed Data

The app currently includes seed data for:
- **6 Continents**: North America, South America, Europe, Africa, Asia, Oceania
- **20 Countries** with current leaders:
  - North America: USA (Biden), Canada (Trudeau), Mexico (Sheinbaum)
  - South America: Brazil (Lula), Argentina (Milei)
  - Europe: UK (Starmer), France (Macron), Germany (Scholz), Italy (Meloni), Spain (Sánchez)
  - Africa: Nigeria (Tinubu), South Africa (Ramaphosa), Egypt (el-Sisi)
  - Asia: China (Xi), India (Modi), Japan (Kishida), South Korea (Yoon), Indonesia (Prabowo)
  - Oceania: Australia (Albanese), New Zealand (Luxon)

**Note**: Promise data is currently empty and ready to be populated for each leader.

### Example Promises (Sample - not currently in database)
The following were example promises from the original Canada-only version:
  - Tax cuts for middle class
  - $12B renewable energy investment
  - Housing (1M new homes)
  - Healthcare transfers
  - $10/day childcare
  - Climate targets (40% reduction by 2030)
  - Universal pharmacare
  - $5B transit infrastructure
  - Skills training for green economy
  - Rural broadband by 2026

## Database Schema

### Core Tables
- **region**: Geographic regions (continents, countries, states, cities)
- **officeholder**: Current and past government officials
- **promise**: Campaign promises with exact quotes and sources
- **evidence**: Proof of promise fulfillment
- **status_snapshot**: Current status of promises

### Market Impact Tables
- **industry**: Industry sectors (GICS codes)
- **policy_tag**: Policy categories (infrastructure, green_subsidies, etc.)
- **policy_tag_industry**: Mapping of policies to industries
- **promise_industry_impact**: Computed impact ranges and confidence scores

### FTS5 Search Tables
- **fts_regions**: Full-text search for regions
- **fts_promises**: Full-text search for promises

## Key Principles

### 1. Primary Sources Only
Every promise must include a URL to an official source:
- Campaign sites/manifestos
- Official government releases (.gc.ca, .gov domains)
- Official YouTube channels with timestamps
- Official social media posts with archives

### 2. Immutable Quotes
Store the exact quote + context (date, venue) - never paraphrase or summarize without the original.

### 3. Transparent Scoring
Every status requires evidence links to primary sources.

### 4. Current Officials Only
Track only current officeholders (auto-updated in future cloud versions).

### 5. Non-Partisan and Auditable
Every statement is traceable to its original, official source.

## Market Impact Feature

The app includes a unique feature that maps government promises to potentially affected industries:

- **Direction**: Whether policy favors (↑) or disadvantages (↓) an industry
- **Impact Range**: Policy-sensitivity bands (e.g., +5% to +10%)
- **Confidence Score**: Based on 5 factors:
  - Policy Intensity (how direct the impact)
  - Budget Scale (size of spending)
  - Timing Proximity (how soon it takes effect)
  - Jurisdiction Weight (scope of authority)
  - Execution Likelihood (political feasibility)
- **Rationale**: Brief explanation of the connection

**Important**: This is informational only, NOT financial advice. Markets are influenced by countless factors.

## Building the App

### Requirements
- Xcode 15.0+
- iOS 17.0+ deployment target
- Swift 5.10+

### Steps
1. Open `GPT.xcodeproj` in Xcode
2. Wait for Swift Package Manager to resolve dependencies (GRDB.swift)
3. Select a simulator or device
4. Build and run (⌘R)

### Dependencies
- **GRDB.swift** (6.0.0+): SQLite toolkit with FTS5 support

## Future Roadmap

### Beta
- Add Canadian provinces (Premiers)
- Add U.S. federal (President)
- Add status snapshots with evidence for existing promises

### v1.0
- Move database to cloud (Supabase/Postgres)
- Admin web console for data ingestion
- Offline sync with signed bundles
- Auto-refresh current officeholders nightly

### Future
- More countries and regions
- State/provincial level tracking
- City/municipal level tracking
- Web version
- API for third-party access

## Data Provenance

All data includes:
- Source URL (required)
- Source type (manifesto_pdf, official_site, official_video, etc.)
- Date made/published
- Context (where and when the promise was made)
- Checksum/hash for verification

## Legal & Ethics

- **Disclaimer**: Informational only, not affiliated with any government or party
- **Election Laws**: Respects local election laws
- **No UGC**: No user-generated political content in v0
- **Official Emblems**: Used only when permitted, otherwise neutral cards
- **Report Issues**: Users can report data issues via email

## Contributing

This is currently a demonstration app built from the plan.md specification. Future versions will include:
- Data validation tools
- Community-driven promise tracking
- Multi-language support
- Accessibility improvements

## License

See LICENSE file for details.

## Contact

For issues or questions about the app, please refer to the plan.md document.

---

Built with Claude Code following the comprehensive plan.md specification.
