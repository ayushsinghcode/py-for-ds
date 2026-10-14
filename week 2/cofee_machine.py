
print("===== WELCOME TO COFFEE MACHINE =====")

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

menu = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "price": 250
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "price": 150
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "price": 300
    }
}

coins = {
    "penny": 1,
    "nickel": 5,
    "dime": 10,
    "quarter": 25
}

while True:

    print("\n===== COFFEE MENU =====")
    print("1. Espresso - $2.50")
    print("2. Latte - $1.50")
    print("3. Cappuccino - $3.00")
    print("4. Turn off machine")

    user_input = input("What would you like? Enter 1, 2, 3, or 4: ")

    if user_input == "4":
        print("Coffee machine turned off.")
        break

    if user_input == "1":
        drink_name = "espresso"
    elif user_input == "2":
        drink_name = "latte"
    elif user_input == "3":
        drink_name = "cappuccino"
    else:
        print("Invalid choice. Please try again.")
        continue

    confirm = input(
        f"You selected {drink_name}. Proceed? (yes/no): "
    ).lower()

    if confirm != "yes":
        print("Order cancelled.")
        continue

    print("\nChecking resources...")

    coffee = menu[drink_name]

    # Check whether all required resources are available
    if (
        resources["water"] < coffee["water"]
        or resources["milk"] < coffee["milk"]
        or resources["coffee"] < coffee["coffee"]
    ):
        print("Sorry, not enough resources.")
        print("Please choose another drink.")
        continue

    print("Resources are sufficient!")
    print("Price:", coffee["price"], "cents")

    # Collect coins
    print("\nPlease insert your coins.")

    quarter = int(input("Number of quarters (25 cents): "))
    dime = int(input("Number of dimes (10 cents): "))
    nickel = int(input("Number of nickels (5 cents): "))
    penny = int(input("Number of pennies (1 cent): "))

    total_money = (
        quarter * coins["quarter"]
        + dime * coins["dime"]
        + nickel * coins["nickel"]
        + penny * coins["penny"]
    )

    print("Total inserted:", total_money, "cents")

    # Check payment
    if total_money < coffee["price"]:
        print("Sorry, insufficient money.")
        print("Refund:", total_money, "cents")
        continue

    # Calculate change
    change = total_money - coffee["price"]

    print("Payment successful!")
    print("Change returned:", change, "cents")

    # Deduct resources
    resources["water"] -= coffee["water"]
    resources["milk"] -= coffee["milk"]
    resources["coffee"] -= coffee["coffee"]

    print("\nPreparing your", drink_name, "...")
    print("Here is your", drink_name, "! Enjoy!")

    # Display remaining resources
    print("\n===== REMAINING RESOURCES =====")
    print("Water:", resources["water"], "ml")
    print("Milk:", resources["milk"], "ml")
    print("Coffee:", resources["coffee"], "g")
