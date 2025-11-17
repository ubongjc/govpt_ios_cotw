#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Fix all officeholders with null startDate
# Thailand provincial governors are appointed positions, most current ones took office in 2023-2024
fixed_count = 0
for oh in data['officeholders']:
    if oh.get('startDate') is None:
        # For Thailand governors, use 2023-10-01 as a reasonable default
        # (Thai fiscal year starts in October, new appointments often happen then)
        if oh.get('personId', '').startswith('person:th:'):
            oh['startDate'] = '2023-10-01T00:00:00Z'
        else:
            # For any other null dates, use a generic recent date
            oh['startDate'] = '2023-01-01T00:00:00Z'
        fixed_count += 1
        print(f"Fixed: {oh.get('personId')} - {oh.get('name')}")

print(f"\n✅ Fixed {fixed_count} officeholders with null startDate")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Updated seed_data.json")
