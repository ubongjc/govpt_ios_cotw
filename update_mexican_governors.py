#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Define transitions - old governors to end and new governors to add
outgoing_governors = {
    'person:mx:chiapas:governor:escandon': '2024-12-08',  # Rutilio Escandón → Eduardo Ramírez
    'person:mx:guanajuato:governor:rodriguez': '2024-09-26',  # Diego Sinhue → Libia García
    'person:mx:jalisco:governor:alfaro': '2024-12-06',  # Enrique Alfaro → Pablo Lemus
    'person:mx:mexicocity:governor:batres': '2024-10-05',  # Martí Batres → Clara Brugada
    'person:mx:morelos:governor:blanco': '2024-10-01',  # Cuauhtémoc Blanco → Margarita González
    'person:mx:puebla:governor:cespedes': '2024-12-14',  # Sergio Salomón → Alejandro Armenta
    'person:mx:tabasco:governor:merino': '2024-10-01',  # Carlos Merino → Javier May
    'person:mx:veracruz:governor:garcia': '2024-12-01',  # Cuitláhuac García → Rocío Nahle
}

# Set endDates for outgoing governors
changes = []
for officeholder in data['officeholders']:
    if officeholder['personId'] in outgoing_governors:
        officeholder['endDate'] = outgoing_governors[officeholder['personId']]
        changes.append(f"Set endDate for {officeholder['name']} to {outgoing_governors[officeholder['personId']]}")

# Add new governors
new_governors = [
    {
        "personId": "person:mx:chiapas:governor:ramirez",
        "name": "Eduardo Ramírez Aguilar",
        "title": "Governor of Chiapas",
        "regionId": "state:mx:chiapas",
        "partyName": "National Regeneration Movement (Morena)",
        "partyURL": None,
        "startDate": "2024-12-08",
        "endDate": None,
        "officialSiteURL": None,
        "photoURL": None
    },
    {
        "personId": "person:mx:guanajuato:governor:garcia",
        "name": "Libia García Muñoz Ledo",
        "title": "Governor of Guanajuato",
        "regionId": "state:mx:guanajuato",
        "partyName": "National Action Party (PAN)",
        "partyURL": None,
        "startDate": "2024-09-26",
        "endDate": None,
        "officialSiteURL": None,
        "photoURL": None
    },
    {
        "personId": "person:mx:jalisco:governor:lemus",
        "name": "Pablo Lemus Navarro",
        "title": "Governor of Jalisco",
        "regionId": "state:mx:jalisco",
        "partyName": "Citizens' Movement",
        "partyURL": None,
        "startDate": "2024-12-06",
        "endDate": None,
        "officialSiteURL": None,
        "photoURL": None
    },
    {
        "personId": "person:mx:mexicocity:governor:brugada",
        "name": "Clara Brugada",
        "title": "Head of Government of Mexico City",
        "regionId": "state:mx:mexicocity",
        "partyName": "National Regeneration Movement (Morena)",
        "partyURL": None,
        "startDate": "2024-10-05",
        "endDate": None,
        "officialSiteURL": None,
        "photoURL": None
    },
    {
        "personId": "person:mx:morelos:governor:gonzalez",
        "name": "Margarita González Saravia",
        "title": "Governor of Morelos",
        "regionId": "state:mx:morelos",
        "partyName": "National Regeneration Movement (Morena)",
        "partyURL": None,
        "startDate": "2024-10-01",
        "endDate": None,
        "officialSiteURL": None,
        "photoURL": None
    },
    {
        "personId": "person:mx:puebla:governor:armenta",
        "name": "Alejandro Armenta Mier",
        "title": "Governor of Puebla",
        "regionId": "state:mx:puebla",
        "partyName": "National Regeneration Movement (Morena)",
        "partyURL": None,
        "startDate": "2024-12-14",
        "endDate": None,
        "officialSiteURL": None,
        "photoURL": None
    },
    {
        "personId": "person:mx:tabasco:governor:may",
        "name": "Javier May Rodríguez",
        "title": "Governor of Tabasco",
        "regionId": "state:mx:tabasco",
        "partyName": "National Regeneration Movement (Morena)",
        "partyURL": None,
        "startDate": "2024-10-01",
        "endDate": None,
        "officialSiteURL": None,
        "photoURL": None
    },
    {
        "personId": "person:mx:veracruz:governor:nahle",
        "name": "Rocío Nahle García",
        "title": "Governor of Veracruz",
        "regionId": "state:mx:veracruz",
        "partyName": "National Regeneration Movement (Morena)",
        "partyURL": None,
        "startDate": "2024-12-01",
        "endDate": None,
        "officialSiteURL": None,
        "photoURL": None
    }
]

data['officeholders'].extend(new_governors)
changes.append(f"Added {len(new_governors)} new governors")

# Write back to the file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Changes made:")
for change in changes:
    print(f"  - {change}")

print(f"\n✅ Successfully updated Mexican governors")
print(f"Total officeholders: {len(data['officeholders'])}")
