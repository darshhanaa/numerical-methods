# secant.py

def f(x):
    return x**3 - x - 2

x0 = float(input("Enter x0: "))
x1 = float(input("Enter x1: "))

i = 0

while True:
    if f(x1) - f(x0) == 0:
        print("Division error")
        break

    x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

    if abs(f(x2)) < 0.0001:
        break

    x0 = x1
    x1 = x2

    i += 1

print("Root:", x2)
print("Iterations:", i)
