<!DOCTYPE html>
<html>
<head>


</head>
<body>
	<header>
		<h1>Email Checker TI Documentation</h1>
	</header>
	<main>
		<h2>Overview</h2>
		<p>Email Checker TI is a Python script that uses the Have I Been Pwned API to check if email addresses have been compromised in a data breach. It reads a list of email addresses from a text file, checks each address against the Have I Been Pwned API, and outputs the results to a JSON file. The script also includes the option to convert the JSON file to a CSV file.</p>
less
Copy code
	<h2>Installation</h2>
	<p>To use the Email Checker TI script, you need to have Python 3 and the requests and termcolor libraries installed.</p>
	<ol>
		<li>Clone the Email Checker TI repository to your local machine:</li>
		<code>git clone https://github.com/threatintel-be/email-checker-ti.git</code>
		<li>Install the required libraries by running the following command:</li>
		<code>pip install -r requirements.txt</code>
		<li>Copy or move the emails.txt file containing the list of email addresses to be checked into the email-checker-ti directory.</li>
		<li>Run the script using the following command:</li>
		<code>python email_checker_ti.py</code>
	</ol>

<h2>Usage</h2>
	<p>The Email Checker TI script can be run from the command line. The default behavior is to check each email address in the emails.txt file against the Have I Been Pwned API and output the results to a JSON file named breaches.json.</p>
	<p>You can also convert the JSON file to a CSV file by running the convert.py script.


