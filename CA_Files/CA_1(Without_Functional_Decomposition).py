#Sending and generating OTP as a program without Functional decomposition

import math
import random
import smtplib

def generate_otp():
    
    digits="0123456789"
    OTP=""
    n=(int(input("Enter your range of otp ")))

    for i in range(n):
        OTP+=digits[math.floor(random.random()*10)]
        otp = OTP + " is your OTP"
    return otp

def send_email():
    
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.starttls() 
    server.login('sender_email@gmail.com',password="xxxx xxxx xxxx xxxx") 
    vars=generate_otp()
    msg=str(vars)

    receivers_email=input("Enter receivers email ")
    
    server.sendmail('sender_email@gmail.com',receivers_email,msg)
    server.quit()
    

send_email()