#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Current Argentine Governors (as of 2023-2025)
current_governors = {
    'province:ar:buenosaires': {'name': 'Axel Kicillof', 'party': 'Partido Justicialista', 'startDate': '2019-12-10'},
    'city:ar:buenosaires': {'name': 'Jorge Macri', 'party': 'Propuesta Republicana', 'startDate': '2023-12-07'},
    'province:ar:catamarca': {'name': 'Raúl Jalil', 'party': 'Partido Justicialista', 'startDate': '2019-12-10'},
    'province:ar:chaco': {'name': 'Leandro Zdero', 'party': 'Unión Cívica Radical', 'startDate': '2023-12-10'},
    'province:ar:chubut': {'name': 'Ignacio Torres', 'party': 'Propuesta Republicana', 'startDate': '2023-12-10'},
    'province:ar:cordoba': {'name': 'Martín Llaryora', 'party': 'Partido Justicialista', 'startDate': '2023-12-10'},
    'province:ar:corrientes': {'name': 'Gustavo Valdés', 'party': 'Unión Cívica Radical', 'startDate': '2017-12-10'},
    'province:ar:entrerios': {'name': 'Rogelio Frigerio', 'party': 'Propuesta Republicana', 'startDate': '2023-12-10'},
    'province:ar:formosa': {'name': 'Gildo Insfrán', 'party': 'Partido Justicialista', 'startDate': '1995-12-10'},
    'province:ar:jujuy': {'name': 'Carlos Sadir', 'party': 'Unión Cívica Radical', 'startDate': '2023-12-10'},
    'province:ar:lapampa': {'name': 'Sergio Ziliotto', 'party': 'Partido Justicialista', 'startDate': '2019-12-10'},
    'province:ar:larioja': {'name': 'Ricardo Quintela', 'party': 'Partido Justicialista', 'startDate': '2019-12-10'},
    'province:ar:mendoza': {'name': 'Alfredo Cornejo', 'party': 'Unión Cívica Radical', 'startDate': '2023-12-10'},
    'province:ar:misiones': {'name': 'Hugo Passalacqua', 'party': 'Frente Renovador de la Concordia', 'startDate': '2023-12-10'},
    'province:ar:neuquen': {'name': 'Rolando Figueroa', 'party': 'Comunidad', 'startDate': '2023-12-10'},
    'province:ar:rionegro': {'name': 'Alberto Weretilneck', 'party': 'Juntos Somos Río Negro', 'startDate': '2023-12-10'},
    'province:ar:salta': {'name': 'Gustavo Sáenz', 'party': 'Partido Identidad Salteña', 'startDate': '2019-12-10'},
    'province:ar:sanjuan': {'name': 'Marcelo Orrego', 'party': 'Producción y Trabajo', 'startDate': '2023-12-10'},
    'province:ar:sanluis': {'name': 'Claudio Poggi', 'party': 'Avanzar San Luis', 'startDate': '2023-12-10'},
    'province:ar:santacruz': {'name': 'Claudio Vidal', 'party': 'SER Santa Cruz', 'startDate': '2023-12-10'},
    'province:ar:santafe': {'name': 'Maximiliano Pullaro', 'party': 'Unión Cívica Radical', 'startDate': '2023-12-10'},
    'province:ar:santiagodelestero': {'name': 'Gerardo Zamora', 'party': 'Frente Cívico por Santiago', 'startDate': '2017-12-10'},
    'province:ar:tierradelfuego': {'name': 'Gustavo Melella', 'party': 'FORJA', 'startDate': '2019-12-17'},
    'province:ar:tucuman': {'name': 'Osvaldo Jaldo', 'party': 'Partido Justicialista', 'startDate': '2023-10-29'}
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

print(f"✅ Updated {updated} Argentine governors and chief of government")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
