sum = float(input())
bills= [5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01]

for a in bills:
    c = sum // a
    sum = sum % a
    if c != 0:
        print(a, "=", c, end=' ')
        