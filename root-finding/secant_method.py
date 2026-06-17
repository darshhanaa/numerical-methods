def f(x):
    return x**3 - x - 2

x0 = float(input("Enter x0: "))
x1 = float(input("Enter x1: "))

for i in range(100):
    if f(x1) - f(x0) == 0:
        print("Division by zero error")
        break

    x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

    if abs(x2 - x1) < 0.0001:
        break

    x0 = x1
    x1 = x2

print("Root:", x2)
print("Iterations:", i)
