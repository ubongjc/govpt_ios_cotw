#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Kenyan County Governors (elected August 2022 for 2022-2027 term)
kenyan_governors = [
    {"personId": "person:ke:mom:governor:nassir", "name": "Abdullswamad Shariff Nassir", "title": "Governor of Mombasa", "regionId": "county:ke:mom", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:kwa:governor:achani", "name": "Fatuma Mohamed Achani", "title": "Governor of Kwale", "regionId": "county:ke:kwa", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:kil:governor:mungaro", "name": "Gideon Maitha Mung'aro", "title": "Governor of Kilifi", "regionId": "county:ke:kil", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:tan:governor:godhana", "name": "Dhadho Godhana", "title": "Governor of Tana River", "regionId": "county:ke:tan", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:lam:governor:timamy", "name": "Issa Timamy", "title": "Governor of Lamu", "regionId": "county:ke:lam", "partyName": "Amani National Congress", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:tak:governor:mwadime", "name": "Andrew Mwadime", "title": "Governor of Taita-Taveta", "regionId": "county:ke:tak", "partyName": "Independent", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:gar:governor:jama", "name": "Nathif Jama", "title": "Governor of Garissa", "regionId": "county:ke:gar", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:waj:governor:jiir", "name": "Ahmed Abdullahi Jiir", "title": "Governor of Wajir", "regionId": "county:ke:waj", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:man:governor:khalif", "name": "Mohamed Adan Khalif", "title": "Governor of Mandera", "regionId": "county:ke:man", "partyName": "United Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:mar:governor:ali", "name": "Mohamud Ali", "title": "Governor of Marsabit", "regionId": "county:ke:mar", "partyName": "United Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:isi:governor:guyo", "name": "Abdi Guyo", "title": "Governor of Isiolo", "regionId": "county:ke:isi", "partyName": "Jubilee Party", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:mer:governor:mutuma", "name": "Isaac Mutuma", "title": "Governor of Meru", "regionId": "county:ke:mer", "partyName": "Independent", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:tha:governor:njuki", "name": "Onesmus Muthomi Njuki", "title": "Governor of Tharaka-Nithi", "regionId": "county:ke:tha", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:emb:governor:mbarire", "name": "Cecily Mbarire", "title": "Governor of Embu", "regionId": "county:ke:emb", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:kit:governor:malombe", "name": "Julius Malombe", "title": "Governor of Kitui", "regionId": "county:ke:kit", "partyName": "Wiper Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:mac:governor:ndeti", "name": "Wavinya Ndeti", "title": "Governor of Machakos", "regionId": "county:ke:mac", "partyName": "Wiper Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:mak:governor:kilonzo", "name": "Mutula Kilonzo", "title": "Governor of Makueni", "regionId": "county:ke:mak", "partyName": "Wiper Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:nyan:governor:kiarie", "name": "Moses Badilisha Kiarie", "title": "Governor of Nyandarua", "regionId": "county:ke:nyan", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:nyer:governor:kahiga", "name": "Edward Mutahi Kahiga", "title": "Governor of Nyeri", "regionId": "county:ke:nyer", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:kir:governor:waiguru", "name": "Anne Mumbi Waiguru", "title": "Governor of Kirinyaga", "regionId": "county:ke:kir", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:mur:governor:kangata", "name": "Irungu Kangata", "title": "Governor of Murang'a", "regionId": "county:ke:mur", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:kia:governor:wamatangi", "name": "Kimani Wamatangi", "title": "Governor of Kiambu", "regionId": "county:ke:kia", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:tur:governor:lomurkai", "name": "Jeremiah Lomurkai", "title": "Governor of Turkana", "regionId": "county:ke:tur", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:wes:governor:kachapin", "name": "Simon Kachapin", "title": "Governor of West Pokot", "regionId": "county:ke:wes", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:sam:governor:leleliit", "name": "Jonathan Lati Leleliit", "title": "Governor of Samburu", "regionId": "county:ke:sam", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:tra:governor:natembeya", "name": "George Natembeya", "title": "Governor of Trans Nzoia", "regionId": "county:ke:tra", "partyName": "Democratic Action Party", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:uas:governor:bii", "name": "Jonathan Bii", "title": "Governor of Uasin Gishu", "regionId": "county:ke:uas", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:ela:governor:rotich", "name": "Wesley Rotich", "title": "Governor of Elgeyo-Marakwet", "regionId": "county:ke:ela", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:nan:governor:sang", "name": "Stephen Sang", "title": "Governor of Nandi", "regionId": "county:ke:nan", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:bar:governor:cheboi", "name": "Benjamin Cheboi", "title": "Governor of Baringo", "regionId": "county:ke:bar", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:lai:governor:irungu", "name": "Joshua Irungu", "title": "Governor of Laikipia", "regionId": "county:ke:lai", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:nak:governor:kihika", "name": "Susan Kihika", "title": "Governor of Nakuru", "regionId": "county:ke:nak", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:nar:governor:ntutu", "name": "Patrick Ntutu", "title": "Governor of Narok", "regionId": "county:ke:nar", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:kaj:governor:lenku", "name": "Joseph Jama Ole Lenku", "title": "Governor of Kajiado", "regionId": "county:ke:kaj", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:kak2:governor:mutai", "name": "Erick Kipkoech Mutai", "title": "Governor of Kericho", "regionId": "county:ke:kak2", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:bom:governor:barchok", "name": "Hillary Barchok", "title": "Governor of Bomet", "regionId": "county:ke:bom", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:kak:governor:barasa", "name": "Fernandes Odinga Barasa", "title": "Governor of Kakamega", "regionId": "county:ke:kak", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:vig:governor:ottichilo", "name": "Wilber Khasilwa Ottichilo", "title": "Governor of Vihiga", "regionId": "county:ke:vig", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:bun:governor:lusaka", "name": "Kenneth Lusaka", "title": "Governor of Bungoma", "regionId": "county:ke:bun", "partyName": "Ford Kenya", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:bus:governor:otuoma", "name": "Paul Otuoma", "title": "Governor of Busia", "regionId": "county:ke:bus", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:sia:governor:orengo", "name": "James Orengo", "title": "Governor of Siaya", "regionId": "county:ke:sia", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:kisu:governor:nyongo", "name": "Peter Anyang' Nyong'o", "title": "Governor of Kisumu", "regionId": "county:ke:kisu", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:hom:governor:wanga", "name": "Gladys Wanga", "title": "Governor of Homa Bay", "regionId": "county:ke:hom", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:mig:governor:ayacko", "name": "Ochilo Ayacko", "title": "Governor of Migori", "regionId": "county:ke:mig", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:kis:governor:arati", "name": "Simba Arati", "title": "Governor of Kisii", "regionId": "county:ke:kis", "partyName": "Orange Democratic Movement", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:nya:governor:nyaribo", "name": "Amos Kimwomi Nyaribo", "title": "Governor of Nyamira", "regionId": "county:ke:nya", "partyName": "United Progressive Alliance", "startDate": "2022-08-25", "endDate": None},
    {"personId": "person:ke:nai:governor:sakaja", "name": "Sakaja Arthur Johnson", "title": "Governor of Nairobi", "regionId": "county:ke:nai", "partyName": "United Democratic Alliance", "startDate": "2022-08-25", "endDate": None}
]

# Add all governors
data['officeholders'].extend(kenyan_governors)

print(f"✅ Added {len(kenyan_governors)} Kenyan county governors")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
