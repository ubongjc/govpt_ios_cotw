#!/usr/bin/env python3
import json

# Read current seed data
with open('GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Add more promises including one for Doug Ford
additional_promises = [
    {
        "promiseId": "promise:ford:healthcare:2023",
        "personId": "person:ca:on:premier:ford",
        "regionId": "province:ca:on",
        "dateMade": "2023-03-01T00:00:00Z",
        "context": "Healthcare expansion announcement",
        "quoteExact": "We will add 3,000 new hospital beds and hire 6,000 more nurses across Ontario.",
        "summary": "Expand healthcare capacity with new beds and nursing staff",
        "tagsJSON": "[\"healthcare\", \"hospitals\", \"nursing\"]",
        "dueBy": "2025-12-31T00:00:00Z",
        "sourcePrimary": "https://news.ontario.ca/en/release/healthcare-expansion",
        "sourceType": "gov_release",
        "policyTagsJSON": "[\"healthcare\", \"public_health\"]",
        "effectInputsJSON": None
    },
    {
        "promiseId": "promise:ford:housing:2023",
        "personId": "person:ca:on:premier:ford",
        "regionId": "province:ca:on",
        "dateMade": "2023-06-15T00:00:00Z",
        "context": "Housing affordability plan",
        "quoteExact": "We will build 1.5 million homes by 2031 to address Ontario's housing crisis.",
        "summary": "Build 1.5 million new homes by 2031",
        "tagsJSON": "[\"housing\", \"construction\", \"affordability\"]",
        "dueBy": "2031-12-31T00:00:00Z",
        "sourcePrimary": "https://news.ontario.ca/housing-plan",
        "sourceType": "official_statement",
        "policyTagsJSON": "[\"housing\", \"urban_development\"]",
        "effectInputsJSON": None
    },
    {
        "promiseId": "promise:ford:transit:2023",
        "personId": "person:ca:on:premier:ford",
        "regionId": "province:ca:on",
        "dateMade": "2023-04-20T00:00:00Z",
        "context": "Transit expansion announcement",
        "quoteExact": "We're building the largest transit expansion in North American history with new subway lines.",
        "summary": "Expand Toronto transit with new subway lines",
        "tagsJSON": "[\"transit\", \"infrastructure\", \"transportation\"]",
        "dueBy": "2030-12-31T00:00:00Z",
        "sourcePrimary": "https://news.ontario.ca/transit",
        "sourceType": "official_statement",
        "policyTagsJSON": "[\"transportation\", \"infrastructure\"]",
        "effectInputsJSON": None
    }
]

# Check if promises already exist before adding
for promise in additional_promises:
    if not any(p['promiseId'] == promise['promiseId'] for p in data['promises']):
        data['promises'].append(promise)

# Add industries for the Markets section
industries = [
    {
        "industryId": "ind:tech",
        "code": "TECH",
        "name": "Technology"
    },
    {
        "industryId": "ind:healthcare",
        "code": "HLTH",
        "name": "Healthcare"
    },
    {
        "industryId": "ind:energy",
        "code": "ENRG",
        "name": "Energy"
    },
    {
        "industryId": "ind:finance",
        "code": "FIN",
        "name": "Finance"
    },
    {
        "industryId": "ind:realestate",
        "code": "RE",
        "name": "Real Estate"
    },
    {
        "industryId": "ind:manufacturing",
        "code": "MFG",
        "name": "Manufacturing"
    },
    {
        "industryId": "ind:retail",
        "code": "RTL",
        "name": "Retail"
    },
    {
        "industryId": "ind:transportation",
        "code": "TRNS",
        "name": "Transportation"
    },
    {
        "industryId": "ind:agriculture",
        "code": "AGRI",
        "name": "Agriculture"
    },
    {
        "industryId": "ind:defense",
        "code": "DEF",
        "name": "Defense"
    }
]

data['industries'] = industries

# Add policy tags
policy_tags = [
    {
        "tag": "infrastructure",
        "description": "Roads, bridges, and public works"
    },
    {
        "tag": "healthcare",
        "description": "Public health and medical services"
    },
    {
        "tag": "education",
        "description": "Schools and educational programs"
    },
    {
        "tag": "housing",
        "description": "Housing development and affordability"
    },
    {
        "tag": "climate",
        "description": "Climate change and environmental policy"
    },
    {
        "tag": "economy",
        "description": "Economic growth and fiscal policy"
    },
    {
        "tag": "defense",
        "description": "National security and defense"
    },
    {
        "tag": "immigration",
        "description": "Immigration and border policy"
    },
    {
        "tag": "technology",
        "description": "Technology and innovation policy"
    },
    {
        "tag": "transportation",
        "description": "Transportation and transit systems"
    }
]

data['policyTags'] = policy_tags

# Add policy tag to industry relationships
policy_tag_industries = [
    {
        "tag": "infrastructure",
        "industryId": "ind:realestate",
        "weight": 1.5
    },
    {
        "tag": "infrastructure",
        "industryId": "ind:manufacturing",
        "weight": 1.2
    },
    {
        "tag": "healthcare",
        "industryId": "ind:healthcare",
        "weight": 2.0
    },
    {
        "tag": "housing",
        "industryId": "ind:realestate",
        "weight": 2.0
    },
    {
        "tag": "housing",
        "industryId": "ind:manufacturing",
        "weight": 1.0
    },
    {
        "tag": "climate",
        "industryId": "ind:energy",
        "weight": 2.0
    },
    {
        "tag": "economy",
        "industryId": "ind:finance",
        "weight": 1.5
    },
    {
        "tag": "defense",
        "industryId": "ind:defense",
        "weight": 2.0
    },
    {
        "tag": "technology",
        "industryId": "ind:tech",
        "weight": 2.0
    },
    {
        "tag": "transportation",
        "industryId": "ind:transportation",
        "weight": 2.0
    }
]

data['policyTagIndustries'] = policy_tag_industries

# Add promise industry impacts (how promises affect different industries)
promise_industry_impacts = [
    # Biden infrastructure impact
    {
        "promiseId": "promise:biden:infrastructure:2021",
        "industryId": "ind:realestate",
        "direction": 1,  # Positive
        "impactClass": "high",
        "pctLow": 2.0,
        "pctHigh": 5.0,
        "confidence": 0.8,
        "rationale": "Infrastructure improvements increase property values and development opportunities"
    },
    {
        "promiseId": "promise:biden:infrastructure:2021",
        "industryId": "ind:manufacturing",
        "direction": 1,
        "impactClass": "high",
        "pctLow": 3.0,
        "pctHigh": 7.0,
        "confidence": 0.9,
        "rationale": "Infrastructure projects require manufactured materials and equipment"
    },
    # Trudeau climate impact
    {
        "promiseId": "promise:trudeau:climate:2021",
        "industryId": "ind:energy",
        "direction": -1,  # Negative for traditional energy
        "impactClass": "high",
        "pctLow": -5.0,
        "pctHigh": -2.0,
        "confidence": 0.7,
        "rationale": "Emissions reduction targets impact traditional energy sectors"
    },
    {
        "promiseId": "promise:trudeau:climate:2021",
        "industryId": "ind:tech",
        "direction": 1,  # Positive for green tech
        "impactClass": "medium",
        "pctLow": 1.0,
        "pctHigh": 3.0,
        "confidence": 0.6,
        "rationale": "Climate goals drive investment in clean technology"
    },
    # Ford healthcare impact
    {
        "promiseId": "promise:ford:healthcare:2023",
        "industryId": "ind:healthcare",
        "direction": 1,
        "impactClass": "high",
        "pctLow": 3.0,
        "pctHigh": 6.0,
        "confidence": 0.85,
        "rationale": "Direct investment in healthcare infrastructure and staffing"
    },
    # Ford housing impact
    {
        "promiseId": "promise:ford:housing:2023",
        "industryId": "ind:realestate",
        "direction": 1,
        "impactClass": "very_high",
        "pctLow": 5.0,
        "pctHigh": 10.0,
        "confidence": 0.9,
        "rationale": "Massive housing construction will boost real estate sector"
    },
    {
        "promiseId": "promise:ford:housing:2023",
        "industryId": "ind:manufacturing",
        "direction": 1,
        "impactClass": "high",
        "pctLow": 2.0,
        "pctHigh": 4.0,
        "confidence": 0.8,
        "rationale": "Construction materials demand will increase manufacturing"
    },
    # Ford transit impact
    {
        "promiseId": "promise:ford:transit:2023",
        "industryId": "ind:transportation",
        "direction": 1,
        "impactClass": "very_high",
        "pctLow": 4.0,
        "pctHigh": 8.0,
        "confidence": 0.85,
        "rationale": "Major transit expansion directly benefits transportation sector"
    },
    {
        "promiseId": "promise:ford:transit:2023",
        "industryId": "ind:realestate",
        "direction": 1,
        "impactClass": "medium",
        "pctLow": 1.0,
        "pctHigh": 3.0,
        "confidence": 0.7,
        "rationale": "Transit expansion increases property values near stations"
    },
    # Newsom housing impact
    {
        "promiseId": "promise:newsom:housing:2023",
        "industryId": "ind:realestate",
        "direction": 1,
        "impactClass": "very_high",
        "pctLow": 4.0,
        "pctHigh": 8.0,
        "confidence": 0.85,
        "rationale": "500,000 homes annually will transform California real estate"
    },
    # Abbott border impact
    {
        "promiseId": "promise:abbott:border:2023",
        "industryId": "ind:defense",
        "direction": 1,
        "impactClass": "medium",
        "pctLow": 1.0,
        "pctHigh": 2.0,
        "confidence": 0.7,
        "rationale": "Border security increases defense contractor opportunities"
    },
    # DeSantis education impact
    {
        "promiseId": "promise:desantis:education:2023",
        "industryId": "ind:tech",
        "direction": 1,
        "impactClass": "low",
        "pctLow": 0.5,
        "pctHigh": 1.5,
        "confidence": 0.6,
        "rationale": "School choice may increase edtech adoption"
    },
    # Whitmer infrastructure impact
    {
        "promiseId": "promise:whitmer:infrastructure:2023",
        "industryId": "ind:manufacturing",
        "direction": 1,
        "impactClass": "high",
        "pctLow": 2.0,
        "pctHigh": 4.0,
        "confidence": 0.8,
        "rationale": "Michigan's auto industry benefits from improved infrastructure"
    },
    # Adams crime reduction impact
    {
        "promiseId": "promise:adams:crime:2023",
        "industryId": "ind:retail",
        "direction": 1,
        "impactClass": "medium",
        "pctLow": 1.0,
        "pctHigh": 2.0,
        "confidence": 0.65,
        "rationale": "Reduced crime improves retail business environment"
    },
    {
        "promiseId": "promise:adams:crime:2023",
        "industryId": "ind:realestate",
        "direction": 1,
        "impactClass": "low",
        "pctLow": 0.5,
        "pctHigh": 1.5,
        "confidence": 0.6,
        "rationale": "Safer neighborhoods increase property values"
    }
]

data['promiseIndustryImpacts'] = promise_industry_impacts

# Statistics
print("Updated Dataset Statistics:")
print(f"Total regions: {len(data['regions'])}")
print(f"Total officeholders: {len(data['officeholders'])}")
print(f"Total promises: {len(data['promises'])}")
print(f"Total industries: {len(data['industries'])}")
print(f"Total policy tags: {len(data['policyTags'])}")
print(f"Total industry impacts: {len(data['promiseIndustryImpacts'])}")

# Save updated data
with open('GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print("\n✅ Successfully added Markets data and Doug Ford promises!")
print("The Markets section should now show industry impacts from government policies.")