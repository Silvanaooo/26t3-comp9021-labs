def f2_1():
    """
    Reference solution: Implements modular arithmetic with validation.
    
    This solution defines two exception classes and a Modulo class for
    representing and validating modular arithmetic operations.
    """
    class IntError(Exception):
        pass
        
    class PrimeError(Exception):
        pass

    class Modulo:
        def __init__(self, k, p):
            # Validate that p is a prime number
            if not isinstance(p, int) or p < 2\
               or any(p % k == 0 for k in range(2, p // 2 + 1)):
                raise PrimeError(f'{p} is not a prime number')
            # Validate that k is an integer
            if not isinstance(k, int):
                raise IntError(f'{k} is not an integer')
            # Store the modulus and the value
            self.modulus = p
            self.k = k % p

        def __repr__(self):
            return f'Modulo({self.k}, {self.modulus})'

        def __str__(self):
            return f'{self.k} (mod {self.modulus})'


def f2_2():
    """
    Beginner-friendly version: Implements modular arithmetic with validation
    using detailed comments and simplified logic.
    """
    class IntError(Exception):
        """
        Custom exception class for handling integer-related errors.
        
        Raised when a value that should be an integer is not.
        """
        pass
        
    class PrimeError(Exception):
        """
        Custom exception class for handling prime number related errors.
        
        Raised when a value that should be a prime number is not.
        """
        pass

    class Modulo:
        """
        Class representing a number in modular arithmetic.
        
        In modular arithmetic, numbers "wrap around" after reaching a certain value (the modulus).
        For example, in mod 5, the numbers are 0, 1, 2, 3, 4, and then back to 0.
        
        Attributes:
            modulus (int): The modulus (must be a prime number)
            k (int): The value in the modular system (0 <= k < modulus)
        
        Methods:
            __init__(k, p): Constructor to create a new modular number
            __repr__(): Returns the formal string representation
            __str__(): Returns the human-readable string representation
        """
        def __init__(self, k, p):
            """
            Create a new modular number.
            
            Args:
                k (int): The value in the modular system
                p (int): The modulus (must be a prime number)
                
            Raises:
                PrimeError: When p is not a prime number
                IntError: When k is not an integer
            """
            # Check if p is an integer and at least 2
            if not isinstance(p, int):
                raise PrimeError(f'{p} is not a prime number')
                
            if p < 2:
                raise PrimeError(f'{p} is not a prime number')
            
            # Check if p is a prime number
            # A prime number is only divisible by 1 and itself
            for n in range(2, p):
                if p % n == 0:
                    raise PrimeError(f'{p} is not a prime number')
            
            # Check if k is an integer
            if not isinstance(k, int):
                raise IntError(f'{k} is not an integer')
            
            # Store the modulus and the value
            # The value is stored as k modulo p (remainder when k is divided by p)
            self.modulus = p
            self.k = k % p

        def __repr__(self):
            """
            Return the formal string representation of the modular number.
            
            This is used for debugging and should ideally be able to recreate the object.
            
            Returns:
                str: A string in the format 'Modulo(k, modulus)'
            """
            return f'Modulo({self.k}, {self.modulus})'

        def __str__(self):
            """
            Return the human-readable string representation of the modular number.
            
            This is used for display purposes.
            
            Returns:
                str: A string in the format 'k (mod modulus)'
            """
            return f'{self.k} (mod {self.modulus})'
