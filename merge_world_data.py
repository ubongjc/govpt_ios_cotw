#!/usr/bin/env python3
import json
from datetime import datetime

# Read the backup file (has other continents)
with open('GPT/Resources/seed_data_backup.json', 'r') as f:
    backup_data = json.load(f)

# Read the current North America focused file
with open('GPT/Resources/seed_data.json', 'r') as f:
    north_america_data = json.load(f)

# Create a merged dataset
merged_data = {
    "regions": [],
    "officeholders": [],
    "promises": [],
    "evidence": [],
    "statusSnapshots": [],
    "industries": [],
    "policyTags": [],
    "policyTagIndustries": [],
    "promiseIndustryImpacts": []
}

# First, add ALL continents
all_continents = [
    {
        "regionId": "cont:africa",
        "name": "Africa",
        "isoCode": "AF",
        "type": "continent",
        "parentRegionId": None,
        "latitude": 8.7832,
        "longitude": 34.5085
    },
    {
        "regionId": "cont:asia",
        "name": "Asia",
        "isoCode": "AS",
        "type": "continent",
        "parentRegionId": None,
        "latitude": 34.0479,
        "longitude": 100.6197
    },
    {
        "regionId": "cont:europe",
        "name": "Europe",
        "isoCode": "EU",
        "type": "continent",
        "parentRegionId": None,
        "latitude": 54.5260,
        "longitude": 15.2551
    },
    {
        "regionId": "cont:north_america",
        "name": "North America",
        "isoCode": "NA",
        "type": "continent",
        "parentRegionId": None,
        "latitude": 54.5260,
        "longitude": -105.2551
    },
    {
        "regionId": "cont:south_america",
        "name": "South America",
        "isoCode": "SA",
        "type": "continent",
        "parentRegionId": None,
        "latitude": -8.7832,
        "longitude": -55.4915
    },
    {
        "regionId": "cont:oceania",
        "name": "Oceania",
        "isoCode": "OC",
        "type": "continent",
        "parentRegionId": None,
        "latitude": -22.7359,
        "longitude": 140.0188
    }
]

merged_data["regions"].extend(all_continents)

# Add all North American regions (countries, states, cities) from our detailed file
for region in north_america_data["regions"]:
    if region["type"] != "continent":  # Skip continent since we added it above
        merged_data["regions"].append(region)

# Add European countries with current leaders
european_countries = [
    {
        "regionId": "country:gb",
        "name": "United Kingdom",
        "isoCode": "GB",
        "type": "country",
        "parentRegionId": "cont:europe",
        "latitude": 55.3781,
        "longitude": -3.4360
    },
    {
        "regionId": "country:fr",
        "name": "France",
        "isoCode": "FR",
        "type": "country",
        "parentRegionId": "cont:europe",
        "latitude": 46.2276,
        "longitude": 2.2137
    },
    {
        "regionId": "country:de",
        "name": "Germany",
        "isoCode": "DE",
        "type": "country",
        "parentRegionId": "cont:europe",
        "latitude": 51.1657,
        "longitude": 10.4515
    },
    {
        "regionId": "country:it",
        "name": "Italy",
        "isoCode": "IT",
        "type": "country",
        "parentRegionId": "cont:europe",
        "latitude": 41.8719,
        "longitude": 12.5674
    },
    {
        "regionId": "country:es",
        "name": "Spain",
        "isoCode": "ES",
        "type": "country",
        "parentRegionId": "cont:europe",
        "latitude": 40.4637,
        "longitude": -3.7492
    },
    {
        "regionId": "country:nl",
        "name": "Netherlands",
        "isoCode": "NL",
        "type": "country",
        "parentRegionId": "cont:europe",
        "latitude": 52.1326,
        "longitude": 5.2913
    },
    {
        "regionId": "country:se",
        "name": "Sweden",
        "isoCode": "SE",
        "type": "country",
        "parentRegionId": "cont:europe",
        "latitude": 60.1282,
        "longitude": 18.6435
    },
    {
        "regionId": "country:no",
        "name": "Norway",
        "isoCode": "NO",
        "type": "country",
        "parentRegionId": "cont:europe",
        "latitude": 60.4720,
        "longitude": 8.4689
    },
    {
        "regionId": "country:pl",
        "name": "Poland",
        "isoCode": "PL",
        "type": "country",
        "parentRegionId": "cont:europe",
        "latitude": 51.9194,
        "longitude": 19.1451
    },
    {
        "regionId": "country:ua",
        "name": "Ukraine",
        "isoCode": "UA",
        "type": "country",
        "parentRegionId": "cont:europe",
        "latitude": 48.3794,
        "longitude": 31.1656
    }
]

