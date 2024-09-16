# Kindle to Anki Converter

This Python script converts Kindle highlights to Anki flashcards.

## Requirements

- Python 3.6+
- genanki library

## Installation

1. Clone this repository or download the `kindle_to_anki.py` script.
2. Install the required library:

```
pip install genanki
```

## Usage

1. Export your Kindle highlights to a text file. You can do this by:
   - Opening your Kindle device
   - Navigating to "My Clippings.txt"
   - Copying the contents to a new text file on your computer

2. Run the script with the following command:

```
python kindle_to_anki.py <input_kindle_file> <output_anki_file> "<deck_name>"
```

Replace the placeholders with your actual file names and desired deck name:
- `<input_kindle_file>`: The path to your Kindle highlights text file
- `<output_anki_file>`: The desired name for your output Anki deck file (should end with .apkg)
- `<deck_name>`: The name you want to give your Anki deck (use quotes if it contains spaces)

Example:
```
python kindle_to_anki.py example_input.txt my_kindle_highlights.apkg "My Kindle Highlights"
```

3. Import the generated .apkg file into Anki.

## Input File Format

The input file should contain Kindle highlights in the following format:

```
Book Title (Author)
- Your Highlight on page X | Location XXX-XXX | Added on Date

Highlighted text

```

You can find an example in the `example_input.txt` file provided in this repository.

## Note

This script creates flashcards with the highlight on the front and the book details on the back. You may need to adjust the script if you want a different card format.
