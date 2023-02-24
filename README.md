# email-checker-ti
Description
This script checks if a list of email addresses have been breached using the Have I Been Pwned API. For each email address in the list, the script sends a request to the Have I Been Pwned API to check if it has been breached. If the email address has been breached, the script adds the breach data to a dictionary, which is then dumped to a JSON file.

Prerequisites
Before running the script, you will need:

Python 3.x installed on your machine
A Have I Been Pwned API key, which can be obtained from the Have I Been Pwned website
Usage
Save a list of email addresses to a file called emails.txt, with each email address on a separate line.

Open the script file in a text editor and replace your_api_key_here with your actual Have I Been Pwned API key.

Save the changes to the script file.

Open a terminal or command prompt and navigate to the directory where the script file is located.

Run the script using the following command:

Copy code
python3 script_name.py
Replace script_name.py with the name of the script file.

The script will run and output the results to a file called breaches.json.

Output
The script outputs a JSON file called breaches.json, which contains the breach data for each email address in the emails.txt file. The JSON file has the following structure:

json
Copy code
{
    "email1@example.com": {
        "pwned": true,
        "breaches": [
            {
                "name": "Breach Name",
                "date": "2020-01-01T00:00:00Z",
                "modified_date": "2020-01-01T00:00:00Z",
                "description": "Breach description"
            },
            {
                "name": "Another Breach",
                "date": "2019-01-01T00:00:00Z",
                "modified_date": null,
                "description": "Another breach description"
            }
        ]
    },
    "email2@example.com": {
        "pwned": false,
        "breaches": []
    }
}
The pwned field indicates whether the email address has been breached (true) or not (false). The breaches field is an array of breach objects, which contain the name, date, modified date, and description of each breach. If the email address has not been breached, the breaches field is an empty array. If data is not available for a particular field, it will be null in the JSON output.

Additional Information
The script uses a rate limiting mechanism to prevent overloading the Have I Been Pwned API. After each request, the script waits for 2 seconds before making the next request. This ensures that the API is not overloaded and prevents the script from being blocked by the API.

The script also includes parameters to disable truncation of the API response and to enable SSL verification. These parameters ensure that we get the full response for each email and that the SSL certificate is verified before making the request.

Finally, the script handles errors gracefully. If the API returns an error, the script will skip that email and move on to the next one. If data is not available for a particular breach field, it will be set to None in the JSON output.
