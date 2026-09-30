"""
If you write using regular division (/) in this question:

while m % 2 == 0:d
    m /= 2 # instead here
    m = int(m)
    k += 1

instead of using integer division (//), like this:

while m % 2 == 0:
    m //= 2
    k += 1
you may get the wrong answer due to floating-point inaccuracies.

Why does this happen?

This is a precision error.

When you use float division, we get the result in float rather than int.
And Float cannot represent this integer exactly.
So python shows it in a scientific notation (it is how float stores in the computer) and it is a rounded approximation,
only the first 16 significant digits remain correct.
And when you use int() to convert it, you will find it is not correct.
You are converting a damaged float. so only the first 16 digits are correct, the rest are wrong.

In short, floating-point precision errors occur because computers store decimal numbers in binary representation,
which can lead to small rounding inaccuracies in arithmetic operations.

You can try

x = 1234567890123456798234

y = 1234567890123456891827

print(x == y) # it will return False

print(float(x)) # 1.2345678901234568e+16

print(float(y)) # 1.2345678901234568e+16

print(float(x) == float(y)) # It will return True

If you're interested in learning more, you can read the official Python documentation here:
https://docs.python.org/3/tutorial/floatingpoint.html

"""

def f6_1(n: int) -> None:
    """
    Decompose an integer n into the form 2^k * m where m is odd (or 0).
    
    This is a straightforward iterative implementation that repeatedly
    divides by 2 and counts how many times the division is possible.
    """
    if not n:
        print('0 = 2^k * 0 for all integers k!')
        return
    k = 0
    m = n
    if n < 0:
        sign = "-"
    else:
        sign = ""
    # or you can simplify it:
    # sign = '-' if n < 0 else ''
    while m % 2 == 0:
        # DO NOT USE float division m /= 2, which will cause precision error
        m //= 2        # Integer division by 2.
        k += 1         # Increment power counter
    print(f'{n} = {sign}2^{k} * {abs(m)}')

def f6_2(n: int) -> None:
    """
    Decompose an integer n into the form 2^k * m where m is odd (or 0).

    This version uses the built-in divmod() function, which returns
    both the quotient and remainder at the same time.

    It repeatedly divides by 2 until the remainder is non-zero, counting how many
    times the division is possible.
    """
    if not n:
        print('0 = 2^k * 0 for all integers k!')
        return

    k = 0
    m = abs(n)
    sign = "-" if n < 0 else ""

    while True:
        q, r = divmod(m, 2)  # q = quotient, r = remainder
        if r != 0:  # Stop if remainder is not zero
            break
        m = q  # Update m with quotient
        k += 1  # Increment power counter

    print(f'{n} = {sign}2^{k} * {m}')

def f6_3(n: int) -> None:
    """
    Decompose an integer n into the form 2^k * m using recursion.
    
    This approach demonstrates a recursive solution where each recursive call
    divides the number by 2 and increments k. It uses a nested function to 
    maintain the original input value throughout the recursion.
    """
    if n == 0:
        print('0 = 2^k * 0 for all integers k!')
        return
    
    original_n = n
    sign = '-' if n < 0 else ''
    
    def decompose(num, k=0):
        abs_num = abs(num)
        if abs_num % 2 != 0:
            print(f'{original_n} = {sign}2^{k} * {abs_num}')
            return
        decompose(num // 2, k + 1)
    
    decompose(n)