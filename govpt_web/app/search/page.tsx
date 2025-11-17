"use client";

import { useState } from "react";
import { Search as SearchIcon, MapPin, User, FileText, Building2 } from "lucide-react";

const mockResults = {
  regions: [
    { id: "1", name: "United States", type: "Country", isoCode: "US" },
    { id: "2", name: "California", type: "State", isoCode: "US-CA" },
  ],
  leaders: [
    { id: "1", name: "Joe Biden", title: "President", region: "United States", party: "Democratic Party" },
    { id: "2", name: "Gavin Newsom", title: "Governor", region: "California", party: "Democratic Party" },
  ],
  promises: [
    {
      id: "1",
      summary: "Infrastructure Investment and Jobs Act",
      leader: "Joe Biden",
      date: "2021-11-15",
      tags: ["Infrastructure", "Economy"],
    },
    {
      id: "2",
      summary: "California High-Speed Rail Project",
      leader: "Gavin Newsom",
      date: "2023-01-10",
      tags: ["Transportation", "Climate"],
    },
  ],
  companies: [
    { id: "1", ticker: "CAT", name: "Caterpillar Inc.", type: "Stock", industry: "Construction Equipment" },
    { id: "2", ticker: "XLI", name: "Industrial Select Sector SPDR Fund", type: "ETF", industry: "Industrials" },
  ],
};

export default function SearchPage() {
  const [query, setQuery] = useState("");
  const [activeFilters, setActiveFilters] = useState<string[]>(["regions", "leaders", "promises", "companies"]);

  const toggleFilter = (filter: string) => {
    setActiveFilters((prev) =>
      prev.includes(filter) ? prev.filter((f) => f !== filter) : [...prev, filter]
    );
  };

  const showResults = query.length > 0;

  return (
    <div className="container mx-auto p-6">
      <div className="mb-6">
        <h1 className="text-3xl font-bold mb-2">Search</h1>
        <p className="text-muted-foreground">
          Find promises, regions, leaders, and companies
        </p>
      </div>

      {/* Search bar */}
      <div className="mb-6">
        <div className="relative">
          <SearchIcon className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-muted-foreground" />
          <input
            type="text"
            placeholder="Search regions, promises, leaders, or companies..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="w-full pl-10 pr-4 py-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
          />
        </div>
      </div>

      {/* Filters */}
      <div className="mb-6 flex gap-3 flex-wrap">
        {["regions", "leaders", "promises", "companies"].map((filter) => (
          <button
            key={filter}
            onClick={() => toggleFilter(filter)}
            className={`px-4 py-2 rounded-full text-sm font-medium transition ${
              activeFilters.includes(filter)
                ? "bg-primary text-primary-foreground"
                : "bg-card border hover:bg-accent"
            }`}
          >
            {filter.charAt(0).toUpperCase() + filter.slice(1)}
          </button>
        ))}
      </div>

      {/* Empty state */}
      {!showResults && (
        <div className="text-center py-16">
          <SearchIcon className="w-16 h-16 mx-auto mb-4 text-muted-foreground" />
          <h3 className="text-xl font-semibold mb-2">Search GovPT</h3>
          <p className="text-muted-foreground mb-6">
            Find promises, regions, and leaders
          </p>
          <div className="space-y-3 max-w-md mx-auto">
            <div className="flex items-center gap-3 text-sm">
              <MapPin className="w-5 h-5 text-primary" />
              <span>Try searching for a country</span>
            </div>
            <div className="flex items-center gap-3 text-sm">
              <User className="w-5 h-5 text-primary" />
              <span>Search for a leader&apos;s name</span>
            </div>
            <div className="flex items-center gap-3 text-sm">
              <FileText className="w-5 h-5 text-primary" />
              <span>Look up specific promises</span>
            </div>
          </div>
        </div>
      )}

      {/* Results */}
      {showResults && (
        <div className="space-y-8">
          {activeFilters.includes("regions") && mockResults.regions.length > 0 && (
            <div>
              <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
                Regions
                <span className="text-sm text-muted-foreground">({mockResults.regions.length})</span>
              </h2>
              <div className="space-y-3">
                {mockResults.regions.map((region) => (
                  <div key={region.id} className="p-4 bg-card rounded-lg border hover:border-primary transition cursor-pointer">
                    <div className="flex items-center gap-3">
                      <MapPin className="w-5 h-5 text-primary" />
                      <div className="flex-1">
                        <h3 className="font-medium">{region.name}</h3>
                        <p className="text-sm text-muted-foreground">
                          {region.type} • {region.isoCode}
                        </p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {activeFilters.includes("leaders") && mockResults.leaders.length > 0 && (
            <div>
              <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
                Leaders
                <span className="text-sm text-muted-foreground">({mockResults.leaders.length})</span>
              </h2>
              <div className="space-y-3">
                {mockResults.leaders.map((leader) => (
                  <div key={leader.id} className="p-4 bg-card rounded-lg border hover:border-primary transition cursor-pointer">
                    <div className="flex items-center gap-3">
                      <User className="w-5 h-5 text-primary" />
                      <div className="flex-1">
                        <h3 className="font-medium">{leader.name}</h3>
                        <p className="text-sm text-muted-foreground">{leader.title}</p>
                        <div className="flex items-center gap-2 mt-1">
                          <MapPin className="w-3 h-3" />
                          <span className="text-xs text-muted-foreground">{leader.region}</span>
                        </div>
                        {leader.party && (
                          <span className="inline-block mt-2 px-2 py-1 bg-primary/10 text-primary text-xs rounded">
                            {leader.party}
                          </span>
                        )}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {activeFilters.includes("promises") && mockResults.promises.length > 0 && (
            <div>
              <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
                Promises
                <span className="text-sm text-muted-foreground">({mockResults.promises.length})</span>
              </h2>
              <div className="space-y-3">
                {mockResults.promises.map((promise) => (
                  <div key={promise.id} className="p-4 bg-card rounded-lg border hover:border-primary transition cursor-pointer">
                    <div className="flex items-start gap-3">
                      <FileText className="w-5 h-5 text-primary mt-1" />
                      <div className="flex-1">
                        <h3 className="font-medium mb-1">{promise.summary}</h3>
                        <p className="text-sm text-muted-foreground mb-2">
                          <User className="w-3 h-3 inline mr-1" />
                          {promise.leader} • {new Date(promise.date).toLocaleDateString()}
                        </p>
                        <div className="flex gap-2 flex-wrap">
                          {promise.tags.map((tag, i) => (
                            <span key={i} className="px-2 py-1 bg-primary/10 text-primary text-xs rounded">
                              {tag}
                            </span>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {activeFilters.includes("companies") && mockResults.companies.length > 0 && (
            <div>
              <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
                Companies
                <span className="text-sm text-muted-foreground">({mockResults.companies.length})</span>
              </h2>
              <div className="space-y-3">
                {mockResults.companies.map((company) => (
                  <div key={company.id} className="p-4 bg-card rounded-lg border hover:border-primary transition cursor-pointer">
                    <div className="flex items-center gap-3">
                      <Building2 className="w-5 h-5 text-primary" />
                      <div className="flex-1">
                        <div className="flex items-center gap-2 mb-1">
                          <span className="px-2 py-0.5 bg-primary text-primary-foreground text-xs font-bold rounded">
                            {company.ticker}
                          </span>
                          <span className="text-xs text-muted-foreground">• {company.type}</span>
                        </div>
                        <h3 className="font-medium">{company.name}</h3>
                        <p className="text-sm text-muted-foreground">{company.industry}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
