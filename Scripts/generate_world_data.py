#!/usr/bin/env python3
"""
World Data Generator for Government Promises Tracker

This script generates comprehensive seed data for all countries, states, and cities.
Run this periodically to update with current officeholders and election data.

Usage:
    python3 generate_world_data.py > ../GPT/Resources/seed_data.json
"""

import json
from datetime import datetime

# All 195 UN-recognized countries
COUNTRIES = {
    # Africa (54)
    "AF": [
        {"code": "DZ", "name": "Algeria", "lat": 28.0339, "lon": 1.6596, "capital": "Algiers"},
        {"code": "AO", "name": "Angola", "lat": -11.2027, "lon": 17.8739, "capital": "Luanda"},
        {"code": "BJ", "name": "Benin", "lat": 9.3077, "lon": 2.3158, "capital": "Porto-Novo"},
        {"code": "BW", "name": "Botswana", "lat": -22.3285, "lon": 24.6849, "capital": "Gaborone"},
        {"code": "BF", "name": "Burkina Faso", "lat": 12.2383, "lon": -1.5616, "capital": "Ouagadougou"},
        {"code": "BI", "name": "Burundi", "lat": -3.3731, "lon": 29.9189, "capital": "Gitega"},
        {"code": "CM", "name": "Cameroon", "lat": 7.3697, "lon": 12.3547, "capital": "Yaoundé"},
        {"code": "CV", "name": "Cape Verde", "lat": 16.5388, "lon": -23.0418, "capital": "Praia"},
        {"code": "CF", "name": "Central African Republic", "lat": 6.6111, "lon": 20.9394, "capital": "Bangui"},
        {"code": "TD", "name": "Chad", "lat": 15.4542, "lon": 18.7322, "capital": "N'Djamena"},
        {"code": "KM", "name": "Comoros", "lat": -11.6455, "lon": 43.3333, "capital": "Moroni"},
        {"code": "CG", "name": "Congo", "lat": -4.0383, "lon": 21.7587, "capital": "Brazzaville"},
        {"code": "CD", "name": "DR Congo", "lat": -4.0383, "lon": 21.7587, "capital": "Kinshasa"},
        {"code": "CI", "name": "Côte d'Ivoire", "lat": 7.5400, "lon": -5.5471, "capital": "Yamoussoukro"},
        {"code": "DJ", "name": "Djibouti", "lat": 11.8251, "lon": 42.5903, "capital": "Djibouti"},
        {"code": "EG", "name": "Egypt", "lat": 26.8206, "lon": 30.8025, "capital": "Cairo"},
        {"code": "GQ", "name": "Equatorial Guinea", "lat": 1.6508, "lon": 10.2679, "capital": "Malabo"},
        {"code": "ER", "name": "Eritrea", "lat": 15.1794, "lon": 39.7823, "capital": "Asmara"},
        {"code": "SZ", "name": "Eswatini", "lat": -26.5225, "lon": 31.4659, "capital": "Mbabane"},
        {"code": "ET", "name": "Ethiopia", "lat": 9.1450, "lon": 40.4897, "capital": "Addis Ababa"},
        {"code": "GA", "name": "Gabon", "lat": -0.8037, "lon": 11.6094, "capital": "Libreville"},
        {"code": "GM", "name": "Gambia", "lat": 13.4432, "lon": -15.3101, "capital": "Banjul"},
        {"code": "GH", "name": "Ghana", "lat": 7.9465, "lon": -1.0232, "capital": "Accra"},
        {"code": "GN", "name": "Guinea", "lat": 9.9456, "lon": -9.6966, "capital": "Conakry"},
        {"code": "GW", "name": "Guinea-Bissau", "lat": 11.8037, "lon": -15.1804, "capital": "Bissau"},
        {"code": "KE", "name": "Kenya", "lat": -0.0236, "lon": 37.9062, "capital": "Nairobi"},
        {"code": "LS", "name": "Lesotho", "lat": -29.6100, "lon": 28.2336, "capital": "Maseru"},
        {"code": "LR", "name": "Liberia", "lat": 6.4281, "lon": -9.4295, "capital": "Monrovia"},
        {"code": "LY", "name": "Libya", "lat": 26.3351, "lon": 17.2283, "capital": "Tripoli"},
        {"code": "MG", "name": "Madagascar", "lat": -18.7669, "lon": 46.8691, "capital": "Antananarivo"},
        {"code": "MW", "name": "Malawi", "lat": -13.2543, "lon": 34.3015, "capital": "Lilongwe"},
        {"code": "ML", "name": "Mali", "lat": 17.5707, "lon": -3.9962, "capital": "Bamako"},
        {"code": "MR", "name": "Mauritania", "lat": 21.0079, "lon": -10.9408, "capital": "Nouakchott"},
        {"code": "MU", "name": "Mauritius", "lat": -20.3484, "lon": 57.5522, "capital": "Port Louis"},
        {"code": "MA", "name": "Morocco", "lat": 31.7917, "lon": -7.0926, "capital": "Rabat"},
        {"code": "MZ", "name": "Mozambique", "lat": -18.6657, "lon": 35.5296, "capital": "Maputo"},
        {"code": "NA", "name": "Namibia", "lat": -22.9576, "lon": 18.4904, "capital": "Windhoek"},
        {"code": "NE", "name": "Niger", "lat": 17.6078, "lon": 8.0817, "capital": "Niamey"},
        {"code": "NG", "name": "Nigeria", "lat": 9.0820, "lon": 8.6753, "capital": "Abuja"},
        {"code": "RW", "name": "Rwanda", "lat": -1.9403, "lon": 29.8739, "capital": "Kigali"},
        {"code": "ST", "name": "São Tomé and Príncipe", "lat": 0.1864, "lon": 6.6131, "capital": "São Tomé"},
        {"code": "SN", "name": "Senegal", "lat": 14.4974, "lon": -14.4524, "capital": "Dakar"},
        {"code": "SC", "name": "Seychelles", "lat": -4.6796, "lon": 55.4920, "capital": "Victoria"},
        {"code": "SL", "name": "Sierra Leone", "lat": 8.4657, "lon": -11.7799, "capital": "Freetown"},
        {"code": "SO", "name": "Somalia", "lat": 5.1521, "lon": 46.1996, "capital": "Mogadishu"},
        {"code": "ZA", "name": "South Africa", "lat": -30.5595, "lon": 22.9375, "capital": "Pretoria"},
        {"code": "SS", "name": "South Sudan", "lat": 6.8770, "lon": 31.3070, "capital": "Juba"},
        {"code": "SD", "name": "Sudan", "lat": 12.8628, "lon": 30.2176, "capital": "Khartoum"},
        {"code": "TZ", "name": "Tanzania", "lat": -6.3690, "lon": 34.8888, "capital": "Dodoma"},
        {"code": "TG", "name": "Togo", "lat": 8.6195, "lon": 0.8248, "capital": "Lomé"},
        {"code": "TN", "name": "Tunisia", "lat": 33.8869, "lon": 9.5375, "capital": "Tunis"},
        {"code": "UG", "name": "Uganda", "lat": 1.3733, "lon": 32.2903, "capital": "Kampala"},
        {"code": "ZM", "name": "Zambia", "lat": -13.1339, "lon": 27.8493, "capital": "Lusaka"},
        {"code": "ZW", "name": "Zimbabwe", "lat": -19.0154, "lon": 29.1549, "capital": "Harare"},
    ],
    # Add more continents with all countries...
    # This is a template - full implementation would include all 195 countries
}

