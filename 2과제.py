def ShouldInputDigit(user_input):
    while(True):
        try: int(user_input)
        except ValueError:
           return user_input
        else: 
             print("the input ",user_input,"is digit")
             user_input = input("please input the string")
   
user_input=input("please input the stringp")    
user_input=ShouldInputDigit(user_input)