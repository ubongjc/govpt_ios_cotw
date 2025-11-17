export default function MapPage() {
  return (
    <div className="container mx-auto p-6">
      <div className="mb-6">
        <h1 className="text-3xl font-bold mb-2">Interactive Map</h1>
        <p className="text-muted-foreground">
          Explore political promises by region, country, and leader
        </p>
      </div>

      <div className="grid gap-6">
        {/* Breadcrumb navigation */}
        <div className="flex items-center gap-2 p-4 bg-card rounded-lg border">
          <button className="flex items-center gap-2 px-3 py-1.5 bg-primary/10 text-primary rounded-md hover:bg-primary/20 transition">
            <svg
              className="w-4 h-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
            World
          </button>
        </div>

        {/* Map placeholder */}
        <div className="relative h-[600px] bg-card rounded-lg border overflow-hidden">
          <div className="absolute inset-0 flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-blue-950 dark:to-indigo-950">
            <div className="text-center">
              <svg
                className="w-16 h-16 mx-auto mb-4 text-primary"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"
                />
              </svg>
              <p className="text-lg font-medium text-muted-foreground mb-2">
                Interactive Map View
              </p>
              <p className="text-sm text-muted-foreground">
                Click on regions to explore political promises and leaders
              </p>
            </div>
          </div>

          {/* Example region markers */}
          <div className="absolute top-32 left-32 group cursor-pointer">
            <div className="relative">
              <div className="w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center shadow-lg group-hover:scale-110 transition">
                <span className="text-white text-lg">🇺🇸</span>
              </div>
              <div className="absolute -bottom-6 left-1/2 -translate-x-1/2 whitespace-nowrap bg-background px-2 py-1 rounded text-xs font-medium shadow-sm border">
                United States
              </div>
            </div>
          </div>

          <div className="absolute top-44 right-64 group cursor-pointer">
            <div className="relative">
              <div className="w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center shadow-lg group-hover:scale-110 transition">
                <span className="text-white text-lg">🇨🇦</span>
              </div>
              <div className="absolute -bottom-6 left-1/2 -translate-x-1/2 whitespace-nowrap bg-background px-2 py-1 rounded text-xs font-medium shadow-sm border">
                Canada
              </div>
            </div>
          </div>

          <div className="absolute bottom-32 right-48 group cursor-pointer">
            <div className="relative">
              <div className="w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center shadow-lg group-hover:scale-110 transition">
                <span className="text-white text-lg">🇬🇧</span>
              </div>
              <div className="absolute -bottom-6 left-1/2 -translate-x-1/2 whitespace-nowrap bg-background px-2 py-1 rounded text-xs font-medium shadow-sm border">
                United Kingdom
              </div>
            </div>
          </div>
        </div>

        {/* Legend */}
        <div className="grid md:grid-cols-3 gap-4">
          <div className="flex items-center gap-3 p-4 bg-card rounded-lg border">
            <div className="w-3 h-3 rounded-full bg-yellow-500 shadow-lg shadow-yellow-500/50"></div>
            <div>
              <p className="font-medium text-sm">Election within 6 months</p>
              <p className="text-xs text-muted-foreground">Upcoming election</p>
            </div>
          </div>
          <div className="flex items-center gap-3 p-4 bg-card rounded-lg border">
            <div className="w-3 h-3 rounded-full bg-blue-500 shadow-lg shadow-blue-500/50"></div>
            <div>
              <p className="font-medium text-sm">No active election</p>
              <p className="text-xs text-muted-foreground">Normal status</p>
            </div>
          </div>
          <div className="flex items-center gap-3 p-4 bg-card rounded-lg border">
            <div className="w-3 h-3 rounded-full bg-gray-500 shadow-lg shadow-gray-500/50"></div>
            <div>
              <p className="font-medium text-sm">Non-democratic</p>
              <p className="text-xs text-muted-foreground">No elections</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
