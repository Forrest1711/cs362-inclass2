import sys


def add(n, m):
    return (n + m)


def subtract(n, m):
    return n-m


def divide(n, m):
    return n/m


def multiply(n, m):
    return n*m


N = int(sys.argv[1])
M = int(sys.argv[2])

print(N, " + ", M, " = ", add(N, M))
print(N, " - ", M, " = ", subtract(N, M))
print(N, " / ", M, " = ", divide(N, M))
print(N, " * ", M, " = ", multiply(N, M))