#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Peruvian Regional Governors (elected October-December 2022 for 2023-2026 term)
peruvian_governors = [
    {"personId": "person:pe:amazonas:governor:horna", "name": "Gilmer Horna Corrales", "title": "Governor of Amazonas", "regionId": "region:pe:amazonas", "partyName": "Sentimiento Amazonense Regional", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:ancash:governor:noriega", "name": "Koki Noriega Brito", "title": "Governor of Áncash", "regionId": "region:pe:ancash", "partyName": "Independent", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:apurimac:governor:godoy", "name": "Percy Godoy Medina", "title": "Governor of Apurímac", "regionId": "region:pe:apurimac", "partyName": "Frente de la Esperanza", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:arequipa:governor:sanchez", "name": "Rohel Sánchez Sánchez", "title": "Governor of Arequipa", "regionId": "region:pe:arequipa", "partyName": "Yo Arequipa", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:ayacucho:governor:oscorima", "name": "Wilfredo Oscorima Núñez", "title": "Governor of Ayacucho", "regionId": "region:pe:ayacucho", "partyName": "Alianza para el Progreso", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:cajamarca:governor:guevara", "name": "Roger Guevara Rodríguez", "title": "Governor of Cajamarca", "regionId": "region:pe:cajamarca", "partyName": "Somos Perú", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:callao:governor:castillo", "name": "Ciro Ronald Catillo Rojo Salas", "title": "Governor of Callao", "regionId": "region:pe:callao", "partyName": "Alianza para el Progreso", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:cusco:governor:salcedo", "name": "Werner Máximo Salcedo Álvarez", "title": "Governor of Cusco", "regionId": "region:pe:cusco", "partyName": "Somos Perú", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:huancavelica:governor:huayllani", "name": "Leoncio Huayllani Taype", "title": "Governor of Huancavelica", "regionId": "region:pe:huancavelica", "partyName": "Movimiento Regional Ayni", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:huanuco:governor:pulgar", "name": "Antonio Leónidas Pulgar Lucas", "title": "Governor of Huánuco", "regionId": "region:pe:huanuco", "partyName": "Perú Primero", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:ica:governor:hurtado", "name": "Jorge Carlos Hurtado Herrera", "title": "Governor of Ica", "regionId": "region:pe:ica", "partyName": "Renovación Popular", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:junin:governor:cardenas", "name": "Zósimo Cárdenas Muje", "title": "Governor of Junín", "regionId": "region:pe:junin", "partyName": "Batalla Perú", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:lalibertad:governor:acuna", "name": "César Acuña Peralta", "title": "Governor of La Libertad", "regionId": "region:pe:lalibertad", "partyName": "Alianza para el Progreso", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:lambayeque:governor:perez", "name": "Jorge Luis Pérez Flores", "title": "Governor of Lambayeque", "regionId": "region:pe:lambayeque", "partyName": "Somos Perú", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:lima:governor:vasquez", "name": "Rosa Gloria Vásquez Cuadrado", "title": "Governor of Lima", "regionId": "region:pe:lima", "partyName": "Alianza para el Progreso", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:loreto:governor:chavez", "name": "Jorge René Chávez Silvano", "title": "Governor of Loreto", "regionId": "region:pe:loreto", "partyName": "Somos Perú", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:madrededios:governor:otsuka", "name": "Luis Otsuka Salazar", "title": "Governor of Madre de Dios", "regionId": "region:pe:madrededios", "partyName": "Somos Perú", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:moquegua:governor:gutierrez", "name": "Gilia Ninfa Gutierrez Ayala", "title": "Governor of Moquegua", "regionId": "region:pe:moquegua", "partyName": "Perú Primero", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:pasco:governor:chombo", "name": "Juan Luis Chombo Heredia", "title": "Governor of Pasco", "regionId": "region:pe:pasco", "partyName": "Somos Perú", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:piura:governor:neyra", "name": "Luis Neyra León", "title": "Governor of Piura", "regionId": "region:pe:piura", "partyName": "Contigo Región", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:puno:governor:hancco", "name": "Richard Hancco Soncco", "title": "Governor of Puno", "regionId": "region:pe:puno", "partyName": "Somos Perú", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:sanmartin:governor:grundel", "name": "Walter Grundel Jiménez", "title": "Governor of San Martín", "regionId": "region:pe:sanmartin", "partyName": "Renovación Popular", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:tacna:governor:torres", "name": "Luis Ramón Torres Robledo", "title": "Governor of Tacna", "regionId": "region:pe:tacna", "partyName": "Independent", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:tumbes:governor:cruces", "name": "Segismundo Cruces Ordinola", "title": "Governor of Tumbes", "regionId": "region:pe:tumbes", "partyName": "Alianza para el Progreso", "startDate": "2023-01-01", "endDate": None},
    {"personId": "person:pe:ucayali:governor:gambini", "name": "Manuel Gambini Rupay", "title": "Governor of Ucayali", "regionId": "region:pe:ucayali", "partyName": "Movimiento Independiente Regional Cambio Ucayalino", "startDate": "2023-01-01", "endDate": None}
]

# Add all governors
data['officeholders'].extend(peruvian_governors)

print(f"✅ Added {len(peruvian_governors)} Peruvian regional governors")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
