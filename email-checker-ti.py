import requests
import json
import csv
import time
from termcolor import colored

# API endpoint and headers
api_url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'
api_headers = {
    'User-Agent': 'Python script',
    'hibp-api-key': 'YOUR_API_KEY_HERE'
}

# Read email addresses from file
with open('emails.txt', 'r') as f:
    emails = f.read().splitlines()

# Process each email address
breaches = []
for email in emails:
    # Make API request
    response = requests.get(api_url + email, headers=api_headers, params={'truncateResponse': 'false'}, verify=True)

    # Handle API response
    if response.status_code == 200:
        # Email address has been breached
        for breach in response.json():
            breaches.append({
                'email': email,
                'name': breach['Name'],
                'domain': breach['Domain'],
                'date': breach['BreachDate'],
                'added_date': breach['AddedDate'],
                'modified_date': breach['ModifiedDate'],
                'description': breach['Description']
            })
            print(colored(f'{email} has been breached in {breach["Name"]} on {breach["BreachDate"]}', 'red'))
    elif response.status_code == 404:
        # Email address has not been breached
        breaches.append({
            'email': email,
            'name': 'N/A',
            'domain': 'N/A',
            'date': 'N/A',
            'added_date': 'N/A',
            'modified_date': 'N/A',
            'description': 'N/A'
        })
        print(colored(f'{email} has not been breached', 'green'))
    else:
        # Something went wrong with the API request
        print(colored(f'Error: {response.status_code}', 'yellow'))

    # Sleep for 7 seconds to avoid rate limiting
    time.sleep(7)

# Write breaches to JSON file
with open('breaches.json', 'w') as f:
    json.dump({'breaches': breaches}, f)

# Write breaches to CSV file
with open('breaches.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['email', 'name', 'domain', 'date', 'added_date', 'modified_date', 'description']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for breach in breaches:
        writer.writerow(breach)

