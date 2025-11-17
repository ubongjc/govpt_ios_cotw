"use client";

import { useState } from "react";
import { TrendingUp, TrendingDown, Building2, ChevronDown, ChevronUp, Info } from "lucide-react";

const mockImpacts = [
  {
    id: "1",
    industry: "Construction & Infrastructure",
    industryCode: "NAICS 23",
    benefits: 3,
    risks: 1,
    companies: [
      { ticker: "CAT", name: "Caterpillar Inc.", type: "Stock" },
      { ticker: "DE", name: "Deere & Company", type: "Stock" },
      { ticker: "XLI", name: "Industrial Select Sector SPDR Fund", type: "ETF" },
    ],
    promises: [
      {
        id: "p1",
        title: "Infrastructure Investment and Jobs Act",
        leader: "Joe Biden",
        country: "United States",
        direction: 1,
        impactClass: "Significant",
        impactRange: "15% to 25%",
        confidence: 0.85,
        rationale: "Direct federal infrastructure spending on roads, bridges, and public works",
      },
    ],
  },
  {
    id: "2",
    industry: "Renewable Energy",
    industryCode: "NAICS 2211",
    benefits: 5,
    risks: 0,
    companies: [
      { ticker: "ICLN", name: "iShares Global Clean Energy ETF", type: "ETF" },
      { ticker: "NEE", name: "NextEra Energy", type: "Stock" },
    ],
    promises: [
      {
        id: "p2",
        title: "Inflation Reduction Act - Clean Energy Provisions",
        leader: "Joe Biden",
        country: "United States",
        direction: 1,
        impactClass: "Transformational",
        impactRange: "30% to 50%",
        confidence: 0.9,
        rationale: "Massive tax credits and subsidies for renewable energy development",
      },
    ],
  },
  {
    id: "3",
    industry: "Oil & Gas",
    industryCode: "NAICS 211",
    benefits: 1,
    risks: 3,
    companies: [
      { ticker: "XLE", name: "Energy Select Sector SPDR Fund", type: "ETF" },
      { ticker: "XOM", name: "Exxon Mobil Corporation", type: "Stock" },
    ],
    promises: [
      {
        id: "p3",
        title: "Transition to clean energy and reduce fossil fuel subsidies",
        leader: "Joe Biden",
        country: "United States",
        direction: -1,
        impactClass: "Moderate",
        impactRange: "5% to 15%",
        confidence: 0.7,
        rationale: "Policy shift toward renewables may reduce demand and regulatory support",
      },
    ],
  },
];

