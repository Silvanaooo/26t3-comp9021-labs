#Loop until valid input is received
while True:
    try:
        # Prompt user for input
        x = input("Enter a number strictly between -1 and 1 (max 2 decimal places): ")
        # check e
        if 'e' in x.lower():
            raise ValueError
        # Check: must contain a decimal point
        if '.' in x:
            parts = x.split('.')
            if len(parts) != 2 or len(parts[1]) > 2:
                raise ValueError

        # Convert to float
        x = float(x)

        # Check: must be strictly between -1 and 1
        if not (-1 < x < 1):
            raise ValueError

        # Valid input, stop loop
        break
    except ValueError:
        # If any check fails, ask again
        print("Invalid input, try again.\n")

# Format the result to 2 decimal places
print(f'\nYou entered {x:.2f} (rounded to two decimal places)')