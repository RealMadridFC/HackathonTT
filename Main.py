import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import datetime as dt

# CODE TO GET CURRENT TIME
# print(dt.datetime.now())

print("WELCOME TO WebDoc")

user_name = str(input('Enter your Name'))
user_loc = str(input('Enter your complete adress in 3 lines '))
user_no = str(input('Enter your mobile no.'))

if user_name is None:
    print("INVALID")
elif user_loc is None:
    print("INVALID")
elif user_no is None:
    print('INVALID')
else:
    print("ACCOUNT CREATED")

z = []
print()
print("1.SENIOR CITIZEN WELLNESS")
print("2. TEEN HEALTH")
print("3. CHILDCARE")
print(" 4. HEALTH STATUS")
print(" 5. AMBULANCE")
ch1 = int(input('Select option according your requirement'))
if ch1 == 1:
    print('SELECTED:SENIOR CITIZEN WELLNESS')

    print()
    print("1. BASIC DIAGNOSIS AND SUGGESTION")
    print("2.DOCTOR")
    print("3.NUTRITON AND DIET")
    print("4.SET UP MEDICATION REMINDER")
    ch2 = int(input("SELECT:"))
    if ch2 == 1:

        print("We want some basic reports info of Yours for diagnosing you properly")

        print()
        BlP_Lu = eval(input("Enter your Blood pressure level"))
        BlP_Ll = eval(input("Enter your Blood pressure level"))
        Hrt_L = eval(input("Enter your Heart beat count"))

        if BlP_Lu > 140 and BlP_Lu < 125:
            print("Upper BP is not normal ")
            print("SUGGESTED : 1. REDUCE SALT IN DIET,2.GET GOOD 8 HOURS SLEEP,3.REDUCE STRESS")
        elif BlP_Ll > 90 and BlP_Ll < 70:
            print("Lower Bp is not normal")
            print("SUGGESTED : 1. REDUCE SALT IN DIET,2.GET GOOD 8 HOURS SLEEP,3.REDUCE STRESS,4. REDUCE WEIGHT")
        elif Hrt_L < 75 and Hrt_L > 128:
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
    elif ch2 == 2:
        print()
        df = pd.read_csv('C:\\Users\\krish\\OneDrive\\Documents\\csvfile.csv')
        print("OUR DOCTORS LIST:")
        print(df)
    elif ch2 == 3:
        print("SELECTED:NUTRITON AND DIET")
        print()
        print("SELECT YOUR CONDITION")
        print()
        print("1.BP and Diabities")
        print("2.Diabities")
        print('3.BP')
        print("4.NOTHING JUST NEED HEALTHY DIET")
        ch3 = int(input("SELECT:"))
        if ch3 == 1:
            print('You have BP and Diabities')
            print()
            print('DIET:')
            print()
            print('AVOID: ALCOHOL,SALT,SUGAR')
            print()
            print("INCLUDE:TOMATOES,BROCCOLI,BEANS,ORANGES")
            print()
            print("FOR MORE  ASSISTANCE CONTACT OUR TEAM")
        elif ch3 == 2:
            print('You have Diabities')
            print()
            print("DIET:")
            print()
            print("AVOID: FRIED MEATS,DEEP FRIED FISH,TOFU,REGULAR CHEESE")
            print()
            print("INCLUDE : BEANS , NUTS , WHOLEGRAINS ,BERRIES")
            print()
            print("FOR MORE  ASSISTANCE CONTACT OUR TEAM")
        elif ch3 == 3:
            print('You have Blood pressure issue ')
            print()
            print("DIET:")
            print()
            print('AVOID: FAST FOOD,TABLE SALT , FRIED FOOD')
            print()
            print('INCLUDE : OLIVE OIL , CITRUS FRUITS , BERRIES , NUTS , SEEDS')
            print()
            print("FOR MORE  ASSISTANCE CONTACT OUR TEAM")
        elif ch3 == 4:
            print("HEALTHY DIET")
            print()
            print("INCLUDE : 8 GLASSES OF WATER , WHOLE GRAINS,BEANS,DARK GREEN VEGGEIS")
            print()
            print("AVOID : FRIED FOOD , JUNK FOOD ")
            print()
            print("FOR MORE  ASSISTANCE CONTACT OUR TEAM")
        else:
            print('ERROR')

    ''' elif ch2==4:
        print("REMINDER")
        dose_n = int(input("ENter no of dose"))
        if dose_n == 3:'''
elif ch1 == 5:
    loc = user_loc
    df2 = pd.read_csv('C:\\Users\\krish\\OneDrive\\Documents\\ambulan.csv')
    # print(df2)
    print('sending help')
    print('ONE OF THE BELOW AMBULANCE WILL BE AT YOUR LOCATION IN 10 MIN')
    print(df2)
elif ch1 == 4:
    print('HEALTH STATUS')
    s = ['Diabetics', 'Blood Pressure', 'Prior Heart Diseases']
    for i in range(len(s)):
        print("Are/were you diagnosed with", s[i])
        x = input()
        if x == 'y' or 'Y':
            z.append()
        else:
            break
    print(z)
