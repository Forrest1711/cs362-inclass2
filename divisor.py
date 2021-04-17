import sys

n = int(sys.argv[1])

for i in range(n):
    if i > 0:
        if n % i == 0:
            print(i)
