from faker import Faker
import pandas as pd
import random

fake = Faker()
leads=[]

for _ in range(25):
    # Biased Dataset
    # 70% to US industries, 30% globaly

    if random.random() < 0.7:
        industry = "Information Technology"
        city, state = fake.city(), fake.state_abbr()
    else:
        industry = fake.job()
        city, state = fake.city(), fake.state_abbr()


    company_name = fake.company()
    actions = random.choice(['New', 'Contacted', 'Qualified', 'Unqualified'])
    product_category = random.choice(['Consulting', 'Investment Banking', 'Software', 'Hardware', 'Services'])
    business_type = random.choice(['B2B', 'B2B2C'])
    employees = random.randint(5,5000)
    revenue =  f'${random.randint(1,5000)}M'
    year_founded = random.randint(1975, 2025)
    bbb_rating = random.choice(['A+', 'A', 'B', 'C', 'NR'])
    street = fake.street_address()
    phone = fake.phone_number()
    email = fake.email()
    source = random.choice(['LinkedIn', 'CrunchBase', 'Apollo', 'Growjo'])
    created_date = fake.date_between(start_date = '-2y', end_date = 'today')
    updated_date = fake.date_between(start_date = created_date, end_date = 'today')
    

    lead = {
        "Company" : company_name,
        'Actions' :actions,
        'Industry' : industry,
        'Links' : f'https://{fake.domain_name()}',
        'Product/Service Category' : product_category,
        'Business Type' : business_type,
        "Employees count" : employees,
        'Revenue' : revenue,
        'Year Founded' : year_founded,
        'BBB Rating' : bbb_rating,
        'Street': street,
        'City' : city,
        'State' : state,
        'Company Phone': phone,
        'Company Email' : email,
        'Source' : source,
        'Created Date' : created_date,
        'Updated' : updated_date
    }
    leads.append(lead)

    leads.append({
        "Company" : 'XYZ Comapany',
        'Actions' :'New',
        'Industry' : 'Invalid industry',
        'Links' : 'http://xyzlink',
        'Product/Service Category' : 'Soap',
        'Business Type' : 'B2B',
        "Employees count" : -1,
        'Revenue' : 'NA',
        'Year Founded' : 1800,
        'BBB Rating' : 'NR',
        'Street': "",
        'City' : 'Nomad',
        'State' : 'Dumpling',
        'Company Phone': 00000,
        'Company Email' : 'xyz@email',
        'Source' : 'Unknown',
        'Created Date' : fake.date_between(start_date = '-3y', end_date = '-2y'),
        'Updated' : fake.date_between(start_date = '-2y', end_date = '-1y')
    })

    df = pd.DataFrame(leads)
    df.to_csv('sample_data.csv', index=False)