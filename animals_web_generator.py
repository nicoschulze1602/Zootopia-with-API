import json
import requests


def load_data(file_path):
    """Loads and parses a JSON file from the given file path."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Converts a single animal dictionary into an HTML <li> block."""
    output = '<li class="cards__item">\n'
    output += '  <div class="card">\n'

    name = animal_obj.get("name", "unknown")
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
            output += f'        <li><strong>{label}:</strong> {value}</li>\n'

    output += '      </ul>\n'
    output += '    </div>\n'
    output += '  </div>\n'
    output += '</li>\n'
    return output


def get_animals_data(data):
    """Returns a string containing all serialized animal entries."""
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output


def main():
    """Loads data, processes it, and writes HTML output."""
    global animals_data
    name = 'Fox'
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url,
                            headers={'X-Api-Key': 'iWcJikrDu06TpQsTIkhWfA==A2V9t0BMUCugf7Yh'})
    if response.status_code == requests.codes.ok:
        data = response.json()
        animals_data = get_animals_data(data).strip()
    else:
        print("Error:", response.status_code, response.text)
    """try:
        data = load_data('animals_data.json')
    except FileNotFoundError:
        print("❌ Error: 'animals_data.json' file not found.")
        return
    except json.JSONDecodeError:
        print("❌ Error: 'animals_data.json' contains no valid JSON.")
        return"""

    try:
        with open('animals_template.html', 'r') as file:
            template = file.read()
    except FileNotFoundError:
        print("❌ Error: 'animals_template.html' file not found.")
        return

    new_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_data)

    try:
        with open('animals.html', 'w', encoding="utf-8") as file:
            file.write(new_html)
        print("✅ File 'animals.html'was successfully created/updated!")
    except Exception as e:
        print(f"❌ Error creating file: {e}")


if __name__ == '__main__':
    main()
