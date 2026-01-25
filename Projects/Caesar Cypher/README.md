# 🔐 Caesar Cipher

Encrypt or decrypt text with a classic shift cipher via CLI or a simple Tkinter GUI.

## 📋 Description

Each letter in your message is shifted forward or backward by a chosen amount. The tool supports both directions so you can encode or decode quickly without extra dependencies.

## 🎯 Features

- 🔄 Encrypt and decrypt modes with custom shift values
- 🖥️ Command-line interface for fast usage
- 🪟 Tkinter GUI for point-and-click encryption
- 🖼️ ASCII art banner included

## 📁 Project Structure

```
Caesar Cypher/
├── art.py   # ASCII art assets
├── gui.py   # Tkinter GUI version
├── main.py  # Command-line interface
└── README.md
```

## 🚀 How to Run

CLI version:

```bash
python main.py
```

GUI version:

```bash
python gui.py
```

## 🧠 How It Works

The Caesar Cipher shifts each alphabetic character by `n` positions. With a shift of 3:

- A → D, B → E, ..., X → A, Y → B, Z → C
- Non-alphabetic characters stay unchanged

## 🛠️ Requirements

- Python 3.x (standard library only)