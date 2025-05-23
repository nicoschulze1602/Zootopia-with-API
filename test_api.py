import requests

name = 'Fox'
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'iWcJikrDu06TpQsTIkhWfA==A2V9t0BMUCugf7Yh'})
if response.status_code == requests.codes.ok:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)