import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"product_id": 123})

# print(get_response.headers)
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())