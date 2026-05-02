import requests

endpoint = "http://localhost:8000/api/products/delete/33/"
get_response = requests.delete(endpoint) # Making a DELETE request to the endpoint (HTTP request)
print(get_response) # Print the response as JSON (HTTP response)