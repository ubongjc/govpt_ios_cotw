#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Current Nigerian State Governors (as of 2023-2025)
# Based on the 2023 gubernatorial elections
current_governors = {
    'state:ng:ab': {'name': 'Alex Otti', 'party': 'Labour Party', 'startDate': '2023-05-29'},
    'state:ng:ad': {'name': 'Ahmadu Umaru Fintiri', 'party': 'Peoples Democratic Party', 'startDate': '2019-05-29'},
    'state:ng:ak': {'name': 'Umo Eno', 'party': 'Peoples Democratic Party', 'startDate': '2023-05-29'},
    'state:ng:an': {'name': 'Charles Soludo', 'party': 'All Progressives Grand Alliance', 'startDate': '2022-03-17'},
    'state:ng:ba': {'name': 'Bala Muhammed', 'party': 'Peoples Democratic Party', 'startDate': '2019-05-29'},
    'state:ng:by': {'name': 'Douye Diri', 'party': 'Peoples Democratic Party', 'startDate': '2020-02-14'},
    'state:ng:be': {'name': 'Hyacinth Alia', 'party': 'All Progressives Congress', 'startDate': '2023-05-29'},
    'state:ng:bo': {'name': 'Babagana Zulum', 'party': 'All Progressives Congress', 'startDate': '2019-05-29'},
    'state:ng:cr': {'name': 'Bassey Otu', 'party': 'All Progressives Congress', 'startDate': '2023-05-29'},
    'state:ng:de': {'name': 'Sheriff Oborevwori', 'party': 'Peoples Democratic Party', 'startDate': '2023-05-29'},
    'state:ng:eb': {'name': 'Francis Nwifuru', 'party': 'All Progressives Congress', 'startDate': '2023-05-29'},
    'state:ng:ed': {'name': 'Monday Okpebholo', 'party': 'All Progressives Congress', 'startDate': '2024-11-12'},
    'state:ng:ek': {'name': 'Biodun Oyebanji', 'party': 'All Progressives Congress', 'startDate': '2022-10-16'},
    'state:ng:en': {'name': 'Peter Mbah', 'party': 'Peoples Democratic Party', 'startDate': '2023-05-29'},
    'state:ng:fc': {'name': 'Nyesom Wike', 'party': 'All Progressives Congress', 'startDate': '2023-08-21'},
    'state:ng:go': {'name': 'Muhammad Inuwa Yahaya', 'party': 'All Progressives Congress', 'startDate': '2019-05-29'},
    'state:ng:im': {'name': 'Hope Uzodinma', 'party': 'All Progressives Congress', 'startDate': '2020-01-15'},
    'state:ng:ji': {'name': 'Umar Namadi', 'party': 'All Progressives Congress', 'startDate': '2023-05-29'},
    'state:ng:kd': {'name': 'Uba Sani', 'party': 'All Progressives Congress', 'startDate': '2023-05-29'},
    'state:ng:kn': {'name': 'Abba Kabir Yusuf', 'party': 'New Nigeria Peoples Party', 'startDate': '2023-05-29'},
    'state:ng:kt': {'name': 'Dikko Umaru Radda', 'party': 'All Progressives Congress', 'startDate': '2023-05-29'},
    'state:ng:ke': {'name': 'Nasir Idris', 'party': 'All Progressives Congress', 'startDate': '2023-05-29'},
    'state:ng:ko': {'name': 'Ahmed Usman Ododo', 'party': 'All Progressives Congress', 'startDate': '2024-01-27'},
    'state:ng:kw': {'name': 'AbdulRahman AbdulRazaq', 'party': 'All Progressives Congress', 'startDate': '2019-05-29'},
    'state:ng:la': {'name': 'Babajide Sanwo-Olu', 'party': 'All Progressives Congress', 'startDate': '2019-05-29'},
    'state:ng:na': {'name': 'Abdullahi Sule', 'party': 'All Progressives Congress', 'startDate': '2019-05-29'},
    'state:ng:ni': {'name': 'Mohammed Umar Bago', 'party': 'All Progressives Congress', 'startDate': '2023-05-29'},
    'state:ng:og': {'name': 'Dapo Abiodun', 'party': 'All Progressives Congress', 'startDate': '2019-05-29'},
    'state:ng:on': {'name': 'Lucky Aiyedatiwa', 'party': 'All Progressives Congress', 'startDate': '2023-12-27'},
    'state:ng:os': {'name': 'Ademola Adeleke', 'party': 'Peoples Democratic Party', 'startDate': '2022-11-27'},
    'state:ng:oy': {'name': 'Seyi Makinde', 'party': 'Peoples Democratic Party', 'startDate': '2019-05-29'},
    'state:ng:pl': {'name': 'Caleb Mutfwang', 'party': 'Peoples Democratic Party', 'startDate': '2023-05-29'},
    'state:ng:ri': {'name': 'Siminalayi Fubara', 'party': 'Peoples Democratic Party', 'startDate': '2023-05-29'},
    'state:ng:so': {'name': 'Ahmad Aliyu', 'party': 'All Progressives Congress', 'startDate': '2023-05-29'},
    'state:ng:ta': {'name': 'Agbu Kefas', 'party': 'Peoples Democratic Party', 'startDate': '2023-05-29'},
    'state:ng:yo': {'name': 'Mai Mala Buni', 'party': 'All Progressives Congress', 'startDate': '2019-05-29'},
    'state:ng:za': {'name': 'Dauda Lawal', 'party': 'Peoples Democratic Party', 'startDate': '2023-05-29'}
}

# Update existing governors
updated = 0
for officeholder in data['officeholders']:
    if officeholder['regionId'] in current_governors:
        gov_info = current_governors[officeholder['regionId']]
        officeholder['name'] = gov_info['name']
        officeholder['partyName'] = gov_info['party']
        officeholder['startDate'] = gov_info['startDate']
        officeholder['endDate'] = None
        updated += 1

print(f"✅ Updated {updated} Nigerian state governors and FCT minister")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
