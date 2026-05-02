import requests

endpoint = "http://localhost:8000/api/products/update/1/"
data = {
    "title": "spiderman",
    "price": 123.99
}
get_response = requests.put(endpoint, json=data) # Making a PUT request to the endpoint (HTTP request)
print(get_response.json()) # Print the response as JSON (HTTP response)