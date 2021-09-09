import requests

response = requests.get('https://reqres.in/api/users?page=2').json()
# a = response.text
print(response["name"])
