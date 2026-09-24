def traffic_light(light_color):
    color = light_color.lower()
    if color == "green":
        return "Go"
    elif color == "yellow":
        return "Yield"
    elif color == "red":
        return "Stop"
    else:
        return "Invalid light color"


light_color = input("Enter the traffic light color: ")
print(traffic_light(light_color))
