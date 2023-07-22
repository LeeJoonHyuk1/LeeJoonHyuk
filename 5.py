from email.message import EmailMessage
import ssl
import smtplib

import random1 as code_generator

emailSender="sjshxukska@gmail.com"
receiverAdress=input("Please enter your email address")
emailPassword= "epztokmkcgkdmstw"

verf_code=code_generator.generate_code()
subject="인증 메일입니다. {verf_code}"

    


em=EmailMessage()
em["From"]=emailSender
em["To"]=receiverAdress
em["subject"]=subject
body = f'''
    your verification code is {verf_code}
'''
em.set_content(body)


context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(emailSender , emailPassword)
    smtp.sendmail(emailSender,receiverAdress , em.as_string())
    
user_input= input("Please enter the verification code you received: ")
if user_input == verf_code:
    print("True")
else:
    print("False")
