#!/usr/bin/env python3
import json
from datetime import datetime, timedelta

# Read current seed data
with open('GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Update US President to Trump (inaugurated January 20, 2025)
for i, person in enumerate(data['officeholders']):
    if person['personId'] == 'person:us:president:biden':
        # Mark Biden as ended
        data['officeholders'][i]['endDate'] = "2025-01-20T00:00:00Z"
        break

# Add Trump as current president
trump = {
    "personId": "person:us:president:trump",
    "name": "Donald Trump",
    "title": "President of the United States",
    "regionId": "country:us",
    "partyName": "Republican Party",
    "partyURL": "https://gop.com",
    "startDate": "2025-01-20T00:00:00Z",
    "endDate": None,
    "officialSiteURL": "https://www.whitehouse.gov",
    "photoURL": None
}

# Check if Trump already exists
if not any(p['personId'] == 'person:us:president:trump' for p in data['officeholders']):
    data['officeholders'].append(trump)

# Update other 2025 leaders (some recent changes)
updates = [
    # UK - Keir Starmer is PM since July 2024
    {
        "old_id": "person:gb:pm:sunak",
        "new_leader": {
            "personId": "person:gb:pm:starmer",
            "name": "Keir Starmer",
            "title": "Prime Minister of United Kingdom",
            "regionId": "country:gb",
            "partyName": "Labour Party",
            "partyURL": "https://labour.org.uk",
            "startDate": "2024-07-05T00:00:00Z",
            "endDate": None,
            "officialSiteURL": "https://www.gov.uk/government/ministers/prime-minister",
            "photoURL": None
        }
    }
]

# Apply updates
for update in updates:
    for i, person in enumerate(data['officeholders']):
        if person['personId'] == update['old_id']:
            data['officeholders'][i]['endDate'] = update['new_leader']['startDate']
            if not any(p['personId'] == update['new_leader']['personId'] for p in data['officeholders']):
                data['officeholders'].append(update['new_leader'])
            break

# Add regions with election dates
# Add electionDate field to regions
elections_2025 = {
    # Countries with elections in next 6 months (by October 2025)
    "country:ca": "2025-10-20T00:00:00Z",  # Canada federal election by October 2025
    "country:de": "2025-09-28T00:00:00Z",  # Germany federal election September 2025
    "country:no": "2025-09-08T00:00:00Z",  # Norway parliamentary election
    "country:cl": "2025-11-21T00:00:00Z",  # Chile presidential election
    "country:ph": "2025-05-12T00:00:00Z",  # Philippines midterm elections

    # Countries with elections later in 2025/2026
    "country:au": "2025-05-17T00:00:00Z",  # Australia federal election by May 2025
    "country:jp": "2025-10-31T00:00:00Z",  # Japan House of Councillors
    "country:ar": "2025-10-26T00:00:00Z",  # Argentina midterm elections
    "country:mx": "2027-06-06T00:00:00Z",  # Mexico (not until 2027)
    "country:fr": "2027-04-23T00:00:00Z",  # France presidential (2027)
    "country:in": "2029-05-01T00:00:00Z",  # India (2029)
    "country:br": "2026-10-02T00:00:00Z",  # Brazil (2026)
    "country:za": "2029-05-08T00:00:00Z",  # South Africa (2029)

    # US elections
    "country:us": "2028-11-07T00:00:00Z",  # US presidential election 2028
    "state:us:ca": "2026-11-03T00:00:00Z",  # California gubernatorial 2026
    "state:us:tx": "2026-11-03T00:00:00Z",  # Texas gubernatorial 2026
    "state:us:fl": "2026-11-03T00:00:00Z",  # Florida gubernatorial 2026
    "state:us:ny": "2026-11-03T00:00:00Z",  # New York gubernatorial 2026
}

# Countries with no foreseeable elections (authoritarian/long-term)
no_elections = [
    "country:cn",  # China - no democratic elections
    "country:cu",  # Cuba - single party state
    "country:vn",  # Vietnam - single party state
]

# Add election dates to regions
for region in data['regions']:
    if region['regionId'] in elections_2025:
        region['nextElection'] = elections_2025[region['regionId']]
    elif region['regionId'] in no_elections:
        region['nextElection'] = None
        region['electionSystem'] = "non-democratic"

# Update promises to reflect Trump administration
trump_promises = [
    {
        "promiseId": "promise:trump:border:2025",
        "personId": "person:us:president:trump",
        "regionId": "country:us",
        "dateMade": "2025-01-20T00:00:00Z",
        "context": "Inauguration speech",
        "quoteExact": "We will complete the border wall and implement the largest deportation operation in American history.",
        "summary": "Complete border wall and increase deportations",
        "tagsJSON": "[\"immigration\", \"border\", \"security\"]",
        "dueBy": "2029-01-20T00:00:00Z",
        "sourcePrimary": "https://www.whitehouse.gov/briefing-room/",
        "sourceType": "official_statement",
        "policyTagsJSON": "[\"immigration\", \"border_security\"]",
        "effectInputsJSON": None
    },
    {
        "promiseId": "promise:trump:economy:2025",
        "personId": "person:us:president:trump",
        "regionId": "country:us",
        "dateMade": "2025-01-20T00:00:00Z",
        "context": "Economic policy announcement",
        "quoteExact": "We will cut taxes, bring manufacturing back to America, and achieve energy independence.",
        "summary": "Tax cuts and manufacturing revival",
        "tagsJSON": "[\"economy\", \"taxes\", \"manufacturing\"]",
        "dueBy": "2027-01-01T00:00:00Z",
        "sourcePrimary": "https://www.whitehouse.gov",
        "sourceType": "official_statement",
        "policyTagsJSON": "[\"economy\", \"manufacturing\"]",
        "effectInputsJSON": None
    }
]

# Add Trump promises
for promise in trump_promises:
    if not any(p['promiseId'] == promise['promiseId'] for p in data['promises']):
        data['promises'].append(promise)

# Remove Biden promises or mark as from previous administration
for i, promise in enumerate(data['promises']):
    if promise['personId'] == 'person:us:president:biden':
        # Mark as from previous administration
        data['promises'][i]['administrationStatus'] = 'previous'

print("Updated leaders for 2025:")
print(f"- Donald Trump as US President (inaugurated Jan 20, 2025)")
print(f"- Keir Starmer as UK PM (since July 2024)")
print(f"- Added election dates for {len(elections_2025)} regions")
print(f"- Total officeholders: {len(data['officeholders'])}")
print(f"- Total promises: {len(data['promises'])}")

# Save updated data
with open('GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print("\n✅ Successfully updated to 2025 data!")