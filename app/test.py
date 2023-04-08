import requests
import json

# Define the endpoint URL and the sentence to be sent
endpoint = 'http://127.0.0.1:5001/update'

# Encode the sentence as a URL parameter
url_param = {"item":"test","date":"2020-01-01","weight":"1","transtype":'purchase',"remark":"test"}

# Send the request to the API endpoint with the URL parameter
response = requests.get(endpoint, params=url_param)

# Print the response from the API
print(json.loads(response.text))