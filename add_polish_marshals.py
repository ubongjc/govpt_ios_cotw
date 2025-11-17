#!/usr/bin/env python3
"""
Script to add all 16 Polish voivodeship marshals to seed_data.json
Adds marshals to the 'officeholders' array in the JSON file.
"""

import json
import sys
from datetime import datetime

# Path to the seed_data.json file
SEED_DATA_PATH = "/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json"

# All 16 Polish voivodeship marshals with current data (2024/2025)
POLISH_MARSHALS = [
    {
        "personId": "person:pl:ds:marshal:gancarz",
        "name": "Paweł Gancarz",
        "title": "Marshal",
        "regionId": "voiv:pl:ds",
        "partyName": "Civic Coalition",
        "partyURL": None,
        "startDate": "2024-05-15T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.umwd.pl",
        "wikipediaURL": None,
        "description": "Marshal of Lower Silesian Voivodeship"
    },
    {
        "personId": "person:pl:kp:marshal:calbecki",
        "name": "Piotr Całbecki",
        "title": "Marshal",
        "regionId": "voiv:pl:kp",
        "partyName": "Civic Coalition",
        "partyURL": None,
        "startDate": "2010-12-01T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.kujawsko-pomorskie.pl",
        "wikipediaURL": "https://en.wikipedia.org/wiki/Piotr_Ca%C5%82becki",
        "description": "Marshal of Kuyavian-Pomeranian Voivodeship"
    },
    {
        "personId": "person:pl:lu:marshal:stawiarski",
        "name": "Jarosław Stawiarski",
        "title": "Marshal",
        "regionId": "voiv:pl:lu",
        "partyName": "Law and Justice",
        "partyURL": None,
        "startDate": "2018-11-21T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.lubelskie.pl",
        "wikipediaURL": "https://en.wikipedia.org/wiki/Jaros%C5%82aw_Stawiarski",
        "description": "Marshal of Lublin Voivodeship, re-elected in May 2024"
    },
    {
        "personId": "person:pl:lb:marshal:polak",
        "name": "Elżbieta Polak",
        "title": "Marshal",
        "regionId": "voiv:pl:lb",
        "partyName": "Civic Platform",
        "partyURL": None,
        "startDate": "2010-11-24T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.lubuskie.pl",
        "wikipediaURL": None,
        "description": "Marshal of Lubusz Voivodeship"
    },
    {
        "personId": "person:pl:ld:marshal:skrzydlewska",
        "name": "Joanna Skrzydlewska",
        "title": "Marshal",
        "regionId": "voiv:pl:ld",
        "partyName": "Civic Coalition",
        "partyURL": None,
        "startDate": "2024-06-01T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.lodzkie.pl",
        "wikipediaURL": None,
        "description": "Marshal of Łódź Voivodeship, elected in June 2024"
    },
    {
        "personId": "person:pl:ma:marshal:smolka",
        "name": "Łukasz Smółka",
        "title": "Marshal",
        "regionId": "voiv:pl:ma",
        "partyName": "Civic Coalition",
        "partyURL": None,
        "startDate": "2024-07-01T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.malopolska.pl",
        "wikipediaURL": None,
        "description": "Marshal of Lesser Poland Voivodeship, elected in July 2024"
    },
    {
        "personId": "person:pl:mz:marshal:struzik",
        "name": "Adam Struzik",
        "title": "Marshal",
        "regionId": "voiv:pl:mz",
        "partyName": "Polish People's Party",
        "partyURL": None,
        "startDate": "2001-12-05T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.mazovia.pl",
        "wikipediaURL": None,
        "description": "Marshal of Masovian Voivodeship"
    },
    {
        "personId": "person:pl:op:marshal:bula",
        "name": "Andrzej Buła",
        "title": "Marshal",
        "regionId": "voiv:pl:op",
        "partyName": "Civic Coalition",
        "partyURL": None,
        "startDate": "2024-05-15T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.opolskie.pl",
        "wikipediaURL": None,
        "description": "Marshal of Opole Voivodeship"
    },
    {
        "personId": "person:pl:pk:marshal:ortyl",
        "name": "Władysław Ortyl",
        "title": "Marshal",
        "regionId": "voiv:pl:pk",
        "partyName": "Law and Justice",
        "partyURL": None,
        "startDate": "2013-01-01T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.podkarpackie.pl",
        "wikipediaURL": None,
        "description": "Marshal of Subcarpathian Voivodeship"
    },
    {
        "personId": "person:pl:pd:marshal:kosicki",
        "name": "Artur Kosicki",
        "title": "Marshal",
        "regionId": "voiv:pl:pd",
        "partyName": "Law and Justice",
        "partyURL": None,
        "startDate": "2018-12-05T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.podlaskie.pl",
        "wikipediaURL": None,
        "description": "Marshal of Podlaskie Voivodeship"
    },
    {
        "personId": "person:pl:pm:marshal:struk",
        "name": "Mieczysław Struk",
        "title": "Marshal",
        "regionId": "voiv:pl:pm",
        "partyName": "Civic Coalition",
        "partyURL": None,
        "startDate": "2010-11-30T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.pomorskie.eu",
        "wikipediaURL": None,
        "description": "Marshal of Pomeranian Voivodeship"
    },
    {
        "personId": "person:pl:sl:marshal:saluga",
        "name": "Wojciech Saługa",
        "title": "Marshal",
        "regionId": "voiv:pl:sl",
        "partyName": "Civic Coalition",
        "partyURL": None,
        "startDate": "2024-05-20T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.slaskie.pl",
        "wikipediaURL": "https://en.wikipedia.org/wiki/Wojciech_Sa%C5%82uga",
        "description": "Marshal of Silesian Voivodeship, elected in May 2024"
    },
    {
        "personId": "person:pl:sk:marshal:jarubas",
        "name": "Adam Jarubas",
        "title": "Marshal",
        "regionId": "voiv:pl:sk",
        "partyName": "Polish People's Party",
        "partyURL": None,
        "startDate": "2006-12-04T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.swietokrzyskie.pro",
        "wikipediaURL": None,
        "description": "Marshal of Świętokrzyskie Voivodeship"
    },
    {
        "personId": "person:pl:wn:marshal:brzezin",
        "name": "Gustaw Marek Brzezin",
        "title": "Marshal",
        "regionId": "voiv:pl:wn",
        "partyName": "Law and Justice",
        "partyURL": None,
        "startDate": "2019-11-19T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.warmia.mazury.pl",
        "wikipediaURL": None,
        "description": "Marshal of Warmian-Masurian Voivodeship"
    },
    {
        "personId": "person:pl:wp:marshal:wozniak",
        "name": "Marek Woźniak",
        "title": "Marshal",
        "regionId": "voiv:pl:wp",
        "partyName": "Civic Platform",
        "partyURL": None,
        "startDate": "2005-10-25T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.wielkopolska.pl",
        "wikipediaURL": None,
        "description": "Marshal of Greater Poland Voivodeship"
    },
    {
        "personId": "person:pl:zp:marshal:geblewicz",
        "name": "Olgierd Geblewicz",
        "title": "Marshal",
        "regionId": "voiv:pl:zp",
        "partyName": "Civic Coalition",
        "partyURL": None,
        "startDate": "2010-11-29T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.wzp.pl",
        "wikipediaURL": "https://en.wikipedia.org/wiki/Olgierd_Geblewicz",
        "description": "Marshal of West Pomeranian Voivodeship"
    }
]