# US States (50)
US_STATES = [
    {"code": "AL", "name": "Alabama", "capital": "Montgomery"},
    {"code": "AK", "name": "Alaska", "capital": "Juneau"},
    {"code": "AZ", "name": "Arizona", "capital": "Phoenix"},
    {"code": "AR", "name": "Arkansas", "capital": "Little Rock"},
    {"code": "CA", "name": "California", "capital": "Sacramento"},
    {"code": "CO", "name": "Colorado", "capital": "Denver"},
    {"code": "CT", "name": "Connecticut", "capital": "Hartford"},
    {"code": "DE", "name": "Delaware", "capital": "Dover"},
    {"code": "FL", "name": "Florida", "capital": "Tallahassee"},
    {"code": "GA", "name": "Georgia", "capital": "Atlanta"},
    {"code": "HI", "name": "Hawaii", "capital": "Honolulu"},
    {"code": "ID", "name": "Idaho", "capital": "Boise"},
    {"code": "IL", "name": "Illinois", "capital": "Springfield"},
    {"code": "IN", "name": "Indiana", "capital": "Indianapolis"},
    {"code": "IA", "name": "Iowa", "capital": "Des Moines"},
    {"code": "KS", "name": "Kansas", "capital": "Topeka"},
    {"code": "KY", "name": "Kentucky", "capital": "Frankfort"},
    {"code": "LA", "name": "Louisiana", "capital": "Baton Rouge"},
    {"code": "ME", "name": "Maine", "capital": "Augusta"},
    {"code": "MD", "name": "Maryland", "capital": "Annapolis"},
    {"code": "MA", "name": "Massachusetts", "capital": "Boston"},
    {"code": "MI", "name": "Michigan", "capital": "Lansing"},
    {"code": "MN", "name": "Minnesota", "capital": "Saint Paul"},
    {"code": "MS", "name": "Mississippi", "capital": "Jackson"},
    {"code": "MO", "name": "Missouri", "capital": "Jefferson City"},
    {"code": "MT", "name": "Montana", "capital": "Helena"},
    {"code": "NE", "name": "Nebraska", "capital": "Lincoln"},
    {"code": "NV", "name": "Nevada", "capital": "Carson City"},
    {"code": "NH", "name": "New Hampshire", "capital": "Concord"},
    {"code": "NJ", "name": "New Jersey", "capital": "Trenton"},
    {"code": "NM", "name": "New Mexico", "capital": "Santa Fe"},
    {"code": "NY", "name": "New York", "capital": "Albany"},
    {"code": "NC", "name": "North Carolina", "capital": "Raleigh"},
    {"code": "ND", "name": "North Dakota", "capital": "Bismarck"},
    {"code": "OH", "name": "Ohio", "capital": "Columbus"},
    {"code": "OK", "name": "Oklahoma", "capital": "Oklahoma City"},
    {"code": "OR", "name": "Oregon", "capital": "Salem"},
    {"code": "PA", "name": "Pennsylvania", "capital": "Harrisburg"},
    {"code": "RI", "name": "Rhode Island", "capital": "Providence"},
    {"code": "SC", "name": "South Carolina", "capital": "Columbia"},
    {"code": "SD", "name": "South Dakota", "capital": "Pierre"},
    {"code": "TN", "name": "Tennessee", "capital": "Nashville"},
    {"code": "TX", "name": "Texas", "capital": "Austin"},
    {"code": "UT", "name": "Utah", "capital": "Salt Lake City"},
    {"code": "VT", "name": "Vermont", "capital": "Montpelier"},
    {"code": "VA", "name": "Virginia", "capital": "Richmond"},
    {"code": "WA", "name": "Washington", "capital": "Olympia"},
    {"code": "WV", "name": "West Virginia", "capital": "Charleston"},
    {"code": "WI", "name": "Wisconsin", "capital": "Madison"},
    {"code": "WY", "name": "Wyoming", "capital": "Cheyenne"},
]