export default function MarketsPage() {
  const [filter, setFilter] = useState<"all" | "benefits" | "risks" | "high">("all");
  const [expandedIndustry, setExpandedIndustry] = useState<string | null>(null);

  const filteredImpacts = mockImpacts.filter((impact) => {
    if (filter === "benefits") return impact.benefits > 0;
    if (filter === "risks") return impact.risks > 0;
    if (filter === "high") return impact.promises.some((p) =>
      p.impactClass === "Significant" || p.impactClass === "Transformational"
    );
    return true;
  });

  return (
    <div className="container mx-auto p-6">
      <div className="mb-6">
        <h1 className="text-3xl font-bold mb-2">Market Impacts</h1>
        <p className="text-muted-foreground">
          Policy promises may impact these industries and companies
        </p>
      </div>

      {/* Filters */}
      <div className="mb-6 flex gap-3 flex-wrap">
        {[
          { key: "all", label: "All" },
          { key: "benefits", label: "Benefits" },
          { key: "risks", label: "Risks" },
          { key: "high", label: "High Impact" },
        ].map((item) => (
          <button
            key={item.key}
            onClick={() => setFilter(item.key as any)}
            className={`px-4 py-2 rounded-full text-sm font-medium transition ${
              filter === item.key
                ? "bg-primary text-primary-foreground"
                : "bg-card border hover:bg-accent"
            }`}
          >
            {item.label}
          </button>
        ))}
      </div>

      {/* Disclaimer */}
      <div className="mb-6 p-4 bg-orange-50 dark:bg-orange-950/20 border border-orange-200 dark:border-orange-900 rounded-lg">
        <div className="flex gap-3">
          <Info className="w-5 h-5 text-orange-600 dark:text-orange-400 mt-0.5 flex-shrink-0" />
          <div>
            <h3 className="font-semibold text-orange-900 dark:text-orange-100 mb-1">
              Market Impact Information
            </h3>
            <p className="text-sm text-orange-800 dark:text-orange-200">
              This feature is informational only and not financial advice. Markets move for many reasons.
              Do your own research before making investment decisions.
            </p>
          </div>
        </div>
      </div>

      {/* Industry Impact Cards */}
      <div className="space-y-4">
        {filteredImpacts.map((impact) => (
          <div key={impact.id} className="bg-card rounded-lg border overflow-hidden">
            <button
              onClick={() => setExpandedIndustry(expandedIndustry === impact.id ? null : impact.id)}
              className="w-full p-6 text-left hover:bg-accent/50 transition"
            >
              <div className="flex items-center justify-between">
                <div className="flex-1">
                  <h3 className="text-lg font-semibold mb-2">{impact.industry}</h3>
                  <div className="flex gap-4 text-sm">
                    {impact.benefits > 0 && (
                      <div className="flex items-center gap-2 text-green-600 dark:text-green-400">
                        <TrendingUp className="w-4 h-4" />
                        <span>{impact.benefits} benefit{impact.benefits !== 1 ? "s" : ""}</span>
                      </div>
                    )}
                    {impact.risks > 0 && (
                      <div className="flex items-center gap-2 text-red-600 dark:text-red-400">
                        <TrendingDown className="w-4 h-4" />
                        <span>{impact.risks} risk{impact.risks !== 1 ? "s" : ""}</span>
                      </div>
                    )}
                  </div>
                </div>
                {expandedIndustry === impact.id ? (
                  <ChevronUp className="w-5 h-5 text-muted-foreground" />
                ) : (
                  <ChevronDown className="w-5 h-5 text-muted-foreground" />
                )}
              </div>
            </button>

            {expandedIndustry === impact.id && (
              <div className="px-6 pb-6 space-y-6">
                <div className="pt-4 border-t">
                  <div className="flex items-center gap-2 mb-4">
                    <Building2 className="w-5 h-5 text-primary" />
                    <h4 className="font-semibold">Related Companies & Securities</h4>
                  </div>
                  <div className="space-y-2">
                    {impact.companies.map((company, idx) => (
                      <div
                        key={idx}
                        className="p-3 bg-background rounded-lg border flex items-center gap-3"
                      >
                        <div className={`px-2 py-1 rounded text-xs font-bold ${
                          company.type === "Stock"
                            ? "bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300"
                            : company.type === "ETF"
                            ? "bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300"
                            : "bg-orange-100 text-orange-700 dark:bg-orange-900 dark:text-orange-300"
                        }`}>
                          {company.ticker}
                        </div>
                        <div className="flex-1">
                          <p className="font-medium text-sm">{company.name}</p>
                          <p className="text-xs text-muted-foreground">{company.type}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                <div className="border-t pt-4">
                  <h4 className="font-semibold mb-4">Policy Promises</h4>
                  <div className="space-y-4">
                    {impact.promises.map((promise) => (
                      <div key={promise.id} className="p-4 bg-background rounded-lg border">
                        <div className="flex gap-3 mb-3">
                          {promise.direction > 0 ? (
                            <TrendingUp className="w-6 h-6 text-green-600 dark:text-green-400 flex-shrink-0" />
                          ) : (
                            <TrendingDown className="w-6 h-6 text-red-600 dark:text-red-400 flex-shrink-0" />
                          )}
                          <div className="flex-1">
                            <div className="flex items-start justify-between gap-4 mb-2">
                              <div>
                                <span className={`text-sm font-semibold ${
                                  promise.direction > 0 ? "text-green-600 dark:text-green-400" : "text-red-600 dark:text-red-400"
                                }`}>
                                  {promise.direction > 0 ? "Potential Benefit" : "Potential Risk"}
                                </span>
                                <div className="flex items-center gap-2 mt-1">
                                  <span className={`px-2 py-1 rounded text-xs font-medium ${
                                    promise.impactClass === "Transformational"
                                      ? "bg-purple-100 text-purple-700 dark:bg-purple-900 dark:text-purple-300"
                                      : promise.impactClass === "Significant"
                                      ? "bg-orange-100 text-orange-700 dark:bg-orange-900 dark:text-orange-300"
                                      : "bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300"
                                  }`}>
                                    {promise.impactClass}
                                  </span>
                                  <span className="text-xs text-muted-foreground">{promise.impactRange}</span>
                                </div>
                              </div>
                              <div className="flex items-center gap-1 text-sm">
                                <div className={`w-2 h-2 rounded-full ${
                                  promise.confidence >= 0.7
                                    ? "bg-green-500"
                                    : promise.confidence >= 0.4
                                    ? "bg-orange-500"
                                    : "bg-red-500"
                                }`}></div>
                                <span className="text-muted-foreground">
                                  {promise.confidence >= 0.7 ? "High" : promise.confidence >= 0.4 ? "Medium" : "Low"}
                                </span>
                              </div>
                            </div>
                            <h5 className="font-medium mb-2">{promise.title}</h5>
                            <p className="text-sm text-muted-foreground mb-2">
                              {promise.leader} • {promise.country}
                            </p>
                            <p className="text-sm text-muted-foreground italic">{promise.rationale}</p>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
