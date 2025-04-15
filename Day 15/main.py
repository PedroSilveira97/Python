menu = {"espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.50},
        "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.50},
        "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.00}}
operations = ["espresso", "latte", "cappuccino", "report", "exit", "refill"]

resources = {"coffee": 100, "water": 300, "milk": 200, "money": 10}

max_resources = {"coffee": 100, "water": 300, "milk": 200}

coins = {"quarter": 0.25, "dime": 0.1, "nickel": 0.05, "penny": 0.01}

insufficient_ingredients = []

on = True

can_make_drink = True
while on:
    for option in operations:
        print(f"{option.capitalize()}")
    button = input(f"Which button would you like to press?")
    if button in menu:
        drink = menu[button]
        for ingredient, amount_required in drink["ingredients"].items():
            if resources[ingredient] < amount_required:
                insufficient_ingredients.append(ingredient)
                can_make_drink = False
            if can_make_drink:
                resources[ingredient] = resources[ingredient] - drink["ingredients"][ingredient]
        if insufficient_ingredients:
            print("Not enough " + ", ".join(insufficient_ingredients))
        if can_make_drink:
            cost = round(drink["cost"], 2)
            to_pay = round(drink["cost"], 2)
            total_paid = 0.00
            while total_paid < cost:
                insert_coin = input(str(f"You still need to insert ${to_pay: .2f}. "
                                        f"What coin would you like to insert?"))
                if insert_coin in coins:
                    inserted_coin = round(coins[insert_coin], 2)
                    to_pay -= inserted_coin
                    total_paid = round(total_paid + inserted_coin, 2)
                if total_paid >= cost:
                    change = round(total_paid - cost, 2)
                    resources["money"] += total_paid - change
                    if change > 0.00:
                        print(f"Your change is ${change}")
                    print(f"Your {button} is ready.")
    elif button == "report":
        for resource, value in resources.items():
            suffix = "ml" if resource in ["water", "milk"] else "g" if resource == "coffee" else ""
            prefix = "" if resource != "money" else "$"
            print(f"{resource.capitalize()}: {prefix}{resources[resource]}{suffix}")
    elif button == "refill":
        for ingredient in resources and max_resources:
            if ingredient != "money":
                refillable_amount = max_resources[ingredient] - resources[ingredient]
                suffix = "ml" if ingredient in ["water", "milk"] else "g"
                print(f"{ingredient.capitalize()} has {resources[ingredient]}{suffix}. You can refill up to "
                      f"{refillable_amount}{suffix} of {ingredient}.")
                if refillable_amount > 0:
                    refill_request = int(input(f"How many {suffix} would you like to refill? "))
                    if 0 <= refill_request <= refillable_amount:
                        resources[ingredient] += refill_request
                        print(f"Refilled {refill_request}{suffix} of {ingredient}. "
                              f"Now it has {resources[ingredient]}{suffix}.")
    elif button == "exit":
        break
