def main():
    number = input("Number: ")

    if calculate_checksum(number):
        if check_card_length(number):
            print_issuing_company(number)
        else:
            print("INVALID")
    else:
        print("INVALID")


def calculate_checksum(card):
    """Calculates whether a card number is valid or not based on Luhn's Algorithm. Returns 'True' if valid, 'False' if not."""

    card_sum = 0
    is_second_digit = False

    # Iterate over every digit in reverse order
    for digit in reversed(card):
        digit = int(digit)
        if is_second_digit:
            digit *= 2
            if digit >= 10:
                digit = (digit % 10) + 1
            card_sum += digit
        else:
            card_sum += digit
        is_second_digit = not is_second_digit

    return card_sum % 10 == 0


def check_card_length(card):
    """Checks for the length of the card number to be either 13, 15 or 16. Returns True if valid, False otherwise."""

    valid_lengths = [13, 15, 16]
    return len(card) in valid_lengths


def print_issuing_company(card):
    """Prints out the name of the company that issued the card based on the first digit/digits. Prints out 'INVALID' if none matches."""

    if card.startswith("4") and len(card) in [13, 16]:
        print("VISA")
    elif card.startswith(("51", "52", "53", "54", "55")) and len(card) == 16:
        print("MASTERCARD")
    elif card.startswith(("34", "37")) and len(card) == 15:
        print("AMEX")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
