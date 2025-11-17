#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Current Italian Regional Presidents (as of November 2024-2025)
current_presidents = {
    'region:it:abr': {'name': 'Marco Marsilio', 'party': 'Brothers of Italy', 'startDate': '2019-02-11'},
    'region:it:vda': {'name': 'Renzo Testolin', 'party': 'Union Valdôtaine', 'startDate': '2023-03-02'},
    'region:it:pug': {'name': 'Michele Emiliano', 'party': 'Democratic Party', 'startDate': '2015-06-01'},
    'region:it:bas': {'name': 'Vito Bardi', 'party': 'Forza Italia', 'startDate': '2019-03-25'},
    'region:it:cal': {'name': 'Roberto Occhiuto', 'party': 'Forza Italia', 'startDate': '2021-10-29'},
    'region:it:cam': {'name': 'Vincenzo De Luca', 'party': 'Democratic Party', 'startDate': '2015-06-01'},
    'region:it:emr': {'name': 'Michele De Pascale', 'party': 'Democratic Party', 'startDate': '2024-12-13'},
    'region:it:fvg': {'name': 'Massimiliano Fedriga', 'party': 'Lega Nord', 'startDate': '2018-04-30'},
    'region:it:laz': {'name': 'Francesco Rocca', 'party': 'Brothers of Italy', 'startDate': '2023-03-02'},
    'region:it:lig': {'name': 'Marco Bucci', 'party': 'Independent', 'startDate': '2024-11-06'},
    'region:it:lom': {'name': 'Attilio Fontana', 'party': 'Lega Nord', 'startDate': '2018-03-26'},
    'region:it:mar': {'name': 'Francesco Acquaroli', 'party': 'Brothers of Italy', 'startDate': '2020-09-30'},
    'region:it:mol': {'name': 'Francesco Roberti', 'party': 'Forza Italia', 'startDate': '2023-07-06'},
    'region:it:pmn': {'name': 'Alberto Cirio', 'party': 'Forza Italia', 'startDate': '2019-06-06'},
    'region:it:sar': {'name': 'Alessandra Todde', 'party': 'Five Star Movement', 'startDate': '2024-03-20'},
    'region:it:sic': {'name': 'Renato Schifani', 'party': 'Forza Italia', 'startDate': '2022-10-13'},
    'region:it:taa': {'name': 'Arno Kompatscher', 'party': 'South Tyrolean People\'s Party', 'startDate': '2024-03-13'},
    'region:it:tos': {'name': 'Eugenio Giani', 'party': 'Democratic Party', 'startDate': '2020-10-08'},
    'region:it:umb': {'name': 'Stefania Proietti', 'party': 'Independent', 'startDate': '2024-12-02'},
    'region:it:ven': {'name': 'Luca Zaia', 'party': 'Lega Nord', 'startDate': '2010-03-30'}
}

# Update existing presidents
updated = 0
for officeholder in data['officeholders']:
    if officeholder['regionId'] in current_presidents:
        pres_info = current_presidents[officeholder['regionId']]
        officeholder['name'] = pres_info['name']
        officeholder['partyName'] = pres_info['party']
        officeholder['startDate'] = pres_info['startDate']
        officeholder['endDate'] = None
        updated += 1

print(f"✅ Updated {updated} Italian regional presidents")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
