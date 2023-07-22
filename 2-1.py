def ShouldInputDigit(user_input):
    while(True):
        try: int(user_input)
        except ValueError:
            print("the input ",user_input,"is not digit")
            user_input = input("please input the digit")
        else:
            return int(user_input)
            
def getInput():
    user_input = input("please input the digit")
    user_input = ShouldInputDigit(user_input)
    return user_input

user_first_input = getInput()

print("the digit the you input is ",user_first_input)

user_second_input = getInput()

print("the digit the you input is ",user_first_input,user_second_input)

user_third_input = getInput()

print("the digit the you input is ",user_first_input,user_second_input,user_third_input)

print("first one + second one + third one = ",int(user_first_input) + int(user_second_input) + int(user_third_input))