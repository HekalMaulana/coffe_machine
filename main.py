from coffe_machine_data import MENU, resources, COIN


def coin_input_calculate(quarter_input, dime_input, nickel_input, penny_input):
    coin_key = []
    result = []
    coin_input_list = [quarter_input, dime_input, nickel_input, penny_input]

    for i in COIN:
        coin_key.append(i)

    for i in range(len(coin_key)):
        result.append(coin_input_list[i] * COIN[f"{coin_key[i]}"])

    return sum(result)


def user_choose_espresso():
    if new_resources["water"] >= MENU["espresso"]["ingredients"]["water"] and new_resources["coffee"] >= \
            MENU["espresso"]["ingredients"]["coffee"]:
        quarter_input = int(input("How many quarter coin ? "))
        dime_input = int(input("How many dime coin ? "))
        nickel_input = int(input("How many nickel coin ? "))
        penny_input = int(input("How many penny coin ? "))

        coin_calculate = coin_input_calculate(quarter_input, dime_input, nickel_input, penny_input)
        if coin_calculate < MENU["espresso"]["cost"]:
            print("You dont have enough money espresso")
        else:
            change = coin_calculate - MENU["espresso"]["cost"]
            new_resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            new_resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print(f"Thanks for order espresso, that's you change {round(change, 2)}")
    else:
        print("this machine dont have more ingredient to make espresso")


def user_choose_latte():
    if new_resources["water"] >= MENU["latte"]["ingredients"]["water"] and new_resources["coffee"] >= \
            MENU["latte"]["ingredients"]["coffee"] and new_resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
        quarter_input = int(input("How many quarter coin ? "))
        dime_input = int(input("How many dime coin ? "))
        nickel_input = int(input("How many nickel coin ? "))
        penny_input = int(input("How many penny coin ? "))

        coin_calculate = coin_input_calculate(quarter_input, dime_input, nickel_input, penny_input)
        if coin_calculate < MENU["latte"]["cost"]:
            print("You dont have enough money for buy latte")
        else:
            change = coin_calculate - MENU["latte"]["cost"]
            new_resources["water"] -= MENU["latte"]["ingredients"]["water"]
            new_resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            new_resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            print(f"Thanks for order latte, that's you change {round(change, 2)}")
    else:
        print("this machine dont have more ingredient to make latte")


def user_choose_cappuccino():
    if new_resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and new_resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"] and new_resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
        quarter_input = int(input("How many quarter coin ? "))
        dime_input = int(input("How many dime coin ? "))
        nickel_input = int(input("How many nickel coin ? "))
        penny_input = int(input("How many penny coin ? "))

        coin_calculate = coin_input_calculate(quarter_input, dime_input, nickel_input, penny_input)

        if coin_calculate < MENU["cappuccino"]["cost"]:
            print("You dont have enough money cappuccino")
        else:
            change = coin_calculate - MENU["cappuccino"]["cost"]
            new_resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            new_resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            new_resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            print(f"Thanks for order cappuccino, that's you change {round(change, 2)}")
    else:
        print("this machine dont have more ingredient to make cappuccino")



new_resources = resources
game_over = False

while not game_over:
    user_choose = input("What would you like (espresso, latte, cappuccino) : ").lower()

    if user_choose == "report":
        print(f"Water : {new_resources['water']}")
        print(f"Milk : {new_resources['milk']}")
        print(f"Coffe : {new_resources['coffee']}")
    elif user_choose == "off":
        game_over = True
        print("Thanks for use this coffee machine")
    elif user_choose == "espresso" or user_choose == "latte" or user_choose == "cappuccino":
        if user_choose == "espresso":
            user_choose_espresso()
        elif user_choose == "latte":
            user_choose_latte()
        elif user_choose == "cappuccino":
            user_choose_cappuccino()
