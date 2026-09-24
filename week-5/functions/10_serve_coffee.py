def serve_coffee(selected_coffee):
    coffee = selected_coffee.lower()
    if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        return "Here is your " + coffee + "!"
    else:
        return "Sorry, we don't have " + coffee + "."


selected_coffee = input("Which coffee would you like (Espresso, Latte, Cappuccino)? ")
print(serve_coffee(selected_coffee))
