ID Generator Microservice


Description: This microservice generates a unique ID for entries based on a provided date and title.

It ensures:

• IDs are generated consistently from the same inputs
• spaces in titles are replaced with underscores
• uppercase letters are converted to lowercase
• special characters are removed from titles

The microservice communicates using text files JSON formatted, not direct function calls:

Request file: pipe/id_request.txt
Response file: pipe/id_response.txt

How to REQUEST an ID
1)Open: pipe/id_request.txt
2)Write a JSON object and save the file.

Request format:

{
 "action": "generate",
 "date": "3/11/26",
 "title": "Morning Run"
}

Example request:

{
 "action": "generate",
 "date": "3/11/26",
 "title": "Morning Run"
}

How to RECEIVE the generated ID:
1)The microservice writes a JSON response to: pipe/id_response.txt

Response format:

{
 "ok": true,
 "id": "31126morning_run"
}

Example invalid request response:

{
 "ok": false,
 "error": "missing_fields"
}

How to run:

1)Clone the repository.
2)Make sure you are in the repository root folder (do not run inside /src, /tests, or /pipe).
3)Start the microservice

Linux / Mac: python3 src/microservice7.py
Windows: python src\microservice7.py

Output should look similar to:

ID Generator Microservice running...
Request file: pipe\id_request.txt
Response file: pipe\id_response.txt

4)Run the test client
5)Open a second terminal and run:

Linux / Mac: python3 tests/test_client.py
Windows: python tests\test_client.py

Output should look similar to:

Generated ID -> {'ok': True, 'id': '31126morning_run'}

Important Notes for Windows: 

• Use \ in file paths
• Make sure you are running commands from the project root folder
• If python does not work, try:

py src\microservice7.py
py tests\test_client.py
