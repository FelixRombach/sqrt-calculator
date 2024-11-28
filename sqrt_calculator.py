def calculate_sqrt(number, precision=0.0001):
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    if number == 0:
        return 0
    
    x = number  # Initial guess
    while True:
        # Newton's method: x = (x + n/x) / 2
        next_x = (x + number/x) / 2
        if abs(x - next_x) < precision:
            return next_x
        x = next_x

def main():
    try:
        number = float(input("Enter a number to calculate its square root: "))
        result = calculate_sqrt(number)
        print(f"The square root of {number} is approximately {result:.4f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()