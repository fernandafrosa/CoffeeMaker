#COFFEE MACHINE - DAY 15 PYTHON

#TODO: IMPORT LIBRARIES NEEDED
from menu import MENU
from menu import resources

money = 0

#TODO: PRINT REPORT
def printReport():
    print(f"Water: {resources['water']}ml \n"
        f"Milk : {resources['milk']}ml  \n"
        f"Coffee: {resources['coffee']}g\n"
        f"Money: ${float(money)}")


#TODO: check resources
def sufficient_resources(drink):
    for item in drink:
        if drink[item] > resources[item]:
            print(f"Sorry there ir not enough {item}")
            return False
    return True


#TODO: HANDLE THE COIN PROCESSING
def process_coins():
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total



#TODO: CHECK IF TRANSACTION IS SUCCESSFUL
def successful_transaction(drink, payment):
    if payment > drink:
        global money
        money += float(drink)
        change = payment - float(drink)
        print(f"Here´s ${round(change, 2)} dollars in change")
        return True

    if payment == drink:
        money += float(MENU[drink]['cost'])
        return True

    #if theres not enough money
    elif payment < drink:
        print("Sorry, that´s not enough money. Money refunded.")
        return False


#TODO: MAKE COFFEE:
def make_coffee(choice, drink):
    for item in drink:
        resources[item] -= drink[item]
    print(f"Here is your {choice} ☕️. Enjoy!")


isOn = True

#TODO: PROMPT CHOICES FOR USER
while isOn:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        isOn = False

    elif choice == "report":
        printReport()

    else:
        drink = MENU[choice]
        if sufficient_resources(drink['ingredients']):
            payment = process_coins()
            if successful_transaction(drink['cost'], payment):
                make_coffee(choice, drink['ingredients'])