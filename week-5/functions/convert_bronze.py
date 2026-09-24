def convert_bronze(bronze_coins):
    bronze_per_silver = 20
    bronze_per_gold = 20 * 15

    gold = bronze_coins // bronze_per_gold
    bronze_coins = bronze_coins % bronze_per_gold
    silver = bronze_coins // bronze_per_silver
    bronze = bronze_coins % bronze_per_silver

    result = ""
    if gold > 0:
        result = result + str(gold) + " gold "
    if silver > 0:
        result = result + str(silver) + " silver "
    if bronze > 0:
        result = result + str(bronze) + " bronze"

    if result == "":
        return "0 bronze"
    return result.strip()


bronze_coins = int(input("Enter the number of bronze coins: "))
print(convert_bronze(bronze_coins))
