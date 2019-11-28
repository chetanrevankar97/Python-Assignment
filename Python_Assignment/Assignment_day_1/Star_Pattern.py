for i in range(4):
    print("*" * i)


for i in range(3, 0, -1):
    print("*" * i)


j = 0
for i in range(3, 0, -1):
    print(" " * j + "*" * i)
    j += 1

j = 4
for i in range(4):
    print(" " * j + "*" * i)
    j -= 1


size = 3
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")