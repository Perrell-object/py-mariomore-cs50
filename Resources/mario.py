# TODO
from cs50 import get_int

# get user input check if valid
while True:
    n = int(input("Height: "))
    if n >= 1 and n <= 8:
        break
    elif n < 1 or n > 8:
        print("\nPlease enter a number between 1 and 8")
# print pryamid
for i in range(n):
    print(" " * (n - 1 - i), end="")
    print("#" * (i + 1), end="")
    print(" " * 2, end="")
    print("#" * (i + 1), end="")
    print(end="\n")