# Add Asian countries
asian_countries = [
    {
        "regionId": "country:cn",
        "name": "China",
        "isoCode": "CN",
        "type": "country",
        "parentRegionId": "cont:asia",
        "latitude": 35.8617,
        "longitude": 104.1954
    },
    {
        "regionId": "country:jp",
        "name": "Japan",
        "isoCode": "JP",
        "type": "country",
        "parentRegionId": "cont:asia",
        "latitude": 36.2048,
        "longitude": 138.2529
    },
    {
        "regionId": "country:in",
        "name": "India",
        "isoCode": "IN",
        "type": "country",
        "parentRegionId": "cont:asia",
        "latitude": 20.5937,
        "longitude": 78.9629
    },
    {
        "regionId": "country:kr",
        "name": "South Korea",
        "isoCode": "KR",
        "type": "country",
        "parentRegionId": "cont:asia",
        "latitude": 35.9078,
        "longitude": 127.7669
    },
    {
        "regionId": "country:sg",
        "name": "Singapore",
        "isoCode": "SG",
        "type": "country",
        "parentRegionId": "cont:asia",
        "latitude": 1.3521,
        "longitude": 103.8198
    },
    {
        "regionId": "country:id",
        "name": "Indonesia",
        "isoCode": "ID",
        "type": "country",
        "parentRegionId": "cont:asia",
        "latitude": -0.7893,
        "longitude": 113.9213
    },
    {
        "regionId": "country:my",
        "name": "Malaysia",
        "isoCode": "MY",
        "type": "country",
        "parentRegionId": "cont:asia",
        "latitude": 4.2105,
        "longitude": 101.9758
    },
    {
        "regionId": "country:th",
        "name": "Thailand",
        "isoCode": "TH",
        "type": "country",
        "parentRegionId": "cont:asia",
        "latitude": 15.8700,
        "longitude": 100.9925
    },
    {
        "regionId": "country:vn",
        "name": "Vietnam",
        "isoCode": "VN",
        "type": "country",
        "parentRegionId": "cont:asia",
        "latitude": 14.0583,
        "longitude": 108.2772
    },
    {
        "regionId": "country:ph",
        "name": "Philippines",
        "isoCode": "PH",
        "type": "country",
        "parentRegionId": "cont:asia",
        "latitude": 12.8797,
        "longitude": 121.7740
    }
]

# Add South American countries
south_american_countries = [
    {
        "regionId": "country:br",
        "name": "Brazil",
        "isoCode": "BR",
        "type": "country",
        "parentRegionId": "cont:south_america",
        "latitude": -14.2350,
        "longitude": -51.9253
    },
    {
        "regionId": "country:ar",
        "name": "Argentina",
        "isoCode": "AR",
        "type": "country",
        "parentRegionId": "cont:south_america",
        "latitude": -38.4161,
        "longitude": -63.6167
    },
    {
        "regionId": "country:cl",
        "name": "Chile",
        "isoCode": "CL",
        "type": "country",
        "parentRegionId": "cont:south_america",
        "latitude": -35.6751,
        "longitude": -71.5430
    },
    {
        "regionId": "country:pe",
        "name": "Peru",
        "isoCode": "PE",
        "type": "country",
        "parentRegionId": "cont:south_america",
        "latitude": -9.1900,
        "longitude": -75.0152
    },
    {
        "regionId": "country:co",
        "name": "Colombia",
        "isoCode": "CO",
        "type": "country",
        "parentRegionId": "cont:south_america",
        "latitude": 4.5709,
        "longitude": -74.2973
    },
    {
        "regionId": "country:ve",
        "name": "Venezuela",
        "isoCode": "VE",
        "type": "country",
        "parentRegionId": "cont:south_america",
        "latitude": 6.4238,
        "longitude": -66.5897
    },
    {
        "regionId": "country:ec",
        "name": "Ecuador",
        "isoCode": "EC",
        "type": "country",
        "parentRegionId": "cont:south_america",
        "latitude": -1.8312,
        "longitude": -78.1834
    },
    {
        "regionId": "country:uy",
        "name": "Uruguay",
        "isoCode": "UY",
        "type": "country",
        "parentRegionId": "cont:south_america",
        "latitude": -32.5228,
        "longitude": -55.7658
    }
]

