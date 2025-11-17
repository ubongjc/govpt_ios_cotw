#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

changes = []

# Add missing territories (ACT and NT)
new_territories = [
    {
        "regionId": "territory:au:act",
        "type": "state",  # Using "state" type since we don't have "territory" in the enum
        "isoCode": "ACT",
        "name": "Australian Capital Territory",
        "parentRegionId": "country:au",
        "shapeRef": None,
        "latitude": -35.2809,
        "longitude": 149.1300,
        "boundingBoxJSON": None,
        "nextElection": None,
        "electionSystem": "Hare-Clark proportional representation"
    },
    {
        "regionId": "territory:au:nt",
        "type": "state",  # Using "state" type since we don't have "territory" in the enum
        "isoCode": "NT",
        "name": "Northern Territory",
        "parentRegionId": "country:au",
        "shapeRef": None,
        "latitude": -12.4634,
        "longitude": 130.8456,
        "boundingBoxJSON": None,
        "nextElection": None,
        "electionSystem": "Optional preferential voting"
    }
]

data['regions'].extend(new_territories)
changes.append(f"Added {len(new_territories)} Australian territories")

# Set endDate for Steven Miles (QLD) - David Crisafulli took office Oct 28, 2024
for officeholder in data['officeholders']:
    if officeholder.get('name') == 'Steven Miles' and officeholder['regionId'] == 'state:au:qld':
        officeholder['endDate'] = '2024-10-28'
        changes.append("Set endDate for Steven Miles to 2024-10-28")

# Add new chief ministers for territories
new_leaders = [
    {
        "personId": "person:au:act:chiefminister:barr",
        "name": "Andrew Barr",
        "title": "Chief Minister of the Australian Capital Territory",
        "regionId": "territory:au:act",
        "partyName": "Australian Labor Party",
        "partyURL": "https://www.actlabor.org.au/",
        "startDate": "2014-12-11",
        "endDate": None,
        "officialSiteURL": "https://www.cmtreasandeconomicdevelopment.act.gov.au/",
        "photoURL": None
    },
    {
        "personId": "person:au:nt:chiefminister:finocchiaro",
        "name": "Lia Finocchiaro",
        "title": "Chief Minister of the Northern Territory",
        "regionId": "territory:au:nt",
        "partyName": "Country Liberal Party",
        "partyURL": "https://www.clp.org.au/",
        "startDate": "2024-08-28",
        "endDate": None,
        "officialSiteURL": "https://dcm.nt.gov.au/",
        "photoURL": None
    }
]

data['officeholders'].extend(new_leaders)
changes.append(f"Added {len(new_leaders)} Australian territory chief ministers")

# Write back to the file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Changes made:")
for change in changes:
    print(f"  - {change}")

print(f"\n✅ Successfully updated Australian states/territories")
print(f"Total regions: {len(data['regions'])}")
print(f"Total officeholders: {len(data['officeholders'])}")
