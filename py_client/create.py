import requests

data = {
    "title": "New Product",
    "price": 29.99
}
endpoint = "http://localhost:8000/api/products/create/"
post_response = requests.post(endpoint, json=data) # Making a POST request to the endpoint (HTTP request)
print(post_response.json()) # Print the response as JSON (HTTP response)