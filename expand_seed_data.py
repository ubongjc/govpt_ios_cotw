#!/usr/bin/env python3
import json
from datetime import datetime

# Read the North America data
with open('GPT/Resources/seed_data_north_america.json', 'r') as f:
    data = json.load(f)

# Add remaining US state governors (as of 2024)
additional_governors = [
    {
        "personId": "person:us:al:governor:ivey",
        "name": "Kay Ivey",
        "title": "Governor of Alabama",
        "regionId": "state:us:al",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2017-04-10T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.alabama.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:ak:governor:dunleavy",
        "name": "Mike Dunleavy",
        "title": "Governor of Alaska",
        "regionId": "state:us:ak",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2018-12-03T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://gov.alaska.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:az:governor:hobbs",
        "name": "Katie Hobbs",
        "title": "Governor of Arizona",
        "regionId": "state:us:az",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2023-01-02T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://azgovernor.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:ar:governor:sanders",
        "name": "Sarah Huckabee Sanders",
        "title": "Governor of Arkansas",
        "regionId": "state:us:ar",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2023-01-10T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.arkansas.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:co:governor:polis",
        "name": "Jared Polis",
        "title": "Governor of Colorado",
        "regionId": "state:us:co",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2019-01-08T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.colorado.gov/governor",
        "photoURL": None
    },
    {
        "personId": "person:us:ct:governor:lamont",
        "name": "Ned Lamont",
        "title": "Governor of Connecticut",
        "regionId": "state:us:ct",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2019-01-09T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://portal.ct.gov/governor",
        "photoURL": None
    },
    {
        "personId": "person:us:de:governor:carney",
        "name": "John Carney",
        "title": "Governor of Delaware",
        "regionId": "state:us:de",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2017-01-17T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.delaware.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:hi:governor:green",
        "name": "Josh Green",
        "title": "Governor of Hawaii",
        "regionId": "state:us:hi",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2022-12-05T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.hawaii.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:id:governor:little",
        "name": "Brad Little",
        "title": "Governor of Idaho",
        "regionId": "state:us:id",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2019-01-07T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://gov.idaho.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:in:governor:holcomb",
        "name": "Eric Holcomb",
        "title": "Governor of Indiana",
        "regionId": "state:us:in",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2017-01-09T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.in.gov/gov",
        "photoURL": None
    },
    {
        "personId": "person:us:ia:governor:reynolds",
        "name": "Kim Reynolds",
        "title": "Governor of Iowa",
        "regionId": "state:us:ia",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2017-05-24T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.iowa.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:ks:governor:kelly",
        "name": "Laura Kelly",
        "title": "Governor of Kansas",
        "regionId": "state:us:ks",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2019-01-14T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.kansas.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:ky:governor:beshear",
        "name": "Andy Beshear",
        "title": "Governor of Kentucky",
        "regionId": "state:us:ky",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2019-12-10T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.ky.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:la:governor:landry",
        "name": "Jeff Landry",
        "title": "Governor of Louisiana",
        "regionId": "state:us:la",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2024-01-08T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://gov.louisiana.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:me:governor:mills",
        "name": "Janet Mills",
        "title": "Governor of Maine",
        "regionId": "state:us:me",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2019-01-02T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.maine.gov/governor",
        "photoURL": None
    },
    {
        "personId": "person:us:md:governor:moore",
        "name": "Wes Moore",
        "title": "Governor of Maryland",
        "regionId": "state:us:md",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2023-01-18T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.maryland.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:ma:governor:healey",
        "name": "Maura Healey",
        "title": "Governor of Massachusetts",
        "regionId": "state:us:ma",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2023-01-05T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.mass.gov/governor",
        "photoURL": None
    },
    {
        "personId": "person:us:mn:governor:walz",
        "name": "Tim Walz",
        "title": "Governor of Minnesota",
        "regionId": "state:us:mn",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2019-01-07T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://mn.gov/governor",
        "photoURL": None
    },
    {
        "personId": "person:us:ms:governor:reeves",
        "name": "Tate Reeves",
        "title": "Governor of Mississippi",
        "regionId": "state:us:ms",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2020-01-14T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governorreeves.ms.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:mo:governor:parson",
        "name": "Mike Parson",
        "title": "Governor of Missouri",
        "regionId": "state:us:mo",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2018-06-01T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.mo.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:mt:governor:gianforte",
        "name": "Greg Gianforte",
        "title": "Governor of Montana",
        "regionId": "state:us:mt",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2021-01-04T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.mt.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:ne:governor:pillen",
        "name": "Jim Pillen",
        "title": "Governor of Nebraska",
        "regionId": "state:us:ne",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2023-01-05T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.nebraska.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:nv:governor:lombardo",
        "name": "Joe Lombardo",
        "title": "Governor of Nevada",
        "regionId": "state:us:nv",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2023-01-02T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://gov.nv.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:nh:governor:sununu",
        "name": "Chris Sununu",
        "title": "Governor of New Hampshire",
        "regionId": "state:us:nh",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2017-01-05T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.governor.nh.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:nj:governor:murphy",
        "name": "Phil Murphy",
        "title": "Governor of New Jersey",
        "regionId": "state:us:nj",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2018-01-16T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://nj.gov/governor",
        "photoURL": None
    },
    {
        "personId": "person:us:nm:governor:grisham",
        "name": "Michelle Lujan Grisham",
        "title": "Governor of New Mexico",
        "regionId": "state:us:nm",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2019-01-01T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.governor.state.nm.us",
        "photoURL": None
    },
    {
        "personId": "person:us:nd:governor:burgum",
        "name": "Doug Burgum",
        "title": "Governor of North Dakota",
        "regionId": "state:us:nd",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2016-12-15T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.nd.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:ok:governor:stitt",
        "name": "Kevin Stitt",
        "title": "Governor of Oklahoma",
        "regionId": "state:us:ok",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2019-01-14T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.ok.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:or:governor:kotek",
        "name": "Tina Kotek",
        "title": "Governor of Oregon",
        "regionId": "state:us:or",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2023-01-09T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.oregon.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:ri:governor:mckee",
        "name": "Dan McKee",
        "title": "Governor of Rhode Island",
        "regionId": "state:us:ri",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2021-03-02T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.ri.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:sc:governor:mcmaster",
        "name": "Henry McMaster",
        "title": "Governor of South Carolina",
        "regionId": "state:us:sc",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2017-01-24T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.sc.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:sd:governor:noem",
        "name": "Kristi Noem",
        "title": "Governor of South Dakota",
        "regionId": "state:us:sd",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2019-01-05T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.sd.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:tn:governor:lee",
        "name": "Bill Lee",
        "title": "Governor of Tennessee",
        "regionId": "state:us:tn",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2019-01-19T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.tn.gov/governor",
        "photoURL": None
    },
    {
        "personId": "person:us:ut:governor:cox",
        "name": "Spencer Cox",
        "title": "Governor of Utah",
        "regionId": "state:us:ut",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2021-01-04T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.utah.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:vt:governor:scott",
        "name": "Phil Scott",
        "title": "Governor of Vermont",
        "regionId": "state:us:vt",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2017-01-05T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.vermont.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:va:governor:youngkin",
        "name": "Glenn Youngkin",
        "title": "Governor of Virginia",
        "regionId": "state:us:va",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2022-01-15T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.governor.virginia.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:wa:governor:inslee",
        "name": "Jay Inslee",
        "title": "Governor of Washington",
        "regionId": "state:us:wa",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2013-01-16T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.governor.wa.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:wv:governor:justice",
        "name": "Jim Justice",
        "title": "Governor of West Virginia",
        "regionId": "state:us:wv",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2017-01-16T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.wv.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:wi:governor:evers",
        "name": "Tony Evers",
        "title": "Governor of Wisconsin",
        "regionId": "state:us:wi",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2019-01-07T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://evers.wi.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:wy:governor:gordon",
        "name": "Mark Gordon",
        "title": "Governor of Wyoming",
        "regionId": "state:us:wy",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2019-01-07T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://governor.wyo.gov",
        "photoURL": None
    }
]

