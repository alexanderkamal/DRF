import requests
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ") # getpass is used to securely input the password without echoing it on the console
auth = {
    "username": username,
    "password": password
}
endpoint = "http://localhost:8000/api/auth/"
auth_response = requests.post(endpoint, json=auth) # Making a POST request to the endpoint (HTTP request)
print(auth_response.json()) # Print the response as JSON (HTTP response)
token = auth_response.json().get("token")
print("Token:", token)
endpoint = "http://localhost:8000/api/products/list_create/"
headers = {
    "Authorization": f"Token {token}"
}
get_response = requests.get(endpoint, headers=headers) # Making a GET request to the endpoint (HTTP request)
print(get_response.json()) # Print the response as JSON (HTTP response)