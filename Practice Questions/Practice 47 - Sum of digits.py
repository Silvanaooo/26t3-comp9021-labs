"""
Sum of Digits - Backtracking Problem

This program finds all possible ways to select digits from a given number
so that the selected digits add up to a target sum.

Example:
    Input: digits = "12234", desired_sum = 5
    Output: 4 solutions
        - Select digits at positions [0,1,2]: 1 + 2 + 2 = 5
        - Select digits at positions [0,4]: 1 + 4 = 5
        - Select digits at positions [1,3]: 2 + 3 = 5
        - Select digits at positions [2,3]: 2 + 3 = 5

    Note: Each position is considered unique, even if the digit values are the same.
"""

# Get input from user
digits = input('Input a natural number for the available digits: ')
desired_sum = int(input('Input a natural number for the desired sum: '))

# Store the length of digits string and initialize solutions list
n = len(digits)
solutions = []


def dfs(start_index, curr_sum, path):
    """
    Use backtracking to find all ways to select digits that sum to desired_sum.

    Args:
        start_index: The position in 'digits' where we start looking for the next digit.
                     This ensures we only consider digits after the previously selected one.
        curr_sum: The sum of all digits we have selected so far.
        path: A list storing the digits we have selected (as strings).

    How it works:
        1. If curr_sum equals desired_sum, we found a valid solution - save it!
        2. If curr_sum exceeds desired_sum or we've looked at all digits, stop searching.
        3. Otherwise, try selecting each remaining digit one by one:
           - Add the digit to our path (make a choice)
           - Recursively search with the new sum (explore that choice)
           - Remove the digit from path (undo the choice, try next option)

    Key insight:
        When curr_sum == desired_sum, we DON'T return immediately because we might
        still be able to add zeros (which don't change the sum). This is why we
        continue exploring even after finding a solution.
    """
    # Base case: We found a valid combination that sums to desired_sum
    if curr_sum == desired_sum:
        solutions.append(path[:])  # Save a copy of the current path
        # Note: We don't return here! We continue to check if we can add more zeros.

    # Stop conditions: sum is too big, or we've checked all digits
    if curr_sum > desired_sum or start_index == n:
        return

    # Try selecting each digit from start_index to the end
    for i in range(start_index, n):
        # Make a choice: select the digit at position i
        path.append(digits[i])

        # Explore: recursively search from the next position with updated sum
        dfs(i + 1, curr_sum + int(digits[i]), path)

        # Undo: remove the digit we just added (backtrack)
        # This allows us to try other possibilities
        path.pop()


# Start the search from position 0, with sum 0, and empty path
dfs(0, 0, [])

# Print the result
if len(solutions) == 1:
    print('There is a unique solution.')
else:
    print(f"There are {len(solutions)} solutions.")





"""
Sum of Digits - Backtracking Problem (Student Version)

This program finds all possible ways to select digits from a given number
so that the selected digits add up to a target sum.

Example:
    Input: digits = "12234", desired_sum = 5
    Output: 4 solutions
        - Select digits at positions [0,1,2]: 1 + 2 + 2 = 5
        - Select digits at positions [0,4]: 1 + 4 = 5
        - Select digits at positions [1,3]: 2 + 3 = 5
        - Select digits at positions [2,3]: 2 + 3 = 5

    Note: Each position is considered unique, even if the digit values are the same.


INSTRUCTIONS FOR STUDENTS:
    1. Complete the count_solutions() function below
    2. Test your solution by running:
       python3 -m doctest sum_of_digits.py -v
    3. All 7 tests should pass!
    4. Try the program normally:
       python3 sum_of_digits.py


HINTS:
    - Use backtracking (make a choice, explore, undo)
    - Remember to copy the path when saving a solution: solutions.append(path[:])
    - Don't return immediately when you find a solution (you can still add zeros!)
    - Use start_index to avoid counting the same combination multiple times
"""


def count_solutions(digits, desired_sum):
    """
    Count the number of ways to select digits that sum to desired_sum.

    Args:
        digits: A string of digits (e.g., "12234")
        desired_sum: The target sum (an integer)

    Returns:
        The number of valid solutions

    Test Cases:
    >>> count_solutions("12234", 5)
    4
    >>> count_solutions("11111", 5)
    1
    >>> count_solutions("1302000", 6)
    16
    >>> count_solutions("123", 6)
    1
    >>> count_solutions("123", 7)
    0
    >>> count_solutions("000", 0)
    8
    >>> count_solutions("12", 5)
    0
    """
    # TODO: Implement this function!
    # Remember:
    # 1. You need a helper function (typically called dfs) for backtracking
    # 2. Keep track of: start_index, current_sum, and path
    # 3. Save solutions when current_sum equals desired_sum
    # 4. Don't return immediately - you might be able to add zeros!
    pass  # Replace this with your implementation


# Main program - only runs when executing the file directly (not during doctest)
if __name__ == "__main__":
    import sys

    # Check if we're running doctests
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        import doctest

        print("Running tests...")
        results = doctest.testmod(verbose=True)
        print(f"\n{results.attempted} tests, {results.failed} failures")
        sys.exit(0 if results.failed == 0 else 1)

    # Normal program execution
    digits = input('Input a natural number for the available digits: ')
    desired_sum = int(input('Input a natural number for the desired sum: '))

    # Call the function to count solutions
    num_solutions = count_solutions(digits, desired_sum)

    # Print the result
    if num_solutions == 1:
        print('There is a unique solution.')
    else:
        print(f"There are {num_solutions} solutions.")