# Add more city mayors
additional_mayors = [
    {
        "personId": "person:us:hou:mayor:whitmire",
        "name": "John Whitmire",
        "title": "Mayor of Houston",
        "regionId": "city:us:hou",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2024-01-02T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.houstontx.gov/mayor",
        "photoURL": None
    },
    {
        "personId": "person:us:phx:mayor:gallego",
        "name": "Kate Gallego",
        "title": "Mayor of Phoenix",
        "regionId": "city:us:phx",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2019-03-21T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.phoenix.gov/mayor",
        "photoURL": None
    },
    {
        "personId": "person:us:phi:mayor:parker",
        "name": "Cherelle Parker",
        "title": "Mayor of Philadelphia",
        "regionId": "city:us:phi",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2024-01-02T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.phila.gov/the-mayor",
        "photoURL": None
    },
    {
        "personId": "person:us:sf:mayor:breed",
        "name": "London Breed",
        "title": "Mayor of San Francisco",
        "regionId": "city:us:sf",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2018-07-11T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://sfmayor.org",
        "photoURL": None
    },
    {
        "personId": "person:us:sea:mayor:harrell",
        "name": "Bruce Harrell",
        "title": "Mayor of Seattle",
        "regionId": "city:us:sea",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2022-01-01T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.seattle.gov/mayor",
        "photoURL": None
    },
    {
        "personId": "person:us:bos:mayor:wu",
        "name": "Michelle Wu",
        "title": "Mayor of Boston",
        "regionId": "city:us:bos",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2021-11-16T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.boston.gov/mayor",
        "photoURL": None
    },
    {
        "personId": "person:us:dc:mayor:bowser",
        "name": "Muriel Bowser",
        "title": "Mayor of Washington D.C.",
        "regionId": "city:us:dc",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2015-01-02T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://mayor.dc.gov",
        "photoURL": None
    },
    {
        "personId": "person:us:mia:mayor:suarez",
        "name": "Francis Suarez",
        "title": "Mayor of Miami",
        "regionId": "city:us:mia",
        "partyName": "Republican Party",
        "partyURL": "https://gop.com",
        "startDate": "2017-11-13T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.miamigov.com/Government/Mayor",
        "photoURL": None
    },
    {
        "personId": "person:us:atl:mayor:dickens",
        "name": "Andre Dickens",
        "title": "Mayor of Atlanta",
        "regionId": "city:us:atl",
        "partyName": "Democratic Party",
        "partyURL": "https://democrats.org",
        "startDate": "2022-01-03T00:00:00Z",
        "endDate": None,
        "officialSiteURL": "https://www.atlantaga.gov/government/mayor",
        "photoURL": None
    },
    {
        "personId": "person:mx:mex:mayor:sheinbaum",
        "name": "Claudia Sheinbaum",
        "title": "Mayor of Mexico City",
        "regionId": "city:mx:mex",
        "partyName": "MORENA",
        "partyURL": "https://morena.org",
        "startDate": "2018-12-05T00:00:00Z",
        "endDate": "2023-06-16T00:00:00Z",
        "officialSiteURL": "https://www.cdmx.gob.mx",
        "photoURL": None
    }
]

