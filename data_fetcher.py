import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_data(animal_name):
    """Fetches animal data from the API."""
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("❌ Error: API key not found. Please check your .env file.")
        return None

    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("API Error:", response.status_code, response.text)
        return None