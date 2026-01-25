# ☕ Coffee Machine

A procedural coffee machine simulator that handles orders, resources, and coin payments.

## 📋 Description

Serve espresso, latte, or cappuccino from the command line. The program checks resources, processes coins, and reports profits—all in a single, easy-to-follow script.

## 🎯 Features

- 🧾 Interactive menu with three drink options
- ✅ Resource validation before brewing
- 💰 Coin-based payment with change calculation
- 📊 `report` command to show inventory and profit
- 📴 `off` command to shut down safely

## 📁 Project Structure

```
Coffee Machine/
├── art.py    # ASCII art logo
├── main.py   # Procedural game logic
└── README.md
```

## 🚀 How to Run

```bash
python main.py
```

## 🕹️ Usage

1. Choose a drink: `espresso`, `latte`, or `cappuccino`.
2. Insert coins when prompted (quarters, dimes, nickels, pennies).
3. Receive change (if any) and your drink when resources are sufficient.
4. Type `report` anytime to view supplies and profit; type `off` to exit.

## 📋 Menu

- **Espresso**: $1.50 — Water 50ml, Coffee 18g
- **Latte**: $2.50 — Water 200ml, Milk 150ml, Coffee 24g
- **Cappuccino**: $3.00 — Water 250ml, Milk 100ml, Coffee 24g

## 🛠️ Requirements

- Python 3.x