# Canadian Provinces/Territories (13)
CANADA_PROVINCES = [
    {"code": "AB", "name": "Alberta", "capital": "Edmonton"},
    {"code": "BC", "name": "British Columbia", "capital": "Victoria"},
    {"code": "MB", "name": "Manitoba", "capital": "Winnipeg"},
    {"code": "NB", "name": "New Brunswick", "capital": "Fredericton"},
    {"code": "NL", "name": "Newfoundland and Labrador", "capital": "St. John's"},
    {"code": "NS", "name": "Nova Scotia", "capital": "Halifax"},
    {"code": "ON", "name": "Ontario", "capital": "Toronto"},
    {"code": "PE", "name": "Prince Edward Island", "capital": "Charlottetown"},
    {"code": "QC", "name": "Quebec", "capital": "Quebec City"},
    {"code": "SK", "name": "Saskatchewan", "capital": "Regina"},
    {"code": "NT", "name": "Northwest Territories", "capital": "Yellowknife"},
    {"code": "NU", "name": "Nunavut", "capital": "Iqaluit"},
    {"code": "YT", "name": "Yukon", "capital": "Whitehorse"},
]

# Major World Cities (100+)
MAJOR_CITIES = [
    # Will include top 100 cities by population/importance
    {"country": "US", "name": "New York City", "state": "NY"},
    {"country": "US", "name": "Los Angeles", "state": "CA"},
    {"country": "US", "name": "Chicago", "state": "IL"},
    # ... more cities
]

# Active Elections (2024-2025)
ACTIVE_ELECTIONS = {
    "usa_2024": {
        "region": "cnt:usa",
        "date": "2024-11-05",
        "type": "presidential",
        "candidates": [
            {"name": "Donald Trump", "party": "Republican"},
            {"name": "Kamala Harris", "party": "Democratic"},
        ]
    },
    # Add more active elections
}

def generate_data():
    """Generate complete world data structure"""
    data = {
        "regions": [],
        "officeholders": [],
        "promises": [],
        "evidence": [],
        "statusSnapshots": [],
        "industries": [],
        "policyTags": [],
        "policyTagIndustries": [],
        "promiseIndustryImpacts": []
    }

    # Generate continents
    continents = [
        {"id": "cont:af", "code": "AF", "name": "Africa", "lat": 0.0, "lon": 20.0},
        {"id": "cont:as", "code": "AS", "name": "Asia", "lat": 30.0, "lon": 100.0},
        {"id": "cont:eu", "code": "EU", "name": "Europe", "lat": 50.0, "lon": 10.0},
        {"id": "cont:na", "code": "NA", "name": "North America", "lat": 45.0, "lon": -100.0},
        {"id": "cont:sa", "code": "SA", "name": "South America", "lat": -15.0, "lon": -60.0},
        {"id": "cont:oc", "code": "OC", "name": "Oceania", "lat": -25.0, "lon": 135.0},
    ]

    for cont in continents:
        data["regions"].append({
            "regionId": cont["id"],
            "type": "continent",
            "isoCode": cont["code"],
            "name": cont["name"],
            "parentRegionId": None,
            "shapeRef": None,
            "latitude": cont["lat"],
            "longitude": cont["lon"],
            "boundingBoxJSON": None
        })

    # TODO: Add all countries, states, cities
    # This template shows the structure

    return data

if __name__ == "__main__":
    data = generate_data()
    print(json.dumps(data, indent=2))
