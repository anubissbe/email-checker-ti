<html>
  <head>
  </head>
  <body>
    <h1>Documentation for Have I Been Pwned API Checker</h1>
    <p>This script uses the Have I Been Pwned API to check if any email addresses in a given file have been involved in a data breach. It then outputs the results to a JSON file.</p>
    <h2>Dependencies</h2>
    <ul>
      <li>Python 3.x</li>
      <li>requests library (can be installed using pip)</li>
      <li>termcolor library (can be installed using pip)</li>
    </ul>
    <h2>Usage</h2>
    <p>The script takes two command-line arguments:</p>
    <ul>
      <li>The path to the input file containing email addresses to check, one per line.</li>
      <li>The path to the output file for the JSON results.</li>
    </ul>
    <p>Example usage:</p>
    <pre><code>python3 email-checker-ti.py </code></pre>
    <h2>Output Format</h2>
    <p>The JSON output file contains an array of objects, each representing a breached email address. Each object has the following properties:</p>
    <ul>
      <li><code>email</code>: The email address that was breached.</li>
      <li><code>pwned</code>: A boolean indicating whether the email address was involved in a breach.</li>
      <li><code>breaches</code>: An array of objects, each representing a breach that the email address was involved in (if any). Each breach object has the following properties:</li>
      <ul>
        <li><code>name</code>: The name of the breached website or service.</li>
        <li><code>domain</code>: The domain of the breached website or service.</li>
        <li><code>date</code>: The date the breach occurred.</li>
        <li><code>modified_date</code>: The date the breach was last modified.</li>
        <li><code>description</code>: A brief description of the breach.</li>
      </ul>
    </ul>
    <p>If an email address was not involved in any breaches, the <code>breaches</code> property will be an empty array.</p>
  </body>
</html>


