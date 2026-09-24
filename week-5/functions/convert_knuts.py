def convert_knuts(knuts):
    knuts_per_sickle = 29
    knuts_per_galleon = 29 * 17

    galleons = knuts // knuts_per_galleon
    knuts = knuts % knuts_per_galleon
    sickles = knuts // knuts_per_sickle
    knuts = knuts % knuts_per_sickle

    result = ""
    if galleons == 1:
        result = result + "1 galleon "
    elif galleons > 1:
        result = result + str(galleons) + " galleons "

    if sickles == 1:
        result = result + "1 sickle "
    elif sickles > 1:
        result = result + str(sickles) + " sickles "

    if knuts == 1:
        result = result + "1 knut"
    elif knuts > 1:
        result = result + str(knuts) + " knuts"

    if result == "":
        return "0 knuts"
    return result.strip()


knuts = int(input("Enter the number of knuts: "))
print(convert_knuts(knuts))
