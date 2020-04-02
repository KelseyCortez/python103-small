# print a nxn square of * characters. prompt user for n

side = int(input('Enter any side of a square: '))

for i in range(side):
    for i in range(side):
        print('*', end = '')
    print()