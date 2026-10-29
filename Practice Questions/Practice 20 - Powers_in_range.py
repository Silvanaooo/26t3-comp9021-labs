from collections import defaultdict

# Read two positive integers separated by space
b = 2
m, n = (int(x) for x in input('Input two positive integers: ').split())

# Dictionary mapping each value to a list of (base, power) pairs.
# We use defaultdict(list) because a single number can have several (base, power) pairs,
# and we need to collect them into a list automatically without checking if the key already exists.
solutions = defaultdict(list)

# Enumerate possible bases b starting from 2.
# Stop when b^2 > n, since p >= 2 means smallest power is b^2.
while b * b <= n:
    p = 2
    result = b * b

    # For each base, keep multiplying by b (increase power)
    # until the result exceeds n.
    while result <= n:
        # If result is within the interval [m, n], record the pair (b, p).
        if result >= m:
            solutions[result].append((b, p))
        result *= b
        p += 1

    # Move to next base
    b += 1

# Compute field width for aligned output (only if we found any result)
if solutions:
    answer_width = len(str(max(k for k in solutions)))

    # Print results in increasing order of the value (answers)
    for value in sorted(solutions):
        # For each (base, power) pair corresponding to this value
        for base, power in sorted(solutions[value]):
            # Right-align the numbers according to answer_width
            print(f"{value:>{answer_width}} = {base}^{power}")
