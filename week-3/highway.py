number = int(input("Enter a highway number: "))

if number < 1 or number > 999:
    print("invalid highway number")
else:
    primary = number % 100
    if primary == 0:
        print("invalid highway number")
    elif primary % 2 == 0:
        print("east/west")
    else:
        print("north/south")
