numbers = [11,22,33,44,55,66,77,88]


for number in numbers:
    print(number)

indexInput = int(input('Enter Index to get number: '))

if indexInput< len(numbers):
    print(numbers[indexInput])
else: 
    print("Invalid Index " + indexInput)    