# Add African countries
african_countries = [
    {
        "regionId": "country:za",
        "name": "South Africa",
        "isoCode": "ZA",
        "type": "country",
        "parentRegionId": "cont:africa",
        "latitude": -30.5595,
        "longitude": 22.9375
    },
    {
        "regionId": "country:ng",
        "name": "Nigeria",
        "isoCode": "NG",
        "type": "country",
        "parentRegionId": "cont:africa",
        "latitude": 9.0820,
        "longitude": 8.6753
    },
    {
        "regionId": "country:eg",
        "name": "Egypt",
        "isoCode": "EG",
        "type": "country",
        "parentRegionId": "cont:africa",
        "latitude": 26.8206,
        "longitude": 30.8025
    },
    {
        "regionId": "country:ke",
        "name": "Kenya",
        "isoCode": "KE",
        "type": "country",
        "parentRegionId": "cont:africa",
        "latitude": -0.0236,
        "longitude": 37.9062
    },
    {
        "regionId": "country:et",
        "name": "Ethiopia",
        "isoCode": "ET",
        "type": "country",
        "parentRegionId": "cont:africa",
        "latitude": 9.1450,
        "longitude": 40.4897
    },
    {
        "regionId": "country:gh",
        "name": "Ghana",
        "isoCode": "GH",
        "type": "country",
        "parentRegionId": "cont:africa",
        "latitude": 7.9465,
        "longitude": -1.0232
    },
    {
        "regionId": "country:ma",
        "name": "Morocco",
        "isoCode": "MA",
        "type": "country",
        "parentRegionId": "cont:africa",
        "latitude": 31.7917,
        "longitude": -7.0926
    },
    {
        "regionId": "country:tz",
        "name": "Tanzania",
        "isoCode": "TZ",
        "type": "country",
        "parentRegionId": "cont:africa",
        "latitude": -6.3690,
        "longitude": 34.8888
    }
]

# Add Oceania countries
oceania_countries = [
    {
        "regionId": "country:au",
        "name": "Australia",
        "isoCode": "AU",
        "type": "country",
        "parentRegionId": "cont:oceania",
        "latitude": -25.2744,
        "longitude": 133.7751
    },
    {
        "regionId": "country:nz",
        "name": "New Zealand",
        "isoCode": "NZ",
        "type": "country",
        "parentRegionId": "cont:oceania",
        "latitude": -40.9006,
        "longitude": 174.8860
    },
    {
        "regionId": "country:fj",
        "name": "Fiji",
        "isoCode": "FJ",
        "type": "country",
        "parentRegionId": "cont:oceania",
        "latitude": -17.7134,
        "longitude": 178.0650
    },
    {
        "regionId": "country:pg",
        "name": "Papua New Guinea",
        "isoCode": "PG",
        "type": "country",
        "parentRegionId": "cont:oceania",
        "latitude": -6.3150,
        "longitude": 143.9555
    }
]

# Add all countries to regions
merged_data["regions"].extend(european_countries)
merged_data["regions"].extend(asian_countries)
merged_data["regions"].extend(south_american_countries)
merged_data["regions"].extend(african_countries)
merged_data["regions"].extend(oceania_countries)

# Add some major cities from around the world
world_cities = [
    # Europe
    {
        "regionId": "city:gb:london",
        "name": "London",
        "isoCode": "LON",
        "type": "city",
        "parentRegionId": "country:gb",
        "latitude": 51.5074,
        "longitude": -0.1278
    },
    {
        "regionId": "city:fr:paris",
        "name": "Paris",
        "isoCode": "PAR",
        "type": "city",
        "parentRegionId": "country:fr",
        "latitude": 48.8566,
        "longitude": 2.3522
    },
    {
        "regionId": "city:de:berlin",
        "name": "Berlin",
        "isoCode": "BER",
        "type": "city",
        "parentRegionId": "country:de",
        "latitude": 52.5200,
        "longitude": 13.4050
    },
    # Asia
    {
        "regionId": "city:jp:tokyo",
        "name": "Tokyo",
        "isoCode": "TYO",
        "type": "city",
        "parentRegionId": "country:jp",
        "latitude": 35.6762,
        "longitude": 139.6503
    },
    {
        "regionId": "city:cn:beijing",
        "name": "Beijing",
        "isoCode": "BEJ",
        "type": "city",
        "parentRegionId": "country:cn",
        "latitude": 39.9042,
        "longitude": 116.4074
    },
    {
        "regionId": "city:in:delhi",
        "name": "New Delhi",
        "isoCode": "DEL",
        "type": "city",
        "parentRegionId": "country:in",
        "latitude": 28.6139,
        "longitude": 77.2090
    },
    # South America
    {
        "regionId": "city:br:saopaulo",
        "name": "São Paulo",
        "isoCode": "SAO",
        "type": "city",
        "parentRegionId": "country:br",
        "latitude": -23.5505,
        "longitude": -46.6333
    },
    {
        "regionId": "city:ar:buenosaires",
        "name": "Buenos Aires",
        "isoCode": "BUE",
        "type": "city",
        "parentRegionId": "country:ar",
        "latitude": -34.6037,
        "longitude": -58.3816
    },
    # Oceania
    {
        "regionId": "city:au:sydney",
        "name": "Sydney",
        "isoCode": "SYD",
        "type": "city",
        "parentRegionId": "country:au",
        "latitude": -33.8688,
        "longitude": 151.2093
    }
]

