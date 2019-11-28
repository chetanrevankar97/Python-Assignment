j = 6
str = input("Enter String to be")
printString = ''
for i in str:
    printString = printString + i
    print(" " * j + printString)
    j -= 1


nterms = int(input("Enter number"))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2

        n1 = n2
        n2 = nth
        count += 1

    '''
    Python
    '''

    data = "PYTHON"
    x = " "
    for i in range(1, len(data) + 1):
        print(x * (len(data) - i), data[0:i])

    for i in range(1, 5):
        print("*" * i)

    for i in range(5, 0, -1):
        print("*" * i)

    j = 0
    for i in range(5, 0, -1):
        print(" " * j + "*" * i)
        j += 1

    j = 4
