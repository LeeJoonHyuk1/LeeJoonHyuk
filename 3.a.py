numbers = []
while(True):
    number= input("input score\n")
    if(number == "stop"):
        break
    try:
        number = int(number)
        numbers.append(number)
    except ValueError:
        print("Please input a number")
   
numbers.sort(reverse=True)
print(numbers)
numbers.sort()
print(numbers)


