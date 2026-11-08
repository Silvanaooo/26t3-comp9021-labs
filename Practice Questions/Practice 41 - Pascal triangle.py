def f2():
    L = [1]
    yield L
    while True:
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]
        yield L

n = int(input('Enter a natural number: '))

rows = []
I = f2()

for _ in range(n + 1):
    rows.append(next(I))

# width = digits of the middle element of the last row
last = rows[-1]
largest_digit = last[len(last) // 2]
width = len(str(largest_digit))

# centered, fixed-width printing
for row in rows:
    left_spaces = ' ' * width * (n - (len(row) - 1))
    body = (' ' * width).join(str(x).rjust(width) for x in row)
    print(left_spaces + body)