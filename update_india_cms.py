#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Current Indian Chief Ministers (as of November 2025)
current_cms = {
    'state:in:ap': {'name': 'N. Chandrababu Naidu', 'party': 'Telugu Desam Party', 'startDate': '2024-06-12'},
    'state:in:ar': {'name': 'Pema Khandu', 'party': 'Bharatiya Janata Party', 'startDate': '2016-07-17'},
    'state:in:as': {'name': 'Himanta Biswa Sarma', 'party': 'Bharatiya Janata Party', 'startDate': '2021-05-10'},
    'state:in:br': {'name': 'Nitish Kumar', 'party': 'Janata Dal (United)', 'startDate': '2015-02-22'},
    'state:in:ct': {'name': 'Vishnu Deo Sai', 'party': 'Bharatiya Janata Party', 'startDate': '2023-12-13'},
    'state:in:ga': {'name': 'Pramod Sawant', 'party': 'Bharatiya Janata Party', 'startDate': '2019-03-19'},
    'state:in:gj': {'name': 'Bhupendrabhai Patel', 'party': 'Bharatiya Janata Party', 'startDate': '2021-09-13'},
    'state:in:hr': {'name': 'Nayab Singh Saini', 'party': 'Bharatiya Janata Party', 'startDate': '2024-03-12'},
    'state:in:hp': {'name': 'Sukhvinder Singh Sukhu', 'party': 'Indian National Congress', 'startDate': '2022-12-11'},
    'state:in:jh': {'name': 'Hemant Soren', 'party': 'Jharkhand Mukti Morcha', 'startDate': '2024-07-04'},
    'state:in:ka': {'name': 'Siddaramaiah', 'party': 'Indian National Congress', 'startDate': '2023-05-20'},
    'state:in:kl': {'name': 'Pinarayi Vijayan', 'party': 'Communist Party of India (Marxist)', 'startDate': '2016-05-25'},
    'state:in:mp': {'name': 'Mohan Yadav', 'party': 'Bharatiya Janata Party', 'startDate': '2023-12-13'},
    'state:in:mh': {'name': 'Devendra Fadnavis', 'party': 'Bharatiya Janata Party', 'startDate': '2024-12-05'},
    'state:in:mn': {'name': 'N. Biren Singh', 'party': 'Bharatiya Janata Party', 'startDate': '2017-03-15'},  # President's Rule ended
    'state:in:ml': {'name': 'Conrad Sangma', 'party': 'National People\'s Party', 'startDate': '2018-03-06'},
    'state:in:mz': {'name': 'Lalduhoma', 'party': 'Zoram People\'s Movement', 'startDate': '2023-12-08'},
    'state:in:nl': {'name': 'Neiphiu Rio', 'party': 'Naga People\'s Front', 'startDate': '2018-03-08'},
    'state:in:or': {'name': 'Mohan Charan Majhi', 'party': 'Bharatiya Janata Party', 'startDate': '2024-06-12'},
    'state:in:pb': {'name': 'Bhagwant Mann', 'party': 'Aam Aadmi Party', 'startDate': '2022-03-16'},
    'state:in:rj': {'name': 'Bhajan Lal Sharma', 'party': 'Bharatiya Janata Party', 'startDate': '2023-12-15'},
    'state:in:sk': {'name': 'Prem Singh Tamang', 'party': 'Sikkim Krantikari Morcha', 'startDate': '2019-05-27'},
    'state:in:tn': {'name': 'M. K. Stalin', 'party': 'Dravida Munnetra Kazhagam', 'startDate': '2021-05-07'},
    'state:in:tg': {'name': 'Anumula Revanth Reddy', 'party': 'Indian National Congress', 'startDate': '2023-12-07'},
    'state:in:tr': {'name': 'Manik Saha', 'party': 'Bharatiya Janata Party', 'startDate': '2022-05-15'},
    'state:in:up': {'name': 'Yogi Adityanath', 'party': 'Bharatiya Janata Party', 'startDate': '2017-03-19'},
    'state:in:ut': {'name': 'Pushkar Singh Dhami', 'party': 'Bharatiya Janata Party', 'startDate': '2021-07-04'},
    'state:in:wb': {'name': 'Mamata Banerjee', 'party': 'All India Trinamool Congress', 'startDate': '2011-05-20'}
}

# Update existing chief ministers
updated = 0
for officeholder in data['officeholders']:
    if officeholder['regionId'] in current_cms:
        cm_info = current_cms[officeholder['regionId']]
        officeholder['name'] = cm_info['name']
        officeholder['partyName'] = cm_info['party']
        officeholder['startDate'] = cm_info['startDate']
        officeholder['endDate'] = None
        updated += 1

print(f"✅ Updated {updated} Indian chief ministers")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
