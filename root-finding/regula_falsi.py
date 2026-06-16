# regula_falsi.py

def f(x):
    return x**3 - x - 2

a = float(input("Enter a: "))
b = float(input("Enter b: "))

if f(a) * f(b) >= 0:
    print("Invalid interval")
    exit()

i = 0

while True:
    c = (a*f(b) - b*f(a)) / (f(b) - f(a))

    if abs(f(c)) < 0.0001:
        break

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

    i += 1

print("Root:", c)
print("Iterations:", i)
