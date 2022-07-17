import requests

endpoint = "http://localhost:8000/api/products/1p/"

get_response = requests.get(endpoint)

print(get_response.json())