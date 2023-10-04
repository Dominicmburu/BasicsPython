MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost": 1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost": 2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost": 3.0,
    }
}

resourses = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resoures_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resourses[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        
    return True

def process_coins():
    print('Please insert coins.')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.1
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost 
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resourses[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True
profit = 0

while True:
    choice = input('What would you like? (espresso/latte/cappuccino): ')

    if choice == 'off':
        is_on = False

    elif choice == 'report':
        print(f"Water: {resourses['water']}ml")
        print(f"Milk: {resourses['milk']}ml")
        print(f"Coffee: {resourses['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        if is_resoures_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
        


















