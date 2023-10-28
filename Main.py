import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import datetime as dt
from playsound import playsound as ps
# CODE TO GET CURRENT TIME
#print(dt.datetime.now())
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
zz = 'y'
z = []
while zz == 'y':
    print()
    print("1.SENIOR CITIZEN WELLNESS")
    print("2. TEEN HEALTH")
    print("3. CHILDCARE")
    print("4. HEALTH STATUS")
    print("5. AMBULANCE")
    ch1 = int(input('Select option according your requirement'))
    if ch1==1:
        c = 'y'
        while c=='y':
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

                if 140 < BlP_Lu < 125:
                    print("Upper BP is not normal ")
                    print("SUGGESTED : 1. REDUCE SALT IN DIET,2.GET GOOD 8 HOURS SLEEP,3.REDUCE STRESS")
                elif 90 < BlP_Ll < 70:
                    print("Lower Bp is not normal")
                    print("SUGGESTED : 1. REDUCE SALT IN DIET,2.GET GOOD 8 HOURS SLEEP,3.REDUCE STRESS,4. REDUCE WEIGHT")
                elif 75 > Hrt_L > 128:
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
                c = input("Enter y to go back to Senior Citizens' page")
            elif ch2 == 2:
                print()
                df=pd.read_csv('C:\\Users\\krish\\OneDrive\\Documents\\csvfile.csv')
                print("OUR DOCTORS LIST:")
                print(df)
                c = input("Enter y to go back to Senior Citizens' page")
            elif ch2 == 3:
                cc = 'y'
                print("SELECTED:NUTRITON AND DIET")
                print()
                print("SELECT YOUR CONDITION")
                print()
                print("1.BP and Diabetes")
                print("2.Diabetes")
                print('3.BP')
                print("4.NOTHING JUST NEED HEALTHY DIET")
                ch3=int(input("SELECT:"))
                while cc == 'y':
                    if ch3==1:
                        print('You have BP and Diabetes')
                        print()
                        print('DIET:')
                        print()
                        print('AVOID: ALCOHOL,SALT,SUGAR')
                        print()
                        print("INCLUDE:TOMATOES,BROCCOLI,BEANS,ORANGES")
                        print()
                        print("FOR MORE  ASSISTANCE CONTACT OUR TEAM")
                        cc = input("Enter y to check other diets")
                    elif ch3==2:
                        print('You have Diabetes')
                        print()
                        print("DIET:")
                        print()
                        print("AVOID: FRIED MEATS,DEEP FRIED FISH,TOFU,REGULAR CHEESE")
                        print()
                        print("INCLUDE : BEANS , NUTS , WHOLEGRAINS ,BERRIES")
                        print()
                        print("FOR MORE  ASSISTANCE CONTACT OUR TEAM")
                        cc = input("Enter y to check other diets")
                    elif ch3==3:
                        print('You have Blood pressure issue ')
                        print()
                        print("DIET:")
                        print()
                        print('AVOID: FAST FOOD,TABLE SALT , FRIED FOOD')
                        print()
                        print('INCLUDE : OLIVE OIL , CITRUS FRUITS , BERRIES , NUTS , SEEDS')
                        print()
                        print("FOR MORE  ASSISTANCE CONTACT OUR TEAM")
                        cc = input("Enter y to check other diets")
                    elif ch3==4:
                        print("HEALTHY DIET")
                        print()
                        print("INCLUDE : 8 GLASSES OF WATER , WHOLE GRAINS,BEANS,DARK GREEN VEGGEIS")
                        print()
                        print("AVOID : FRIED FOOD , JUNK FOOD ")
                        print()
                        print("FOR MORE  ASSISTANCE CONTACT OUR TEAM")
                        cc = input("Enter y to check other diets")
                    else:
                        print('ERROR')
                        cc = input("Enter y to check other diets")
                c = input("Enter y to go back to Senior Citizens' page")
            elif ch2==4:
                print("REMINDER")
                '''df2=pd.read_csv('C:\\Users\\krish\\OneDrive\\Documents\\ambulan.csv')
                print(df2)'''
                dose_n = int(input('Enter no of dosage you take in a day'))
                if dose_n ==1:
                    rem_hour1 = int(input('Enter Hour'))
                    rem_min1 = int(input('Enter minute'))
                    rem_am1 = input("am/pm: ")
                    if rem_am1 =="pm":
                        rem_hour1+=12
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                elif dose_n ==2:
                    rem_hour1 = int(input('Enter Hour(1 DOSE)'))
                    rem_min1 = int(input('Enter minute(1 DOSE)'))
                    rem_am1 = input("am/pm:(1 DOSE) ")
                    rem_hour2 = int(input('Enter Hour(2 DOSE)'))
                    rem_min2 = int(input('Enter minute(2 DOSE)'))
                    rem_am2 = input("am/pm:(2 DOSE) ")

                    if rem_am1 =="pm" and rem_am2 == "pm":
                        rem_hour1+=12
                        rem_hour2+=12
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                            elif rem_hour2==dt.datetime.now().hour and rem_min2==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 2 nd DOSE')
                    elif rem_am1=="pm" and rem_am2 =="am":
                        rem_am1+=12
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                            elif rem_hour2==dt.datetime.now().hour and rem_min2==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 2 nd DOSE')
                    elif rem_am1=="am" and rem_am2=="pm":
                        rem_am2+=12
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                            elif rem_hour2==dt.datetime.now().hour and rem_min2==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 2 nd DOSE')
                    elif rem_am1=="am" and rem_am2=="am":
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                            elif rem_hour2==dt.datetime.now().hour and rem_min2==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 2 nd DOSE')
                elif dose_n ==3:
                    rem_hour1 = int(input('Enter Hour(1 DOSE)'))
                    rem_min1 = int(input('Enter minute(1 DOSE)'))
                    rem_am1 = input("am/pm:(1 DOSE) ")

                    rem_hour2 = int(input('Enter Hour(2 DOSE)'))
                    rem_min2 = int(input('Enter minute(2 DOSE)'))
                    rem_am2 = input("am/pm:(2 DOSE) ")

                    rem_hour3 = int(input('Enter Hour(3 DOSE)'))
                    rem_min3 = int(input('Enter minute(3 DOSE)'))
                    rem_am3 = input("am/pm:(3 DOSE) ")

                    if rem_am1 =="pm" and rem_am2=="pm" and rem_am3 =='pm':
                        rem_hour1+=12
                        rem_hour2+=12
                        rem_hour3+=12
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                            elif rem_hour2==dt.datetime.now().hour and rem_min2==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 2 nd DOSE')
                            elif rem_hour3==dt.datetime.now().hour and rem_min3==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 3 nd DOSE')

                    elif rem_am1 =="am" and rem_am2=="pm" and rem_am3 =='pm':
                        #rem_hour1+=12
                        rem_hour2+=12
                        rem_hour3+=12
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                            elif rem_hour2==dt.datetime.now().hour and rem_min2==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 2 nd DOSE')
                            elif rem_hour3==dt.datetime.now().hour and rem_min3==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 3 nd DOSE')
                    elif rem_am1 =="pm" and rem_am2=="am" and rem_am3 =='pm':
                        rem_hour1+=12
                        #rem_hour2+=12
                        rem_hour3+=12
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                            elif rem_hour2==dt.datetime.now().hour and rem_min2==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 2 nd DOSE')
                            elif rem_hour3==dt.datetime.now().hour and rem_min3==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 3 nd DOSE')
                    elif rem_am1 =="pm" and rem_am2=="pm" and rem_am3 =='am':
                        rem_hour1+=12
                        rem_hour2+=12
                        #rem_hour3+=12
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                            elif rem_hour2==dt.datetime.now().hour and rem_min2==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 2 nd DOSE')
                            elif rem_hour3==dt.datetime.now().hour and rem_min3==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 3 nd DOSE')
                    elif rem_am1 =="am" and rem_am2=="am" and rem_am3 =='pm':
                        #rem_hour1+=12
                        #rem_hour2+=12
                        rem_hour3+=12
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                            elif rem_hour2==dt.datetime.now().hour and rem_min2==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 2 nd DOSE')
                            elif rem_hour3==dt.datetime.now().hour and rem_min3==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 3 nd DOSE')
                    elif rem_am1 =="pm" and rem_am2=="am" and rem_am3 =='am':
                        rem_hour1+=12
                        #rem_hour2+=12
                        #rem_hour3+=12
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                            elif rem_hour2==dt.datetime.now().hour and rem_min2==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 2 nd DOSE')
                            elif rem_hour3==dt.datetime.now().hour and rem_min3==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 3 nd DOSE')
                    elif rem_am1 =="am" and rem_am2=="pm" and rem_am3 =='am':
                        #rem_hour1+=12
                        rem_hour2+=12
                        #rem_hour3+=12
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                            elif rem_hour2==dt.datetime.now().hour and rem_min2==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 2 nd DOSE')
                            elif rem_hour3==dt.datetime.now().hour and rem_min3==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 3 nd DOSE')
                    if rem_am1 =="am" and rem_am2=="am" and rem_am3 =='am':
                        '''rem_hour1+=12
                        rem_hour2+=12
                        rem_hour3+=12'''
                        while True:
                            if rem_hour1==dt.datetime.now().hour and rem_min1==dt.datetime.now().minute:
                                print("TAKE YOUR MEDICINES 1")
                                #ps("C:\\Users\\krish\\OneDrive\\Documents\20\ring.mp3")
                                break
                            elif rem_hour2==dt.datetime.now().hour and rem_min2==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 2 nd DOSE')
                            elif rem_hour3==dt.datetime.now().hour and rem_min3==dt.datetime.now().minute:
                                print('TAKE YOUR MEDICINES 3 nd DOSE')
                            else:
                                exit
                else:
                    exit
                c = input("Enter y to go back to Senior Citizens' page")
            else:
                exit
        zz = input("Enter y to continue:")
    elif ch1 == 2:
        import matplotlib.pyplot as pl
        print("Hello ! How has your Day been?")
        a = int(input("1 : Stress Levels and Management\n2 : Nutrition\n3 : Consult a Doctor"))
        if a == 1:
            aa = 0
            print("Please answer these few questions")
            print(
                "*Please note that this is not a diagnostic tool. Only a professional can identify the real issue\n1:Never to 5:Always")
            x = int(input("Do you have trouble staying at the present moment?"))
            aa += x
            x = int(input("Do you struggle to fall asleep at night?"))
            aa += x
            x = int(input("On average, do you get less than 7-8 hours of sleep a night? "))
            aa += x
            x = int(input("Do you experience headaches or muscle tension?"))
            aa += x
            x = int(input("Do you have problem in concentrating in your tasks?"))
            aa += x
            if aa >= 21:
                print("You show symptoms of HIGH LEVEL stress")
                print("Please seek help and indulge in activities like Yoga and Meditation")
                print("You are not alone")
                if aa >= 25:
                    print("Call our doctor and seek guidance. It's FREE :)")
                    print("Dr.Keerthana : 7992739048")
            if 10 < aa < 21:
                print("You have shown symptoms of MODERATE stress levels")
                if 10 < aa < 14:
                    print("A moderate stress is required and is healthy. Maintain your stress in this level")
                if 14 < aa < 21:
                    print(
                        "Though your levels seem to be moderate it is very close to high levels. Adopt habits like excercise,yoga and meditation.")
            if aa <= 10:
                print("You have LOW levels of stress")
                if 1 <= aa <= 6:
                    print(
                        "Though Low levels are healthy and compromising, a little stress is required to have you driven in your life.")
        xx = [(aa * 10 / 3), 100]
        pl.pie(xx, labels=["Your stress", "Total"])
        pl.show()

        #if a == 2:
        zz = input("Enter y to continue:")
    elif ch1==5:
        loc = user_loc
        df2=pd.read_csv('C:\\Users\\krish\\OneDrive\\Documents\\ambulan.csv')
        #print(df2)
        print('sending help')
        print('ONE OF THE BELOW AMBULANCE WILL BE AT YOUR LOCATION IN 10 MIN')
        print(df2)
        zz = input("Enter y to continue:")
    elif ch1 == 4:
        print('HEALTH STATUS')
        print()
        print("Are you diabetic")
        d_a = input("yes/no: ")
        if d_a =="yes":
            print("AS ANSWERED YOU ARE DIABETIC")
            print()
            print('Are you victim of high BP?')
            b_a = input("yes/no: ")
            if b_a=="yes":
                print('DIABETIES AND BP PATIENT')
                print()
                print("Are you suffering from any heart diseases")
                h_a = input("yes/no: ")
                if h_a == "yes":
                    print ('YOU ARE AT VERY CRITICAL STAGE')
                    #readcsv doctors
                elif h_a =="no":
                    print("You are at borderline of critical stage")
                    print('SUGGESTED : VISIT DOCTORS ')
                else:
                    print("ERROR")
            if b_a=="no":
                print("are you having any heart related problem")
                h_a2 = input("yes/no: ")
                if h_a2 =="yes":
                    print('SUFFERING: DIABITIES AND HEALTH DISEASES')
                    print('SUGGESTED : VISIT DOCTORS ')
                elif h_a2=="no":
                    print("OUT OF DANGER BUT CONTROL GLUCOSE LEVELS")
        elif d_a == "no":
            print('Are you victim of high BP')
            b_a = input("yes/no: ")
            if b_a=="yes":
                print('DIABETIES AND BP PATIENT')
                print()
                print("Are you suffering from any heart diseases")
                h_a = input("yes/no: ")
                if h_a == "yes":
                    print ('YOU ARE AT VERY CRITICAL STAGE')
                    #readcsv doctors
                if h_a =="no":
                    print("You are at borderline of critical stage")
                    print('SUGGESTED : VISIT DOCTORS ')
                else:
                    print("ERROR")
            if b_a=="no":
                print("are you having any heart related problem")
                h_a2 = input("yes/no: ")
                if h_a2 =="yes":
                    print('SUFFERING: DIABITIES AND HEALTH DISEASES')
                    print('SUGGESTED : VISIT DOCTORS ')
                elif h_a2=="no":
                    print("OUT OF DANGER BUT CONTROL GLUCOSE LEVELS")
#hii


