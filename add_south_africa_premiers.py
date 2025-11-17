#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# South African Provincial Premiers (June 2024 - present)
# All elected/re-elected in June 2024 for the 7th administration
south_african_premiers = [
    {
        "personId": "person:za:ec:premier:mabuyane",
        "name": "Oscar Mabuyane",
        "title": "Premier of Eastern Cape",
        "regionId": "prov:za:ec",
        "partyName": "African National Congress",
        "startDate": "2024-06-14",
        "endDate": None
    },
    {
        "personId": "person:za:fs:premier:letsoha",
        "name": "Maqueen Letsoha-Mathae",
        "title": "Premier of Free State",
        "regionId": "prov:za:fs",
        "partyName": "African National Congress",
        "startDate": "2024-06-13",
        "endDate": None
    },
    {
        "personId": "person:za:gt:premier:lesufi",
        "name": "Panyaza Lesufi",
        "title": "Premier of Gauteng",
        "regionId": "prov:za:gt",
        "partyName": "African National Congress",
        "startDate": "2024-06-14",
        "endDate": None
    },
    {
        "personId": "person:za:nl:premier:ntuli",
        "name": "Thami Ntuli",
        "title": "Premier of KwaZulu-Natal",
        "regionId": "prov:za:nl",
        "partyName": "Inkatha Freedom Party",
        "startDate": "2024-06-14",
        "endDate": None
    },
    {
        "personId": "person:za:lp:premier:ramathuba",
        "name": "Phophi Ramathuba",
        "title": "Premier of Limpopo",
        "regionId": "prov:za:lp",
        "partyName": "African National Congress",
        "startDate": "2024-06-13",
        "endDate": None
    },
    {
        "personId": "person:za:mp:premier:ndlovu",
        "name": "Mandla Ndlovu",
        "title": "Premier of Mpumalanga",
        "regionId": "prov:za:mp",
        "partyName": "African National Congress",
        "startDate": "2024-06-18",
        "endDate": None
    },
    {
        "personId": "person:za:nc:premier:saul",
        "name": "Zamani Saul",
        "title": "Premier of Northern Cape",
        "regionId": "prov:za:nc",
        "partyName": "African National Congress",
        "startDate": "2024-06-13",
        "endDate": None
    },
    {
        "personId": "person:za:nw:premier:mokgosi",
        "name": "Lazzy Mokgosi",
        "title": "Premier of North West",
        "regionId": "prov:za:nw",
        "partyName": "African National Congress",
        "startDate": "2024-06-13",
        "endDate": None
    },
    {
        "personId": "person:za:wc:premier:winde",
        "name": "Alan Winde",
        "title": "Premier of Western Cape",
        "regionId": "prov:za:wc",
        "partyName": "Democratic Alliance",
        "startDate": "2024-06-13",
        "endDate": None
    }
]

# Add all premiers
data['officeholders'].extend(south_african_premiers)

print(f"✅ Added {len(south_african_premiers)} South African provincial premiers")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
