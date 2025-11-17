#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# French Regional Presidents (as of 2024-2025)
# 13 Metropolitan + 5 Overseas regions
french_presidents = [
    # Metropolitan Regions
    {
        "personId": "person:fr:ara:president:wauquiez",
        "name": "Laurent Wauquiez",
        "title": "President of Auvergne-Rhône-Alpes",
        "regionId": "region:fr:ara",
        "partyName": "The Republicans",
        "startDate": "2015-12-18",
        "endDate": None
    },
    {
        "personId": "person:fr:bfc:president:revet",
        "name": "Marie-Guite Dufay",
        "title": "President of Bourgogne-Franche-Comté",
        "regionId": "region:fr:bfc",
        "partyName": "Socialist Party",
        "startDate": "2015-12-23",
        "endDate": None
    },
    {
        "personId": "person:fr:bre:president:chesnais",
        "name": "Loïg Chesnais-Girard",
        "title": "President of Brittany",
        "regionId": "region:fr:bre",
        "partyName": "Socialist Party",
        "startDate": "2017-06-23",
        "endDate": None
    },
    {
        "personId": "person:fr:cvl:president:bonneau",
        "name": "François Bonneau",
        "title": "President of Centre-Val de Loire",
        "regionId": "region:fr:cvl",
        "partyName": "Socialist Party",
        "startDate": "2015-12-17",
        "endDate": None
    },
    {
        "personId": "person:fr:20r:president:simeoni",
        "name": "Gilles Simeoni",
        "title": "President of Corsica",
        "regionId": "region:fr:20r",
        "partyName": "Femu a Corsica",
        "startDate": "2015-12-18",
        "endDate": None
    },
    {
        "personId": "person:fr:ges:president:rottner",
        "name": "Frédéric Rottner",
        "title": "President of Grand Est",
        "regionId": "region:fr:ges",
        "partyName": "The Republicans",
        "startDate": "2017-10-20",
        "endDate": None
    },
    {
        "personId": "person:fr:hdf:president:bertrand",
        "name": "Xavier Bertrand",
        "title": "President of Hauts-de-France",
        "regionId": "region:fr:hdf",
        "partyName": "The Republicans",
        "startDate": "2015-12-14",
        "endDate": None
    },
    {
        "personId": "person:fr:idf:president:pecresse",
        "name": "Valérie Pécresse",
        "title": "President of Île-de-France",
        "regionId": "region:fr:idf",
        "partyName": "The Republicans",
        "startDate": "2015-12-18",
        "endDate": None
    },
    {
        "personId": "person:fr:nor:president:morin",
        "name": "Hervé Morin",
        "title": "President of Normandy",
        "regionId": "region:fr:nor",
        "partyName": "The Centrists",
        "startDate": "2015-12-21",
        "endDate": None
    },
    {
        "personId": "person:fr:naq:president:rousset",
        "name": "Alain Rousset",
        "title": "President of Nouvelle-Aquitaine",
        "regionId": "region:fr:naq",
        "partyName": "Socialist Party",
        "startDate": "2015-12-14",
        "endDate": None
    },
    {
        "personId": "person:fr:occ:president:delga",
        "name": "Carole Delga",
        "title": "President of Occitanie",
        "regionId": "region:fr:occ",
        "partyName": "Socialist Party",
        "startDate": "2015-12-14",
        "endDate": None
    },
    {
        "personId": "person:fr:pdl:president:ayrault",
        "name": "Christelle Morançais",
        "title": "President of Pays de la Loire",
        "regionId": "region:fr:pdl",
        "partyName": "The Republicans",
        "startDate": "2017-05-05",
        "endDate": None
    },
    {
        "personId": "person:fr:pac:president:muselier",
        "name": "Renaud Muselier",
        "title": "President of Provence-Alpes-Côte d'Azur",
        "regionId": "region:fr:pac",
        "partyName": "The Republicans",
        "startDate": "2015-12-14",
        "endDate": None
    },
    # Overseas Regions
    {
        "personId": "person:fr:gp:president:chalus",
        "name": "Ary Chalus",
        "title": "President of Guadeloupe",
        "regionId": "region:fr:gp",
        "partyName": "Various Left",
        "startDate": "2021-07-02",
        "endDate": None
    },
    {
        "personId": "person:fr:mq:president:letchimy",
        "name": "Serge Letchimy",
        "title": "President of Martinique",
        "regionId": "region:fr:mq",
        "partyName": "Martinican Progressive Party",
        "startDate": "2015-12-18",
        "endDate": None
    },
    {
        "personId": "person:fr:gf:president:serville",
        "name": "Gabriel Serville",
        "title": "President of French Guiana",
        "regionId": "region:fr:gf",
        "partyName": "Guianese Decolonization and Social Emancipation Movement",
        "startDate": "2021-07-02",
        "endDate": None
    },
    {
        "personId": "person:fr:re:president:bello",
        "name": "Huguette Bello",
        "title": "President of Réunion",
        "regionId": "region:fr:re",
        "partyName": "For Réunion",
        "startDate": "2021-07-02",
        "endDate": None
    },
    {
        "personId": "person:fr:yt:president:ousseni",
        "name": "Ben Issa Ousseni",
        "title": "President of Mayotte",
        "regionId": "region:fr:yt",
        "partyName": "The Republicans",
        "startDate": "2021-07-02",
        "endDate": None
    }
]

# Add all presidents
data['officeholders'].extend(french_presidents)

print(f"✅ Added {len(french_presidents)} French regional presidents")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
