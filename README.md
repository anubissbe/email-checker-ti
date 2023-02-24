<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Have I Been Pwned Email Checker</title>
  </head>
  <body>
    <h1>Have I Been Pwned Email Checker</h1>
less
Copy code
<p>This script checks if a list of email addresses have been breached using the Have I Been Pwned API. For each email address in the list, the script sends a request to the Have I Been Pwned API to check if it has been breached. If the email address has been breached, the script adds the breach data to a dictionary, which is then dumped to a JSON file.</p>

<h2>Prerequisites</h2>

<p>Before running the script, you will need:</p>

<ul>
  <li>Python 3.x installed on your machine</li>
  <li>A Have I Been Pwned API key, which can be obtained from the <a href="https://haveibeenpwned.com/API/Key">Have I Been Pwned website</a></li>
</ul>

<h2>Usage</h2>

<ol>
  <li>Save a list of email addresses to a file called <code>emails.txt</code>, with each email address on a separate line.</li>
  <li>Open the script file in a text editor and replace <code>your_api_key_here</code> with your actual Have I Been Pwned API key.</li>
  <li>Save the changes to the script file.</li>
  <li>Open a terminal or command prompt and navigate to the directory where the script file is located.</li>
  <li>Run the script using the following command:<br><code>python3 email-checker-ti.py</code><br>Replace <code>email-checker-ti.py</code> with the name of the script file.</li>
  <li>The script will run and output the results to a file called <code>breaches.json</code>.</li>
</ol>

<h2>Output</h2>

<p>The script outputs a JSON file called <code>breaches.json</code>, which contains the breach data for each email address in the <code>emails.txt</code> file. The JSON file has the following structure:</p>

<pre><code>{
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
}</code></pre>

css
Copy code
<p>The <code>pwned</code> field indicates whether the email address has been breache
