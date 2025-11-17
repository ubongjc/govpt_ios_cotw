#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Define all 27 current Brazilian governors (2023-2027 term)
# All took office on January 1, 2023
current_governors = {
    'state:br:acre': {'name': 'Gladson Cameli', 'party': 'Progressistas'},
    'state:br:alagoas': {'name': 'Paulo Dantas', 'party': 'Movimento Democrático Brasileiro'},
    'state:br:amapa': {'name': 'Clécio Luís', 'party': 'Solidariedade'},
    'state:br:amazonas': {'name': 'Wilson Lima', 'party': 'União Brasil'},
    'state:br:bahia': {'name': 'Jerônimo Rodrigues', 'party': 'Partido dos Trabalhadores'},
    'state:br:ceara': {'name': 'Elmano de Freitas', 'party': 'Partido dos Trabalhadores'},
    'state:br:distritofederal': {'name': 'Ibaneis Rocha', 'party': 'Movimento Democrático Brasileiro'},
    'state:br:espiritosanto': {'name': 'Renato Casagrande', 'party': 'Partido Socialista Brasileiro'},
    'state:br:goias': {'name': 'Ronaldo Caiado', 'party': 'União Brasil'},
    'state:br:maranhao': {'name': 'Carlos Brandão', 'party': 'Partido Socialista Brasileiro'},
    'state:br:matogrosso': {'name': 'Mauro Mendes', 'party': 'União Brasil'},
    'state:br:matogrossodosul': {'name': 'Eduardo Riedel', 'party': 'Progressistas'},
    'state:br:minasgerais': {'name': 'Romeu Zema', 'party': 'NOVO'},
    'state:br:para': {'name': 'Helder Barbalho', 'party': 'Movimento Democrático Brasileiro'},
    'state:br:paraiba': {'name': 'João Azevêdo', 'party': 'Partido Socialista Brasileiro'},
    'state:br:parana': {'name': 'Ratinho Júnior', 'party': 'Partido Social Democrático'},
    'state:br:pernambuco': {'name': 'Raquel Lyra', 'party': 'Partido Social Democrático'},
    'state:br:piaui': {'name': 'Rafael Fonteles', 'party': 'Partido dos Trabalhadores'},
    'state:br:riodejaneiro': {'name': 'Cláudio Castro', 'party': 'Partido Liberal'},
    'state:br:riograndedonorte': {'name': 'Fátima Bezerra', 'party': 'Partido dos Trabalhadores'},
    'state:br:riograndedosul': {'name': 'Eduardo Leite', 'party': 'Partido Social Democrático'},
    'state:br:rondonia': {'name': 'Marcos Rocha', 'party': 'União Brasil'},
    'state:br:roraima': {'name': 'Antonio Denarium', 'party': 'Progressistas'},
    'state:br:saopaulo': {'name': 'Tarcísio de Freitas', 'party': 'Republicanos'},
    'state:br:santacatarina': {'name': 'Jorginho Mello', 'party': 'Partido Liberal'},
    'state:br:sergipe': {'name': 'Fábio Mitidieri', 'party': 'Partido Social Democrático'},
    'state:br:tocantins': {'name': 'Wanderlei Barbosa', 'party': 'Republicanos'}
}

# Update existing governors
updated = 0
for officeholder in data['officeholders']:
    if officeholder['regionId'] in current_governors:
        gov_info = current_governors[officeholder['regionId']]
        officeholder['name'] = gov_info['name']
        officeholder['partyName'] = gov_info['party']
        officeholder['startDate'] = '2023-01-01'
        officeholder['endDate'] = None
        updated += 1

print(f"✅ Updated {updated} Brazilian governors")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
EOF