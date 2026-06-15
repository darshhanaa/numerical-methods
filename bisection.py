

def f(x):
    return x**3 - x - 2

a = float(input("Enter a: "))
b = float(input("Enter b: "))

if f(a) * f(b) >= 0:
    print("Invalid interval")
    exit()

i = 0

while (b - a) >= 0.0001:
    c = (a + b) / 2

    if f(c) == 0:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

    i += 1

print("Root:", c)
print("Iterations:", i)
