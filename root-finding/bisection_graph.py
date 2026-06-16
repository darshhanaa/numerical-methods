import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x - 2

x = np.linspace(0, 2, 400)
y = f(x)

plt.figure(figsize=(8,5))
plt.plot(x, y, label='f(x) = x³ - x - 2')
plt.axhline(0)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Bisection Method Function Graph")
plt.legend()
plt.grid(True)

plt.savefig("../graphs/bisection_graph.png")
plt.show()
