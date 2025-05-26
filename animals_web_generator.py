import html
from data_fetcher import fetch_data


def serialize_animal(animal_obj):
    """Convert a single animal dictionary into an HTML <li> card block."""
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
    """Convert a list of animal dictionaries into a complete HTML block."""
    output = ''
    for animal in data:
        output += serialize_animal(animal)
    return output


def get_animal_name():
    """Prompts the user to enter an animal name."""
    while True:
        name = input('Enter the name of an animal (or "exit" to quit): ').strip()
        if not name:
            print('Input cannot be empty.')
            return None
        if name.lower() == "exit":
            return None
        return name


def load_template(template_path='animals_template.html'):
    """Load the HTML template file."""
    try:
        with open(template_path, 'r', encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ Error: '{template_path}' file not found.")
        return None


def write_output_file(html_output, filepath='animals.html'):
    """Writes the total HTML content to the file."""
    try:
        with open(filepath, 'w', encoding="utf-8") as animal_file:
            animal_file.write(html_output)
        print("✅ File 'animals.html' was successfully created/updated!")
        print("ℹ️ To create another page, please run the program again.")
    except Exception as e:
        print(f"❌ Error creating file: {e}")


def main():
    name = get_animal_name()
    if not name:
        return

    raw_data = fetch_data(name)
    if raw_data is None:
        return

    if not raw_data:
        animals_data = f'<p class="no-results">Sorry! The animal "{html.escape(name)}" doesn\'t exist.</p>'
    else:
        animals_data = get_animals_data(raw_data).strip()

    template = load_template()
    if not template:
        return

    new_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_data)
    write_output_file(new_html)

if __name__ == "__main__":
    main()