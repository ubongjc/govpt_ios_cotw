#!/usr/bin/env python3
import json
from datetime import datetime

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Define the new premiers to add
new_premiers = [
    {
        "personId": "person:ca:bc:premier:eby",
        "name": "David Eby",
        "title": "Premier of British Columbia",
        "regionId": "province:ca:bc",
        "partyName": "British Columbia New Democratic Party",
        "partyURL": "https://www.bcndp.ca/",
        "startDate": "2022-11-18",
        "endDate": None,
        "officialSiteURL": "https://news.gov.bc.ca/office-of-the-premier",
        "photoURL": None
    },
    {
        "personId": "person:ca:ab:premier:smith",
        "name": "Danielle Smith",
        "title": "Premier of Alberta",
        "regionId": "province:ca:ab",
        "partyName": "United Conservative Party",
        "partyURL": "https://www.unitedconservative.ca/",
        "startDate": "2022-10-11",
        "endDate": None,
        "officialSiteURL": "https://www.alberta.ca/premier",
        "photoURL": None
    },
    {
        "personId": "person:ca:sk:premier:moe",
        "name": "Scott Moe",
        "title": "Premier of Saskatchewan",
        "regionId": "province:ca:sk",
        "partyName": "Saskatchewan Party",
        "partyURL": "https://www.saskparty.com/",
        "startDate": "2018-02-02",
        "endDate": None,
        "officialSiteURL": "https://www.saskatchewan.ca/government/government-structure/premier-scott-moe",
        "photoURL": None
    },
    {
        "personId": "person:ca:mb:premier:kinew",
        "name": "Wab Kinew",
        "title": "Premier of Manitoba",
        "regionId": "province:ca:mb",
        "partyName": "New Democratic Party of Manitoba",
        "partyURL": "https://www.manitobandp.ca/",
        "startDate": "2023-10-18",
        "endDate": None,
        "officialSiteURL": "https://www.gov.mb.ca/minister/premier/",
        "photoURL": None
    },
    {
        "personId": "person:ca:nb:premier:holt",
        "name": "Susan Holt",
        "title": "Premier of New Brunswick",
        "regionId": "province:ca:nb",
        "partyName": "New Brunswick Liberal Association",
        "partyURL": "https://nbliberal.ca/",
        "startDate": "2024-11-02",
        "endDate": None,
        "officialSiteURL": "https://www.gnb.ca/en/org/office-of-the-premier.html",
        "photoURL": None
    },
    {
        "personId": "person:ca:ns:premier:houston",
        "name": "Tim Houston",
        "title": "Premier of Nova Scotia",
        "regionId": "province:ca:ns",
        "partyName": "Progressive Conservative Association of Nova Scotia",
        "partyURL": "https://pcpartyns.ca/",
        "startDate": "2021-08-31",
        "endDate": None,
        "officialSiteURL": "https://premier.novascotia.ca/",
        "photoURL": None
    },
    {
        "personId": "person:ca:pe:premier:lantz",
        "name": "Rob Lantz",
        "title": "Premier of Prince Edward Island",
        "regionId": "province:ca:pe",
        "partyName": "Progressive Conservative Party of Prince Edward Island",
        "partyURL": "https://www.pcpei.ca/",
        "startDate": "2025-02-21",
        "endDate": None,
        "officialSiteURL": "https://www.princeedwardisland.ca/en/topic/premier-of-prince-edward-island",
        "photoURL": None
    },
    {
        "personId": "person:ca:nl:premier:wakeham",
        "name": "Tony Wakeham",
        "title": "Premier of Newfoundland and Labrador",
        "regionId": "province:ca:nl",
        "partyName": "Progressive Conservative Party of Newfoundland and Labrador",
        "partyURL": "https://www.pcparty.nf.ca/",
        "startDate": "2025-10-29",
        "endDate": None,
        "officialSiteURL": "https://www.gov.nl.ca/exec/premier/",
        "photoURL": None
    },
    {
        "personId": "person:ca:yt:premier:pemberton",
        "name": "Mike Pemberton",
        "title": "Premier of Yukon",
        "regionId": "province:ca:yt",
        "partyName": "Yukon Liberal Party",
        "partyURL": "https://liberal.yk.ca/",
        "startDate": "2025-06-27",
        "endDate": None,
        "officialSiteURL": "https://yukon.ca/en/your-government/office-premier",
        "photoURL": None
    },
    {
        "personId": "person:ca:nt:premier:simpson",
        "name": "R.J. Simpson",
        "title": "Premier of Northwest Territories",
        "regionId": "province:ca:nt",
        "partyName": None,
        "partyURL": None,
        "startDate": "2023-12-08",
        "endDate": None,
        "officialSiteURL": "https://www.gov.nt.ca/en/premier-rj-simpson",
        "photoURL": None
    },
    {
        "personId": "person:ca:nu:premier:akeeagok",
        "name": "P.J. Akeeagok",
        "title": "Premier of Nunavut",
        "regionId": "province:ca:nu",
        "partyName": None,
        "partyURL": None,
        "startDate": "2021-11-19",
        "endDate": None,
        "officialSiteURL": "https://www.premier.gov.nu.ca/en",
        "photoURL": None
    }
]

# Add the new premiers to the officeholders array
data['officeholders'].extend(new_premiers)

# Write back to the file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully added {len(new_premiers)} Canadian premiers")
print(f"Total officeholders: {len(data['officeholders'])}")
