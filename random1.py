from random import shuffle
A = input("Enter the random size: ")
x = [[i] for i in range(int(A))]
shuffle(x)
print(x)