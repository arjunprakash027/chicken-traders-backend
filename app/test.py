import requests

# Define the endpoint URL and the sentence to be sent
endpoint = 'http://127.0.0.1:5001/getall'

# Encode the sentence as a URL parameter
url_param = {"item":"broiler","date":"2020-01-01","weight":"1","transtype":"sale","remark":"test"}

# Send the request to the API endpoint with the URL parameter
response = requests.get(endpoint, params=url_param)

# Print the response from the API
print(response.text)