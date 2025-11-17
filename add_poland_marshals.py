#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Polish Voivodeship Marshals (as of 2024-2025)
# Marshals are elected by regional assemblies and typically serve 5-year terms
polish_marshals = [
    {"personId": "person:pl:wp:marshal:wozniak", "name": "Marek Woźniak", "title": "Marshal of Greater Poland Voivodeship", "regionId": "voiv:pl:wp", "partyName": "Civic Coalition", "startDate": "2018-11-21", "endDate": None},
    {"personId": "person:pl:kp:marshal:calbecki", "name": "Piotr Całbecki", "title": "Marshal of Kuyavian-Pomeranian Voivodeship", "regionId": "voiv:pl:kp", "partyName": "Civic Coalition", "startDate": "2010-12-03", "endDate": None},
    {"personId": "person:pl:ma:marshal:smolka", "name": "Łukasz Smółka", "title": "Marshal of Lesser Poland Voivodeship", "regionId": "voiv:pl:ma", "partyName": "Law and Justice", "startDate": "2023-11-23", "endDate": None},
    {"personId": "person:pl:ld:marshal:schreiber", "name": "Grzegorz Schreiber", "title": "Marshal of Łódź Voivodeship", "regionId": "voiv:pl:ld", "partyName": "Civic Coalition", "startDate": "2018-11-21", "endDate": None},
    {"personId": "person:pl:ds:marshal:gancarz", "name": "Paweł Gancarz", "title": "Marshal of Lower Silesian Voivodeship", "regionId": "voiv:pl:ds", "partyName": "Civic Coalition", "startDate": "2018-11-22", "endDate": None},
    {"personId": "person:pl:lu:marshal:stawiarski", "name": "Jarosław Stawiarski", "title": "Marshal of Lublin Voivodeship", "regionId": "voiv:pl:lu", "partyName": "Law and Justice", "startDate": "2018-12-17", "endDate": None},
    {"personId": "person:pl:lb:marshal:polak", "name": "Elżbieta Polak", "title": "Marshal of Lubusz Voivodeship", "regionId": "voiv:pl:lb", "partyName": "Civic Coalition", "startDate": "2018-11-21", "endDate": None},
    {"personId": "person:pl:mz:marshal:struzik", "name": "Adam Struzik", "title": "Marshal of Masovian Voivodeship", "regionId": "voiv:pl:mz", "partyName": "Polish People's Party", "startDate": "2006-11-16", "endDate": None},
    {"personId": "person:pl:op:marshal:bula", "name": "Andrzej Buła", "title": "Marshal of Opole Voivodeship", "regionId": "voiv:pl:op", "partyName": "Civic Coalition", "startDate": "2018-11-22", "endDate": None},
    {"personId": "person:pl:pd:marshal:kosicki", "name": "Artur Kosicki", "title": "Marshal of Podlaskie Voivodeship", "regionId": "voiv:pl:pd", "partyName": "Civic Coalition", "startDate": "2018-11-26", "endDate": None},
    {"personId": "person:pl:pm:marshal:struk", "name": "Mieczysław Struk", "title": "Marshal of Pomeranian Voivodeship", "regionId": "voiv:pl:pm", "partyName": "Civic Coalition", "startDate": "2010-11-29", "endDate": None},
    {"personId": "person:pl:sl:marshal:saluga", "name": "Wojciech Saługa", "title": "Marshal of Silesian Voivodeship", "regionId": "voiv:pl:sl", "partyName": "Civic Coalition", "startDate": "2018-11-19", "endDate": None},
    {"personId": "person:pl:pk:marshal:ortyl", "name": "Władysław Ortyl", "title": "Marshal of Subcarpathian Voivodeship", "regionId": "voiv:pl:pk", "partyName": "Law and Justice", "startDate": "2015-12-07", "endDate": None},
    {"personId": "person:pl:sk:marshal:jarubas", "name": "Adam Jarubas", "title": "Marshal of Świętokrzyskie Voivodeship", "regionId": "voiv:pl:sk", "partyName": "Polish People's Party", "startDate": "2018-11-26", "endDate": None},
    {"personId": "person:pl:wn:marshal:brzezin", "name": "Gustaw Marek Brzezin", "title": "Marshal of Warmian-Masurian Voivodeship", "regionId": "voiv:pl:wn", "partyName": "Law and Justice", "startDate": "2018-11-22", "endDate": None},
    {"personId": "person:pl:zp:marshal:geblewicz", "name": "Olgierd Geblewicz", "title": "Marshal of West Pomeranian Voivodeship", "regionId": "voiv:pl:zp", "partyName": "Civic Coalition", "startDate": "2014-12-01", "endDate": None}
]

# Add all marshals
data['officeholders'].extend(polish_marshals)

print(f"✅ Added {len(polish_marshals)} Polish voivodeship marshals")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
