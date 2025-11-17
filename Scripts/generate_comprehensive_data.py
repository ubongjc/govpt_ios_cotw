#!/usr/bin/env python3
"""
Complete Comprehensive Data Generator
Generates seed_data.json with:
- All 195 countries with current leaders
- All 50 US states with governors
- All 13 Canadian provinces with premiers
- Trump 2024 campaign promises (20+)
- Trudeau promises (15+)
- Evidence for kept promises
- Industries and policy tags for market impact
"""

import json
from datetime import datetime

def load_world_leaders():
    """Load all 195 world leaders"""
    with open('Scripts/world_leaders_2025.json', 'r') as f:
        return json.load(f)['leaders']

def get_country_data():
    """Get country names and coordinates"""
    return {
        "AF": {"name": "Afghanistan", "lat": 33.9391, "lon": 67.7100, "continent": "cont:as"},
        "AL": {"name": "Albania", "lat": 41.1533, "lon": 20.1683, "continent": "cont:eu"},
        "DZ": {"name": "Algeria", "lat": 28.0339, "lon": 1.6596, "continent": "cont:af"},
        "AD": {"name": "Andorra", "lat": 42.5063, "lon": 1.5218, "continent": "cont:eu"},
        "AO": {"name": "Angola", "lat": -11.2027, "lon": 17.8739, "continent": "cont:af"},
        "AG": {"name": "Antigua and Barbuda", "lat": 17.0608, "lon": -61.7964, "continent": "cont:na"},
        "AR": {"name": "Argentina", "lat": -38.4161, "lon": -63.6167, "continent": "cont:sa"},
        "AM": {"name": "Armenia", "lat": 40.0691, "lon": 45.0382, "continent": "cont:as"},
        "AU": {"name": "Australia", "lat": -25.2744, "lon": 133.7751, "continent": "cont:oc"},
        "AT": {"name": "Austria", "lat": 47.5162, "lon": 14.5501, "continent": "cont:eu"},
        "AZ": {"name": "Azerbaijan", "lat": 40.1431, "lon": 47.5769, "continent": "cont:as"},
        "BS": {"name": "Bahamas", "lat": 25.0343, "lon": -77.3963, "continent": "cont:na"},
        "BH": {"name": "Bahrain", "lat": 26.0667, "lon": 50.5577, "continent": "cont:as"},
        "BD": {"name": "Bangladesh", "lat": 23.6850, "lon": 90.3563, "continent": "cont:as"},
        "BB": {"name": "Barbados", "lat": 13.1939, "lon": -59.5432, "continent": "cont:na"},
        "BY": {"name": "Belarus", "lat": 53.7098, "lon": 27.9534, "continent": "cont:eu"},
        "BE": {"name": "Belgium", "lat": 50.5039, "lon": 4.4699, "continent": "cont:eu"},
        "BZ": {"name": "Belize", "lat": 17.1899, "lon": -88.4976, "continent": "cont:na"},
        "BJ": {"name": "Benin", "lat": 9.3077, "lon": 2.3158, "continent": "cont:af"},
        "BT": {"name": "Bhutan", "lat": 27.5142, "lon": 90.4336, "continent": "cont:as"},
        "BO": {"name": "Bolivia", "lat": -16.2902, "lon": -63.5887, "continent": "cont:sa"},
        "BA": {"name": "Bosnia and Herzegovina", "lat": 43.9159, "lon": 17.6791, "continent": "cont:eu"},
        "BW": {"name": "Botswana", "lat": -22.3285, "lon": 24.6849, "continent": "cont:af"},
        "BR": {"name": "Brazil", "lat": -14.2350, "lon": -51.9253, "continent": "cont:sa"},
        "BN": {"name": "Brunei", "lat": 4.5353, "lon": 114.7277, "continent": "cont:as"},
        "BG": {"name": "Bulgaria", "lat": 42.7339, "lon": 25.4858, "continent": "cont:eu"},
        "BF": {"name": "Burkina Faso", "lat": 12.2383, "lon": -1.5616, "continent": "cont:af"},
        "BI": {"name": "Burundi", "lat": -3.3731, "lon": 29.9189, "continent": "cont:af"},
        "CV": {"name": "Cabo Verde", "lat": 16.5388, "lon": -23.0418, "continent": "cont:af"},
        "KH": {"name": "Cambodia", "lat": 12.5657, "lon": 104.9910, "continent": "cont:as"},
        "CM": {"name": "Cameroon", "lat": 7.3697, "lon": 12.3547, "continent": "cont:af"},
        "CA": {"name": "Canada", "lat": 56.1304, "lon": -106.3468, "continent": "cont:na"},
        "CF": {"name": "Central African Republic", "lat": 6.6111, "lon": 20.9394, "continent": "cont:af"},
        "TD": {"name": "Chad", "lat": 15.4542, "lon": 18.7322, "continent": "cont:af"},
        "CL": {"name": "Chile", "lat": -35.6751, "lon": -71.5430, "continent": "cont:sa"},
        "CN": {"name": "China", "lat": 35.8617, "lon": 104.1954, "continent": "cont:as"},
        "CO": {"name": "Colombia", "lat": 4.5709, "lon": -74.2973, "continent": "cont:sa"},
        "KM": {"name": "Comoros", "lat": -11.8750, "lon": 43.8722, "continent": "cont:af"},
        "CG": {"name": "Congo", "lat": -0.2280, "lon": 15.8277, "continent": "cont:af"},
        "CD": {"name": "Democratic Republic of the Congo", "lat": -4.0383, "lon": 21.7587, "continent": "cont:af"},
        "CR": {"name": "Costa Rica", "lat": 9.7489, "lon": -83.7534, "continent": "cont:na"},
        "CI": {"name": "Côte d'Ivoire", "lat": 7.5400, "lon": -5.5471, "continent": "cont:af"},
        "HR": {"name": "Croatia", "lat": 45.1000, "lon": 15.2000, "continent": "cont:eu"},
        "CU": {"name": "Cuba", "lat": 21.5218, "lon": -77.7812, "continent": "cont:na"},
        "CY": {"name": "Cyprus", "lat": 35.1264, "lon": 33.4299, "continent": "cont:eu"},
        "CZ": {"name": "Czech Republic", "lat": 49.8175, "lon": 15.4730, "continent": "cont:eu"},
        "DK": {"name": "Denmark", "lat": 56.2639, "lon": 9.5018, "continent": "cont:eu"},
        "DJ": {"name": "Djibouti", "lat": 11.8251, "lon": 42.5903, "continent": "cont:af"},
        "DM": {"name": "Dominica", "lat": 15.4150, "lon": -61.3710, "continent": "cont:na"},
        "DO": {"name": "Dominican Republic", "lat": 18.7357, "lon": -70.1627, "continent": "cont:na"},
        "EC": {"name": "Ecuador", "lat": -1.8312, "lon": -78.1834, "continent": "cont:sa"},
        "EG": {"name": "Egypt", "lat": 26.8206, "lon": 30.8025, "continent": "cont:af"},
        "SV": {"name": "El Salvador", "lat": 13.7942, "lon": -88.8965, "continent": "cont:na"},
        "GQ": {"name": "Equatorial Guinea", "lat": 1.6508, "lon": 10.2679, "continent": "cont:af"},
        "ER": {"name": "Eritrea", "lat": 15.1794, "lon": 39.7823, "continent": "cont:af"},
        "EE": {"name": "Estonia", "lat": 58.5953, "lon": 25.0136, "continent": "cont:eu"},
        "SZ": {"name": "Eswatini", "lat": -26.5225, "lon": 31.4659, "continent": "cont:af"},
        "ET": {"name": "Ethiopia", "lat": 9.1450, "lon": 40.4897, "continent": "cont:af"},
        "FJ": {"name": "Fiji", "lat": -17.7134, "lon": 178.0650, "continent": "cont:oc"},
        "FI": {"name": "Finland", "lat": 61.9241, "lon": 25.7482, "continent": "cont:eu"},
        "FR": {"name": "France", "lat": 46.2276, "lon": 2.2137, "continent": "cont:eu"},
        "GA": {"name": "Gabon", "lat": -0.8037, "lon": 11.6094, "continent": "cont:af"},
        "GM": {"name": "Gambia", "lat": 13.4432, "lon": -15.3101, "continent": "cont:af"},
        "GE": {"name": "Georgia", "lat": 42.3154, "lon": 43.3569, "continent": "cont:as"},
        "DE": {"name": "Germany", "lat": 51.1657, "lon": 10.4515, "continent": "cont:eu"},
        "GH": {"name": "Ghana", "lat": 7.9465, "lon": -1.0232, "continent": "cont:af"},
        "GR": {"name": "Greece", "lat": 39.0742, "lon": 21.8243, "continent": "cont:eu"},
        "GD": {"name": "Grenada", "lat": 12.1165, "lon": -61.6790, "continent": "cont:na"},
        "GT": {"name": "Guatemala", "lat": 15.7835, "lon": -90.2308, "continent": "cont:na"},
        "GN": {"name": "Guinea", "lat": 9.9456, "lon": -9.6966, "continent": "cont:af"},
        "GW": {"name": "Guinea-Bissau", "lat": 11.8037, "lon": -15.1804, "continent": "cont:af"},
        "GY": {"name": "Guyana", "lat": 4.8604, "lon": -58.9302, "continent": "cont:sa"},
        "HT": {"name": "Haiti", "lat": 18.9712, "lon": -72.2852, "continent": "cont:na"},
        "HN": {"name": "Honduras", "lat": 15.2000, "lon": -86.2419, "continent": "cont:na"},
        "HU": {"name": "Hungary", "lat": 47.1625, "lon": 19.5033, "continent": "cont:eu"},
        "IS": {"name": "Iceland", "lat": 64.9631, "lon": -19.0208, "continent": "cont:eu"},
        "IN": {"name": "India", "lat": 20.5937, "lon": 78.9629, "continent": "cont:as"},
        "ID": {"name": "Indonesia", "lat": -0.7893, "lon": 113.9213, "continent": "cont:as"},
        "IR": {"name": "Iran", "lat": 32.4279, "lon": 53.6880, "continent": "cont:as"},
        "IQ": {"name": "Iraq", "lat": 33.2232, "lon": 43.6793, "continent": "cont:as"},
        "IE": {"name": "Ireland", "lat": 53.4129, "lon": -8.2439, "continent": "cont:eu"},
        "IL": {"name": "Israel", "lat": 31.0461, "lon": 34.8516, "continent": "cont:as"},
        "IT": {"name": "Italy", "lat": 41.8719, "lon": 12.5674, "continent": "cont:eu"},
        "JM": {"name": "Jamaica", "lat": 18.1096, "lon": -77.2975, "continent": "cont:na"},
        "JP": {"name": "Japan", "lat": 36.2048, "lon": 138.2529, "continent": "cont:as"},
        "JO": {"name": "Jordan", "lat": 30.5852, "lon": 36.2384, "continent": "cont:as"},
        "KZ": {"name": "Kazakhstan", "lat": 48.0196, "lon": 66.9237, "continent": "cont:as"},
        "KE": {"name": "Kenya", "lat": -0.0236, "lon": 37.9062, "continent": "cont:af"},
        "KI": {"name": "Kiribati", "lat": -3.3704, "lon": -168.7340, "continent": "cont:oc"},
        "KP": {"name": "North Korea", "lat": 40.3399, "lon": 127.5101, "continent": "cont:as"},
        "KR": {"name": "South Korea", "lat": 35.9078, "lon": 127.7669, "continent": "cont:as"},
        "KW": {"name": "Kuwait", "lat": 29.3117, "lon": 47.4818, "continent": "cont:as"},
        "KG": {"name": "Kyrgyzstan", "lat": 41.2044, "lon": 74.7661, "continent": "cont:as"},
        "LA": {"name": "Laos", "lat": 19.8563, "lon": 102.4955, "continent": "cont:as"},
        "LV": {"name": "Latvia", "lat": 56.8796, "lon": 24.6032, "continent": "cont:eu"},
        "LB": {"name": "Lebanon", "lat": 33.8547, "lon": 35.8623, "continent": "cont:as"},
        "LS": {"name": "Lesotho", "lat": -29.6100, "lon": 28.2336, "continent": "cont:af"},
        "LR": {"name": "Liberia", "lat": 6.4281, "lon": -9.4295, "continent": "cont:af"},
        "LY": {"name": "Libya", "lat": 26.3351, "lon": 17.2283, "continent": "cont:af"},
        "LI": {"name": "Liechtenstein", "lat": 47.1660, "lon": 9.5554, "continent": "cont:eu"},
        "LT": {"name": "Lithuania", "lat": 55.1694, "lon": 23.8813, "continent": "cont:eu"},
        "LU": {"name": "Luxembourg", "lat": 49.8153, "lon": 6.1296, "continent": "cont:eu"},
        "MG": {"name": "Madagascar", "lat": -18.7669, "lon": 46.8691, "continent": "cont:af"},
        "MW": {"name": "Malawi", "lat": -13.2543, "lon": 34.3015, "continent": "cont:af"},
        "MY": {"name": "Malaysia", "lat": 4.2105, "lon": 101.9758, "continent": "cont:as"},
        "MV": {"name": "Maldives", "lat": 3.2028, "lon": 73.2207, "continent": "cont:as"},
        "ML": {"name": "Mali", "lat": 17.5707, "lon": -3.9962, "continent": "cont:af"},
        "MT": {"name": "Malta", "lat": 35.9375, "lon": 14.3754, "continent": "cont:eu"},
        "MH": {"name": "Marshall Islands", "lat": 7.1315, "lon": 171.1845, "continent": "cont:oc"},
        "MR": {"name": "Mauritania", "lat": 21.0079, "lon": -10.9408, "continent": "cont:af"},
        "MU": {"name": "Mauritius", "lat": -20.3484, "lon": 57.5522, "continent": "cont:af"},
        "MX": {"name": "Mexico", "lat": 23.6345, "lon": -102.5528, "continent": "cont:na"},
        "FM": {"name": "Micronesia", "lat": 7.4256, "lon": 150.5508, "continent": "cont:oc"},
        "MD": {"name": "Moldova", "lat": 47.4116, "lon": 28.3699, "continent": "cont:eu"},
        "MC": {"name": "Monaco", "lat": 43.7384, "lon": 7.4246, "continent": "cont:eu"},
        "MN": {"name": "Mongolia", "lat": 46.8625, "lon": 103.8467, "continent": "cont:as"},
        "ME": {"name": "Montenegro", "lat": 42.7087, "lon": 19.3744, "continent": "cont:eu"},
        "MA": {"name": "Morocco", "lat": 31.7917, "lon": -7.0926, "continent": "cont:af"},
        "MZ": {"name": "Mozambique", "lat": -18.6657, "lon": 35.5296, "continent": "cont:af"},
        "MM": {"name": "Myanmar", "lat": 21.9162, "lon": 95.9560, "continent": "cont:as"},
        "NA": {"name": "Namibia", "lat": -22.9576, "lon": 18.4904, "continent": "cont:af"},
        "NR": {"name": "Nauru", "lat": -0.5228, "lon": 166.9315, "continent": "cont:oc"},
        "NP": {"name": "Nepal", "lat": 28.3949, "lon": 84.1240, "continent": "cont:as"},
        "NL": {"name": "Netherlands", "lat": 52.1326, "lon": 5.2913, "continent": "cont:eu"},
        "NZ": {"name": "New Zealand", "lat": -40.9006, "lon": 174.8860, "continent": "cont:oc"},
        "NI": {"name": "Nicaragua", "lat": 12.8654, "lon": -85.2072, "continent": "cont:na"},
        "NE": {"name": "Niger", "lat": 17.6078, "lon": 8.0817, "continent": "cont:af"},
        "NG": {"name": "Nigeria", "lat": 9.0820, "lon": 8.6753, "continent": "cont:af"},
        "MK": {"name": "North Macedonia", "lat": 41.6086, "lon": 21.7453, "continent": "cont:eu"},
        "NO": {"name": "Norway", "lat": 60.4720, "lon": 8.4689, "continent": "cont:eu"},
        "OM": {"name": "Oman", "lat": 21.4735, "lon": 55.9754, "continent": "cont:as"},
        "PK": {"name": "Pakistan", "lat": 30.3753, "lon": 69.3451, "continent": "cont:as"},
        "PW": {"name": "Palau", "lat": 7.5150, "lon": 134.5825, "continent": "cont:oc"},
        "PA": {"name": "Panama", "lat": 8.5380, "lon": -80.7821, "continent": "cont:na"},
        "PG": {"name": "Papua New Guinea", "lat": -6.3150, "lon": 143.9555, "continent": "cont:oc"},
        "PY": {"name": "Paraguay", "lat": -23.4425, "lon": -58.4438, "continent": "cont:sa"},
        "PE": {"name": "Peru", "lat": -9.1900, "lon": -75.0152, "continent": "cont:sa"},
        "PH": {"name": "Philippines", "lat": 12.8797, "lon": 121.7740, "continent": "cont:as"},
        "PL": {"name": "Poland", "lat": 51.9194, "lon": 19.1451, "continent": "cont:eu"},
        "PT": {"name": "Portugal", "lat": 39.3999, "lon": -8.2245, "continent": "cont:eu"},
        "QA": {"name": "Qatar", "lat": 25.3548, "lon": 51.1839, "continent": "cont:as"},
        "RO": {"name": "Romania", "lat": 45.9432, "lon": 24.9668, "continent": "cont:eu"},
        "RU": {"name": "Russia", "lat": 61.5240, "lon": 105.3188, "continent": "cont:eu"},
        "RW": {"name": "Rwanda", "lat": -1.9403, "lon": 29.8739, "continent": "cont:af"},
        "KN": {"name": "Saint Kitts and Nevis", "lat": 17.3578, "lon": -62.7830, "continent": "cont:na"},
        "LC": {"name": "Saint Lucia", "lat": 13.9094, "lon": -60.9789, "continent": "cont:na"},
        "VC": {"name": "Saint Vincent and the Grenadines", "lat": 12.9843, "lon": -61.2872, "continent": "cont:na"},
        "WS": {"name": "Samoa", "lat": -13.7590, "lon": -172.1046, "continent": "cont:oc"},
        "SM": {"name": "San Marino", "lat": 43.9424, "lon": 12.4578, "continent": "cont:eu"},
        "ST": {"name": "São Tomé and Príncipe", "lat": 0.1864, "lon": 6.6131, "continent": "cont:af"},
        "SA": {"name": "Saudi Arabia", "lat": 23.8859, "lon": 45.0792, "continent": "cont:as"},
        "SN": {"name": "Senegal", "lat": 14.4974, "lon": -14.4524, "continent": "cont:af"},
        "RS": {"name": "Serbia", "lat": 44.0165, "lon": 21.0059, "continent": "cont:eu"},
        "SC": {"name": "Seychelles", "lat": -4.6796, "lon": 55.4920, "continent": "cont:af"},
        "SL": {"name": "Sierra Leone", "lat": 8.4606, "lon": -11.7799, "continent": "cont:af"},
        "SG": {"name": "Singapore", "lat": 1.3521, "lon": 103.8198, "continent": "cont:as"},
        "SK": {"name": "Slovakia", "lat": 48.6690, "lon": 19.6990, "continent": "cont:eu"},
        "SI": {"name": "Slovenia", "lat": 46.1512, "lon": 14.9955, "continent": "cont:eu"},
        "SB": {"name": "Solomon Islands", "lat": -9.6457, "lon": 160.1562, "continent": "cont:oc"},
        "SO": {"name": "Somalia", "lat": 5.1521, "lon": 46.1996, "continent": "cont:af"},
        "ZA": {"name": "South Africa", "lat": -30.5595, "lon": 22.9375, "continent": "cont:af"},
        "SS": {"name": "South Sudan", "lat": 6.8770, "lon": 31.3070, "continent": "cont:af"},
        "ES": {"name": "Spain", "lat": 40.4637, "lon": -3.7492, "continent": "cont:eu"},
        "LK": {"name": "Sri Lanka", "lat": 7.8731, "lon": 80.7718, "continent": "cont:as"},
        "SD": {"name": "Sudan", "lat": 12.8628, "lon": 30.2176, "continent": "cont:af"},
        "SR": {"name": "Suriname", "lat": 3.9193, "lon": -56.0278, "continent": "cont:sa"},
        "SE": {"name": "Sweden", "lat": 60.1282, "lon": 18.6435, "continent": "cont:eu"},
        "CH": {"name": "Switzerland", "lat": 46.8182, "lon": 8.2275, "continent": "cont:eu"},
        "SY": {"name": "Syria", "lat": 34.8021, "lon": 38.9968, "continent": "cont:as"},
        "TW": {"name": "Taiwan", "lat": 23.6978, "lon": 120.9605, "continent": "cont:as"},
        "TJ": {"name": "Tajikistan", "lat": 38.8610, "lon": 71.2761, "continent": "cont:as"},
        "TZ": {"name": "Tanzania", "lat": -6.3690, "lon": 34.8888, "continent": "cont:af"},
        "TH": {"name": "Thailand", "lat": 15.8700, "lon": 100.9925, "continent": "cont:as"},
        "TL": {"name": "Timor-Leste", "lat": -8.8742, "lon": 125.7275, "continent": "cont:as"},
        "TG": {"name": "Togo", "lat": 8.6195, "lon": 0.8248, "continent": "cont:af"},
        "TO": {"name": "Tonga", "lat": -21.1789, "lon": -175.1982, "continent": "cont:oc"},
        "TT": {"name": "Trinidad and Tobago", "lat": 10.6918, "lon": -61.2225, "continent": "cont:na"},
        "TN": {"name": "Tunisia", "lat": 33.8869, "lon": 9.5375, "continent": "cont:af"},
        "TR": {"name": "Turkey", "lat": 38.9637, "lon": 35.2433, "continent": "cont:as"},
        "TM": {"name": "Turkmenistan", "lat": 38.9697, "lon": 59.5563, "continent": "cont:as"},
        "TV": {"name": "Tuvalu", "lat": -7.1095, "lon": 177.6493, "continent": "cont:oc"},
        "UG": {"name": "Uganda", "lat": 1.3733, "lon": 32.2903, "continent": "cont:af"},
        "UA": {"name": "Ukraine", "lat": 48.3794, "lon": 31.1656, "continent": "cont:eu"},
        "AE": {"name": "United Arab Emirates", "lat": 23.4241, "lon": 53.8478, "continent": "cont:as"},
        "GB": {"name": "United Kingdom", "lat": 55.3781, "lon": -3.4360, "continent": "cont:eu"},
        "US": {"name": "United States", "lat": 37.0902, "lon": -95.7129, "continent": "cont:na"},
        "UY": {"name": "Uruguay", "lat": -32.5228, "lon": -55.7658, "continent": "cont:sa"},
        "UZ": {"name": "Uzbekistan", "lat": 41.3775, "lon": 64.5853, "continent": "cont:as"},
        "VU": {"name": "Vanuatu", "lat": -15.3767, "lon": 166.9592, "continent": "cont:oc"},
        "VA": {"name": "Vatican City", "lat": 41.9029, "lon": 12.4534, "continent": "cont:eu"},
        "VE": {"name": "Venezuela", "lat": 6.4238, "lon": -66.5897, "continent": "cont:sa"},
        "VN": {"name": "Vietnam", "lat": 14.0583, "lon": 108.2772, "continent": "cont:as"},
        "YE": {"name": "Yemen", "lat": 15.5527, "lon": 48.5164, "continent": "cont:as"},
        "ZM": {"name": "Zambia", "lat": -13.1339, "lon": 27.8493, "continent": "cont:af"},
        "ZW": {"name": "Zimbabwe", "lat": -19.0154, "lon": 29.1549, "continent": "cont:af"}
    }

