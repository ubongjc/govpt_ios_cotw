# GovPT Web

**GovPT** (Government Promises Tracker) is a web application that tracks political promises with status tracking and economic impact signals from verified sources.

## Overview

This is the web version of the GovPT iOS application. It provides:

- **Interactive Map**: Explore political promises by region, country, and leader
- **Search**: Find promises, regions, leaders, and companies
- **Markets**: View market impact predictions for industries and companies
- **Settings**: Manage preferences and account settings

## Tech Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript 5
- **Styling**: Tailwind CSS 3
- **UI Components**: Custom components with shadcn/ui principles
- **Database**: Prisma 6 (ready for PostgreSQL)
- **Icons**: Lucide React

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
```

2. Run the development server:
```bash
npm run dev
```

3. Open [http://localhost:3000](http://localhost:3000) in your browser

## Project Structure

```
govpt_web/
├── app/                    # Next.js App Router pages
│   ├── map/               # Interactive map view
│   ├── search/            # Search functionality
│   ├── markets/           # Market impacts view
│   ├── settings/          # Settings page
│   ├── layout.tsx         # Root layout
│   └── page.tsx           # Home page (redirects to /map)
├── components/            # Reusable React components
│   └── navigation.tsx     # Main navigation bar
├── lib/                   # Utility functions
│   └── utils.ts           # Helper functions
└── public/                # Static assets
```

## Features

### Map View
- Interactive world map with regions and countries
- Color-coded election status indicators
- Breadcrumb navigation
- Region detail panels

### Search View
- Search across regions, promises, leaders, and companies
- Filter results by type
- Real-time search functionality

### Markets View
- Industry impact predictions
- Company and security listings
- Promise-to-market impact mapping
- Confidence ratings and impact ranges

### Settings View
- Default region preferences
- Notification settings
- Data export functionality
- Privacy and support information

## Development

### Build for Production

```bash
npm run build
npm start
```

### Lint Code

```bash
npm run lint
```

## Database Setup (Future)

The application is set up to use Prisma with PostgreSQL. To set up the database:

1. Create a `.env` file with your database URL
2. Run Prisma migrations:
```bash
npx prisma migrate dev
npx prisma generate
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

ISC

## Related Projects

- **GovPT iOS**: The iOS version of this application

---

Built with ❤️ for government transparency and accountability
