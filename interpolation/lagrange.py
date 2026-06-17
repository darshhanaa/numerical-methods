def lagrange(x, y, xp):
    n = len(x)
    result = 0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term = term * (xp - x[j]) / (x[i] - x[j])
        result += term

    return result


x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

xp = float(input("Enter interpolation point: "))

print("Interpolated value:", lagrange(x, y, xp))
