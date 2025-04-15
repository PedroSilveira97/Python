from main import*
to_pay = round(drink["cost"], 2)
def insert_coins(coin) :
    if insert_coin in coins:
        inserted_coin = round(coins[insert_coin], 2)
        to_pay -= inserted_coin
        total_paid = round(total_paid + inserted_coin, 2)
        resources["money"] = total_paid
        if to_pay < 0:
            change = to_pay
            print(f"Your change is ${-change: .2f}")
            print(f"Your {button} is ready.")
        elif to_pay == 0:
            print(f"Your {button} is ready.")
    return to_pay