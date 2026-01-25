# ☕ Coffee Machine (OOP Version)

An object-oriented coffee vending simulator that highlights clean class design and modular code organization.

## 📋 Description

This refactor of the procedural Coffee Machine project uses classes to manage brewing, menus, and payments. It serves espresso, latte, and cappuccino while tracking resources and profits in a reusable, testable design.

## 🎯 Features

- 🧱 Class-based architecture (`CoffeeMaker`, `Menu`/`MenuItem`, `MoneyMachine`)
- ✅ Resource checks before brewing and payment validation with change handling
- 📊 Built-in menu of three drinks with ingredient and cost data
- 📄 `report` command to view resources and profits; `off` to shut down gracefully

## 📁 Project Structure

```
Coffee Machine OOPS/
├── coffee_maker.py   # CoffeeMaker class - manages resources and brewing
├── menu.py           # Menu and MenuItem classes - handles menu operations
├── money_machine.py  # MoneyMachine class - processes payments
├── main.py           # Program loop and user interaction
└── README.md         # Project documentation
```

## 🧩 Core Classes

- **CoffeeMaker**: `report()`, `is_resource_sufficient()`, and `make_coffee()` to track and brew drinks.
- **Menu & MenuItem**: `get_items()` to list options and `find_drink()` to fetch selections with ingredients and cost.
- **MoneyMachine**: `process_coins()`, `make_payment()`, and `report()` to handle cashflow and profits.

## 🚀 How to Run

```bash
cd "Projects/Coffee Machine OOPS"
python main.py
```

## 🛠️ Usage

- Order a drink: type `espresso`, `latte`, or `cappuccino`.
- Check resources: type `report`.
- Turn off the machine: type `off`.
- Insert coins when prompted: quarters, dimes, nickels, and pennies.

## 📊 Available Drinks

| Drink | Water | Milk | Coffee | Cost |
|-------|-------|------|--------|------|
| Espresso | 50ml | 0ml | 18g | $1.50 |
| Latte | 200ml | 150ml | 24g | $2.50 |
| Cappuccino | 250ml | 50ml | 24g | $3.00 |

## 🔄 Differences from Procedural Version

| Aspect | Procedural | OOP |
|--------|------------|-----|
| Code Organization | Single file with functions | Multiple files with classes |
| Data Management | Global variables/dictionaries | Encapsulated in objects |
| Maintainability | Harder to modify | Easier to extend and modify |
| Scalability | Limited | Highly scalable |
| Reusability | Limited function reuse | Classes can be reused/imported |

## 🎓 Learning Outcomes

- Understand encapsulation, abstraction, and modularity
- Create and compose multiple classes across modules
- Manage object state and behavior for a real-world process
- Contrast procedural and OOP approaches to the same problem

## 🛠️ Future Enhancements

- Add more drink options using inheritance
- Implement a GUI on top of the existing classes
- Add persistence to save machine state
- Create an admin mode for maintenance
- Allow custom drink creation

## 📝 Notes

This project showcases how OOP improves clarity and reuse compared to the procedural version. For the original implementation, see the [Coffee Machine](../Coffee%20Machine) folder.
