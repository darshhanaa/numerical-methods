def f(x):
    return x**3 - x - 2

a = float(input("Enter lower bound (a): "))
b = float(input("Enter upper bound (b): "))

if f(a) * f(b) >= 0:
    print("Invalid interval. f(a) and f(b) must have opposite signs.")
    exit()

for i in range(100):
    c = (a + b) / 2

    if abs(f(c)) < 0.0001:
        break

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print("Root:", c)
print("Iterations:", i)