def get_us_states():
    """Get all 50 US states with current governors (2025)"""
    return [
        {"code": "AL", "name": "Alabama", "lat": 32.3182, "lon": -86.9023, "governor": "Kay Ivey", "party": "Republican", "start": "2017-04-10"},
        {"code": "AK", "name": "Alaska", "lat": 64.2008, "lon": -149.4937, "governor": "Mike Dunleavy", "party": "Republican", "start": "2018-12-03"},
        {"code": "AZ", "name": "Arizona", "lat": 34.0489, "lon": -111.0937, "governor": "Katie Hobbs", "party": "Democratic", "start": "2023-01-05"},
        {"code": "AR", "name": "Arkansas", "lat": 35.2010, "lon": -91.8318, "governor": "Sarah Huckabee Sanders", "party": "Republican", "start": "2023-01-10"},
        {"code": "CA", "name": "California", "lat": 36.7783, "lon": -119.4179, "governor": "Gavin Newsom", "party": "Democratic", "start": "2019-01-07"},
        {"code": "CO", "name": "Colorado", "lat": 39.5501, "lon": -105.7821, "governor": "Jared Polis", "party": "Democratic", "start": "2019-01-08"},
        {"code": "CT", "name": "Connecticut", "lat": 41.6032, "lon": -73.0877, "governor": "Ned Lamont", "party": "Democratic", "start": "2019-01-09"},
        {"code": "DE", "name": "Delaware", "lat": 38.9108, "lon": -75.5277, "governor": "John Carney", "party": "Democratic", "start": "2017-01-17"},
        {"code": "FL", "name": "Florida", "lat": 27.6648, "lon": -81.5158, "governor": "Ron DeSantis", "party": "Republican", "start": "2019-01-08"},
        {"code": "GA", "name": "Georgia", "lat": 32.1656, "lon": -82.9001, "governor": "Brian Kemp", "party": "Republican", "start": "2019-01-14"},
        {"code": "HI", "name": "Hawaii", "lat": 19.8968, "lon": -155.5828, "governor": "Josh Green", "party": "Democratic", "start": "2022-12-05"},
        {"code": "ID", "name": "Idaho", "lat": 44.0682, "lon": -114.7420, "governor": "Brad Little", "party": "Republican", "start": "2019-01-07"},
        {"code": "IL", "name": "Illinois", "lat": 40.6331, "lon": -89.3985, "governor": "JB Pritzker", "party": "Democratic", "start": "2019-01-14"},
        {"code": "IN", "name": "Indiana", "lat": 40.2672, "lon": -86.1349, "governor": "Mike Braun", "party": "Republican", "start": "2025-01-13"},
        {"code": "IA", "name": "Iowa", "lat": 41.8780, "lon": -93.0977, "governor": "Kim Reynolds", "party": "Republican", "start": "2017-05-24"},
        {"code": "KS", "name": "Kansas", "lat": 39.0119, "lon": -98.4842, "governor": "Laura Kelly", "party": "Democratic", "start": "2019-01-14"},
        {"code": "KY", "name": "Kentucky", "lat": 37.8393, "lon": -84.2700, "governor": "Andy Beshear", "party": "Democratic", "start": "2019-12-10"},
        {"code": "LA", "name": "Louisiana", "lat": 30.9843, "lon": -91.9623, "governor": "Jeff Landry", "party": "Republican", "start": "2024-01-08"},
        {"code": "ME", "name": "Maine", "lat": 45.2538, "lon": -69.4455, "governor": "Janet Mills", "party": "Democratic", "start": "2019-01-02"},
        {"code": "MD", "name": "Maryland", "lat": 39.0458, "lon": -76.6413, "governor": "Wes Moore", "party": "Democratic", "start": "2023-01-18"},
        {"code": "MA", "name": "Massachusetts", "lat": 42.4072, "lon": -71.3824, "governor": "Maura Healey", "party": "Democratic", "start": "2023-01-05"},
        {"code": "MI", "name": "Michigan", "lat": 44.3148, "lon": -85.6024, "governor": "Gretchen Whitmer", "party": "Democratic", "start": "2019-01-01"},
        {"code": "MN", "name": "Minnesota", "lat": 46.7296, "lon": -94.6859, "governor": "Tim Walz", "party": "Democratic", "start": "2019-01-07"},
        {"code": "MS", "name": "Mississippi", "lat": 32.3547, "lon": -89.3985, "governor": "Tate Reeves", "party": "Republican", "start": "2020-01-14"},
        {"code": "MO", "name": "Missouri", "lat": 37.9643, "lon": -91.8318, "governor": "Mike Kehoe", "party": "Republican", "start": "2025-01-13"},
        {"code": "MT", "name": "Montana", "lat": 46.8797, "lon": -110.3626, "governor": "Greg Gianforte", "party": "Republican", "start": "2021-01-04"},
        {"code": "NE", "name": "Nebraska", "lat": 41.4925, "lon": -99.9018, "governor": "Jim Pillen", "party": "Republican", "start": "2023-01-05"},
        {"code": "NV", "name": "Nevada", "lat": 38.8026, "lon": -116.4194, "governor": "Joe Lombardo", "party": "Republican", "start": "2023-01-03"},
        {"code": "NH", "name": "New Hampshire", "lat": 43.1939, "lon": -71.5724, "governor": "Kelly Ayotte", "party": "Republican", "start": "2025-01-02"},
        {"code": "NJ", "name": "New Jersey", "lat": 40.0583, "lon": -74.4057, "governor": "Phil Murphy", "party": "Democratic", "start": "2018-01-16"},
        {"code": "NM", "name": "New Mexico", "lat": 34.5199, "lon": -105.8701, "governor": "Michelle Lujan Grisham", "party": "Democratic", "start": "2019-01-01"},
        {"code": "NY", "name": "New York", "lat": 43.2994, "lon": -74.2179, "governor": "Kathy Hochul", "party": "Democratic", "start": "2021-08-24"},
        {"code": "NC", "name": "North Carolina", "lat": 35.7596, "lon": -79.0193, "governor": "Josh Stein", "party": "Democratic", "start": "2025-01-01"},
        {"code": "ND", "name": "North Dakota", "lat": 47.5515, "lon": -101.0020, "governor": "Kelly Armstrong", "party": "Republican", "start": "2024-12-15"},
        {"code": "OH", "name": "Ohio", "lat": 40.4173, "lon": -82.9071, "governor": "Mike DeWine", "party": "Republican", "start": "2019-01-14"},
        {"code": "OK", "name": "Oklahoma", "lat": 35.4676, "lon": -97.5164, "governor": "Kevin Stitt", "party": "Republican", "start": "2019-01-14"},
        {"code": "OR", "name": "Oregon", "lat": 43.8041, "lon": -120.5542, "governor": "Tina Kotek", "party": "Democratic", "start": "2023-01-09"},
        {"code": "PA", "name": "Pennsylvania", "lat": 41.2033, "lon": -77.1945, "governor": "Josh Shapiro", "party": "Democratic", "start": "2023-01-17"},
        {"code": "RI", "name": "Rhode Island", "lat": 41.5801, "lon": -71.4774, "governor": "Dan McKee", "party": "Democratic", "start": "2021-03-02"},
        {"code": "SC", "name": "South Carolina", "lat": 33.8361, "lon": -81.1637, "governor": "Henry McMaster", "party": "Republican", "start": "2017-01-24"},
        {"code": "SD", "name": "South Dakota", "lat": 43.9695, "lon": -99.9018, "governor": "Kristi Noem", "party": "Republican", "start": "2019-01-05"},
        {"code": "TN", "name": "Tennessee", "lat": 35.5175, "lon": -86.5804, "governor": "Bill Lee", "party": "Republican", "start": "2019-01-19"},
        {"code": "TX", "name": "Texas", "lat": 31.9686, "lon": -99.9018, "governor": "Greg Abbott", "party": "Republican", "start": "2015-01-20"},
        {"code": "UT", "name": "Utah", "lat": 39.3210, "lon": -111.0937, "governor": "Spencer Cox", "party": "Republican", "start": "2021-01-04"},
        {"code": "VT", "name": "Vermont", "lat": 44.5588, "lon": -72.5778, "governor": "Phil Scott", "party": "Republican", "start": "2017-01-05"},
        {"code": "VA", "name": "Virginia", "lat": 37.4316, "lon": -78.6569, "governor": "Glenn Youngkin", "party": "Republican", "start": "2022-01-15"},
        {"code": "WA", "name": "Washington", "lat": 47.7511, "lon": -120.7401, "governor": "Bob Ferguson", "party": "Democratic", "start": "2025-01-15"},
        {"code": "WV", "name": "West Virginia", "lat": 38.5976, "lon": -80.4549, "governor": "Patrick Morrisey", "party": "Republican", "start": "2025-01-13"},
        {"code": "WI", "name": "Wisconsin", "lat": 43.7844, "lon": -88.7879, "governor": "Tony Evers", "party": "Democratic", "start": "2019-01-07"},
        {"code": "WY", "name": "Wyoming", "lat": 43.0760, "lon": -107.2903, "governor": "Mark Gordon", "party": "Republican", "start": "2019-01-07"}
    ]

