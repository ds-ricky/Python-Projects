from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def suf_res(required_resources):
    for i in required_resources:
        if required_resources[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def coin():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    total = (0.25*quarters) + (0.10*dimes) + (0.05*nickles) + (0.01*pennies)
    return total

def suf_coin(money,required_money):
    if money < required_money:
        print("Sorry that's not enough money")
        return False
    else:
        change = round(money - required_money,2)
        print(f"Here is ${change} dollars in change")
        return required_money,True

def order_delivery(drink_name,material):
    for item in material:
        resources[item] -= material[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

machine = True
while machine:
    print(logo)
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        if suf_res(MENU[choice]['ingredients']):
            customer_money = coin()
            change_to_customer,next_step = suf_coin(customer_money,MENU[choice]['cost'])
            profit += change_to_customer
            if next_step:
                order_delivery(choice, MENU[choice]['ingredients'])


