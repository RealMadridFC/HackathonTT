import pandas as pd
import numpy as np
import matplotlib.pyplot as pl



print("WELCOME TO WebDoc")


user_name = eval(input('Enter your Name'))
user_loc = eval(input('Enter your complete adress in 3 lines '))
user_no = eval(input('Enter your mobile no.'))


if user_name is None:
    print ("INVALID")
elif user_loc is None:
    print("INVALID")
elif user_no is None:
    print('INVALID')
else:
    print("ACCOUNT CREATED")


print()
print("1.SENIOR CITIZEN WELLNESS")
print("2. TEEN HEALTH")
print("3. CHILDCARE")
print(" 4. HEALTH STATUS")
print(" 5. AMBULANCE")
ch1 = int(input('Select option according your requirement'))
if ch1==1:
    print('SELECTED:SENIOR CITIZEN WELLNESS')
    print("We want some basic reports info of Yours for diagnosing you properly")

    print()
    BlP_Lu = eval(input("Enter your Blood pressure level"))
    BlP_Ll = eval(input("Enter your Blood pressure level"))
    Hrt_L = eval(input("Enter your Heart beat count"))
    Db_Lbf = eval(input("Enter sugar level before breakfast(Fasting)"))
    Db_Laf = eval(input("Enter sugar level after meal"))

    if BlP_Lu >140 and BlP_Lu<125:


