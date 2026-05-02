import requests

endpoint = "http://localhost:8000/api/products/alt_view/"
# endpoint = "http://localhost:8000/api/products/alt_view/"
get_response = requests.get(endpoint) # Making a GET request to the endpoint (HTTP request)
print(get_response.json()) # Print the response as JSON (HTTP response)
# endpoint = "http://localhost:8000/api/products/alt_view/2/"
# post_response = requests.post(endpoint, json={"title": "Updated Product", "price": 423.99}) # Making a POST request to the endpoint (HTTP request)
# print(post_response.json()) # Print the response as JSON (HTTP response) 