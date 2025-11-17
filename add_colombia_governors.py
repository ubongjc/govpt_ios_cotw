#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Colombian Department Governors (elected October 2023 for 2024-2027 term)
# Note: Magdalena's governor was dismissed, so not included
colombian_governors = [
    {"personId": "person:co:amazonas:governor:sanchez", "name": "Óscar Enrique Sánchez Guerrero", "title": "Governor of Amazonas", "regionId": "dept:co:amazonas", "partyName": "Pacto Histórico", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:antioquia:governor:rendon", "name": "Andrés Julián Rendón Cardona", "title": "Governor of Antioquia", "regionId": "dept:co:antioquia", "partyName": "Centro Democrático", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:arauca:governor:martinez", "name": "Renson Jesús Martínez Prada", "title": "Governor of Arauca", "regionId": "dept:co:arauca", "partyName": "Liberal Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:atlantico:governor:verano", "name": "Eduardo Ignacio Verano De La Rosa", "title": "Governor of Atlántico", "regionId": "dept:co:atlantico", "partyName": "Liberal Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:bolivar:governor:arana", "name": "Yamil Hernando Arana Padauí", "title": "Governor of Bolívar", "regionId": "dept:co:bolivar", "partyName": "Conservative Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:boyaca:governor:amaya", "name": "Carlos Andrés Amaya Rodríguez", "title": "Governor of Boyacá", "regionId": "dept:co:boyaca", "partyName": "Alianza Verde", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:caldas:governor:gutierrez", "name": "Henry Gutiérrez Ángel", "title": "Governor of Caldas", "regionId": "dept:co:caldas", "partyName": "Partido de la Unión", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:caqueta:governor:ruiz", "name": "Luis Francisco Ruiz Aguilar", "title": "Governor of Caquetá", "regionId": "dept:co:caqueta", "partyName": "Independent", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:casanare:governor:ortiz", "name": "César Augusto Ortiz Zorro", "title": "Governor of Casanare", "regionId": "dept:co:casanare", "partyName": "Alianza Verde", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:cauca:governor:guzman", "name": "Jorge Octavio Guzmán Gutiérrez", "title": "Governor of Cauca", "regionId": "dept:co:cauca", "partyName": "Colombia Renaciente", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:cesar:governor:sanjuan", "name": "Elvia Milena Sanjuán Dávila", "title": "Governor of Cesar", "regionId": "dept:co:cesar", "partyName": "Partido de la Unión", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:choco:governor:cordoba", "name": "Nubia Carolina Córdoba Curí", "title": "Governor of Chocó", "regionId": "dept:co:choco", "partyName": "Liberal Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:cordoba:governor:zuleta", "name": "Erasmo Elías Zuleta Bechara", "title": "Governor of Córdoba", "regionId": "dept:co:cordoba", "partyName": "Partido de la Unión", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:cundinamarca:governor:rey", "name": "Jorge Emilio Rey Ángel", "title": "Governor of Cundinamarca", "regionId": "dept:co:cundinamarca", "partyName": "Colombia Renaciente", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:guainia:governor:rivera", "name": "Arnulfo Rivera Naranjo", "title": "Governor of Guainía", "regionId": "dept:co:guainia", "partyName": "Liberal Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:guaviare:governor:rojas", "name": "Yeison Ferney Rojas Martínez", "title": "Governor of Guaviare", "regionId": "dept:co:guaviare", "partyName": "Conservative Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:huila:governor:villalba", "name": "Rodrigo Villalba Mosquera", "title": "Governor of Huila", "regionId": "dept:co:huila", "partyName": "Liberal Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:laguajira:governor:aguilar", "name": "Jairo Alfonso Aguilar Deluque", "title": "Governor of La Guajira", "regionId": "dept:co:laguajira", "partyName": "Partido de la Unión", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:meta:governor:cortes", "name": "Rafaela Cortés Zambrano", "title": "Governor of Meta", "regionId": "dept:co:meta", "partyName": "Centro Democrático", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:narino:governor:escobar", "name": "Luis Alfonso Escobar Jaramillo", "title": "Governor of Nariño", "regionId": "dept:co:narino", "partyName": "Pacto Histórico", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:nortsantander:governor:villamizar", "name": "William Villamizar Laguado", "title": "Governor of Norte de Santander", "regionId": "dept:co:nortsantander", "partyName": "Conservative Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:putumayo:governor:molina", "name": "Jhon Gabriel Molina Acosta", "title": "Governor of Putumayo", "regionId": "dept:co:putumayo", "partyName": "Conservative Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:quindio:governor:galvis", "name": "Juan Miguel Galvis Bedoya", "title": "Governor of Quindío", "regionId": "dept:co:quindio", "partyName": "Creemos Colombia", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:risaralda:governor:patino", "name": "Juan Diego Patiño Ochoa", "title": "Governor of Risaralda", "regionId": "dept:co:risaralda", "partyName": "Liberal Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:sanandres:governor:gallardo", "name": "Nicolás Iván Gallardo Vásquez", "title": "Governor of San Andrés y Providencia", "regionId": "dept:co:sanandres", "partyName": "Liberal Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:santander:governor:diaz", "name": "Juvenal Díaz Mateus", "title": "Governor of Santander", "regionId": "dept:co:santander", "partyName": "Centro Democrático", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:sucre:governor:garcia", "name": "Lucy Inés García Montes", "title": "Governor of Sucre", "regionId": "dept:co:sucre", "partyName": "Liberal Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:tolima:governor:matiz", "name": "Adriana Magali Matiz", "title": "Governor of Tolima", "regionId": "dept:co:tolima", "partyName": "Conservative Party", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:valdelcauca:governor:toro", "name": "Dilian Francisca Toro Torres", "title": "Governor of Valle del Cauca", "regionId": "dept:co:valdelcauca", "partyName": "Partido de la Unión", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:vaupes:governor:gutierrez", "name": "Luis Alfredo Gutiérrez García", "title": "Governor of Vaupés", "regionId": "dept:co:vaupes", "partyName": "Gente en Movimiento", "startDate": "2024-01-01", "endDate": None},
    {"personId": "person:co:vichada:governor:benito", "name": "Hecson Alexis Benito Castro", "title": "Governor of Vichada", "regionId": "dept:co:vichada", "partyName": "Partido de la Unión", "startDate": "2024-01-01", "endDate": None}
]

# Add all governors
data['officeholders'].extend(colombian_governors)

print(f"✅ Added {len(colombian_governors)} Colombian department governors")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
