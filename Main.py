import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import datetime as dt

# CODE TO GET CURRENT TIME
#print(dt.datetime.now())

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

    print()
    print("1. BASIC DIAGNOSIS AND SUGGESTION")
    print("2.DOCTOR")
    print("3.NUTRITON AND DIET")
    print("4.SET UP MEDICATION REMINDER")
    ch2=int(input("SELECT:"))
    if ch2==1:

        print("We want some basic reports info of Yours for diagnosing you properly")

        print()
        BlP_Lu = eval(input("Enter your Blood pressure level"))
        BlP_Ll = eval(input("Enter your Blood pressure level"))
        Hrt_L = eval(input("Enter your Heart beat count"))

        if BlP_Lu >140 and BlP_Lu<125:
            print("Upper BP is not normal ")
            print("SUGGESTED : 1. REDUCE SALT IN DIET,2.GET GOOD 8 HOURS SLEEP,3.REDUCE STRESS")
        elif BlP_Ll > 90 and BlP_Ll<70:
            print("Lower Bp is not normal")
            print("SUGGESTED : 1. REDUCE SALT IN DIET,2.GET GOOD 8 HOURS SLEEP,3.REDUCE STRESS,4. REDUCE WEIGHT")
        elif Hrt_L <75 and Hrt_L>128:
            print("IRREGULAR HEART RATE")
            print("SUGGESTED : VISIT DOCTOR")
        else:
            print('error')
        print('SELECT YOUR CONDITION')
        print()
        print("1.DIABETIC")
        print("2.NON-DIABETIC")
        cond_d = int(input('ENTER CONDTION'))
        if cond_d == 1:
            print("DIABETIC")
            print("SUGGESTED:Eat foods that are rich in chromium and magnesium,reduce stress")
        else:
            print('NON DIABETIC')
    elif ch2==2:
        print()
    elif ch2==3:
        print("SELECTED:NUTRITON AND DIET")



    '''elif ch2==4:
        print("REMINDER")
        dose_n = int(input("ENter no of dose"))
        if dose_n == 3:'''






