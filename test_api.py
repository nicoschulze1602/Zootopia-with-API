import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()
api_key = os.getenv("API_KEY")

name = 'Monkey'
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': api_key})
if response.status_code == requests.codes.ok:
    pprint(response.json())
else:
    print("Error:", response.status_code, response.text)