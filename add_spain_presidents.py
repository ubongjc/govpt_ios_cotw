#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Spanish Autonomous Community and City Presidents (2024-2025)
spanish_presidents = [
    {
        "personId": "person:es:an:president:moreno",
        "name": "Juan Manuel Moreno",
        "title": "President of Andalusia",
        "regionId": "region:es:an",
        "partyName": "People's Party",
        "startDate": "2019-01-18",
        "endDate": None
    },
    {
        "personId": "person:es:ar:president:azcon",
        "name": "Jorge Azcón",
        "title": "President of Aragon",
        "regionId": "region:es:ar",
        "partyName": "People's Party",
        "startDate": "2023-08-11",
        "endDate": None
    },
    {
        "personId": "person:es:as:president:barbon",
        "name": "Adrián Barbón",
        "title": "President of Asturias",
        "regionId": "region:es:as",
        "partyName": "Spanish Socialist Workers' Party",
        "startDate": "2019-07-20",
        "endDate": None
    },
    {
        "personId": "person:es:ib:president:prohens",
        "name": "Marga Prohens",
        "title": "President of the Balearic Islands",
        "regionId": "region:es:ib",
        "partyName": "People's Party",
        "startDate": "2023-07-06",
        "endDate": None
    },
    {
        "personId": "person:es:pv:president:pradales",
        "name": "Imanol Pradales",
        "title": "Lehendakari of Basque Country",
        "regionId": "region:es:pv",
        "partyName": "Basque Nationalist Party",
        "startDate": "2024-06-22",
        "endDate": None
    },
    {
        "personId": "person:es:cn:president:clavijo",
        "name": "Fernando Clavijo",
        "title": "President of the Canary Islands",
        "regionId": "region:es:cn",
        "partyName": "Canarian Coalition",
        "startDate": "2023-07-12",
        "endDate": None
    },
    {
        "personId": "person:es:cb:president:buruaga",
        "name": "María José Sáenz de Buruaga",
        "title": "President of Cantabria",
        "regionId": "region:es:cb",
        "partyName": "People's Party",
        "startDate": "2023-07-04",
        "endDate": None
    },
    {
        "personId": "person:es:cl:president:manueco",
        "name": "Alfonso Fernández Mañueco",
        "title": "President of Castile and León",
        "regionId": "region:es:cl",
        "partyName": "People's Party",
        "startDate": "2019-07-12",
        "endDate": None
    },
    {
        "personId": "person:es:cm:president:page",
        "name": "Emiliano García-Page",
        "title": "President of Castilla-La Mancha",
        "regionId": "region:es:cm",
        "partyName": "Spanish Socialist Workers' Party",
        "startDate": "2015-07-04",
        "endDate": None
    },
    {
        "personId": "person:es:ct:president:illa",
        "name": "Salvador Illa",
        "title": "President of Catalonia",
        "regionId": "region:es:ct",
        "partyName": "Socialists' Party of Catalonia",
        "startDate": "2024-08-10",
        "endDate": None
    },
    {
        "personId": "person:es:ce:president:vivas",
        "name": "Juan Jesús Vivas",
        "title": "President of Ceuta",
        "regionId": "city:es:ce",
        "partyName": "People's Party",
        "startDate": "2001-02-06",
        "endDate": None
    },
    {
        "personId": "person:es:ex:president:guardiola",
        "name": "María Guardiola",
        "title": "President of Extremadura",
        "regionId": "region:es:ex",
        "partyName": "People's Party",
        "startDate": "2023-07-14",
        "endDate": None
    },
    {
        "personId": "person:es:ga:president:rueda",
        "name": "Alfonso Rueda",
        "title": "President of Galicia",
        "regionId": "region:es:ga",
        "partyName": "People's Party",
        "startDate": "2022-05-13",
        "endDate": None
    },
    {
        "personId": "person:es:ri:president:capellan",
        "name": "Gonzalo Capellán",
        "title": "President of La Rioja",
        "regionId": "region:es:ri",
        "partyName": "People's Party",
        "startDate": "2023-06-28",
        "endDate": None
    },
    {
        "personId": "person:es:md:president:ayuso",
        "name": "Isabel Díaz Ayuso",
        "title": "President of the Community of Madrid",
        "regionId": "region:es:md",
        "partyName": "People's Party",
        "startDate": "2019-08-17",
        "endDate": None
    },
    {
        "personId": "person:es:ml:president:imbroda",
        "name": "Juan José Imbroda",
        "title": "President of Melilla",
        "regionId": "city:es:ml",
        "partyName": "People's Party",
        "startDate": "2023-07-07",
        "endDate": None
    },
    {
        "personId": "person:es:mc:president:miras",
        "name": "Fernando López Miras",
        "title": "President of the Region of Murcia",
        "regionId": "region:es:mc",
        "partyName": "People's Party",
        "startDate": "2017-05-02",
        "endDate": None
    },
    {
        "personId": "person:es:nc:president:chivite",
        "name": "María Chivite",
        "title": "President of Navarre",
        "regionId": "region:es:nc",
        "partyName": "Spanish Socialist Workers' Party",
        "startDate": "2019-08-06",
        "endDate": None
    },
    {
        "personId": "person:es:vc:president:mazon",
        "name": "Carlos Mazón",
        "title": "President of the Valencian Community",
        "regionId": "region:es:vc",
        "partyName": "People's Party",
        "startDate": "2023-07-14",
        "endDate": None
    }
]

# Add all presidents
data['officeholders'].extend(spanish_presidents)

print(f"✅ Added {len(spanish_presidents)} Spanish autonomous community/city presidents")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
