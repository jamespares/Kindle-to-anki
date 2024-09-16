import re
import sys
import genanki
import random

def parse_kindle_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to match Kindle highlights
    pattern = r'(.+) \((.+)\)\r?\n- Your Highlight on page (\d+) \| Location (\d+)-(\d+) \| Added on (.+)\r?\n\r?\n(.+)'
    matches = re.findall(pattern, content, re.DOTALL)

    snippets = []
    for match in matches:
        book_title, author, page, loc_start, loc_end, date, highlight = match
        snippets.append({
            'book_title': book_title,
            'author': author,
            'page': page,
            'location': f'{loc_start}-{loc_end}',
            'date': date,
            'highlight': highlight.strip()
        })

    return snippets

def create_anki_deck(snippets, deck_name):
    # Create a unique model ID
    model_id = random.randrange(1 << 30, 1 << 31)

    # Define the Anki note model
    model = genanki.Model(
        model_id,
        'Kindle Highlight Model',
        fields=[
            {'name': 'Highlight'},
            {'name': 'Book Title'},
            {'name': 'Author'},
            {'name': 'Page'},
            {'name': 'Location'},
            {'name': 'Date'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Highlight}}',
                'afmt': '{{FrontSide}}<hr id="answer">Book: {{Book Title}}<br>Author: {{Author}}<br>Page: {{Page}}<br>Location: {{Location}}<br>Date: {{Date}}',
            },
        ])

    # Create a unique deck ID
    deck_id = random.randrange(1 << 30, 1 << 31)

    # Create the deck
    deck = genanki.Deck(deck_id, deck_name)

    # Add notes to the deck
    for snippet in snippets:
        note = genanki.Note(
            model=model,
            fields=[
                snippet['highlight'],
                snippet['book_title'],
                snippet['author'],
                snippet['page'],
                snippet['location'],
                snippet['date'],
            ])
        deck.add_note(note)

    return deck

def main():
    if len(sys.argv) != 4:
        print("Usage: python kindle_to_anki.py <input_kindle_file> <output_anki_file> <deck_name>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    deck_name = sys.argv[3]

    try:
        snippets = parse_kindle_file(input_file)
        if not snippets:
            print("No highlights found in the input file.")
            sys.exit(1)

        deck = create_anki_deck(snippets, deck_name)
        genanki.Package(deck).write_to_file(output_file)
        print(f"Successfully created Anki deck: {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
