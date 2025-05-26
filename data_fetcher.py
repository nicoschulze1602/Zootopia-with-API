import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def fetch_data(animal_name):
    """Fetches animal data from the API."""
    if not API_KEY:
        print("❌ Error: API key not found. Please check your .env file.")
        return None

    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("API Error:", response.status_code, response.text)
        return None