merged_data["regions"].extend(world_cities)

# Add all North American officeholders from our detailed data
merged_data["officeholders"].extend(north_america_data["officeholders"])

# Add leaders from other continents
world_leaders = [
    # Europe
    {
        "personId": "person:gb:pm:sunak",
        "name": "Rishi Sunak",
        "title": "Prime Minister of United Kingdom",
        "regionId": "country:gb",
        "partyName": "Conservative Party",
        "partyURL": "https://www.conservatives.com",
        "startDate": "2022-10-25T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.gov.uk/government/ministers/prime-minister",
        "photoURL": None
    },
    {
        "personId": "person:fr:president:macron",
        "name": "Emmanuel Macron",
        "title": "President of France",
        "regionId": "country:fr",
        "partyName": "Renaissance",
        "partyURL": "https://renaissance.fr",
        "startDate": "2017-05-14T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.elysee.fr",
        "photoURL": None
    },
    {
        "personId": "person:de:chancellor:scholz",
        "name": "Olaf Scholz",
        "title": "Chancellor of Germany",
        "regionId": "country:de",
        "partyName": "Social Democratic Party",
        "partyURL": "https://www.spd.de",
        "startDate": "2021-12-08T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.bundeskanzler.de",
        "photoURL": None
    },
    {
        "personId": "person:it:pm:meloni",
        "name": "Giorgia Meloni",
        "title": "Prime Minister of Italy",
        "regionId": "country:it",
        "partyName": "Brothers of Italy",
        "partyURL": "https://www.fratelli-italia.it",
        "startDate": "2022-10-22T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.governo.it",
        "photoURL": None
    },
    {
        "personId": "person:ua:president:zelensky",
        "name": "Volodymyr Zelensky",
        "title": "President of Ukraine",
        "regionId": "country:ua",
        "partyName": "Servant of the People",
        "partyURL": None,
        "startDate": "2019-05-20T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.president.gov.ua",
        "photoURL": None
    },
    # Asia
    {
        "personId": "person:cn:president:xi",
        "name": "Xi Jinping",
        "title": "President of China",
        "regionId": "country:cn",
        "partyName": "Communist Party of China",
        "partyURL": None,
        "startDate": "2013-03-14T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "http://www.gov.cn",
        "photoURL": None
    },
    {
        "personId": "person:jp:pm:kishida",
        "name": "Fumio Kishida",
        "title": "Prime Minister of Japan",
        "regionId": "country:jp",
        "partyName": "Liberal Democratic Party",
        "partyURL": "https://www.jimin.jp",
        "startDate": "2021-10-04T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.kantei.go.jp",
        "photoURL": None
    },
    {
        "personId": "person:in:pm:modi",
        "name": "Narendra Modi",
        "title": "Prime Minister of India",
        "regionId": "country:in",
        "partyName": "Bharatiya Janata Party",
        "partyURL": "https://www.bjp.org",
        "startDate": "2014-05-26T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.pmindia.gov.in",
        "photoURL": None
    },
    {
        "personId": "person:kr:president:yoon",
        "name": "Yoon Suk Yeol",
        "title": "President of South Korea",
        "regionId": "country:kr",
        "partyName": "People Power Party",
        "partyURL": None,
        "startDate": "2022-05-10T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.president.go.kr",
        "photoURL": None
    },
    # South America
    {
        "personId": "person:br:president:lula",
        "name": "Luiz Inácio Lula da Silva",
        "title": "President of Brazil",
        "regionId": "country:br",
        "partyName": "Workers' Party",
        "partyURL": "https://pt.org.br",
        "startDate": "2023-01-01T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.gov.br/planalto",
        "photoURL": None
    },
    {
        "personId": "person:ar:president:milei",
        "name": "Javier Milei",
        "title": "President of Argentina",
        "regionId": "country:ar",
        "partyName": "La Libertad Avanza",
        "partyURL": None,
        "startDate": "2023-12-10T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.argentina.gob.ar",
        "photoURL": None
    },
    # Africa
    {
        "personId": "person:za:president:ramaphosa",
        "name": "Cyril Ramaphosa",
        "title": "President of South Africa",
        "regionId": "country:za",
        "partyName": "African National Congress",
        "partyURL": "https://www.anc1912.org.za",
        "startDate": "2018-02-15T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.thepresidency.gov.za",
        "photoURL": None
    },
    {
        "personId": "person:ng:president:tinubu",
        "name": "Bola Tinubu",
        "title": "President of Nigeria",
        "regionId": "country:ng",
        "partyName": "All Progressives Congress",
        "partyURL": None,
        "startDate": "2023-05-29T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://statehouse.gov.ng",
        "photoURL": None
    },
    {
        "personId": "person:eg:president:sisi",
        "name": "Abdel Fattah el-Sisi",
        "title": "President of Egypt",
        "regionId": "country:eg",
        "partyName": "Independent",
        "partyURL": None,
        "startDate": "2014-06-08T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.presidency.eg",
        "photoURL": None
    },
    # Oceania
    {
        "personId": "person:au:pm:albanese",
        "name": "Anthony Albanese",
        "title": "Prime Minister of Australia",
        "regionId": "country:au",
        "partyName": "Labor Party",
        "partyURL": "https://www.alp.org.au",
        "startDate": "2022-05-23T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.pm.gov.au",
        "photoURL": None
    },
    {
        "personId": "person:nz:pm:luxon",
        "name": "Christopher Luxon",
        "title": "Prime Minister of New Zealand",
        "regionId": "country:nz",
        "partyName": "National Party",
        "partyURL": "https://www.national.org.nz",
        "startDate": "2023-11-27T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.beehive.govt.nz/minister/prime-minister",
        "photoURL": None
    }
]

