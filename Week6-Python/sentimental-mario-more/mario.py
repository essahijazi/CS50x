def get_height():
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                return height
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 8.")

def print_pyramid(height):
    for i in range(height):
        # Print leading spaces
        print(" " * (height - i - 1), end="")
        # Print first set of hashes
        print("#" * (i + 1), end="")
        # Print middle space
        print("  ", end="")
        # Print second set of hashes
        print("#" * (i + 1), end="")
        # Move to the next line
        print()

def main():
    height = get_height()
    print_pyramid(height)

if __name__ == "__main__":
    main()
