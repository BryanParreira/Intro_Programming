def serve_icecream(selected_flavor):
    flavor = selected_flavor.lower()
    if flavor == "vanilla" or flavor == "chocolate" or flavor == "strawberry":
        return "Here is your " + flavor + " ice cream!"
    else:
        return "Sorry, we don't have " + flavor + " ice cream."


selected_flavor = input("Which flavor would you like (Vanilla, Chocolate, Strawberry)? ")
print(serve_icecream(selected_flavor))
