def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
for i in range(19):
    if i == 18:
        print(fibonacci(i), end=".")
    else:
    print(fibonacci(i), end=",")
print()
