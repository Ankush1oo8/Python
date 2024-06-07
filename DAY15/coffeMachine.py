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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"SORRY THERE IS NOT ENOUGH {item}")
            return False
        return True

def transaction(money_rec,dink_cost):
    if(money_rec>=dink_cost):
        change=round(money_rec-dink_cost,2)
        print(f"Here is {change} in change")


        global profit
        profit+=dink_cost
        return True
    else:
        print("Sorry that's not enough money. MONEY REFUNDED...")
        return False

def process_cooins():
    print("please insert coins:") 
    total=int(input("How many Quarters? : "))*0.25
    total +=int(input("How many Dimes? : "))*0.1
    total +=int(input("How many Nickles? : "))*0.05
    total +=int(input("How many pennies? : "))*0.01
    return total
    
def make_coffee(drink_name,order_Ingredients):
    for item in order_Ingredients:
        resources[item]-=order_Ingredients[item]
    print(f"here is your {drink_name}🍵")
is_on=True
while is_on:
    prompt=input("What would you like? (espresso/latte/cappuccino):  ")
    if prompt=="off":
        is_on=False
    elif prompt=="report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money:${profit}")
    else:
        drink=MENU[prompt]
        if is_resource_sufficient(drink['ingredients']):
            payment=process_cooins()
            if transaction(payment,drink["cost"]):
                make_coffee(prompt,drink["ingredients"])
                
        