def add_marshals_to_seed_data():
    """
    Reads seed_data.json, adds Polish voivodeship marshals to officeholders array,
    and writes the updated data back to the file.
    """
    print(f"Reading seed data from: {SEED_DATA_PATH}")

    try:
        # Read the existing seed data
        with open(SEED_DATA_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Verify that 'officeholders' key exists
        if 'officeholders' not in data:
            print("ERROR: 'officeholders' key not found in seed_data.json")
            return False

        # Get existing person IDs to avoid duplicates
        existing_person_ids = {oh['personId'] for oh in data['officeholders']}
        print(f"Found {len(data['officeholders'])} existing officeholders")

        # Add marshals that don't already exist
        added_count = 0
        skipped_count = 0

        for marshal in POLISH_MARSHALS:
            if marshal['personId'] in existing_person_ids:
                print(f"  Skipping {marshal['name']} - already exists")
                skipped_count += 1
            else:
                data['officeholders'].append(marshal)
                print(f"  Added {marshal['name']} - {marshal['description']}")
                added_count += 1

        # Write the updated data back to the file
        if added_count > 0:
            print(f"\nWriting updated data back to {SEED_DATA_PATH}")
            with open(SEED_DATA_PATH, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Successfully updated seed_data.json")

        # Print summary
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        print(f"Total marshals processed: {len(POLISH_MARSHALS)}")
        print(f"Marshals added: {added_count}")
        print(f"Marshals skipped (already exist): {skipped_count}")
        print(f"Total officeholders in file: {len(data['officeholders'])}")
        print("="*60)

        return True

    except FileNotFoundError:
        print(f"ERROR: Could not find file: {SEED_DATA_PATH}")
        return False
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in seed_data.json: {e}")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False


if __name__ == "__main__":
    success = add_marshals_to_seed_data()
    sys.exit(0 if success else 1)