def get_canadian_provinces():
    """Get all 13 Canadian provinces and territories with premiers (2025)"""
    return [
        {"code": "AB", "name": "Alberta", "lat": 53.9333, "lon": -116.5765, "premier": "Danielle Smith", "party": "United Conservative Party", "start": "2022-10-11"},
        {"code": "BC", "name": "British Columbia", "lat": 53.7267, "lon": -127.6476, "premier": "David Eby", "party": "BC New Democratic Party", "start": "2022-11-18"},
        {"code": "MB", "name": "Manitoba", "lat": 53.7609, "lon": -98.8139, "premier": "Wab Kinew", "party": "Manitoba New Democratic Party", "start": "2023-10-18"},
        {"code": "NB", "name": "New Brunswick", "lat": 46.5653, "lon": -66.4619, "premier": "Blaine Higgs", "party": "Progressive Conservative Party", "start": "2018-11-09"},
        {"code": "NL", "name": "Newfoundland and Labrador", "lat": 53.1355, "lon": -57.6604, "premier": "Andrew Furey", "party": "Liberal Party", "start": "2020-08-19"},
        {"code": "NS", "name": "Nova Scotia", "lat": 45.0000, "lon": -63.0000, "premier": "Tim Houston", "party": "Progressive Conservative Party", "start": "2021-08-31"},
        {"code": "ON", "name": "Ontario", "lat": 51.2538, "lon": -85.3232, "premier": "Doug Ford", "party": "Progressive Conservative Party", "start": "2018-06-29"},
        {"code": "PE", "name": "Prince Edward Island", "lat": 46.5107, "lon": -63.4168, "premier": "Dennis King", "party": "Progressive Conservative Party", "start": "2019-04-23"},
        {"code": "QC", "name": "Quebec", "lat": 52.9399, "lon": -73.5491, "premier": "François Legault", "party": "Coalition Avenir Québec", "start": "2018-10-18"},
        {"code": "SK", "name": "Saskatchewan", "lat": 52.9399, "lon": -106.4509, "premier": "Scott Moe", "party": "Saskatchewan Party", "start": "2018-02-02"},
        {"code": "NT", "name": "Northwest Territories", "lat": 64.8255, "lon": -124.8457, "premier": "R.J. Simpson", "party": "Consensus Government", "start": "2023-12-08"},
        {"code": "NU", "name": "Nunavut", "lat": 70.2998, "lon": -83.1076, "premier": "P.J. Akeeagok", "party": "Consensus Government", "start": "2021-11-19"},
        {"code": "YT", "name": "Yukon", "lat": 64.2823, "lon": -135.0000, "premier": "Ranj Pillai", "party": "Yukon Liberal Party", "start": "2023-01-14"}
    ]

