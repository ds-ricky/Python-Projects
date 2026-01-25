# ☕ Coffee Machine (OOP Version)

An object-oriented programming (OOP) implementation of a coffee vending machine simulator. This is a refactored version of the procedural Coffee Machine project, demonstrating the power and organization of OOP principles.

## 🎯 Project Overview

This project simulates a coffee vending machine that can prepare different types of coffee drinks (espresso, latte, cappuccino) while managing resources and processing payments. Unlike the procedural version, this implementation uses classes and objects to create a more modular, maintainable, and scalable codebase.

## 🔑 OOP Concepts Demonstrated

### Classes and Objects
- **CoffeeMaker**: Manages coffee machine resources and coffee preparation
- **Menu & MenuItem**: Handles menu items and their properties
- **MoneyMachine**: Processes payments and tracks profits

### Encapsulation
- Each class encapsulates related data and functionality
- Private attributes and public methods provide controlled access
- Resources, menu items, and money are managed within their respective classes

### Abstraction
- Complex operations are hidden behind simple method calls
- Users interact with high-level methods without worrying about implementation details
- Example: `make_payment()` handles all coin processing internally

### Modularity
- Each class is defined in its own file for better organization
- Components can be modified independently
- Easy to extend functionality without affecting other parts

## 📁 Project Structure

```
Coffee Machine OOPS/
│
├── main.py              # Main program loop and user interaction
├── coffee_maker.py      # CoffeeMaker class - manages resources and brewing
├── menu.py             # Menu and MenuItem classes - handles menu operations
├── money_machine.py    # MoneyMachine class - handles payment processing
└── README.md           # This file
```

## 🏗️ Class Architecture

### CoffeeMaker
- **Attributes**: resources (water, milk, coffee)
- **Methods**: 
  - `report()`: Display current resources
  - `is_resource_sufficient()`: Check if enough resources available
  - `make_coffee()`: Prepare the drink and deduct resources

### Menu & MenuItem
- **MenuItem Attributes**: name, cost, ingredients
- **Menu Methods**:
  - `get_items()`: Return available drink options
  - `find_drink()`: Search for a drink by name

### MoneyMachine
- **Attributes**: profit, money_received
- **Methods**:
  - `report()`: Display total profit
  - `process_coins()`: Accept and calculate coin input
  - `make_payment()`: Verify payment and return change

## 🚀 How to Run

1. Navigate to the project directory:
```bash
cd "Projects/Coffee Machine OOPS"
```

2. Run the program:
```bash
python main.py
```

3. Follow the prompts to order drinks!

## 💡 Usage

- **Order a drink**: Type `espresso`, `latte`, or `cappuccino`
- **Check resources**: Type `report`
- **Turn off machine**: Type `off`
- **Insert coins**: Enter the number of quarters, dimes, nickles, and pennies when prompted

## 📊 Available Drinks

| Drink | Water | Milk | Coffee | Cost |
|-------|-------|------|--------|------|
| Espresso | 50ml | 0ml | 18g | $1.50 |
| Latte | 200ml | 150ml | 24g | $2.50 |
| Cappuccino | 250ml | 50ml | 24g | $3.00 |

## 🔄 Differences from Procedural Version

| Aspect | Procedural | OOP |
|--------|-----------|-----|
| Code Organization | Single file with functions | Multiple files with classes |
| Data Management | Global variables/dictionaries | Encapsulated in objects |
| Maintainability | Harder to modify | Easy to extend and modify |
| Scalability | Limited | Highly scalable |
| Reusability | Limited function reuse | Classes can be reused/imported |

## 🎓 Learning Outcomes

- Understanding of OOP principles (encapsulation, abstraction, modularity)
- Creating and working with multiple classes
- Organizing code into separate modules
- Managing object state and behavior
- Implementing real-world systems using OOP design

## 🛠️ Future Enhancements

- Add more drink options using inheritance
- Implement a GUI using the existing classes
- Add data persistence to save machine state
- Create an Admin class for machine maintenance
- Add custom drink creation feature

## 📝 Notes

This project demonstrates how OOP makes code more organized and maintainable compared to procedural programming. Each class has a single responsibility, making the code easier to understand, test, and extend.

---

**Comparison**: Check out the [Coffee Machine](../Coffee%20Machine) folder to see the procedural implementation of the same project!
