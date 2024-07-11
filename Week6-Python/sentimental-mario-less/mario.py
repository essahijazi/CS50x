def get_height():
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                return height
            else:
                print("Height must be between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 8.")

def print_pyramid(height):
    for i in range(height):
        print(" " * (height - i - 1) + "#" * (i + 1))

def main():
    height = get_height()
    print_pyramid(height)

if __name__ == "__main__":
    main()
