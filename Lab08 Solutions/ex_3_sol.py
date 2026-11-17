def f3_1():
    """
    Reference solution: Extends the Modulo class with additional operations.
    
    This solution adds a ModuloError exception class and implements addition
    and multiplication operations for modular arithmetic.
    """
    class IntError(Exception):
        pass
        
    class PrimeError(Exception):
        pass
    
    class ModuloError(Exception):
        pass

    class Modulo:
        def __init__(self, k, p):
            if not isinstance(p, int) or p < 2\
               or any(p % k == 0 for k in range(2, p // 2 + 1)):
                raise PrimeError(f'{p} is not a prime number')
            if not isinstance(k, int):
                raise IntError(f'{k} is not an integer')
            self.modulus = p
            self.k = k % p

        def _validate(self, m):
            if not isinstance(m, Modulo):
                raise ModuloError(f'{m} is not a Modulo object')
            if m.modulus != self.modulus:
                raise ModuloError(f'{self} and {m} do not have the same modulus')         

        def __repr__(self):
            return f'Modulo({self.k}, {self.modulus})'

        def __str__(self):
            return f'{self.k} (mod {self.modulus})'

        def __add__(self, m):
            self._validate(m)
            return Modulo(self.k + m.k, self.modulus)
            
        def __iadd__(self, m):
            self._validate(m)
            self.k = (self.k + m.k) % self.modulus
            return self

        def __mul__(self, m):
            self._validate(m)
            return Modulo(self.k * m.k, self.modulus)
            
        def __imul__(self, m):
            self._validate(m)
            self.k = self.k * m.k % self.modulus
            return self


def f3_2():
    """
    Beginner-friendly version: Extends the Modulo class with additional operations
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
    
    class ModuloError(Exception):
        """
        Custom exception class for handling modular arithmetic errors.
        
        Raised when operations are performed on incompatible Modulo objects
        or when an object is not a Modulo instance.
        """
        pass

    class Modulo:
        """
        Class representing a number in modular arithmetic with arithmetic operations.
        
        In modular arithmetic, numbers "wrap around" after reaching a certain value (the modulus).
        This class supports addition and multiplication operations between Modulo objects.
        
        Attributes:
            modulus (int): The modulus (must be a prime number)
            k (int): The value in the modular system (0 <= k < modulus)
        
        Methods:
            __init__(k, p): Constructor to create a new modular number
            _validate(m): Helper method to validate another Modulo object for operations
            __repr__(): Returns the formal string representation
            __str__(): Returns the human-readable string representation
            __add__(m): Implements addition with another Modulo object (returns new object)
            __iadd__(m): Implements in-place addition with another Modulo object
            __mul__(m): Implements multiplication with another Modulo object (returns new object)
            __imul__(m): Implements in-place multiplication with another Modulo object
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
            is_prime = True
            for i in range(2, p // 2 + 1):
                if p % i == 0:  # If p is divisible by i, then p is not prime
                    is_prime = False
                    break
            
            if not is_prime:
                raise PrimeError(f'{p} is not a prime number')
            
            # Check if k is an integer
            if not isinstance(k, int):
                raise IntError(f'{k} is not an integer')
            
            # Store the modulus and the value
            # The value is stored as k modulo p (remainder when k is divided by p)
            self.modulus = p
            self.k = k % p

        def _validate(self, m):
            """
            Validate that another object is a compatible Modulo object.
            
            This helper method checks that:
            1. The other object is a Modulo instance
            2. The other object has the same modulus as this one
            
            Args:
                m: The object to validate
                
            Raises:
                ModuloError: When m is not a Modulo object or has a different modulus
            """
            # Check if m is a Modulo object
            if not isinstance(m, Modulo):
                raise ModuloError(f'{m} is not a Modulo object')
            
            # Check if m has the same modulus
            if m.modulus != self.modulus:
                raise ModuloError(f'{self} and {m} do not have the same modulus')

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

        def __add__(self, m):
            """
            Add another Modulo object to this one (returns a new object).
            
            In modular arithmetic, addition is performed by adding the values
            and then taking the result modulo the modulus.
            
            Args:
                m: Another Modulo object with the same modulus
                
            Returns:
                Modulo: A new Modulo object representing the sum
                
            Raises:
                ModuloError: When m is not a Modulo object or has a different modulus
            """
            # Validate the other object
            self._validate(m)
            
            # Create a new Modulo object with the sum of values
            # The modulo operation is handled in the constructor
            return Modulo(self.k + m.k, self.modulus)
            
        def __iadd__(self, m):
            """
            Add another Modulo object to this one in-place.
            
            This modifies the current object instead of creating a new one.
            
            Args:
                m: Another Modulo object with the same modulus
                
            Returns:
                Modulo: This object, modified
                
            Raises:
                ModuloError: When m is not a Modulo object or has a different modulus
            """
            # Validate the other object
            self._validate(m)
            
            # Update the value of this object
            # Explicitly apply modulo to ensure the result is in range
            self.k = (self.k + m.k) % self.modulus
            
            # Return this object (required for in-place operators)
            return self

        def __mul__(self, m):
            """
            Multiply this Modulo object by another one (returns a new object).
            
            In modular arithmetic, multiplication is performed by multiplying the values
            and then taking the result modulo the modulus.
            
            Args:
                m: Another Modulo object with the same modulus
                
            Returns:
                Modulo: A new Modulo object representing the product
                
            Raises:
                ModuloError: When m is not a Modulo object or has a different modulus
            """
            # Validate the other object
            self._validate(m)
            
            # Create a new Modulo object with the product of values
            # The modulo operation is handled in the constructor
            return Modulo(self.k * m.k, self.modulus)
            
        def __imul__(self, m):
            """
            Multiply this Modulo object by another one in-place.
            
            This modifies the current object instead of creating a new one.
            
            Args:
                m: Another Modulo object with the same modulus
                
            Returns:
                Modulo: This object, modified
                
            Raises:
                ModuloError: When m is not a Modulo object or has a different modulus
            """
            # Validate the other object
            self._validate(m)
            
            # Update the value of this object
            # Explicitly apply modulo to ensure the result is in range
            self.k = (self.k * m.k) % self.modulus
            
            # Return this object (required for in-place operators)
            return self