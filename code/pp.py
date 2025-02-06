N = int(input("Enter N: "))
current_number = 2

while current_number <= N:
    if current_number % 2 == 0:
        print(current_number)
    current_number += 1