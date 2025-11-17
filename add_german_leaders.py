#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Add all 16 German minister-presidents
german_leaders = [
    {
        "personId": "person:de:bw:ministerpres:kretschmann",
        "name": "Winfried Kretschmann",
        "title": "Minister-President of Baden-Württemberg",
        "regionId": "state:de:bw",
        "partyName": "Alliance 90/The Greens",
        "partyURL": "https://www.gruene.de/",
        "startDate": "2011-05-12",
        "endDate": None,
        "officialSiteURL": "https://www.baden-wuerttemberg.de/de/regierung/",
        "photoURL": None
    },
    {
        "personId": "person:de:by:ministerpres:soeder",
        "name": "Markus Söder",
        "title": "Minister-President of Bavaria",
        "regionId": "state:de:by",
        "partyName": "Christian Social Union",
        "partyURL": "https://www.csu.de/",
        "startDate": "2018-03-16",
        "endDate": None,
        "officialSiteURL": "https://www.bayern.de/",
        "photoURL": None
    },
    {
        "personId": "person:de:be:mayor:wegner",
        "name": "Kai Wegner",
        "title": "Governing Mayor of Berlin",
        "regionId": "state:de:be",
        "partyName": "Christian Democratic Union",
        "partyURL": "https://www.cdu.de/",
        "startDate": "2023-04-27",
        "endDate": None,
        "officialSiteURL": "https://www.berlin.de/rbmskzl/",
        "photoURL": None
    },
    {
        "personId": "person:de:bb:ministerpres:woidke",
        "name": "Dietmar Woidke",
        "title": "Minister-President of Brandenburg",
        "regionId": "state:de:bb",
        "partyName": "Social Democratic Party",
        "partyURL": "https://www.spd.de/",
        "startDate": "2013-08-28",
        "endDate": None,
        "officialSiteURL": "https://www.brandenburg.de/",
        "photoURL": None
    },
    {
        "personId": "person:de:hb:mayor:bovenschulte",
        "name": "Andreas Bovenschulte",
        "title": "President of the Senate and Mayor of Bremen",
        "regionId": "state:de:hb",
        "partyName": "Social Democratic Party",
        "partyURL": "https://www.spd.de/",
        "startDate": "2019-08-15",
        "endDate": None,
        "officialSiteURL": "https://www.senatspressestelle.bremen.de/",
        "photoURL": None
    },
    {
        "personId": "person:de:hh:mayor:tschentscher",
        "name": "Peter Tschentscher",
        "title": "First Mayor of Hamburg",
        "regionId": "state:de:hh",
        "partyName": "Social Democratic Party",
        "partyURL": "https://www.spd.de/",
        "startDate": "2018-03-28",
        "endDate": None,
        "officialSiteURL": "https://www.hamburg.de/",
        "photoURL": None
    },
    {
        "personId": "person:de:he:ministerpres:rhein",
        "name": "Boris Rhein",
        "title": "Minister-President of Hesse",
        "regionId": "state:de:he",
        "partyName": "Christian Democratic Union",
        "partyURL": "https://www.cdu.de/",
        "startDate": "2022-05-31",
        "endDate": None,
        "officialSiteURL": "https://www.hessen.de/",
        "photoURL": None
    },
    {
        "personId": "person:de:ni:ministerpres:lies",
        "name": "Olaf Lies",
        "title": "Minister-President of Lower Saxony",
        "regionId": "state:de:ni",
        "partyName": "Social Democratic Party",
        "partyURL": "https://www.spd.de/",
        "startDate": "2025-05-20",
        "endDate": None,
        "officialSiteURL": "https://www.niedersachsen.de/",
        "photoURL": None
    },
    {
        "personId": "person:de:mv:ministerpres:schwesig",
        "name": "Manuela Schwesig",
        "title": "Minister-President of Mecklenburg-Vorpommern",
        "regionId": "state:de:mv",
        "partyName": "Social Democratic Party",
        "partyURL": "https://www.spd.de/",
        "startDate": "2017-07-04",
        "endDate": None,
        "officialSiteURL": "https://www.regierung-mv.de/",
        "photoURL": None
    },
    {
        "personId": "person:de:nw:ministerpres:wuest",
        "name": "Hendrik Wüst",
        "title": "Minister-President of North Rhine-Westphalia",
        "regionId": "state:de:nw",
        "partyName": "Christian Democratic Union",
        "partyURL": "https://www.cdu.de/",
        "startDate": "2021-10-27",
        "endDate": None,
        "officialSiteURL": "https://www.land.nrw/",
        "photoURL": None
    },
    {
        "personId": "person:de:rp:ministerpres:schweitzer",
        "name": "Alexander Schweitzer",
        "title": "Minister-President of Rhineland-Palatinate",
        "regionId": "state:de:rp",
        "partyName": "Social Democratic Party",
        "partyURL": "https://www.spd.de/",
        "startDate": "2024-07-10",
        "endDate": None,
        "officialSiteURL": "https://www.rlp.de/",
        "photoURL": None
    },
    {
        "personId": "person:de:sl:ministerpres:rehlinger",
        "name": "Anke Rehlinger",
        "title": "Minister-President of Saarland",
        "regionId": "state:de:sl",
        "partyName": "Social Democratic Party",
        "partyURL": "https://www.spd.de/",
        "startDate": "2022-04-25",
        "endDate": None,
        "officialSiteURL": "https://www.saarland.de/",
        "photoURL": None
    },
    {
        "personId": "person:de:sn:ministerpres:kretschmer",
        "name": "Michael Kretschmer",
        "title": "Minister-President of Saxony",
        "regionId": "state:de:sn",
        "partyName": "Christian Democratic Union",
        "partyURL": "https://www.cdu.de/",
        "startDate": "2017-12-13",
        "endDate": None,
        "officialSiteURL": "https://www.sachsen.de/",
        "photoURL": None
    },
    {
        "personId": "person:de:st:ministerpres:haseloff",
        "name": "Reiner Haseloff",
        "title": "Minister-President of Saxony-Anhalt",
        "regionId": "state:de:st",
        "partyName": "Christian Democratic Union",
        "partyURL": "https://www.cdu.de/",
        "startDate": "2011-04-19",
        "endDate": None,
        "officialSiteURL": "https://www.sachsen-anhalt.de/",
        "photoURL": None
    },
    {
        "personId": "person:de:sh:ministerpres:guenther",
        "name": "Daniel Günther",
        "title": "Minister-President of Schleswig-Holstein",
        "regionId": "state:de:sh",
        "partyName": "Christian Democratic Union",
        "partyURL": "https://www.cdu.de/",
        "startDate": "2017-06-28",
        "endDate": None,
        "officialSiteURL": "https://www.schleswig-holstein.de/",
        "photoURL": None
    },
    {
        "personId": "person:de:th:ministerpres:voigt",
        "name": "Mario Voigt",
        "title": "Minister-President of Thuringia",
        "regionId": "state:de:th",
        "partyName": "Christian Democratic Union",
        "partyURL": "https://www.cdu.de/",
        "startDate": "2024-12-12",
        "endDate": None,
        "officialSiteURL": "https://www.thueringen.de/",
        "photoURL": None
    }
]

data['officeholders'].extend(german_leaders)

# Write back to the file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully added {len(german_leaders)} German minister-presidents")
print(f"Total officeholders: {len(data['officeholders'])}")
