import main
import menu
import sys
import art

MONEY = float(0)


def start_coffee_machine():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "espresso":
        if check_resources(user_choice):
            process_coins(user_choice)
    elif user_choice == "latte":
        if check_resources(user_choice):
            process_coins(user_choice)
    elif user_choice == "cappuccino":
        if check_resources(user_choice):
            process_coins(user_choice)
    elif user_choice == "off":
        turn_off()
    elif user_choice == "report":
        display_report()
    else:
        print("Invalid input! Please try again")

    start_coffee_machine()


def turn_off():
    sys.exit("The coffee machine has been turned off")


def calculate_money(quarters, dimes, nickles, pennies):
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def check_inserted_money(user_choice, user_coins):
    if user_coins < menu.MENU[user_choice]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    elif menu.MENU[user_choice]['cost'] == user_coins:
        make_drink(user_choice)
        main.MONEY += user_coins
        print(f"Here is your {user_choice} ☕. Enjoy!")
    elif user_coins > menu.MENU[user_choice]['cost']:
        change = user_coins - menu.MENU[user_choice]['cost']
        main.MONEY += menu.MENU[user_choice]['cost']
        make_drink(user_choice)
        print(f"Here is ${format(change, '.2f')} in change.")
        print(f"Here is your {user_choice} ☕. Enjoy!")
    else:
        start_coffee_machine()


def process_coins(user_choice):
    print("Please insert coins.")
    quarters = float(input("How many quarter?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    user_coins = calculate_money(quarters, dimes, nickles, pennies)
    check_inserted_money(user_choice, user_coins)


def display_report():
    print(f"Water: {menu.resources['water']}ml\nMilk: {menu.resources['milk']}ml")
    print(f"Coffee: {menu.resources['coffee']}g\nMoney: ${format(MONEY, '.2f')}")


def resources_sufficient_message(resources):
    print(f"Sorry there is not enough {resources}.")


def check_resources(user_choice):
    if user_choice == "espresso":
        if menu.resources['water'] < 50:
            return resources_sufficient_message('water')
        elif menu.resources['coffee'] < 18:
            return resources_sufficient_message('coffee')
        else:
            return True

    if user_choice == "latte":
        if menu.resources['water'] < 200:
            return resources_sufficient_message('water')
        elif menu.resources['coffee'] < 24:
            return resources_sufficient_message('coffee')
        elif menu.resources['milk'] < 150:
            return resources_sufficient_message('milk')
        else:
            return True

    if user_choice == "cappuccino":
        if menu.resources['water'] < 250:
            return resources_sufficient_message('water')
        elif menu.resources['coffee'] < 24:
            return resources_sufficient_message('coffee')
        elif menu.resources['milk'] < 100:
            return resources_sufficient_message('milk')
        else:
            return True


def make_drink(user_choice):
    if user_choice == "espresso":
        updated_water = int(menu.resources['water']) - 50
        menu.resources['water'] = updated_water
        updated_coffee = int(menu.resources['coffee']) - 18
        menu.resources['coffee'] = updated_coffee
    elif user_choice == "latte":
        updated_water = int(menu.resources['water']) - 200
        menu.resources['water'] = updated_water
        updated_coffee = int(menu.resources['coffee']) - 24
        menu.resources['coffee'] = updated_coffee
        updated_milk = int(menu.resources['milk']) - 150
        menu.resources['milk'] = updated_milk
    elif user_choice == "cappuccino":
        updated_water = int(menu.resources['water']) - 250
        menu.resources['water'] = updated_water
        updated_coffee = int(menu.resources['coffee']) - 24
        menu.resources['coffee'] = updated_coffee
        updated_milk = int(menu.resources['milk']) - 100
        menu.resources['milk'] = updated_milk


print(art.logo_coffee)
start_coffee_machine()