def generate_trump_promises():
    """Generate Trump 2024 campaign promises with exact quotes"""
    promises = []
    evidence = []
    statuses = []

    # Promise 1: Border Wall
    promises.append({
        "promiseId": "pr:usa:trump:001",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-01-15T00:00:00Z",
        "context": "2024 Campaign Rally - Iowa",
        "quoteExact": "We will finish the wall and we will seal the border.",
        "summary": "Complete construction of the border wall with Mexico",
        "tagsJSON": json.dumps(["immigration", "border", "security"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:001",
        "status": "in_progress",
        "score": 0.3,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Executive orders signed to resume border wall construction"
    })

    # Promise 2: Mass Deportations
    promises.append({
        "promiseId": "pr:usa:trump:002",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-03-20T00:00:00Z",
        "context": "2024 Campaign Speech - Texas",
        "quoteExact": "We will carry out the largest domestic deportation operation in American history.",
        "summary": "Launch mass deportation program for undocumented immigrants",
        "tagsJSON": json.dumps(["immigration", "deportation", "law-enforcement"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:002",
        "status": "in_progress",
        "score": 0.2,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Executive orders signed, operations beginning"
    })

    # Promise 3: No Tax on Tips
    promises.append({
        "promiseId": "pr:usa:trump:003",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-06-09T00:00:00Z",
        "context": "2024 Campaign Rally - Nevada",
        "quoteExact": "No tax on tips for working people!",
        "summary": "Eliminate federal income tax on tips for service workers",
        "tagsJSON": json.dumps(["taxation", "economy", "workers"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:003",
        "status": "pending",
        "score": 0.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Requires legislation, not yet proposed to Congress"
    })

    # Promise 4: No Tax on Social Security
    promises.append({
        "promiseId": "pr:usa:trump:004",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-07-31T00:00:00Z",
        "context": "Truth Social Post",
        "quoteExact": "SENIORS SHOULD NOT PAY TAX ON SOCIAL SECURITY!",
        "summary": "Eliminate federal tax on Social Security benefits",
        "tagsJSON": json.dumps(["taxation", "seniors", "social-security"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_social",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:004",
        "status": "pending",
        "score": 0.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Requires legislation, not yet proposed"
    })

    # Promise 5: Universal Tariffs
    promises.append({
        "promiseId": "pr:usa:trump:005",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-02-14T00:00:00Z",
        "context": "2024 Campaign Interview",
        "quoteExact": "I will impose a 10% baseline tariff on all imports coming into the United States.",
        "summary": "Implement 10-20% baseline tariff on all imports",
        "tagsJSON": json.dumps(["trade", "tariffs", "economy"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:005",
        "status": "in_progress",
        "score": 0.4,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Executive orders signed implementing targeted tariffs"
    })

    # Promise 6: End Ukraine War
    promises.append({
        "promiseId": "pr:usa:trump:006",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-05-27T00:00:00Z",
        "context": "2024 Campaign Rally",
        "quoteExact": "I will end the war in Ukraine within 24 hours.",
        "summary": "Negotiate end to Russia-Ukraine war within 24 hours",
        "tagsJSON": json.dumps(["foreign-policy", "ukraine", "russia"]),
        "dueBy": "2025-01-21T00:00:00Z",
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:006",
        "status": "broken",
        "score": 0.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "War continues beyond 24-hour deadline, negotiations ongoing"
    })

    # Promise 7: January 6 Pardons
    promises.append({
        "promiseId": "pr:usa:trump:007",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-03-04T00:00:00Z",
        "context": "2024 Campaign Speech",
        "quoteExact": "I will free the January 6th hostages being wrongfully imprisoned.",
        "summary": "Pardon January 6 Capitol riot defendants",
        "tagsJSON": json.dumps(["pardons", "january-6", "justice"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:007",
        "status": "kept",
        "score": 1.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Pardons issued on January 20, 2025"
    })

    evidence.append({
        "evidenceId": "ev:usa:trump:007:001",
        "promiseId": "pr:usa:trump:007",
        "date": "2025-01-20T18:00:00Z",
        "actionType": "executive_order",
        "sourceURL": "https://www.whitehouse.gov/briefing-room/presidential-actions/",
        "sourcePrimary": "https://www.whitehouse.gov/briefing-room/presidential-actions/",
        "sourceType": "gov_release",
        "title": "Executive Grant of Clemency",
        "description": "President Trump issued pardons for January 6 defendants",
        "bodyMarkdown": "Executive order granting pardons to approximately 1,500 January 6 defendants"
    })

    # Promise 8: Eliminate Department of Education
    promises.append({
        "promiseId": "pr:usa:trump:008",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-01-30T00:00:00Z",
        "context": "Agenda47 Video",
        "quoteExact": "We will ultimately eliminate the federal Department of Education.",
        "summary": "Abolish the U.S. Department of Education",
        "tagsJSON": json.dumps(["education", "federal-government", "deregulation"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_video",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:008",
        "status": "pending",
        "score": 0.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Requires Congressional approval, not yet proposed"
    })

    # Promise 9: Drill Baby Drill
    promises.append({
        "promiseId": "pr:usa:trump:009",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-08-15T00:00:00Z",
        "context": "Republican National Convention",
        "quoteExact": "Drill, baby, drill! We will unleash American energy dominance.",
        "summary": "Maximize oil and gas drilling on federal lands",
        "tagsJSON": json.dumps(["energy", "oil", "gas", "environment"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_video",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:009",
        "status": "in_progress",
        "score": 0.5,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Executive orders signed opening federal lands to drilling"
    })

    # Promise 10: Roll Back EV Mandates
    promises.append({
        "promiseId": "pr:usa:trump:010",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-04-02T00:00:00Z",
        "context": "2024 Campaign Speech - Michigan",
        "quoteExact": "I will terminate Biden's insane electric vehicle mandate on day one.",
        "summary": "Eliminate Biden-era electric vehicle regulations",
        "tagsJSON": json.dumps(["automobiles", "environment", "regulation"]),
        "dueBy": "2025-01-20T00:00:00Z",
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:010",
        "status": "kept",
        "score": 1.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Executive order signed rescinding EPA EV regulations"
    })

    evidence.append({
        "evidenceId": "ev:usa:trump:010:001",
        "promiseId": "pr:usa:trump:010",
        "date": "2025-01-20T12:00:00Z",
        "actionType": "executive_order",
        "sourceURL": "https://www.whitehouse.gov/briefing-room/presidential-actions/",
        "sourcePrimary": "https://www.whitehouse.gov/briefing-room/presidential-actions/",
        "sourceType": "gov_release",
        "title": "Executive Order on Energy Independence",
        "description": "Rescinds EPA tailpipe emissions standards",
        "bodyMarkdown": "Executive order rolling back Biden-era EPA regulations on vehicle emissions"
    })

    # Promise 11: Birthright Citizenship
    promises.append({
        "promiseId": "pr:usa:trump:011",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-05-30T00:00:00Z",
        "context": "Agenda47 Video",
        "quoteExact": "I will sign an executive order to end birthright citizenship.",
        "summary": "End automatic citizenship for children born in the US to undocumented parents",
        "tagsJSON": json.dumps(["immigration", "citizenship", "constitution"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_video",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:011",
        "status": "in_progress",
        "score": 0.1,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Executive order signed but immediately challenged in courts"
    })

    # Promise 12: Paris Climate Exit
    promises.append({
        "promiseId": "pr:usa:trump:012",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-09-17T00:00:00Z",
        "context": "2024 Campaign Rally",
        "quoteExact": "I will immediately withdraw from the Paris Climate Accord.",
        "summary": "Withdraw from Paris Climate Agreement",
        "tagsJSON": json.dumps(["climate", "international", "environment"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:012",
        "status": "kept",
        "score": 1.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Withdrawal notice submitted on January 20, 2025"
    })

    evidence.append({
        "evidenceId": "ev:usa:trump:012:001",
        "promiseId": "pr:usa:trump:012",
        "date": "2025-01-20T14:00:00Z",
        "actionType": "executive_order",
        "sourceURL": "https://www.whitehouse.gov/briefing-room/presidential-actions/",
        "sourcePrimary": "https://www.whitehouse.gov/briefing-room/presidential-actions/",
        "sourceType": "gov_release",
        "title": "Letter to United Nations - Paris Agreement Withdrawal",
        "description": "US withdraws from Paris Climate Agreement",
        "bodyMarkdown": "Official notice of withdrawal from Paris Climate Agreement submitted to UN"
    })

    # Promise 13: Fire Rogue Bureaucrats
    promises.append({
        "promiseId": "pr:usa:trump:013",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-07-19T00:00:00Z",
        "context": "Agenda47 Policy Video",
        "quoteExact": "We will clean out the corrupt Deep State and fire rogue bureaucrats.",
        "summary": "Remove career civil servants and restructure federal workforce",
        "tagsJSON": json.dumps(["government", "bureaucracy", "reform"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_video",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:013",
        "status": "in_progress",
        "score": 0.3,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Executive orders signed, Schedule F reinstated"
    })

    # Promise 14: Secure Elections
    promises.append({
        "promiseId": "pr:usa:trump:014",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-11-01T00:00:00Z",
        "context": "2024 Campaign Rally - Pennsylvania",
        "quoteExact": "We will ensure one-day voting with paper ballots and voter ID.",
        "summary": "Mandate voter ID and restrict mail-in voting",
        "tagsJSON": json.dumps(["elections", "voting", "voter-id"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:014",
        "status": "pending",
        "score": 0.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Requires state-level legislation, limited federal authority"
    })

    # Promise 15: China Tariffs
    promises.append({
        "promiseId": "pr:usa:trump:015",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-08-20T00:00:00Z",
        "context": "2024 Campaign Speech",
        "quoteExact": "I will impose a 60% tariff on all goods from China.",
        "summary": "Implement 60% tariff on Chinese imports",
        "tagsJSON": json.dumps(["trade", "china", "tariffs"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:015",
        "status": "in_progress",
        "score": 0.5,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Tariffs announced but phased implementation ongoing"
    })

    # Promise 16: Ban TikTok
    promises.append({
        "promiseId": "pr:usa:trump:016",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-12-16T00:00:00Z",
        "context": "Truth Social Post",
        "quoteExact": "TikTok must be sold or banned. National security requires it.",
        "summary": "Force sale or ban of TikTok in the United States",
        "tagsJSON": json.dumps(["technology", "national-security", "china"]),
        "dueBy": None,
        "sourcePrimary": "https://truthsocial.com/@realDonaldTrump",
        "sourceType": "official_social",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:016",
        "status": "in_progress",
        "score": 0.4,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Negotiations ongoing for forced sale"
    })

    # Promise 17: End Gender Ideology
    promises.append({
        "promiseId": "pr:usa:trump:017",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-01-31T00:00:00Z",
        "context": "Agenda47 Video",
        "quoteExact": "I will revoke every Biden policy promoting gender ideology in schools.",
        "summary": "Ban transgender policies in federal programs and schools",
        "tagsJSON": json.dumps(["education", "gender", "transgender"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_video",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:017",
        "status": "in_progress",
        "score": 0.6,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Executive orders signed, implementation beginning"
    })

    # Promise 18: Veterans Care
    promises.append({
        "promiseId": "pr:usa:trump:018",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-11-11T00:00:00Z",
        "context": "Veterans Day Speech",
        "quoteExact": "We will ensure every veteran gets the care they deserve.",
        "summary": "Expand VA healthcare and benefits for veterans",
        "tagsJSON": json.dumps(["veterans", "healthcare", "military"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:018",
        "status": "pending",
        "score": 0.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "No specific policy actions taken yet"
    })

    # Promise 19: End Homelessness
    promises.append({
        "promiseId": "pr:usa:trump:019",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-04-18T00:00:00Z",
        "context": "2024 Campaign Speech - California",
        "quoteExact": "We will get the homeless off our streets and into facilities where they can get help.",
        "summary": "Create tent cities and mandate treatment for homeless individuals",
        "tagsJSON": json.dumps(["homelessness", "housing", "mental-health"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:019",
        "status": "pending",
        "score": 0.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "No legislation or executive action yet"
    })

    # Promise 20: School Prayer
    promises.append({
        "promiseId": "pr:usa:trump:020",
        "personId": "p:donald_trump",
        "regionId": "cnt:us",
        "dateMade": "2024-02-29T00:00:00Z",
        "context": "Agenda47 Video",
        "quoteExact": "We will support bringing prayer back to our schools.",
        "summary": "Promote school prayer and religious freedom in education",
        "tagsJSON": json.dumps(["religion", "education", "first-amendment"]),
        "dueBy": None,
        "sourcePrimary": "https://www.donaldjtrump.com/agenda47",
        "sourceType": "official_video",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:usa:trump:020",
        "status": "pending",
        "score": 0.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "No policy action taken"
    })

    return {"promises": promises, "evidence": evidence, "statuses": statuses}

def generate_trudeau_promises():
    """Generate Trudeau promises from 2021 election and recent commitments"""
    promises = []
    evidence = []
    statuses = []

    # Promise 1: Dental Care
    promises.append({
        "promiseId": "pr:can:trudeau:001",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2021-08-15T00:00:00Z",
        "context": "2021 Liberal Election Platform",
        "quoteExact": "We will create a new Canadian Dental Care Plan for families with incomes under $90,000.",
        "summary": "National dental care plan for low-income families",
        "tagsJSON": json.dumps(["healthcare", "dental", "families"]),
        "dueBy": "2025-12-31T00:00:00Z",
        "sourcePrimary": "https://liberal.ca/our-platform/",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:001",
        "status": "in_progress",
        "score": 0.7,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Bill C-31 passed, program rolling out in phases"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:001:001",
        "promiseId": "pr:can:trudeau:001",
        "date": "2022-12-15T00:00:00Z",
        "actionType": "bill_passed",
        "sourceURL": "https://www.parl.ca/legisinfo/en/bill/44-1/c-31",
        "sourcePrimary": "https://www.parl.ca/legisinfo/en/bill/44-1/c-31",
        "sourceType": "gov_release",
        "title": "Bill C-31: Canadian Dental Benefit",
        "description": "Legislation establishing interim dental benefit",
        "bodyMarkdown": "Bill C-31 passed establishing interim dental benefit for children under 12"
    })

    # Promise 2: $10/day Childcare
    promises.append({
        "promiseId": "pr:can:trudeau:002",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2021-04-19T00:00:00Z",
        "context": "2021 Federal Budget",
        "quoteExact": "We will build a Canada-wide early learning and child care system with $10-a-day child care.",
        "summary": "$10/day national childcare program",
        "tagsJSON": json.dumps(["childcare", "families", "affordability"]),
        "dueBy": "2026-03-31T00:00:00Z",
        "sourcePrimary": "https://budget.canada.ca/2021/home-accueil-en.html",
        "sourceType": "gov_release",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:002",
        "status": "kept",
        "score": 0.95,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Agreements signed with all provinces/territories, most regions at $10/day"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:002:001",
        "promiseId": "pr:can:trudeau:002",
        "date": "2021-07-01T00:00:00Z",
        "actionType": "budget_line",
        "sourceURL": "https://www.canada.ca/en/employment-social-development/programs/early-learning-child-care/reports/2021-agreements.html",
        "sourcePrimary": "https://www.canada.ca/en/employment-social-development/programs/early-learning-child-care/reports/2021-agreements.html",
        "sourceType": "gov_release",
        "title": "Canada-wide Early Learning and Child Care Agreements",
        "description": "$30B funding agreements with provinces",
        "bodyMarkdown": "Bilateral agreements signed with all provinces and territories for $10/day childcare"
    })

    # Promise 3: Pharmacare
    promises.append({
        "promiseId": "pr:can:trudeau:003",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2021-09-01T00:00:00Z",
        "context": "2021 Liberal Election Platform",
        "quoteExact": "We will introduce a Canada Pharmacare Act and work towards universal coverage.",
        "summary": "Universal pharmacare program",
        "tagsJSON": json.dumps(["healthcare", "pharmacare", "prescriptions"]),
        "dueBy": "2025-12-31T00:00:00Z",
        "sourcePrimary": "https://liberal.ca/our-platform/",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:003",
        "status": "in_progress",
        "score": 0.5,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Bill C-64 introduced in Parliament, diabetes/contraceptive coverage starting 2025"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:003:001",
        "promiseId": "pr:can:trudeau:003",
        "date": "2024-02-29T00:00:00Z",
        "actionType": "bill_passed",
        "sourceURL": "https://www.parl.ca/legisinfo/en/bill/44-1/c-64",
        "sourcePrimary": "https://www.parl.ca/legisinfo/en/bill/44-1/c-64",
        "sourceType": "gov_release",
        "title": "Bill C-64: Pharmacare Act",
        "description": "Framework legislation for national pharmacare",
        "bodyMarkdown": "Pharmacare Act passed establishing framework for national prescription drug coverage"
    })

    # Promise 4: Ban Single-Use Plastics
    promises.append({
        "promiseId": "pr:can:trudeau:004",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2019-06-10T00:00:00Z",
        "context": "2019 G7 Summit Announcement",
        "quoteExact": "We will ban harmful single-use plastics as early as 2021.",
        "summary": "Ban single-use plastic items nationwide",
        "tagsJSON": json.dumps(["environment", "plastics", "pollution"]),
        "dueBy": "2021-12-31T00:00:00Z",
        "sourcePrimary": "https://www.canada.ca/en/environment-climate-change/services/managing-reducing-waste/reduce-plastics.html",
        "sourceType": "gov_release",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:004",
        "status": "kept",
        "score": 1.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Ban implemented December 2023"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:004:001",
        "promiseId": "pr:can:trudeau:004",
        "date": "2022-06-20T00:00:00Z",
        "actionType": "regulation_published",
        "sourceURL": "https://gazette.gc.ca/rp-pr/p2/2022/2022-06-25/html/sor-dors138-eng.html",
        "sourcePrimary": "https://gazette.gc.ca/rp-pr/p2/2022/2022-06-25/html/sor-dors138-eng.html",
        "sourceType": "legal_gazette",
        "title": "Single-use Plastics Prohibition Regulations",
        "description": "Regulations banning six categories of single-use plastics",
        "bodyMarkdown": "Regulations published in Canada Gazette banning checkout bags, cutlery, straws, stir sticks, rings, and food containers"
    })

    # Promise 5: Net-Zero by 2050
    promises.append({
        "promiseId": "pr:can:trudeau:005",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2019-09-24T00:00:00Z",
        "context": "2019 UN Climate Summit",
        "quoteExact": "Canada will achieve net-zero emissions by 2050.",
        "summary": "Achieve net-zero greenhouse gas emissions by 2050",
        "tagsJSON": json.dumps(["climate", "emissions", "environment"]),
        "dueBy": "2050-12-31T00:00:00Z",
        "sourcePrimary": "https://www.canada.ca/en/services/environment/weather/climatechange/climate-plan/net-zero-emissions-2050.html",
        "sourceType": "gov_release",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:005",
        "status": "in_progress",
        "score": 0.3,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Net-zero legislation passed, emissions reduction targets ongoing"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:005:001",
        "promiseId": "pr:can:trudeau:005",
        "date": "2021-06-29T00:00:00Z",
        "actionType": "bill_passed",
        "sourceURL": "https://www.parl.ca/legisinfo/en/bill/43-2/c-12",
        "sourcePrimary": "https://www.parl.ca/legisinfo/en/bill/43-2/c-12",
        "sourceType": "gov_release",
        "title": "Canadian Net-Zero Emissions Accountability Act",
        "description": "Legislation enshrining net-zero 2050 target in law",
        "bodyMarkdown": "Bill C-12 passed establishing legal framework for achieving net-zero emissions by 2050"
    })

    # Promise 6: Ban Foreign Home Buyers
    promises.append({
        "promiseId": "pr:can:trudeau:006",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2021-09-07T00:00:00Z",
        "context": "2021 Liberal Election Platform",
        "quoteExact": "We will ban foreign buyers from purchasing non-recreational residential property in Canada for two years.",
        "summary": "Two-year ban on foreign home purchases",
        "tagsJSON": json.dumps(["housing", "foreign-investment", "affordability"]),
        "dueBy": "2023-01-01T00:00:00Z",
        "sourcePrimary": "https://liberal.ca/our-platform/",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:006",
        "status": "kept",
        "score": 1.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Ban implemented January 1, 2023, extended to 2027"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:006:001",
        "promiseId": "pr:can:trudeau:006",
        "date": "2023-01-01T00:00:00Z",
        "actionType": "regulation_published",
        "sourceURL": "https://laws.justice.gc.ca/eng/acts/P-25.2/",
        "sourcePrimary": "https://laws.justice.gc.ca/eng/acts/P-25.2/",
        "sourceType": "legal_gazette",
        "title": "Prohibition on the Purchase of Residential Property by Non-Canadians Act",
        "description": "Two-year ban on foreign home purchases",
        "bodyMarkdown": "Act prohibiting non-Canadians from purchasing residential property came into force January 1, 2023"
    })

    # Promise 7: Clean Drinking Water for Reserves
    promises.append({
        "promiseId": "pr:can:trudeau:007",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2015-08-20T00:00:00Z",
        "context": "2015 Liberal Election Platform",
        "quoteExact": "We will end all long-term drinking water advisories on reserves within five years.",
        "summary": "End all drinking water advisories on First Nations reserves",
        "tagsJSON": json.dumps(["indigenous", "water", "infrastructure"]),
        "dueBy": "2021-03-31T00:00:00Z",
        "sourcePrimary": "https://liberal.ca/realchange/",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:007",
        "status": "broken",
        "score": 0.6,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Deadline missed, 132 advisories lifted but 32 remain as of 2025"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:007:001",
        "promiseId": "pr:can:trudeau:007",
        "date": "2024-12-31T00:00:00Z",
        "actionType": "public_data_metric",
        "sourceURL": "https://www.sac-isc.gc.ca/eng/1506514143353/1533317130660",
        "sourcePrimary": "https://www.sac-isc.gc.ca/eng/1506514143353/1533317130660",
        "sourceType": "gov_release",
        "title": "Drinking Water Advisories Tracker",
        "description": "132 long-term advisories lifted since 2015",
        "bodyMarkdown": "Government data shows 132 advisories lifted but 32 long-term advisories remain"
    })

    # Promise 8: Plant 2 Billion Trees
    promises.append({
        "promiseId": "pr:can:trudeau:008",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2019-09-27T00:00:00Z",
        "context": "2019 Liberal Election Platform",
        "quoteExact": "We will plant two billion trees over the next 10 years.",
        "summary": "Plant 2 billion trees by 2030",
        "tagsJSON": json.dumps(["environment", "climate", "forestry"]),
        "dueBy": "2030-12-31T00:00:00Z",
        "sourcePrimary": "https://www.canada.ca/en/campaign/2-billion-trees.html",
        "sourceType": "gov_release",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:008",
        "status": "in_progress",
        "score": 0.15,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Program launched but only ~300M trees planted so far, behind schedule"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:008:001",
        "promiseId": "pr:can:trudeau:008",
        "date": "2021-05-01T00:00:00Z",
        "actionType": "program_launched",
        "sourceURL": "https://www.canada.ca/en/campaign/2-billion-trees.html",
        "sourcePrimary": "https://www.canada.ca/en/campaign/2-billion-trees.html",
        "sourceType": "gov_release",
        "title": "2 Billion Trees Program Launch",
        "description": "Tree planting program officially launched",
        "bodyMarkdown": "$3.2B program launched to plant 2 billion trees by 2030"
    })

    # Promise 9: Lower Cell Phone Bills
    promises.append({
        "promiseId": "pr:can:trudeau:009",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2019-10-15T00:00:00Z",
        "context": "2019 Liberal Election Platform",
        "quoteExact": "We will reduce wireless costs by 25 percent over the next four years.",
        "summary": "Reduce cell phone bills by 25%",
        "tagsJSON": json.dumps(["telecommunications", "affordability", "consumers"]),
        "dueBy": "2023-10-15T00:00:00Z",
        "sourcePrimary": "https://liberal.ca/our-platform/",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:009",
        "status": "kept",
        "score": 1.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "CRTC reports 25%+ reduction achieved by 2023"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:009:001",
        "promiseId": "pr:can:trudeau:009",
        "date": "2023-10-01T00:00:00Z",
        "actionType": "public_data_metric",
        "sourceURL": "https://crtc.gc.ca/eng/publications/reports/policymonitoring/2023/cmr5.htm",
        "sourcePrimary": "https://crtc.gc.ca/eng/publications/reports/policymonitoring/2023/cmr5.htm",
        "sourceType": "gov_release",
        "title": "CRTC Communications Monitoring Report",
        "description": "Wireless costs down 27% since 2019",
        "bodyMarkdown": "CRTC data shows average wireless costs decreased 27% between 2019-2023"
    })

    # Promise 10: Build 1.4M Homes
    promises.append({
        "promiseId": "pr:can:trudeau:010",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2022-04-07T00:00:00Z",
        "context": "2022 Federal Budget - Housing Announcement",
        "quoteExact": "We will build 1.4 million homes over the next four years through the Housing Accelerator Fund.",
        "summary": "Build 1.4 million new homes by 2026",
        "tagsJSON": json.dumps(["housing", "construction", "affordability"]),
        "dueBy": "2026-03-31T00:00:00Z",
        "sourcePrimary": "https://www.cmhc-schl.gc.ca/professionals/project-funding-and-mortgage-financing/funding-programs/all-funding-programs/housing-accelerator-fund",
        "sourceType": "gov_release",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:010",
        "status": "in_progress",
        "score": 0.35,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "~490,000 units completed/approved so far, on track but behind pace"
    })

    # Promise 11: Electoral Reform
    promises.append({
        "promiseId": "pr:can:trudeau:011",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2015-06-16T00:00:00Z",
        "context": "2015 Liberal Election Platform",
        "quoteExact": "2015 will be the last federal election conducted under the first-past-the-post voting system.",
        "summary": "Replace first-past-the-post electoral system",
        "tagsJSON": json.dumps(["democracy", "electoral-reform", "voting"]),
        "dueBy": "2019-10-21T00:00:00Z",
        "sourcePrimary": "https://liberal.ca/realchange/",
        "sourceType": "official_site",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:011",
        "status": "broken",
        "score": 0.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Promise abandoned in 2017, no reform implemented"
    })

    # Promise 12: Universal Broadband
    promises.append({
        "promiseId": "pr:can:trudeau:012",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2020-11-09T00:00:00Z",
        "context": "Universal Broadband Fund Announcement",
        "quoteExact": "We will connect 98% of Canadians to high-speed internet by 2026, and 100% by 2030.",
        "summary": "Universal high-speed internet access by 2030",
        "tagsJSON": json.dumps(["internet", "infrastructure", "rural"]),
        "dueBy": "2030-12-31T00:00:00Z",
        "sourcePrimary": "https://ised-isde.canada.ca/site/high-speed-internet-canada/en",
        "sourceType": "gov_release",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:012",
        "status": "in_progress",
        "score": 0.5,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "~95% coverage achieved, on track for 2026 target"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:012:001",
        "promiseId": "pr:can:trudeau:012",
        "date": "2024-12-31T00:00:00Z",
        "actionType": "public_data_metric",
        "sourceURL": "https://ised-isde.canada.ca/site/high-speed-internet-canada/en/canadas-connectivity-progress-dashboard",
        "sourcePrimary": "https://ised-isde.canada.ca/site/high-speed-internet-canada/en/canadas-connectivity-progress-dashboard",
        "sourceType": "gov_release",
        "title": "Connectivity Progress Dashboard",
        "description": "95% of Canadians now have access to high-speed internet",
        "bodyMarkdown": "Government data shows 95% of households now have access to 50/10 Mbps internet"
    })

    # Promise 13: Carbon Pricing
    promises.append({
        "promiseId": "pr:can:trudeau:013",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2018-10-23T00:00:00Z",
        "context": "Federal Carbon Pricing Announcement",
        "quoteExact": "We will implement a rising carbon price reaching $170 per tonne by 2030.",
        "summary": "Implement carbon tax rising to $170/tonne by 2030",
        "tagsJSON": json.dumps(["climate", "carbon-pricing", "environment"]),
        "dueBy": "2030-04-01T00:00:00Z",
        "sourcePrimary": "https://www.canada.ca/en/environment-climate-change/services/climate-change/pricing-pollution-how-it-will-work.html",
        "sourceType": "gov_release",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:013",
        "status": "in_progress",
        "score": 0.5,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Carbon price at $80/tonne in 2025, increasing annually to $170 by 2030"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:013:001",
        "promiseId": "pr:can:trudeau:013",
        "date": "2021-03-11T00:00:00Z",
        "actionType": "regulation_published",
        "sourceURL": "https://gazette.gc.ca/rp-pr/p1/2021/2021-03-27/html/reg2-eng.html",
        "sourcePrimary": "https://gazette.gc.ca/rp-pr/p1/2021/2021-03-27/html/reg2-eng.html",
        "sourceType": "legal_gazette",
        "title": "Carbon Pricing Amendment Regulations",
        "description": "Regulations implementing rising carbon price to $170/tonne",
        "bodyMarkdown": "Regulations published establishing carbon price trajectory to $170/tonne by 2030"
    })

    # Promise 14: Gun Control
    promises.append({
        "promiseId": "pr:can:trudeau:014",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2020-05-01T00:00:00Z",
        "context": "Order in Council Announcement",
        "quoteExact": "We will ban military-style assault weapons and implement a buyback program.",
        "summary": "Ban assault-style weapons and implement buyback",
        "tagsJSON": json.dumps(["gun-control", "public-safety", "firearms"]),
        "dueBy": "2025-12-31T00:00:00Z",
        "sourcePrimary": "https://www.publicsafety.gc.ca/cnt/cntrng-crm/frrms/index-en.aspx",
        "sourceType": "gov_release",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:014",
        "status": "in_progress",
        "score": 0.6,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Ban implemented, buyback program delayed"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:014:001",
        "promiseId": "pr:can:trudeau:014",
        "date": "2020-05-01T00:00:00Z",
        "actionType": "regulation_published",
        "sourceURL": "https://gazette.gc.ca/rp-pr/p2/2020/2020-05-01-x3/html/sor-dors96-eng.html",
        "sourcePrimary": "https://gazette.gc.ca/rp-pr/p2/2020/2020-05-01-x3/html/sor-dors96-eng.html",
        "sourceType": "legal_gazette",
        "title": "Regulations Amending the Classification of Firearms",
        "description": "Order banning 1,500+ models of assault-style firearms",
        "bodyMarkdown": "Order in Council banning over 1,500 models of assault-style firearms effective May 1, 2020"
    })

    # Promise 15: Statutory Holidays
    promises.append({
        "promiseId": "pr:can:trudeau:015",
        "personId": "p:justin_trudeau",
        "regionId": "cnt:ca",
        "dateMade": "2021-05-30T00:00:00Z",
        "context": "Truth and Reconciliation Announcement",
        "quoteExact": "We will make September 30th, National Day for Truth and Reconciliation, a federal statutory holiday.",
        "summary": "Create National Day for Truth and Reconciliation as federal holiday",
        "tagsJSON": json.dumps(["indigenous", "reconciliation", "statutory-holiday"]),
        "dueBy": "2021-09-30T00:00:00Z",
        "sourcePrimary": "https://www.canada.ca/en/canadian-heritage/campaigns/national-day-truth-reconciliation.html",
        "sourceType": "gov_release",
        "policyTagsJSON": None,
        "effectInputsJSON": None
    })

    statuses.append({
        "promiseId": "pr:can:trudeau:015",
        "status": "kept",
        "score": 1.0,
        "computedAt": "2025-01-30T00:00:00Z",
        "explanation": "Holiday implemented September 30, 2021"
    })

    evidence.append({
        "evidenceId": "ev:can:trudeau:015:001",
        "promiseId": "pr:can:trudeau:015",
        "date": "2021-06-03T00:00:00Z",
        "actionType": "bill_passed",
        "sourceURL": "https://www.parl.ca/legisinfo/en/bill/43-2/c-5",
        "sourcePrimary": "https://www.parl.ca/legisinfo/en/bill/43-2/c-5",
        "sourceType": "gov_release",
        "title": "Bill C-5: An Act to amend the Bills of Exchange Act",
        "description": "Legislation creating National Day for Truth and Reconciliation",
        "bodyMarkdown": "Bill passed creating September 30 as federal statutory holiday for Truth and Reconciliation"
    })

    return {"promises": promises, "evidence": evidence, "statuses": statuses}

def generate_industries():
    """Generate industry categories for market impact"""
    return [
        {"industryId": "ind:energy", "code": "10", "name": "Energy"},
        {"industryId": "ind:materials", "code": "15", "name": "Materials"},
        {"industryId": "ind:industrials", "code": "20", "name": "Industrials"},
        {"industryId": "ind:consumer-discretionary", "code": "25", "name": "Consumer Discretionary"},
        {"industryId": "ind:consumer-staples", "code": "30", "name": "Consumer Staples"},
        {"industryId": "ind:healthcare", "code": "35", "name": "Health Care"},
        {"industryId": "ind:financials", "code": "40", "name": "Financials"},
        {"industryId": "ind:technology", "code": "45", "name": "Information Technology"},
        {"industryId": "ind:telecom", "code": "50", "name": "Telecommunications"},
        {"industryId": "ind:utilities", "code": "55", "name": "Utilities"},
        {"industryId": "ind:real-estate", "code": "60", "name": "Real Estate"}
    ]

def generate_policy_tags():
    """Generate policy tags for categorization"""
    tags = ["immigration", "border", "security", "taxation", "economy", "trade", "tariffs",
            "foreign-policy", "energy", "environment", "climate", "healthcare", "education",
            "gun-control", "law-enforcement", "veterans", "housing", "infrastructure",
            "indigenous", "childcare", "families", "affordability", "telecommunications"]

    return [{"policyTagId": f"tag:{tag}", "name": tag} for tag in tags]

def main():
    """Generate complete comprehensive seed data"""
    print("Loading world leaders data...")
    world_leaders = load_world_leaders()
    country_data = get_country_data()
    us_states = get_us_states()
    can_provinces = get_canadian_provinces()

    print("Generating comprehensive data structure...")

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

    # Add continents
    print("Adding continents...")
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

    # Add all 195 countries with leaders
    print(f"Adding {len(world_leaders)} countries with current leaders...")
    for leader in world_leaders:
        country_code = leader['country']
        if country_code in country_data:
            country_info = country_data[country_code]

            # Add country region
            data["regions"].append({
                "regionId": f"cnt:{country_code.lower()}",
                "type": "country",
                "isoCode": country_code,
                "name": country_info['name'],
                "parentRegionId": country_info['continent'],
                "shapeRef": None,
                "latitude": country_info['lat'],
                "longitude": country_info['lon'],
                "boundingBoxJSON": None
            })

            # Add leader
            person_id = f"p:{leader['name'].lower().replace(' ', '_').replace('.', '')}"
            data["officeholders"].append({
                "personId": person_id,
                "name": leader['name'],
                "title": leader['title'],
                "regionId": f"cnt:{country_code.lower()}",
                "partyName": leader.get('party'),
                "partyURL": None,
                "startDate": leader['start'] + "T00:00:00Z",
                "endDate": None,
                "officialSiteURL": None,
                "photoURL": None
            })

    # Add all 50 US states with governors
    print(f"Adding {len(us_states)} US states with governors...")
    for state in us_states:
        # Add state region
        data["regions"].append({
            "regionId": f"st:us:{state['code'].lower()}",
            "type": "state",
            "isoCode": f"US-{state['code']}",
            "name": state['name'],
            "parentRegionId": "cnt:us",
            "shapeRef": None,
            "latitude": state['lat'],
            "longitude": state['lon'],
            "boundingBoxJSON": None
        })

        # Add governor
        person_id = f"p:{state['governor'].lower().replace(' ', '_')}"
        data["officeholders"].append({
            "personId": person_id,
            "name": state['governor'],
            "title": f"Governor of {state['name']}",
            "regionId": f"st:us:{state['code'].lower()}",
            "partyName": state['party'],
            "partyURL": None,
            "startDate": state['start'] + "T00:00:00Z",
            "endDate": None,
            "officialSiteURL": None,
            "photoURL": None
        })

    # Add all 13 Canadian provinces with premiers
    print(f"Adding {len(can_provinces)} Canadian provinces with premiers...")
    for prov in can_provinces:
        # Add province region
        data["regions"].append({
            "regionId": f"pv:ca:{prov['code'].lower()}",
            "type": "province",
            "isoCode": f"CA-{prov['code']}",
            "name": prov['name'],
            "parentRegionId": "cnt:ca",
            "shapeRef": None,
            "latitude": prov['lat'],
            "longitude": prov['lon'],
            "boundingBoxJSON": None
        })

        # Add premier
        person_id = f"p:{prov['premier'].lower().replace(' ', '_')}"
        data["officeholders"].append({
            "personId": person_id,
            "name": prov['premier'],
            "title": f"Premier of {prov['name']}",
            "regionId": f"pv:ca:{prov['code'].lower()}",
            "partyName": prov['party'],
            "partyURL": None,
            "startDate": prov['start'] + "T00:00:00Z",
            "endDate": None,
            "officialSiteURL": None,
            "photoURL": None
        })

    # Add Trump promises
    print("Generating Trump 2024 campaign promises...")
    trump_data = generate_trump_promises()
    data["promises"].extend(trump_data['promises'])
    data["evidence"].extend(trump_data['evidence'])
    data["statusSnapshots"].extend(trump_data['statuses'])

    # Add Trudeau promises
    print("Generating Trudeau promises...")
    trudeau_data = generate_trudeau_promises()
    data["promises"].extend(trudeau_data['promises'])
    data["evidence"].extend(trudeau_data['evidence'])
    data["statusSnapshots"].extend(trudeau_data['statuses'])

    # Add industries and policy tags
    print("Adding industries and policy tags...")
    data["industries"] = generate_industries()
    data["policyTags"] = generate_policy_tags()

    # Write to file
    output_file = "GPT/Resources/seed_data.json"
    print(f"\nWriting to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("\n" + "="*60)
    print("✅ COMPLETE! Comprehensive seed data generated")
    print("="*60)
    print(f"📊 Generated:")
    print(f"   • {len([r for r in data['regions'] if r['type'] == 'continent'])} continents")
    print(f"   • {len([r for r in data['regions'] if r['type'] == 'country'])} countries")
    print(f"   • {len([r for r in data['regions'] if r['type'] == 'state'])} US states")
    print(f"   • {len([r for r in data['regions'] if r['type'] == 'province'])} Canadian provinces")
    print(f"   • {len(data['officeholders'])} officeholders")
    print(f"   • {len(data['promises'])} promises")
    print(f"   • {len(data['evidence'])} evidence entries")
    print(f"   • {len(data['statusSnapshots'])} status snapshots")
    print(f"   • {len(data['industries'])} industries")
    print(f"   • {len(data['policyTags'])} policy tags")
    print(f"\n💾 File saved to: {output_file}")
    print(f"📁 File size: ~{len(json.dumps(data)) / 1024:.1f} KB")
    print("\n🚀 Ready to build and run in Xcode!")

if __name__ == "__main__":
    main()
