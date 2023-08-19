import requests
import json
from flask import jsonify

# The URL of your flask application's webhook receiver
url = 'http://localhost:5000/webhookcallback'

# The data to be sent

body = {}

headers = {
    'Content-Type': 'application/json',
    'id': '123'
}

# Send the POST request and STORE IT under a variable
response = requests.post(url, data=json.dumps(body), headers=headers)

# Print the response status code (should be 200 if the request was successful)
print(response.status_code)