def f1_1():
    """
    Reference solution: Implements a prime number validation and storage class.
    """
    from math import sqrt

    class PrimeError(Exception):
        pass

    class Prime:
        primes = set()

        def reset():
            Prime.primes = set()

        def __init__(self, p):
            if not isinstance(p, int) or p < 2\
               or any(p % k == 0 for k in range(2, round(sqrt(p)) + 1)):
                raise PrimeError(f'{p} is not a prime number')
            if p in Prime.primes:
                raise PrimeError(f'We have seen {p} before')
            Prime.primes.add(p)

    return PrimeError, Prime


def f1_2():
    """
    Beginner-friendly version: Implements a prime number validation and storage class
    with detailed comments and simplified logic.
    """
    from math import sqrt

    class PrimeError(Exception):
        """
        Custom exception class for handling prime number related errors.

        Raised when the input is not a prime number or has been added before.
        """
        pass

    class Prime:
        """
        Prime number class for validating and storing prime numbers.

        Attributes:
            primes (set): Class variable to store all prime numbers that have been created

        Methods:
            reset(): Static method to reset the set of stored prime numbers
            __init__(p): Constructor to validate and store a new prime number
        """
        # Class variable to store all prime numbers that have been created
        primes = set()

        @staticmethod
        def reset():
            """
            Reset the set of stored prime numbers.

            Call this method when you need to clear all stored prime numbers.
            """
            Prime.primes = set()

        def __init__(self, p):
            """
            Create a new prime number instance.

            Args:
                p: The value to validate and store

            Raises:
                PrimeError: When the input is not an integer, less than 2,
                           not a prime number, or has been added before
            """
            # Check if the input is an integer and at least 2
            if not isinstance(p, int):
                raise PrimeError(f'{p} is not a prime number')

            if p < 2:
                raise PrimeError(f'{p} is not a prime number')

            # Check if the input is a prime number
            # Only need to check up to sqrt(p) because if p has a factor,
            # at least one of them is less than or equal to sqrt(p)
            for k in range(2, int(sqrt(p)) + 1):
                if p % k == 0:
                    raise PrimeError(f'{p} is not a prime number')

            # Check if the input has been added before
            if p in Prime.primes:
                raise PrimeError(f'We have seen {p} before')

            # Add the validated prime number to the set
            Prime.primes.add(p)