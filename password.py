import random
import string
import sys

numby = int(sys.argv[1])

arr = ""

for i in range(numby):
    randomLetter = random.choice(string.ascii_letters)
    arr += (randomLetter)

print(arr)
