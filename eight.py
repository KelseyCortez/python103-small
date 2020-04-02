# prompt the user for the number to start on and the number to end on

start_num = int(input('Enter number to start '))
end_num = int(input('Enter number to end '))

count = start_num

while count <= end_num:
    print(count)
    count = count + 1