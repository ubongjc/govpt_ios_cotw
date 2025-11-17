#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# US Governor Promises with Market Impact
us_governor_promises = [
    # CALIFORNIA - Gavin Newsom
    {
        "promiseId": "promise:ca:newsom:ev:2024",
        "personId": "person:us:ca:newsom",
        "regionId": "state:us:ca",
        "summary": "Accelerate zero-emission vehicle transition with $10B infrastructure investment",
        "quoteExact": "California will lead the nation in zero-emission vehicles. We're investing $10 billion to build the infrastructure and incentives needed to get 5 million ZEVs on the road by 2030.",
        "context": "2024 State of the State Address",
        "dateMade": "2024-01-08T00:00:00Z",
        "dueBy": "2030-12-31T00:00:00Z",
        "sourcePrimary": "https://www.gov.ca.gov/speeches/",
        "sourceType": "official_statement",
        "tagsJSON": "[\"clean energy\", \"infrastructure\", \"climate\"]",
        "policyTagsJSON": "[\"transportation\", \"environment\", \"economy\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Automotive\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Major boost for EV manufacturers, charging infrastructure companies\"}, {\"sector\": \"Clean Energy\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Increased demand for batteries, solar, charging stations\"}, {\"sector\": \"Oil & Gas\", \"impact\": \"negative\", \"magnitude\": \"medium\", \"description\": \"Long-term reduction in gasoline demand\"}], \"estimatedJobs\": 150000, \"estimatedInvestment\": 10000000000}"
    },
    {
        "promiseId": "promise:ca:newsom:housing:2024",
        "personId": "person:us:ca:newsom",
        "regionId": "state:us:ca",
        "summary": "Build 2.5 million new homes by 2030 to address housing crisis",
        "quoteExact": "We're cutting red tape and streamlining approvals to build 2.5 million homes over the next six years. Every Californian deserves affordable housing.",
        "context": "Housing Crisis Summit",
        "dateMade": "2024-03-15T00:00:00Z",
        "dueBy": "2030-12-31T00:00:00Z",
        "sourcePrimary": "https://www.gov.ca.gov/housing/",
        "sourceType": "policy_announcement",
        "tagsJSON": "[\"housing\", \"construction\", \"affordability\"]",
        "policyTagsJSON": "[\"housing\", \"economy\", \"development\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Real Estate\", \"impact\": \"positive\", \"magnitude\": \"very_high\", \"description\": \"Massive construction boom, increased housing supply\"}, {\"sector\": \"Construction\", \"impact\": \"positive\", \"magnitude\": \"very_high\", \"description\": \"Major demand for builders, materials, labor\"}, {\"sector\": \"Banking\", \"impact\": \"positive\", \"magnitude\": \"medium\", \"description\": \"Increased mortgage lending opportunities\"}], \"estimatedJobs\": 400000, \"estimatedInvestment\": 250000000000}"
    },

    # TEXAS - Greg Abbott
    {
        "promiseId": "promise:tx:abbott:chips:2024",
        "personId": "person:us:tx:abbott",
        "regionId": "state:us:tx",
        "summary": "Attract $100B in semiconductor manufacturing investments",
        "quoteExact": "Texas will become America's semiconductor powerhouse. We're offering unprecedented incentives to bring chip manufacturing home, with a goal of $100 billion in private investment.",
        "context": "Texas Economic Development Summit",
        "dateMade": "2024-02-20T00:00:00Z",
        "dueBy": "2028-12-31T00:00:00Z",
        "sourcePrimary": "https://gov.texas.gov/news/",
        "sourceType": "official_statement",
        "tagsJSON": "[\"semiconductors\", \"manufacturing\", \"technology\"]",
        "policyTagsJSON": "[\"manufacturing\", \"technology\", \"economy\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Semiconductors\", \"impact\": \"positive\", \"magnitude\": \"very_high\", \"description\": \"Major fab construction, chip production capacity increase\"}, {\"sector\": \"Technology\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Supply chain benefits, tech ecosystem growth\"}, {\"sector\": \"Construction\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Fab construction projects worth billions\"}], \"estimatedJobs\": 50000, \"estimatedInvestment\": 100000000000}"
    },
    {
        "promiseId": "promise:tx:abbott:energy:2024",
        "personId": "person:us:tx:abbott",
        "regionId": "state:us:tx",
        "summary": "Modernize power grid with $25B investment to prevent outages",
        "quoteExact": "Never again will Texans face the crisis we saw in 2021. We're investing $25 billion to modernize our grid, add capacity, and ensure reliable power.",
        "context": "Energy Reliability Press Conference",
        "dateMade": "2024-01-12T00:00:00Z",
        "dueBy": "2027-12-31T00:00:00Z",
        "sourcePrimary": "https://gov.texas.gov/energy/",
        "sourceType": "policy_announcement",
        "tagsJSON": "[\"energy\", \"infrastructure\", \"reliability\"]",
        "policyTagsJSON": "[\"energy\", \"infrastructure\", \"public_safety\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Utilities\", \"impact\": \"positive\", \"magnitude\": \"very_high\", \"description\": \"Grid modernization, capacity expansion projects\"}, {\"sector\": \"Energy\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Natural gas, renewable energy capacity additions\"}, {\"sector\": \"Construction\", \"impact\": \"positive\", \"magnitude\": \"medium\", \"description\": \"Power plant and transmission infrastructure build-out\"}], \"estimatedJobs\": 35000, \"estimatedInvestment\": 25000000000}"
    },

    # FLORIDA - Ron DeSantis
    {
        "promiseId": "promise:fl:desantis:insurance:2024",
        "personId": "person:us:fl:desantis",
        "regionId": "state:us:fl",
        "summary": "Reform property insurance market to reduce premiums by 30%",
        "quoteExact": "Florida homeowners are drowning in insurance costs. Our comprehensive reforms will stabilize the market and reduce premiums by at least 30% over the next three years.",
        "context": "Insurance Reform Signing Ceremony",
        "dateMade": "2024-04-10T00:00:00Z",
        "dueBy": "2027-04-10T00:00:00Z",
        "sourcePrimary": "https://www.flgov.com/insurance-reform/",
        "sourceType": "official_statement",
        "tagsJSON": "[\"insurance\", \"consumer_protection\", \"housing\"]",
        "policyTagsJSON": "[\"insurance\", \"economy\", \"housing\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Insurance\", \"impact\": \"mixed\", \"magnitude\": \"high\", \"description\": \"Market stabilization but reduced premiums for insurers\"}, {\"sector\": \"Real Estate\", \"impact\": \"positive\", \"magnitude\": \"medium\", \"description\": \"Lower insurance costs boost home affordability\"}, {\"sector\": \"Construction\", \"impact\": \"positive\", \"magnitude\": \"medium\", \"description\": \"Building code updates create retrofit opportunities\"}], \"estimatedJobs\": 15000, \"estimatedCostSavings\": 8000000000}"
    },

    # NEW YORK - Kathy Hochul
    {
        "promiseId": "promise:ny:hochul:cannabis:2024",
        "personId": "person:us:ny:hochul",
        "regionId": "state:us:ny",
        "summary": "Launch $200M cannabis equity program to create 10,000 minority-owned businesses",
        "quoteExact": "New York's cannabis industry will be a model for equity and opportunity. We're investing $200 million to help minority entrepreneurs launch 10,000 cannabis businesses.",
        "context": "Cannabis Equity Initiative Launch",
        "dateMade": "2024-03-01T00:00:00Z",
        "dueBy": "2026-12-31T00:00:00Z",
        "sourcePrimary": "https://www.governor.ny.gov/cannabis/",
        "sourceType": "policy_announcement",
        "tagsJSON": "[\"cannabis\", \"equity\", \"entrepreneurship\"]",
        "policyTagsJSON": "[\"business\", \"social_justice\", \"economy\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Cannabis\", \"impact\": \"positive\", \"magnitude\": \"very_high\", \"description\": \"Major retail expansion, cultivation growth\"}, {\"sector\": \"Real Estate\", \"impact\": \"positive\", \"magnitude\": \"medium\", \"description\": \"Demand for dispensary and grow facility spaces\"}, {\"sector\": \"Agriculture\", \"impact\": \"positive\", \"magnitude\": \"medium\", \"description\": \"New cultivation operations statewide\"}], \"estimatedJobs\": 50000, \"estimatedInvestment\": 2000000000}"
    },
    {
        "promiseId": "promise:ny:hochul:transit:2024",
        "personId": "person:us:ny:hochul",
        "regionId": "state:us:ny",
        "summary": "Complete $68B MTA modernization to improve NYC subway reliability",
        "quoteExact": "Our $68 billion investment in the MTA will transform New York's transit system with new trains, modern signals, and accessible stations across the network.",
        "context": "MTA Capital Plan Announcement",
        "dateMade": "2024-01-18T00:00:00Z",
        "dueBy": "2029-12-31T00:00:00Z",
        "sourcePrimary": "https://www.governor.ny.gov/transit/",
        "sourceType": "budget_announcement",
        "tagsJSON": "[\"transit\", \"infrastructure\", \"modernization\"]",
        "policyTagsJSON": "[\"infrastructure\", \"transportation\", \"economy\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Transportation\", \"impact\": \"positive\", \"magnitude\": \"very_high\", \"description\": \"Major equipment orders, construction contracts\"}, {\"sector\": \"Construction\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Station renovations, infrastructure upgrades\"}, {\"sector\": \"Real Estate\", \"impact\": \"positive\", \"magnitude\": \"medium\", \"description\": \"Improved transit boosts property values\"}], \"estimatedJobs\": 80000, \"estimatedInvestment\": 68000000000}"
    },

    # PENNSYLVANIA - Josh Shapiro
    {
        "promiseId": "promise:pa:shapiro:hydrogen:2024",
        "personId": "person:us:pa:shapiro",
        "regionId": "state:us:pa",
        "summary": "Establish Pennsylvania as national hydrogen hub with $2B federal-state investment",
        "quoteExact": "Pennsylvania will lead America's clean hydrogen future. With $2 billion in combined investment, we're building the infrastructure to power the economy of tomorrow.",
        "context": "Hydrogen Hub Announcement",
        "dateMade": "2024-02-28T00:00:00Z",
        "dueBy": "2028-12-31T00:00:00Z",
        "sourcePrimary": "https://www.governor.pa.gov/hydrogen/",
        "sourceType": "official_statement",
        "tagsJSON": "[\"hydrogen\", \"clean_energy\", \"manufacturing\"]",
        "policyTagsJSON": "[\"energy\", \"environment\", \"economy\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Clean Energy\", \"impact\": \"positive\", \"magnitude\": \"very_high\", \"description\": \"Hydrogen production, fuel cell manufacturing\"}, {\"sector\": \"Manufacturing\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Industrial decarbonization opportunities\"}, {\"sector\": \"Natural Gas\", \"impact\": \"positive\", \"magnitude\": \"medium\", \"description\": \"Blue hydrogen from natural gas reforming\"}], \"estimatedJobs\": 25000, \"estimatedInvestment\": 2000000000}"
    },

    # ILLINOIS - JB Pritzker
    {
        "promiseId": "promise:il:pritzker:quantum:2024",
        "personId": "person:us:il:pritzker",
        "regionId": "state:us:il",
        "summary": "Build $500M quantum computing campus to attract tech companies",
        "quoteExact": "Illinois is home to world-leading quantum research. We're investing $500 million to build a quantum campus that will attract companies and create thousands of high-paying jobs.",
        "context": "Quantum Innovation Initiative",
        "dateMade": "2024-03-22T00:00:00Z",
        "dueBy": "2027-12-31T00:00:00Z",
        "sourcePrimary": "https://www2.illinois.gov/quantum/",
        "sourceType": "policy_announcement",
        "tagsJSON": "[\"quantum_computing\", \"technology\", \"research\"]",
        "policyTagsJSON": "[\"technology\", \"research\", \"economy\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Technology\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Quantum computing companies, research facilities\"}, {\"sector\": \"Real Estate\", \"impact\": \"positive\", \"magnitude\": \"medium\", \"description\": \"Tech campus development\"}, {\"sector\": \"Finance\", \"impact\": \"positive\", \"magnitude\": \"medium\", \"description\": \"Quantum applications in financial modeling\"}], \"estimatedJobs\": 8000, \"estimatedInvestment\": 500000000}"
    },

    # GEORGIA - Brian Kemp
    {
        "promiseId": "promise:ga:kemp:ev:2024",
        "personId": "person:us:ga:kemp",
        "regionId": "state:us:ga",
        "summary": "Transform Georgia into EV manufacturing capital with $20B in private investment",
        "quoteExact": "Georgia is becoming the electric vehicle capital of America. We've secured commitments for over $20 billion in EV and battery manufacturing, creating 30,000 jobs.",
        "context": "Economic Development Conference",
        "dateMade": "2024-01-25T00:00:00Z",
        "dueBy": "2027-12-31T00:00:00Z",
        "sourcePrimary": "https://gov.georgia.gov/ev-manufacturing/",
        "sourceType": "official_statement",
        "tagsJSON": "[\"electric_vehicles\", \"manufacturing\", \"jobs\"]",
        "policyTagsJSON": "[\"manufacturing\", \"economy\", \"environment\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Automotive\", \"impact\": \"positive\", \"magnitude\": \"very_high\", \"description\": \"Major EV and battery plant construction\"}, {\"sector\": \"Manufacturing\", \"impact\": \"positive\", \"magnitude\": \"very_high\", \"description\": \"Supply chain development, component manufacturing\"}, {\"sector\": \"Real Estate\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Industrial land development\"}], \"estimatedJobs\": 30000, \"estimatedInvestment\": 20000000000}"
    },

    # MICHIGAN - Gretchen Whitmer
    {
        "promiseId": "promise:mi:whitmer:auto:2024",
        "personId": "person:us:mi:whitmer",
        "regionId": "state:us:mi",
        "summary": "Secure Michigan's auto industry future with $5B EV transition fund",
        "quoteExact": "We're not letting Michigan's auto legacy slip away. Our $5 billion EV transition fund will retool factories, retrain workers, and keep our state as America's automotive leader.",
        "context": "Auto Industry Summit",
        "dateMade": "2024-02-14T00:00:00Z",
        "dueBy": "2028-12-31T00:00:00Z",
        "sourcePrimary": "https://www.michigan.gov/auto-transition/",
        "sourceType": "policy_announcement",
        "tagsJSON": "[\"automotive\", \"electric_vehicles\", \"workforce\"]",
        "policyTagsJSON": "[\"manufacturing\", \"economy\", \"workforce\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Automotive\", \"impact\": \"positive\", \"magnitude\": \"very_high\", \"description\": \"EV manufacturing, battery production, retooling\"}, {\"sector\": \"Manufacturing\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Supply chain transformation\"}, {\"sector\": \"Education\", \"impact\": \"positive\", \"magnitude\": \"medium\", \"description\": \"Workforce training programs\"}], \"estimatedJobs\": 45000, \"estimatedInvestment\": 5000000000}"
    },

    # ARIZONA - Katie Hobbs
    {
        "promiseId": "promise:az:hobbs:water:2024",
        "personId": "person:us:az:hobbs",
        "regionId": "state:us:az",
        "summary": "Invest $1B in water infrastructure to secure Arizona's growth",
        "quoteExact": "Water is Arizona's most precious resource. We're investing $1 billion in desalination, recycling, and conservation to ensure sustainable growth for generations.",
        "context": "Water Security Initiative",
        "dateMade": "2024-03-08T00:00:00Z",
        "dueBy": "2029-12-31T00:00:00Z",
        "sourcePrimary": "https://azgovernor.gov/water/",
        "sourceType": "policy_announcement",
        "tagsJSON": "[\"water\", \"infrastructure\", \"sustainability\"]",
        "policyTagsJSON": "[\"water\", \"environment\", \"infrastructure\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Utilities\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Water infrastructure modernization\"}, {\"sector\": \"Real Estate\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Removes growth constraints from water scarcity\"}, {\"sector\": \"Agriculture\", \"impact\": \"positive\", \"magnitude\": \"medium\", \"description\": \"Improved water efficiency technologies\"}], \"estimatedJobs\": 12000, \"estimatedInvestment\": 1000000000}"
    },

    # NORTH CAROLINA - Roy Cooper
    {
        "promiseId": "promise:nc:cooper:offshore:2024",
        "personId": "person:us:nc:cooper",
        "regionId": "state:us:nc",
        "summary": "Develop $8B offshore wind industry to power 700,000 homes",
        "quoteExact": "North Carolina's offshore wind potential is enormous. We're partnering with developers to build $8 billion in wind farms that will power 700,000 homes with clean energy.",
        "context": "Offshore Wind Summit",
        "dateMade": "2024-01-30T00:00:00Z",
        "dueBy": "2030-12-31T00:00:00Z",
        "sourcePrimary": "https://governor.nc.gov/offshore-wind/",
        "sourceType": "official_statement",
        "tagsJSON": "[\"offshore_wind\", \"clean_energy\", \"jobs\"]",
        "policyTagsJSON": "[\"energy\", \"environment\", \"economy\"]",
        "administrationStatus": "current",
        "effectInputsJSON": "{\"marketSectors\": [{\"sector\": \"Clean Energy\", \"impact\": \"positive\", \"magnitude\": \"very_high\", \"description\": \"Offshore wind development, manufacturing\"}, {\"sector\": \"Construction\", \"impact\": \"positive\", \"magnitude\": \"high\", \"description\": \"Port facilities, transmission infrastructure\"}, {\"sector\": \"Utilities\", \"impact\": \"mixed\", \"magnitude\": \"medium\", \"description\": \"Renewable integration challenges and opportunities\"}], \"estimatedJobs\": 18000, \"estimatedInvestment\": 8000000000}"
    }
]

# Add all promises
data['promises'].extend(us_governor_promises)

print(f"✅ Added {len(us_governor_promises)} US governor promises with market impact data")
print(f"Total promises: {len(data['promises'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
