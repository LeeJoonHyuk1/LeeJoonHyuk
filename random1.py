import string
import random

code=list(string.ascii_letters+string.digits+"!@#$%^&*()")

def generate_code():
    random.shuffle(code)
    
    verify_code=[]
    for X in range(0,10):
        verify_code.append(random.choice(code))
        
    random.shuffle(verify_code)
    
    fullcode="".join(verify_code)
    return fullcode
    
generate_code()        
