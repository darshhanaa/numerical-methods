# Gauss Elimination Method

n = int(input("Enter number of variables: "))

# Augmented matrix
A = []

print("Enter coefficients row-wise:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

# Forward Elimination
for i in range(n):
    for j in range(i + 1, n):
        factor = A[j][i] / A[i][i]

        for k in range(n + 1):
            A[j][k] = A[j][k] - factor * A[i][k]

# Back Substitution
x = [0] * n

x[n - 1] = A[n - 1][n] / A[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    sum = 0

    for j in range(i + 1, n):
        sum += A[i][j] * x[j]

    x[i] = (A[i][n] - sum) / A[i][i]

print("\nSolution:")

for i in range(n):
    print(f"x{i+1} = {x[i]}")
