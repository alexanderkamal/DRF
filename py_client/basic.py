import requests

# endpoint1 = "https://httpbin.org" 
# get_response = requests.get(endpoint1) # Making a GET request to the endpoint (HTTP request)

# endpoint2 = "https://httpbin.org/anything" # Another endpoint that receives any type of request and echoes back the details

# get_response2_1 = requests.get(endpoint2) # Making a GET request without parameters

# get_response2_2 = requests.get(endpoint2, params={"abc": 123}, headers={"custom-header": "hello world"}) # Making a GET request with parameters and custom headers
# get_response2_2 = requests.get(endpoint2, json={"name": "Alexander"}) # Making a GET request with a JSON body
# print(get_response2_2.text) # Print the response text (HTTP response)
# print(get_response2_2.json()) # Print the response as JSON (HTTP response)

# get_response2_3 = requests.get(endpoint2,json={"name":"Alexander"}) # Making a GET request with a JSON body
# print(get_response2_3.json()) # Print the response text (HTTP response)


# endpoint = "http://localhost:8000/api/test/" #localhost = 127.0.0.1
# get_response = requests.get(endpoint,params= {"abc": 123, "def": 456}, json={"query":"Hello World"}) # Making a GET request to the endpoint (HTTP request)
# print(get_response.json()) # Print the response as JSON (HTTP response)
# print(get_response.status_code) # Print the status code of the response


# endpoint = "http://localhost:8000/api/" #localhost = 127.0.0.1
# get_response = requests.get(endpoint) # Making a GET request to the endpoint (HTTP request)
# print(get_response.json()) # Print the response as JSON (HTTP response)

# endpoint = "http://localhost:8000/api/drf_get/" #localhost = 127.0.0.1
# get_response = requests.get(endpoint) # Making a GET request to the endpoint (HTTP request)
# print(get_response.json()) # Print the response as JSON (HTTP response)

endpoint = "http://localhost:8000/api/drf_post/" #localhost = 127.0.0.1
post_response = requests.post(endpoint, json={"title": "xzzxx", "price": 19.99}) # Making a POST request to the endpoint (HTTP request)
print(post_response.json()) # Print the response as JSON (HTTP response)