"use client";

import { useState } from "react";
import { Star, Bell, Database, Shield, HelpCircle, Mail, Github, ExternalLink } from "lucide-react";

export default function SettingsPage() {
  const [defaultRegion, setDefaultRegion] = useState("none");
  const [notifications, setNotifications] = useState(false);

  return (
    <div className="container mx-auto p-6 max-w-4xl">
      <div className="mb-6">
        <h1 className="text-3xl font-bold mb-2">Settings</h1>
        <p className="text-muted-foreground">
          Manage your preferences and account settings
        </p>
      </div>

      <div className="space-y-6">
        {/* Preferences Section */}
        <div className="bg-card rounded-lg border p-6">
          <h2 className="text-xl font-semibold mb-4">Preferences</h2>
          <div className="space-y-4">
            <div>
              <div className="flex items-center gap-2 mb-2">
                <Star className="w-5 h-5 text-yellow-500" />
                <label className="font-medium">Default Region</label>
              </div>
              <select
                value={defaultRegion}
                onChange={(e) => setDefaultRegion(e.target.value)}
                className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
              >
                <option value="none">None</option>
                <option value="us">United States</option>
                <option value="ca">Canada</option>
                <option value="uk">United Kingdom</option>
                <option value="au">Australia</option>
              </select>
              <p className="text-sm text-muted-foreground mt-1">
                Set your default region to start on the map view
              </p>
            </div>

            <div className="flex items-center justify-between pt-2">
              <div className="flex items-center gap-2">
                <Bell className="w-5 h-5 text-primary" />
                <div>
                  <p className="font-medium">Notifications</p>
                  <p className="text-sm text-muted-foreground">
                    Get notified about promise updates
                  </p>
                </div>
              </div>
              <button
                onClick={() => setNotifications(!notifications)}
                className={`relative inline-flex h-6 w-11 items-center rounded-full transition ${
                  notifications ? "bg-primary" : "bg-gray-300 dark:bg-gray-600"
                }`}
              >
                <span
                  className={`inline-block h-4 w-4 transform rounded-full bg-white transition ${
                    notifications ? "translate-x-6" : "translate-x-1"
                  }`}
                />
              </button>
            </div>
          </div>
        </div>

        {/* Data Section */}
        <div className="bg-card rounded-lg border p-6">
          <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
            <Database className="w-5 h-5" />
            Data Management
          </h2>
          <div className="space-y-3">
            <button className="w-full px-4 py-3 bg-background border rounded-md hover:bg-accent transition text-left">
              <p className="font-medium">Export Your Data</p>
              <p className="text-sm text-muted-foreground">
                Download all your data in JSON format
              </p>
            </button>
            <button className="w-full px-4 py-3 bg-background border rounded-md hover:bg-accent transition text-left">
              <p className="font-medium">Clear Cache</p>
              <p className="text-sm text-muted-foreground">
                Clear locally stored data and reload from server
              </p>
            </button>
          </div>
        </div>

        {/* Privacy & Security */}
        <div className="bg-card rounded-lg border p-6">
          <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
            <Shield className="w-5 h-5" />
            Privacy & Security
          </h2>
          <div className="space-y-3">
            <a
              href="#"
              className="flex items-center justify-between px-4 py-3 bg-background border rounded-md hover:bg-accent transition"
            >
              <div>
                <p className="font-medium">Privacy Policy</p>
                <p className="text-sm text-muted-foreground">
                  Learn how we handle your data
                </p>
              </div>
              <ExternalLink className="w-4 h-4 text-muted-foreground" />
            </a>
            <a
              href="#"
              className="flex items-center justify-between px-4 py-3 bg-background border rounded-md hover:bg-accent transition"
            >
              <div>
                <p className="font-medium">Terms of Service</p>
                <p className="text-sm text-muted-foreground">
                  Read our terms and conditions
                </p>
              </div>
              <ExternalLink className="w-4 h-4 text-muted-foreground" />
            </a>
          </div>
        </div>

        {/* Support Section */}
        <div className="bg-card rounded-lg border p-6">
          <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
            <HelpCircle className="w-5 h-5" />
            Support & Feedback
          </h2>
          <div className="space-y-3">
            <a
              href="mailto:support@govpt.app"
              className="flex items-center gap-3 px-4 py-3 bg-background border rounded-md hover:bg-accent transition"
            >
              <Mail className="w-5 h-5 text-primary" />
              <div>
                <p className="font-medium">Contact Support</p>
                <p className="text-sm text-muted-foreground">
                  support@govpt.app
                </p>
              </div>
            </a>
            <a
              href="https://github.com/govpt"
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center justify-between px-4 py-3 bg-background border rounded-md hover:bg-accent transition"
            >
              <div className="flex items-center gap-3">
                <Github className="w-5 h-5" />
                <div>
                  <p className="font-medium">GitHub</p>
                  <p className="text-sm text-muted-foreground">
                    View source code and contribute
                  </p>
                </div>
              </div>
              <ExternalLink className="w-4 h-4 text-muted-foreground" />
            </a>
          </div>
        </div>

        {/* About Section */}
        <div className="bg-card rounded-lg border p-6">
          <h2 className="text-xl font-semibold mb-4">About GovPT</h2>
          <p className="text-sm text-muted-foreground mb-4">
            GovPT is a global transparency platform that tracks political promises with status tracking
            and economic impact signals from verified sources. Our mission is to provide citizens,
            journalists, and investors with clean promise → progress → impact pipelines.
          </p>
          <div className="flex items-center justify-between pt-4 border-t">
            <div className="text-sm text-muted-foreground">
              <p>Version 1.0.0</p>
              <p>© 2024 GovPT. All rights reserved.</p>
            </div>
          </div>
        </div>

        {/* Statistics */}
        <div className="grid md:grid-cols-3 gap-4">
          <div className="bg-card rounded-lg border p-4 text-center">
            <p className="text-3xl font-bold text-primary mb-1">150+</p>
            <p className="text-sm text-muted-foreground">Regions Tracked</p>
          </div>
          <div className="bg-card rounded-lg border p-4 text-center">
            <p className="text-3xl font-bold text-primary mb-1">90+</p>
            <p className="text-sm text-muted-foreground">Political Leaders</p>
          </div>
          <div className="bg-card rounded-lg border p-4 text-center">
            <p className="text-3xl font-bold text-primary mb-1">500+</p>
            <p className="text-sm text-muted-foreground">Promises Tracked</p>
          </div>
        </div>
      </div>
    </div>
  );
}
