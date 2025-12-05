# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

# Main program
if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = check_even_odd(number)
        print(result)
    except ValueError:
        print("Please enter a valid integer")