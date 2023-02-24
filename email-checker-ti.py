import requests
import json
import time

# Load list of emails from emails.txt
with open('emails.txt', 'r') as f:
    emails = [line.strip() for line in f]

# Set API key
api_key = 'your-api-key'


# Send request to Have I Been Pwned API for each email
breaches = {}
for email in emails:
    url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}'
    headers = {
        'User-Agent': 'My Python script',
        'hibp-api-key': api_key
    }
    params = {
        'truncateResponse': 'false'
    }
    response = requests.get(url, headers=headers, params=params, verify=True)

    # If the email has been breached, add breach data to dictionary and set pwned flag to True
    if response.status_code == 200:
        data = response.json()
        for breach in data:
            name = breach['Name']
            date = breach.get('BreachDate', None) or breach.get('AddedDate', None)
            modified_date = breach.get('ModifiedDate', None)
            description = breach.get('Description', None)
            if email not in breaches:
                breaches[email] = {'pwned': True, 'breaches': []}
            breaches[email]['breaches'].append({'name': name, 'date': date, 'modified_date': modified_date, 'description': description})
    # If the email has not been breached, set pwned flag to False
    elif response.status_code == 404:
        if email not in breaches:
            breaches[email] = {'pwned': False, 'breaches': []}

    # Wait for 2 seconds before making the next request
    time.sleep(2)

# Dump breaches data to JSON file
with open('breaches.json', 'w') as f:
    json.dump(breaches, f, indent=4)
