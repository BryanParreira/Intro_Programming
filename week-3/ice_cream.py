flavors = {"vanilla", "chocolate", "strawberry"}

flavor_choice = input("What flavor of ice cream would you like? ")

if flavor_choice in flavors:
    print(f"Here is your {flavor_choice} ice cream!")
else:
    print(f"Sorry, we don't have {flavor_choice} flavor.")