merged_data["officeholders"].extend(world_leaders)

# Add all promises from North America
merged_data["promises"].extend(north_america_data["promises"])

# Add some promises from world leaders
world_promises = [
    {
        "promiseId": "promise:zelensky:victory:2023",
        "personId": "person:ua:president:zelensky",
        "regionId": "country:ua",
        "dateMade": "2023-02-24T00:00:00Z",
        "context": "One year anniversary of war speech",
        "quoteExact": "We will liberate all our territories and restore peace to Ukraine.",
        "summary": "Complete liberation of Ukrainian territories",
        "tagsJSON": "[\"defense\", \"sovereignty\", \"war\"]",
        "dueBy": None,
        "sourcePrimary": "https://www.president.gov.ua/en/news",
        "sourceType": "official_statement",
        "policyTagsJSON": "[\"defense\", \"national_security\"]",
        "effectInputsJSON": None
    },
    {
        "promiseId": "promise:modi:economy:2023",
        "personId": "person:in:pm:modi",
        "regionId": "country:in",
        "dateMade": "2023-08-15T00:00:00Z",
        "context": "Independence Day speech",
        "quoteExact": "India will become a $5 trillion economy and a developed nation by 2047.",
        "summary": "Make India a $5 trillion economy",
        "tagsJSON": "[\"economy\", \"development\", \"growth\"]",
        "dueBy": "2047-01-01T00:00:00Z",
        "sourcePrimary": "https://www.pmindia.gov.in",
        "sourceType": "official_statement",
        "policyTagsJSON": "[\"economic_development\", \"growth\"]",
        "effectInputsJSON": None
    }
]

merged_data["promises"].extend(world_promises)

# Sort everything for organization
merged_data["regions"].sort(key=lambda x: (x["type"], x.get("name", "")))
merged_data["officeholders"].sort(key=lambda x: x["name"])
merged_data["promises"].sort(key=lambda x: x["dateMade"])

# Statistics
print("Dataset Statistics:")
print(f"Total regions: {len(merged_data['regions'])}")
print(f"  - Continents: {len([r for r in merged_data['regions'] if r['type'] == 'continent'])}")
print(f"  - Countries: {len([r for r in merged_data['regions'] if r['type'] == 'country'])}")
print(f"  - States/Provinces: {len([r for r in merged_data['regions'] if r['type'] in ['state', 'province']])}")
print(f"  - Cities: {len([r for r in merged_data['regions'] if r['type'] == 'city'])}")
print(f"Total officeholders: {len(merged_data['officeholders'])}")
print(f"Total promises: {len(merged_data['promises'])}")

# Save the complete world dataset
with open('GPT/Resources/seed_data.json', 'w') as f:
    json.dump(merged_data, f, indent=2)

print("\n✅ Successfully merged all world data!")
print("The complete dataset has been saved to GPT/Resources/seed_data.json")