import requests

endpoint = "http://localhost:8000/api/products/list_create/"
data = {
    "title": "List Create Product",
    "price": 39.99
}
# post_response = requests.post(endpoint, json=data) # Making a POST request to the endpoint (HTTP request)
# print(post_response.json()) # Print the response as JSON (HTTP response)

get_response = requests.get(endpoint) # Making a GET request to the endpoint (HTTP request)
print(get_response.json()) # Print the response as JSON (HTTP response) 