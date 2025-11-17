"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Map, Search, TrendingUp, Settings } from "lucide-react";
import { cn } from "@/lib/utils";

const navItems = [
  { name: "Map", href: "/map", icon: Map },
  { name: "Search", href: "/search", icon: Search },
  { name: "Markets", href: "/markets", icon: TrendingUp },
  { name: "Settings", href: "/settings", icon: Settings },
];

export function Navigation() {
  const pathname = usePathname();

  return (
    <nav className="border-b bg-background sticky top-0 z-50">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <Link href="/" className="text-2xl font-bold text-primary">
            GovPT
          </Link>

          <div className="flex space-x-1">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = pathname === item.href;

              return (
                <Link
                  key={item.name}
                  href={item.href}
                  className={cn(
                    "flex items-center gap-2 px-4 py-2 rounded-md transition-colors",
                    isActive
                      ? "bg-primary text-primary-foreground"
                      : "hover:bg-accent"
                  )}
                >
                  <Icon className="w-5 h-5" />
                  <span className="hidden md:inline">{item.name}</span>
                </Link>
              );
            })}
          </div>
        </div>
      </div>
    </nav>
  );
}
