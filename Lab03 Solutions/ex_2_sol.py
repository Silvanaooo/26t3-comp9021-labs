def f2_1(n: int) -> None:
    """
    Prints a pattern where even digits (0,2,4,6,8) are represented by white squares ⬜
    and odd digits (1,3,5,7,9) are represented by black squares ⬛.
    
    Uses string conversion and for loop to process each digit.
    """
    result = ""  # Initialize empty result string
    for digit in str(n):  # Convert number to string and iterate through each digit
        if int(digit) % 2 == 0:  # Check if digit is even
            result += "⬜"  # Add white square for even digit
        else:
            result += "⬛"  # Add black square for odd digit
    print(result)  # Print the final result (not returning)


def f2_2(n: int) -> None:
    """
    Prints a pattern where even digits (0,2,4,6,8) are represented by white squares ⬜
    and odd digits (1,3,5,7,9) are represented by black squares ⬛.
    
    Uses dictionary mapping and string conversion.
    """
    # Dictionary mapping each digit to its corresponding square
    digit_map = {
        '0': '⬜', '2': '⬜', '4': '⬜', '6': '⬜', '8': '⬜',  # Even digits -> white
        '1': '⬛', '3': '⬛', '5': '⬛', '7': '⬛', '9': '⬛'   # Odd digits -> black
    }
    
    # Convert number to string, map each digit to square, and join
    result = ''.join(digit_map[digit] for digit in str(n))
    print(result)  # Print the final result

def f2_3(n: int) -> None:
    """
    Prints a pattern where even digits (0,2,4,6,8) are represented by white squares ⬜
    and odd digits (1,3,5,7,9) are represented by black squares ⬛.
    
    Uses recursion to process each digit.
    """
    # Base case
    if n == 0:
        print("⬜")  # 0 is even, so white square
        return
    
    # Helper function to convert a number to squares recursively
    def number_to_squares(num):
        if num == 0:
            return ""
        
        # Process the rightmost digit
        digit = num % 10
        square = "⬜" if digit % 2 == 0 else "⬛"
        
        # Recursively process the rest of the number
        return number_to_squares(num // 10) + square
    