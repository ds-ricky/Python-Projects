# Caesar Cipher

This is a simple Python implementation of the Caesar Cipher, a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.

## Features

- Encrypt and decrypt messages using the Caesar Cipher.
- Command-line interface via `main.py`.
- Graphical user interface via `gui.py`.

## Files

- `main.py`: The main script for command-line usage.
- `gui.py`: The graphical user interface using Tkinter.
- `art.py`: Contains ASCII art for the application.

## Usage

### Command-Line

Run the main script:

```bash
python main.py
```

### GUI

Run the GUI script:

```bash
python gui.py
```

## Requirements

- Python 3.x

No external dependencies are required beyond the standard library.

## How It Works

The Caesar Cipher shifts each letter in the message by a fixed number of positions. For example, with a shift of 3:

- A becomes D
- B becomes E
- ...
- X becomes A
- Y becomes B
- Z becomes C

Non-alphabetic characters remain unchanged.

## Contributing

Feel free to contribute improvements or bug fixes.