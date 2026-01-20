# Coffee Machine

A Python-based coffee machine simulator that manages orders, inventory, and payments.

## Description

This project simulates a real coffee machine that dispenses different types of coffee drinks. The program manages:
- **Menu**: Espresso, Latte, and Cappuccino with their respective ingredients and costs
- **Inventory**: Tracks available water, milk, and coffee resources
- **Payments**: Accepts coin input (quarters, dimes, nickels, pennies) and calculates change
- **Reporting**: Displays current resource levels and total profit

## Features

- Interactive menu with three coffee options
- Resource availability checking before order processing
- Coin-based payment system with automatic change calculation
- Inventory management with resource depletion tracking
- Report functionality to check current supplies and profit
- Graceful error handling for insufficient resources or payment

## How to Run

```bash
python main.py
```

## Usage

1. The program displays the coffee machine menu
2. Choose your desired drink (espresso, latte, or cappuccino)
3. Insert the required amount of coins (quarters, dimes, nickels, pennies)
4. The machine dispenses your drink if there are sufficient resources
5. Special commands:
   - Type `"off"` to turn off the machine
   - Type `"report"` to see current inventory and profit

## Menu

- **Espresso**: $1.50 - Water (50ml), Coffee (18g)
- **Latte**: $2.50 - Water (200ml), Milk (150ml), Coffee (24g)
- **Cappuccino**: $3.00 - Water (250ml), Milk (100ml), Coffee (24g)

## Files

- `main.py`: Main program logic for the coffee machine
- `art.py`: ASCII art display for the coffee machine logo
