import json
import requests
import os
from dotenv import load_dotenv
import html

# Lädt Umgebungsvariablen aus der .env-Datei
load_dotenv()

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    output = '<li class="cards__item">\n'
    output += '  <div class="card">\n'

    name = html.escape(animal_obj.get("name", "unknown"))
    output += f'    <div class="card__title">{name}</div>\n'
    output += '    <div class="card__text">\n'
    output += '      <ul class="card__list">\n'

    characteristics = animal_obj.get('characteristics', {})
    locations = animal_obj.get('locations', [])

    fields = {
        "Diet": characteristics.get("diet"),
        "Location": locations[0] if locations else None,
        "Type": characteristics.get("type"),
        "Lifespan": characteristics.get("lifespan"),
        "Group": characteristics.get("group"),
        "Color": characteristics.get("color"),
        "Skin Type": characteristics.get("skin_type"),
    }

    for label, value in fields.items():
        if value:
            output += f'        <li><strong>{label}:</strong> {html.escape(str(value))}</li>\n'

    output += '      </ul>\n'
    output += '    </div>\n'
    output += '  </div>\n'
    output += '</li>\n'
    return output


def get_animals_data(data):
    return ''.join([serialize_animal(animal) for animal in data])


def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("❌ Error: API key not found. Please check your .env file.")
        return

    while True:
        name = input('Enter the name of an animal (or "exit" to quit): ').strip()
        if not name:
            print('Input cannot be empty.')
            continue
        if name.lower() == "exit":
            break

        api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
        response = requests.get(api_url, headers={'X-Api-Key': api_key})

        if response.status_code == requests.codes.ok:
            data = response.json()
            animals_data = get_animals_data(data).strip()
        else:
            print("Error:", response.status_code, response.text)
            return

        try:
            with open('animals_template.html', 'r', encoding="utf-8") as file:
                template = file.read()
        except FileNotFoundError:
            print("❌ Error: 'animals_template.html' file not found.")
            return

        try:
            with open('animals.html', 'w', encoding="utf-8") as file:
                new_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_data)
                file.write(new_html)
            print("✅ File 'animals.html' was successfully created/updated!")
        except Exception as e:
            print(f"❌ Error creating file: {e}")

if __name__ == "__main__":
    main()