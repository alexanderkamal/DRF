import requests

endpoint = "http://localhost:8000/api/products/mixin/"

get_response = requests.put(endpoint) # Making a GET request to the endpoint (HTTP request)
print(get_response.json()) # Print the response as JSON (HTTP response) 