# Add the additional officeholders
data['officeholders'].extend(additional_governors)
data['officeholders'].extend(additional_mayors)

# Add some more promises for variety
additional_promises = [
    {
        "promiseId": "promise:desantis:education:2023",
        "personId": "person:us:fl:governor:desantis",
        "regionId": "state:us:fl",
        "dateMade": "2023-05-01T00:00:00Z",
        "context": "Education reform announcement",
        "quoteExact": "We will raise teacher starting salaries to $65,000 and expand school choice programs statewide.",
        "summary": "Increase teacher pay and expand school choice",
        "tagsJSON": "[\"education\", \"teachers\", \"school_choice\"]",
        "dueBy": "2025-01-01T00:00:00Z",
        "sourcePrimary": "https://www.flgov.com/2023/05/01/education-reform",
        "sourceType": "official_statement",
        "policyTagsJSON": "[\"education\", \"teacher_compensation\"]",
        "effectInputsJSON": None
    },
    {
        "promiseId": "promise:whitmer:infrastructure:2023",
        "personId": "person:us:mi:governor:whitmer",
        "regionId": "state:us:mi",
        "dateMade": "2023-02-20T00:00:00Z",
        "context": "State infrastructure plan",
        "quoteExact": "We will fix 100 bridges and repair 2,000 miles of roads by 2025.",
        "summary": "Major road and bridge repair initiative",
        "tagsJSON": "[\"infrastructure\", \"transportation\", \"roads\"]",
        "dueBy": "2025-12-31T00:00:00Z",
        "sourcePrimary": "https://www.michigan.gov/governor/infrastructure",
        "sourceType": "gov_release",
        "policyTagsJSON": "[\"infrastructure\", \"transportation\"]",
        "effectInputsJSON": None
    },
    {
        "personId": "person:ca:qc:premier:legault",
        "promiseId": "promise:legault:language:2023",
        "regionId": "province:ca:qc",
        "dateMade": "2023-03-15T00:00:00Z",
        "context": "French language protection announcement",
        "quoteExact": "We will strengthen Bill 96 and ensure French remains the primary language of business and education in Quebec.",
        "summary": "Strengthen French language protection laws",
        "tagsJSON": "[\"language\", \"culture\", \"education\"]",
        "dueBy": "2024-12-31T00:00:00Z",
        "sourcePrimary": "https://www.quebec.ca/premier-ministre/language",
        "sourceType": "official_statement",
        "policyTagsJSON": "[\"language_policy\", \"cultural_preservation\"]",
        "effectInputsJSON": None
    },
    {
        "promiseId": "promise:amlo:poverty:2023",
        "personId": "person:mx:president:amlo",
        "regionId": "country:mx",
        "dateMade": "2023-01-01T00:00:00Z",
        "context": "New Year's address on poverty reduction",
        "quoteExact": "We will lift 5 million more Mexicans out of poverty through expanded social programs.",
        "summary": "Expand social programs to reduce poverty",
        "tagsJSON": "[\"poverty\", \"social_programs\", \"welfare\"]",
        "dueBy": "2024-12-01T00:00:00Z",
        "sourcePrimary": "https://www.gob.mx/presidencia/poverty-reduction",
        "sourceType": "official_statement",
        "policyTagsJSON": "[\"poverty_reduction\", \"social_welfare\"]",
        "effectInputsJSON": None
    }
]

data['promises'].extend(additional_promises)

# Sort all arrays for better organization
data['regions'].sort(key=lambda x: (x['type'], x['name']))
data['officeholders'].sort(key=lambda x: x['name'])
data['promises'].sort(key=lambda x: x['dateMade'])

# Count statistics
print(f"Total regions: {len(data['regions'])}")
print(f"  - Countries: {len([r for r in data['regions'] if r['type'] == 'country'])}")
print(f"  - States/Provinces: {len([r for r in data['regions'] if r['type'] in ['state', 'province']])}")
print(f"  - Cities: {len([r for r in data['regions'] if r['type'] == 'city'])}")
print(f"Total officeholders: {len(data['officeholders'])}")
print(f"Total promises: {len(data['promises'])}")

# Save the complete dataset
with open('GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print("\nSeed data has been updated with comprehensive North American data!")
print("The file has been saved to GPT/Resources/seed_data.json")