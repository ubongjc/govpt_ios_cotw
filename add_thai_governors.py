#!/usr/bin/env python3
"""
Script to add Thai provincial governors to seed_data.json
Adds all 77 governors (Bangkok + 76 provinces)
"""

import json
import sys

# Thai provincial governors data (2024/2025)
THAI_GOVERNORS = [
    # Bangkok - Special Administrative Region (Elected)
    {
        "province": "Bangkok",
        "governor": "Chadchart Sittipunt",
        "code": "bkk",
        "party": "Independent",
        "is_elected": True
    },
    # Pattaya - Special Administrative Region
    {
        "province": "Pattaya",
        "governor": "Poramet Ngampichet",
        "code": "pty",
        "party": "Rao Rak Pattaya Group",
        "is_elected": True
    },
    # 75 Provinces (Appointed)
    {"province": "Amnat Charoen", "governor": "Thaweep Butpho", "code": "ac"},
    {"province": "Ang Thong", "governor": "Verasak Vichitsangsri", "code": "at"},
    {"province": "Bueng Kan", "governor": "Sanit Khaosa-ard", "code": "bk"},
    {"province": "Buriram", "governor": "Thatchakorn Hatthathayakul", "code": "br"},
    {"province": "Chachoengsao", "governor": "Maitree Traitilanan", "code": "cc"},
    {"province": "Chai Nat", "governor": "Rangsan Tancharoen", "code": "cn"},
    {"province": "Chaiyaphum", "governor": "Kraisorn Kongchalard", "code": "cp"},
    {"province": "Chanthaburi", "governor": "Suthee Thongyam", "code": "ct"},
    {"province": "Chiang Mai", "governor": "Nirat Pongsitthaworn", "code": "cm"},
    {"province": "Chiang Rai", "governor": "Puttipong Sirimart", "code": "cr"},
    {"province": "Chonburi", "governor": "Thawatchai Srithong", "code": "cb"},
    {"province": "Chumphon", "governor": "Teera Anantaseriwittaya", "code": "ch"},
    {"province": "Kalasin", "governor": "Songpol Jai-krim", "code": "ks"},
    {"province": "Kamphaeng Phet", "governor": "Chawalit Saeng-uthai", "code": "kp"},
    {"province": "Kanchanaburi", "governor": "Jirakiat Phumsawat", "code": "kb"},
    {"province": "Khon Kaen", "governor": "Somsak Jangtrakul", "code": "kk"},
    {"province": "Krabi", "governor": "Phutthiphong Sirimat", "code": "kr"},
    {"province": "Lampang", "governor": "Sithichai Jindaluang", "code": "lp"},
    {"province": "Lamphun", "governor": "Worayut Naowarat", "code": "lh"},
    {"province": "Loei", "governor": "Chaitawat Niemsiri", "code": "le"},
    {"province": "Lopburi", "governor": "Niwat Rungsakorn", "code": "lb"},
    {"province": "Mae Hong Son", "governor": "Akkawit Meepian", "code": "ms"},
    {"province": "Maha Sarakham", "governor": "Kiattisak Trongsiri", "code": "mk"},
    {"province": "Mukdahan", "governor": "Chaloemphon Mangkhang", "code": "md"},
    {"province": "Nakhon Nayok", "governor": "Amphon Angkapakornkun", "code": "ny"},
    {"province": "Nakhon Pathom", "governor": "Surasak Charoensirichot", "code": "np"},
    {"province": "Nakhon Phanom", "governor": "Chathip Ruchanaseri", "code": "nh"},
    {"province": "Nakhon Ratchasima", "governor": "Wichian Chantaranothai", "code": "nr"},
    {"province": "Nakhon Sawan", "governor": "Chayan Sirimas", "code": "ns"},
    {"province": "Nakhon Si Thammarat", "governor": "Kraisorn Wisitwong", "code": "nt"},
    {"province": "Nan", "governor": "Akkawit Meepian", "code": "nn"},
    {"province": "Narathiwat", "governor": "Sanan Pongaksorn", "code": "nw"},
    {"province": "Nong Bua Lamphu", "governor": "Siwaporn Chuasawas", "code": "nb"},
    {"province": "Nong Khai", "governor": "Monsit Phaisanthanawat", "code": "nk"},
    {"province": "Nonthaburi", "governor": "Suchin Chaichumsak", "code": "no"},
    {"province": "Pathum Thani", "governor": "Somkid Chanthomruk", "code": "pt"},
    {"province": "Pattani", "governor": "Pateemoh Sadeeyamu", "code": "pn"},
    {"province": "Phang Nga", "governor": "Chamroen Thipphayaphongthada", "code": "pg"},
    {"province": "Phatthalung", "governor": "Ratthasat Chitchu", "code": "pl"},
    {"province": "Phayao", "governor": "Chokdee Amornwat", "code": "py"},
    {"province": "Phetchabun", "governor": "Krit Kongmuang", "code": "pb"},
    {"province": "Phetchaburi", "governor": "Pakapong Tawipat", "code": "pc"},
    {"province": "Phichit", "governor": "Paiboon Nabutchom", "code": "pi"},
    {"province": "Phitsanulok", "governor": "Ronnachai Chitwiset", "code": "ps"},
    {"province": "Phra Nakhon Si Ayutthaya", "governor": "Weerachai Nakmas", "code": "ay"},
    {"province": "Phrae", "governor": "Somwang Phuangbangpho", "code": "ph"},
    {"province": "Phuket", "governor": "Narong Woonsiew", "code": "pk"},
    {"province": "Prachinburi", "governor": "Woraphan Suwannus", "code": "pr"},
    {"province": "Prachuap Khiri Khan", "governor": "Vacant", "code": "pk2"},
    {"province": "Ranong", "governor": "Somkiat Sisanet", "code": "rn"},
    {"province": "Ratchaburi", "governor": "Ronnapop Luangpairote", "code": "rb"},
    {"province": "Rayong", "governor": "Channa Iamsaeng", "code": "ry"},
    {"province": "Roi Et", "governor": "Phusit Somchit", "code": "re"},
    {"province": "Sa Kaeo", "governor": "Parinya Phothisat", "code": "sk"},
    {"province": "Sakon Nakhon", "governor": "Chureerat Thep-at", "code": "sn"},
    {"province": "Samut Prakan", "governor": "Wanchai Kongkasem", "code": "sp"},
    {"province": "Samut Sakhon", "governor": "Narong Rakroi", "code": "ss"},
    {"province": "Samut Songkhram", "governor": "Charas Bunnasa", "code": "sg"},
    {"province": "Saraburi", "governor": "Manrat Rattanasukhon", "code": "sb"},
    {"province": "Satun", "governor": "Sakra Kapilkan", "code": "st"},
    {"province": "Sing Buri", "governor": "Chaichan Sittiwirattham", "code": "si"},
    {"province": "Sisaket", "governor": "Watthana Phutthichat", "code": "se"},
    {"province": "Songkhla", "governor": "Chotnarin Kerdsom", "code": "so"},
    {"province": "Sukhothai", "governor": "Wirun Phandevi", "code": "su"},
    {"province": "Suphan Buri", "governor": "Natthapat Suwanprateep", "code": "sb2"},
    {"province": "Surat Thani", "governor": "Jessada Jitrat", "code": "sr"},
    {"province": "Surin", "governor": "Suvapong Kitiphatpiboon", "code": "sn2"},
    {"province": "Tak", "governor": "Chucheep Pongchai", "code": "tk"},
    {"province": "Trang", "governor": "Khajornsak Charoensopha", "code": "tr"},
    {"province": "Trat", "governor": "Chamnanwit Terat", "code": "tt"},
    {"province": "Ubon Ratchathani", "governor": "Pongrat Phiromrat", "code": "ub"},
    {"province": "Udon Thani", "governor": "Siam Sirimongkol", "code": "ud"},
    {"province": "Uthai Thani", "governor": "Khajonkiat Rakpanichmanee", "code": "ut"},
    {"province": "Uttaradit", "governor": "Phol Damtham", "code": "un"},
    {"province": "Yala", "governor": "Supot Rodruang Na Nongkhai", "code": "yl"},
    {"province": "Yasothon", "governor": "Chonlatee Yangtrong", "code": "ys"},
]

