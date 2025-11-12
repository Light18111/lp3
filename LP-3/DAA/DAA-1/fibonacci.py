recSteps = 0
iterSteps = 0

def fibRecursive(n):  # recursive Fibonacci
    global recSteps
    recSteps += 1
    if n <= 1:
        return n
    return fibRecursive(n - 1) + fibRecursive(n - 2)

def fibIterative(n):  # iterative Fibonacci
    global iterSteps
    a, b = 0, 1
    iterSteps = 1
    for i in range(2, n + 1):
        iterSteps += 1
        a, b = b, a + b
    return b

n = int(input("Enter n: "))

print("\nFibonacci Series :", end=" ")
iterSeries = []
a, b = 0, 1
for i in range(n + 1):
    iterSeries.append(a)
    a, b = b, a + b
print(*iterSeries)

recSteps = 0
recAns = fibRecursive(n)

iterSteps = 0
iterAns = fibIterative(n)

print("Fibonacci (Recursive) =", recAns)
print("Step Count (Recursive) =", recSteps)
print("Fibonacci (Iterative) =", iterAns)
print("Step Count (Iterative) =", iterSteps)
