def calculate_num_of_coins(coin_denomination, change_owed):
    num_of_coins = 0
    while change_owed >= coin_denomination:
        num_of_coins += 1
        change_owed -= coin_denomination
    return num_of_coins

def main():
    while True:
        try:
            change_owed = float(input("Change Owed: "))
            if change_owed >= 0:
                break
            else:
                print("Change must be non-negative.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    change_owed = round(change_owed * 100)  # Convert dollars to cents
    num_of_coins = 0

    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    num_of_coins += calculate_num_of_coins(quarter, change_owed)
    change_owed %= quarter

    num_of_coins += calculate_num_of_coins(dime, change_owed)
    change_owed %= dime

    num_of_coins += calculate_num_of_coins(nickel, change_owed)
    change_owed %= nickel

    num_of_coins += calculate_num_of_coins(penny, change_owed)

    print(num_of_coins)

if __name__ == "__main__":
    main()