def create_person_id(governor_name, province_code):
    """Create personId from governor's last name and province code"""
    # Extract last name (last word in name)
    parts = governor_name.strip().split()
    if governor_name == "Vacant":
        lastname = "vacant"
    else:
        lastname = parts[-1].lower()

    return f"person:th:{province_code}:gov:{lastname}"

def create_region_id(province_code):
    """Create regionId for province"""
    return f"province:th:{province_code}"

def create_officeholder_entry(governor_data):
    """Create an officeholder entry for a Thai governor"""
    province = governor_data["province"]
    governor = governor_data["governor"]
    code = governor_data["code"]
    is_elected = governor_data.get("is_elected", False)
    party = governor_data.get("party", "Appointed by Ministry of Interior")

    # Skip vacant positions
    if governor == "Vacant":
        return None

    entry = {
        "personId": create_person_id(governor, code),
        "name": governor,
        "title": "Governor",
        "regionId": create_region_id(code),
        "partyName": party,
        "partyURL": None,
        "startDate": None,
        "endDate": None,
        "officialSiteURL": None,
        "photoURL": None
    }

    return entry

def main():
    """Main function to add Thai governors to seed_data.json"""

    # Read the existing seed_data.json
    seed_file = "/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json"

    print(f"Reading {seed_file}...")
    with open(seed_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Verify officeholders key exists
    if 'officeholders' not in data:
        print("ERROR: 'officeholders' key not found in seed_data.json")
        sys.exit(1)

    print(f"Current number of officeholders: {len(data['officeholders'])}")

    # Get existing Thai governor personIds to avoid duplicates
    existing_th_gov_ids = set()
    for oh in data['officeholders']:
        person_id = oh.get('personId', '')
        if ':th:' in person_id and ':gov:' in person_id:
            existing_th_gov_ids.add(person_id)

    print(f"Existing Thai governors: {len(existing_th_gov_ids)}")

    # Create officeholder entries for all governors
    new_entries = []
    skipped = 0

    for gov_data in THAI_GOVERNORS:
        entry = create_officeholder_entry(gov_data)
        if entry is None:
            skipped += 1
            continue

        # Check if already exists
        if entry['personId'] in existing_th_gov_ids:
            print(f"  Skipping duplicate: {entry['name']} ({entry['personId']})")
            skipped += 1
            continue

        new_entries.append(entry)

    # Add new entries to officeholders
    data['officeholders'].extend(new_entries)

    print(f"\nAdding {len(new_entries)} new Thai governors...")
    print(f"Skipped: {skipped} (vacant or duplicates)")

    # Write back to file
    print(f"\nWriting updated data to {seed_file}...")
    with open(seed_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nSUCCESS!")
    print(f"Total officeholders after update: {len(data['officeholders'])}")
    print(f"Thai provincial governors added: {len(new_entries)}")

    # Print sample entries
    print("\nSample entries added:")
    for entry in new_entries[:3]:
        print(f"  - {entry['name']} ({entry['title']}) -> {entry['regionId']}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
