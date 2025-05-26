# Web-basierter Tierdaten-Generator
[![Python](https://img.shields.io/badge/Python-%3E=3.8-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) Dieses Python-Skript ermöglicht es Nutzern, Informationen über ein bestimmtes Tier abzurufen und diese in einer einfachen HTML-Seite anzuzeigen. Der Nutzer wird aufgefordert, einen Tiernamen einzugeben, woraufhin die Daten von einer externen API abgerufen und mithilfe eines HTML-Templates formatiert dargestellt werden.

## Funktionsweise

1.  **Nutzereingabe:** Das Skript fordert den Nutzer auf, den Namen eines Tieres einzugeben.
2.  **Datenabruf:** Mithilfe der eingegebenen Tierbezeichnung werden über die API-Ninjas Animals API (`https://api.api-ninjas.com/v1/animals`) die entsprechenden Tierdaten abgerufen. Hierfür ist ein API-Schlüssel erforderlich, der über eine `.env`-Datei geladen wird.
3.  **Datenverarbeitung:** Die abgerufenen Tierdaten werden in eine HTML-Struktur umgewandelt.
4.  **HTML-Generierung:** Ein vordefiniertes HTML-Template (`animals_template.html`) wird geladen. Platzhalter im Template werden mit den abgerufenen und verarbeiteten Tierdaten gefüllt.
5.  **Ausgabe:** Die generierte HTML-Seite wird in einer Datei namens `animals.html` gespeichert und kann im Browser geöffnet werden.

## Installation

1.  **Voraussetzungen:**
    * Python 3.8 oder höher ist erforderlich.
    * `pip` (Python Package Installer) sollte installiert sein.

2.  **Repository klonen (optional):**
    ```bash
    git clone [https://github.com/DeinNutzername/DeinRepoName.git](https://github.com/nicoschulze1602/Zootopia-with-API.git)
    cd DeinRepoName
    ```

3.  **Abhängigkeiten installieren:**
    Stelle sicher, dass du die benötigten Python-Pakete installiert hast. Erstelle eine `requirements.txt`-Datei mit folgendem Inhalt (falls noch nicht vorhanden):
    ```
    requests
    python-dotenv
    ```
    Installiere die Abhängigkeiten mit:
    ```bash
    pip install -r requirements.txt
    ```

4.  **API-Schlüssel einrichten:**
    * Erstelle eine `.env`-Datei im Hauptverzeichnis des Projekts.
    * Füge deinen API-Schlüssel von API-Ninjas in die `.env`-Datei ein:
        ```
        API_KEY=DEIN_API_SCHLÜSSEL_HIER
        ```
        **Wichtig:** Teile deinen API-Schlüssel nicht öffentlich!

5.  **HTML-Template:**
    Stelle sicher, dass sich eine Datei namens `animals_template.html` im selben Verzeichnis wie dein Python-Skript befindet. Der Inhalt dieser Datei sollte ein HTML-Grundgerüst mit einem Platzhalter `__REPLACE_ANIMALS_INFO__` enthalten, an dem die Tierdaten eingefügt werden. Ein Beispiel für `animals_template.html`:

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tierinformationen</title>
        <style>
            .cards {
                display: flex;
                flex-wrap: wrap;
                list-style: none;
                padding: 0;
            }

            .cards__item {
                padding: 1rem;
                width: calc(50% - 1rem); /* Für zwei Karten pro Zeile */
            }

            .card {
                background-color: #f1f1f1;
                border-radius: 0.25rem;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                display: flex;
                flex-direction: column;
                overflow: hidden;
            }

            .card__title {
                padding: 1rem;
                font-size: 1.2rem;
                font-weight: bold;
                text-align: center;
                background-color: #ddd;
            }

            .card__text {
                padding: 1rem;
            }

            .card__list {
                list-style: none;
                padding: 0;
            }

            .card__list li {
                margin-bottom: 0.5rem;
            }

            .no-results {
                font-style: italic;
                color: gray;
            }
        </style>
    </head>
    <body>
        <ul class="cards">
            __REPLACE_ANIMALS_INFO__
        </ul>
    </body>
    </html>
    ```

## Verwendung

1.  Navigiere im Terminal zum Verzeichnis des Projekts.
2.  Führe das Hauptskript (`web_generator.py`) aus:
    ```bash
    python web_generator.py
    ```
3.  Das Skript fordert dich auf, einen Tiernamen einzugeben. Gib den gewünschten Tiernamen ein und drücke Enter.
4.  Nachdem die Daten abgerufen und die HTML-Seite generiert wurde, findest du die Datei `animals.html` im selben Verzeichnis. Öffne diese Datei in deinem Webbrowser, um die Tierinformationen anzuzeigen.
5.  Um eine weitere Tierseite zu erstellen, führe das Skript erneut aus.
6.  Gib `exit` ein, um das Programm zu beenden.

## Beispiele

Nachdem du beispielsweise "Cat" eingegeben hast, könnte die generierte `animals.html`-Seite Informationen wie Diät, Lebensraum, Typ und andere Merkmale der Katze anzeigen.

## Abhängigkeiten

* `requests`: Für das Senden von HTTP-Anfragen an die API.
* `python-dotenv`: Zum Laden von Umgebungsvariablen aus der `.env`-Datei (für den API-Schlüssel).

## Dateien im Projekt

* `web_generator.py`: Das Hauptskript zur Nutzerinteraktion, Datenabfrage und HTML-Generierung.
* `data_fetcher.py`: Modul zum Abrufen der Tierdaten von der API.
* `.env`: Datei zur Speicherung des API-Schlüssels (nicht im Repository speichern!).
* `requirements.txt`: Liste der benötigten Python-Pakete.
* `animals_template.html`: HTML-Vorlage für die Darstellung der Tierdaten.
* `animals.html`: Die generierte HTML-Datei mit den Tierinformationen.
* `README.md`: Diese Datei.

## Lizenz

Dieses Projekt ist unter der [MIT Lizenz](https://opensource.org/licenses/MIT) lizenziert. Siehe die `LICENSE`-Datei für weitere Details.

## Kontakt

[Nico Schulze](https://github.com/nicoschulze1602)

---

Viel Spaß beim Generieren von Tierseiten!