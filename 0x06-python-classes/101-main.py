#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(0, (10, 0))
print(my_square)

print("--")

my_square = Square(0, (10, 10))
print(my_square)

print("--")

my_square = Square(0, (0, 0))
print(my_square)

print("--")

my_square = Square(3, (4, 1))
print(my_square)
