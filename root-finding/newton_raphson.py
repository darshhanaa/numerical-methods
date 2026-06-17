def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

x = float(input("Enter initial guess: "))
i = 0

while True:
    x_new = x - f(x)/df(x)

    if abs(x_new - x) < 0.0001:
        break

    x = x_new
    i += 1
print("Root:", x_new)
print("Iterations:", i)
