import requests

endpoint = "http://localhost:8000/api/products/4/"
get_response = requests.get(endpoint) # Making a GET request to the endpoint (HTTP request)
print(get_response.json()) # Print the response as JSON (HTTP response)