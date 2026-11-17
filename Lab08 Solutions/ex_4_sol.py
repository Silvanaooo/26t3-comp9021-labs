def f4_1():
    """
    Reference solution: Implements a prime number iterator.
    
    This solution creates a class that can be used to iterate through
    prime numbers, generating them one by one.
    """
    class Prime:
        def __init__(self):
            Prime.p = 2

        def __iter__(self):
            return self

        def __next__(self):
            if Prime.p == 2:
                Prime.p = 1
                return 2
            else:
                while True:
                    Prime.p += 2
                    if all(Prime.p % k for k in range(3, Prime.p // 2 + 1, 2)):
                        return Prime.p
    
    return Prime


def f4_2():
    """
    Beginner-friendly version: Implements a prime number iterator
    with detailed comments and simplified logic.
    """
    class Prime:
        """
        Iterator class that generates prime numbers in sequence.
        
        This class implements the iterator protocol, allowing it to be used
        in for loops and other iteration contexts to generate prime numbers
        one by one, starting from 2.
        
        Methods:
            __init__(): Constructor to initialize the iterator
            __iter__(): Returns the iterator object itself
            __next__(): Returns the next prime number in the sequence
        """
        def __init__(self):
            """
            Initialize the prime number iterator.
            
            Sets up a class variable to track the current state of the iterator.
            Initially set to 2, which is the first prime number.
            """
            # Class variable to track the current state
            Prime.p = 2

        def __iter__(self):
            """
            Return the iterator object itself.
            
            This method is required for the iterator protocol and allows
            the object to be used in for loops.
            
            Returns:
                self: The iterator object
            """
            return self

        def __next__(self):
            """
            Generate and return the next prime number in the sequence.
            
            This method implements the core logic for finding prime numbers:
            1. Special case for the first prime number (2)
            2. For subsequent primes, check odd numbers starting from 3
            
            Returns:
                int: The next prime number in the sequence
            """
            # Special case for the first prime number (2)
            if Prime.p == 2:
                # Set p to 1 so that the next call will start checking from 3
                Prime.p = 1
                return 2
            else:
                # Keep incrementing by 2 (checking only odd numbers)
                # until we find the next prime
                while True:
                    Prime.p += 2  # Increment by 2 to check only odd numbers
                    
                    # Check if Prime.p is prime by testing divisibility
                    # We only need to check odd divisors up to Prime.p // 2
                    is_prime = True
                    for k in range(3, Prime.p // 2 + 1, 2):
                        if Prime.p % k == 0:  # If divisible, not prime
                            is_prime = False
                            break
                    
                    # If we found a prime, return it
                    if is_prime:
                        return Prime.p