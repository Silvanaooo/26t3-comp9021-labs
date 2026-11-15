from collections import defaultdict

# global counter: how many times each fibo(n) is computed across calls
fib_calls = defaultdict(int)

def f6(n):
    """
    This function prints a readable recursion trace for fibonacci numbers.
    Indentation reflects recursion depth (one tab per level).

    n : int the target n (n >= 0)
    """
    _f6(n, nb_of_tabs=0)

def _f6(n, nb_of_tabs):
    """
    recursive helper that computes fibo(n) and prints a trace.

    n : int
        the current n to compute
    nb_of_tabs : int
        how many tab characters to print for indentation at this level
    """
    # step 1: on entry, bump the counter and print the "starting" line
    fib_calls[n] += 1
    print('\t' * nb_of_tabs + f'Computation nb {fib_calls[n]} of fibo({n})...')

    # step 2: base cases
    # step 2: base cases
    if n < 2:
        result = n
    else:
        # step 3: recursive case; go one level deeper for each subcall
        left = _f6(n - 1, nb_of_tabs + 1)
        right = _f6(n - 2, nb_of_tabs + 1)
        result = left + right

    # step 4: after subcalls return, print the "computed as" line
    print('\t' * nb_of_tabs + f'... computed as {result}')
    return result