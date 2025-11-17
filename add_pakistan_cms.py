#!/usr/bin/env python3
"""
Script to add Pakistani provincial and territorial Chief Ministers to seed_data.json
Adds leaders for 4 provinces + 2 territories (Gilgit-Baltistan and Azad Kashmir)
"""

import json
import sys
from datetime import datetime

# Path to seed_data.json
SEED_DATA_PATH = "/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json"

# Pakistani Chief Ministers and leaders (as of 2024-2025)
PAKISTANI_LEADERS = [
    {
        "personId": "person:pk:pb:cm:nawaz",
        "name": "Maryam Nawaz Sharif",
        "title": "Chief Minister",
        "regionId": "prov:pk:pb",  # Punjab
        "partyName": "Pakistan Muslim League (Nawaz)",
        "partyURL": "https://www.pmlnpunjab.org.pk",
        "startDate": "2024-02-26T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://punjab.gov.pk",
        "photoURL": None
    },
    {
        "personId": "person:pk:sd:cm:shah",
        "name": "Syed Murad Ali Shah",
        "title": "Chief Minister",
        "regionId": "prov:pk:sd",  # Sindh
        "partyName": "Pakistan Peoples Party",
        "partyURL": "https://www.ppp.org.pk",
        "startDate": "2024-02-26T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://cm.sindh.gov.pk",
        "photoURL": None
    },
    {
        "personId": "person:pk:kp:cm:gandapur",
        "name": "Ali Amin Gandapur",
        "title": "Chief Minister",
        "regionId": "prov:pk:kp",  # Khyber Pakhtunkhwa
        "partyName": "Pakistan Tehreek-e-Insaf",
        "partyURL": "https://www.insaf.pk",
        "startDate": "2024-03-02T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://kp.gov.pk",
        "photoURL": None
    },
    {
        "personId": "person:pk:ba:cm:bugti",
        "name": "Mir Sarfraz Bugti",
        "title": "Chief Minister",
        "regionId": "prov:pk:ba",  # Balochistan
        "partyName": "Pakistan Peoples Party",
        "partyURL": "https://www.ppp.org.pk",
        "startDate": "2024-03-02T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://balochistan.gov.pk",
        "photoURL": None
    },
    {
        "personId": "person:pk:gb:cm:khan",
        "name": "Haji Gulbar Khan",
        "title": "Chief Minister",
        "regionId": "terr:pk:gb",  # Gilgit-Baltistan
        "partyName": "Pakistan Peoples Party",
        "partyURL": "https://www.ppp.org.pk",
        "startDate": "2023-07-10T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://gilgitbaltistan.gov.pk",
        "photoURL": None
    },
    {
        "personId": "person:pk:aj:pm:haq",
        "name": "Chaudhry Anwar-ul-Haq",
        "title": "Prime Minister",  # Note: AJK has PM, not CM
        "regionId": "terr:pk:aj",  # Azad Jammu and Kashmir
        "partyName": "Pakistan Peoples Party",
        "partyURL": "https://www.ppp.org.pk",
        "startDate": "2023-04-20T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://ajk.gov.pk",
        "photoURL": None
    }
]

def load_seed_data():
    """Load the seed_data.json file"""
    print(f"Loading seed data from: {SEED_DATA_PATH}")
    with open(SEED_DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_seed_data(data):
    """Save the updated seed_data.json file"""
    print(f"Saving seed data to: {SEED_DATA_PATH}")
    with open(SEED_DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def check_existing_leaders(data):
    """Check if any of the leaders already exist"""
    existing_person_ids = {oh.get('personId') for oh in data.get('officeholders', [])}
    return existing_person_ids

def add_pakistani_leaders(data):
    """Add Pakistani leaders to the officeholders array"""

    if 'officeholders' not in data:
        print("ERROR: 'officeholders' key not found in seed_data.json!")
        return 0

    existing_ids = check_existing_leaders(data)
    added_count = 0
    skipped_count = 0

    for leader in PAKISTANI_LEADERS:
        person_id = leader['personId']

        if person_id in existing_ids:
            print(f"SKIP: {leader['name']} ({person_id}) already exists")
            skipped_count += 1
            continue

        # Add the leader to officeholders
        data['officeholders'].append(leader)
        print(f"ADDED: {leader['name']} - {leader['title']} of {leader['regionId']}")
        added_count += 1

    return added_count, skipped_count

def main():
    """Main function"""
    print("=" * 70)
    print("Adding Pakistani Provincial and Territorial Leaders")
    print("=" * 70)
    print()

    try:
        # Load the seed data
        data = load_seed_data()

        # Verify regionIds exist
        print("\nVerifying region IDs exist in data...")
        region_ids = {r.get('regionId') for r in data.get('regions', [])}

        expected_regions = ['prov:pk:pb', 'prov:pk:sd', 'prov:pk:kp', 'prov:pk:ba',
                          'terr:pk:gb', 'terr:pk:aj']

        for region_id in expected_regions:
            if region_id in region_ids:
                print(f"  ✓ Found: {region_id}")
            else:
                print(f"  ✗ Missing: {region_id}")

        print()

        # Add the leaders
        added_count, skipped_count = add_pakistani_leaders(data)

        if added_count > 0:
            # Save the updated data
            save_seed_data(data)
            print()
            print("=" * 70)
            print(f"SUCCESS: Added {added_count} new Pakistani leaders!")
            if skipped_count > 0:
                print(f"Skipped {skipped_count} existing leaders")
            print("=" * 70)
        else:
            print()
            print("=" * 70)
            print("No new leaders added (all already exist)")
            print("=" * 70)

        # Print summary
        print("\nSummary of leaders:")
        print("-" * 70)
        for leader in PAKISTANI_LEADERS:
            status = "EXISTING" if leader['personId'] in check_existing_leaders(data) else "NEW"
            print(f"[{status}] {leader['name']}")
            print(f"        Title: {leader['title']}")
            print(f"        Region: {leader['regionId']}")
            print(f"        Party: {leader['partyName']}")
            print(f"        Start Date: {leader['startDate']}")
            print()

        return 0

    except FileNotFoundError:
        print(f"ERROR: Could not find file: {SEED_DATA_PATH}")
        return 1
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in seed_data.json: {e}")
        return 1
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
