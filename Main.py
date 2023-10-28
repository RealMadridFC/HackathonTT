import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import datetime as dt
#from playsound import playsound as ps
import webbrowser

# CODE TO GET CURRENT TIME
#print(dt.datetime.now())
print("WELCOME TO WebDoc")

user_name = str(input('Enter your Name :'))
user_loc = str(input('Enter your complete adress in 3 lines: '))
user_no = int(input('Enter your mobile no. :'))

if user_name is None:
    print("INVALID")
elif user_loc is None:
    print("INVALID")
elif user_no is None:
    print('INVALID')
else:
    print("ACCOUNT CREATED")
zz = 'yes'
z = []
while zz == 'yes':
    print()
    print("1.SENIOR CITIZEN WELLNESS")
    print("2. TEEN HEALTH")
    print("3. CHILDCARE")
    print("4. HEALTH STATUS")
    print("5. AMBULANCE")
    print("6.WEBSITE")
    ch1 = int(input('Select option according your requirement :'))
    if ch1==1:
        c = 1
        while c==1:
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
                BlP_Lu = eval(input("Enter your upper Blood pressure level:"))
                BlP_Ll = eval(input("Enter your lower Blood pressure level:"))
                Hrt_L = eval(input("Enter your Heart beat count:"))

                if 140 > BlP_Lu < 125:
                    print("Upper BP is not normal ")
                    print("SUGGESTED : 1. REDUCE SALT IN DIET,2.GET GOOD 8 HOURS SLEEP,3.REDUCE STRESS")
                if 90 > BlP_Ll < 70:
                    print("Lower Bp is not normal")
                    print("SUGGESTED : 1. REDUCE SALT IN DIET,2.GET GOOD 8 HOURS SLEEP,3.REDUCE STRESS,4. REDUCE WEIGHT")
                if 75 > Hrt_L > 128:
                    print("IRREGULAR HEART RATE")
                    print("SUGGESTED : VISIT DOCTOR")
                else:
                    print('')
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
                c = int(input("Enter 1 to go back to Senior Citizens' page"))
                if c != 1:
                    zz = input("Enter yes to go to Main page:")
            elif ch2 == 2:
                print()
                df=pd.read_csv('csvfile.csv')
                print("OUR DOCTORS LIST:")
                print(df)
                c = int(input("Enter y to go back to Senior Citizens' page"))
                if c!=1:
                    zz = input("Enter yes to go to Main page:")
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
                        if cc != 'y':
                            c = int(input("Enter 1 to go back to Senior Citizens' page:"))
                            if c != 1:
                                zz = input("Enter yes to go to Main page:")
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
                        if cc != 'y':
                            c = int(input("Enter 1 to go back to Senior Citizens' page:"))
                            if c != 1:
                                zz = input("Enter yes to go to Main page:")
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
                        if cc != 'y':
                            c = int(input("Enter 1 to go back to Senior Citizens' page:"))
                            if c != 1:
                                zz = input("Enter yes to go to Main page:")
                    elif ch3==4:
                        print("HEALTHY DIET")
                        print()
                        print("INCLUDE : 8 GLASSES OF WATER , WHOLE GRAINS,BEANS,DARK GREEN VEGGEIS")
                        print()
                        print("AVOID : FRIED FOOD , JUNK FOOD ")
                        print()
                        print("FOR MORE  ASSISTANCE CONTACT OUR TEAM")
                        cc = input("Enter y to check other diets")
                        if cc != 'y':
                            c = int(input("Enter 1 to go back to Senior Citizens' page:"))
                            if c != 1:
                                zz = input("Enter yes to go to Main page:")
                    else:
                        print('ERROR')
                        cc = input("Enter y to check other diets")
                        if cc != 'y':
                            c = int(input("Enter 1 to go back to Senior Citizens' page:"))
                            if c != 1:
                                zz = input("Enter yes to go to Main page:")
            elif ch2==4:
                print("REMINDER")
                #df2=pd.read_csv('ambulan.csv')
                #print(df2)
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
                c = int(input("Enter y to go back to Senior Citizens' page"))
            else:
                exit
        zz = input("Enter yes to go to main page:")
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
                    print("Though your levels seem to be moderate it is very close to high levels. Adopt habits like excercise,yoga and meditation.")
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
        df2=pd.read_csv('ambulan.csv')
        #print(df2)
        print('sending help')
        print('ONE OF THE BELOW AMBULANCE WILL BE AT YOUR LOCATION IN 10 MIN')
        print(df2)
        zz = input("Enter y to go to main page:")
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
    elif ch1==3:
        print("CHILD CARE ")
        print()
        print("1.VACINATION")
        print("2.NUTRITION/DIET")
        print("3.DOCTOR")
        ch4=int(input('ENTER OPTION'))
        if ch4==1:
            print("VACINATION")
            print()
            print('Have your child polio vaccine completed?')
            p_ans = input("yes/no: ")
            if p_ans =="yes":
                print('IS your child tetanus vaccination completed?')
                t_ans = input("yes/no: ")
                if t_ans == "yes":
                    print("Is your child measles vaccination done?")
                    m_ans = input("yes/no: ")
                    if m_ans =="yes" :
                        print("YOUR CHILD IS SAFE AS HIS VACINATION IS COMPLETED")
                    elif m_ans=="no":
                        print("2 out of 3 done \n complete others asap \n doctors list:")
                        df3=pd.read_csv("vaccine.csv")
                        print(df3)
                        #print("PLEASE TRY AGAIN LATER")
                    else:
                        print('TRY AGAIN LATER')
                elif t_ans=="no":
                    print("Is your child measles vaccination done?")
                    m_ans = input("yes/no: ")
                    if m_ans =="yes" :
                        print("2 out of 3 Vaccines Completed \n DO COMPLETE REMAINING ASAP \n OUR DOCTORS:")
                        df3=pd.read_csv("vaccine.csv")
                        print(df3)
                    elif m_ans=="no":
                        print("ONLY 1 Completed \n complete others as soon as possible")
                        print("DOCTORS LIST")
                        df3=pd.read_csv("vaccine.csv")
                        print(df3)
            elif p_ans == "no":
                print('IS your child tetanus vaccination completed?')
                t_ans = input("yes/no :")
                if t_ans == "yes":
                    print("Is your child measles vaccination done?")
                    m_ans = input("yes/no: ")
                    if m_ans =="yes" :
                        print("YOUR CHILD IS SAFE AS HIS VACINATION IS COMPLETED")
                    elif m_ans=="no":
                        print("2 out of 3 done")
                        print()
                        print("COMPLETE OTHERS ASAP \n DOctors list")
                        df3=pd.read_csv("vaccine.csv")
                        print(df3)
                elif t_ans=="no":
                    print("Is your child measles vaccination done?")
                    m_ans = input("yes/no: ")
                    if m_ans =="yes" :
                        print("2 out of 3 Vaccines Completed \n DO COMPLETE REMAINING ASAP \n OUR DOCTORS:")
                        df3=pd.read_csv("vaccine.csv")
                        print(df3)
                    else:
                        print("NONE COMPLETED")
                        print("VISIT DOCTOR ASAP")
                        print("DOCTORS")
                        df3=pd.read_csv("vaccine.csv")
                        print(df3)
        elif ch4==2:
            print("DO YOU NEED DIET FOR your CHILD")
            ans = input("yes/no: ")
            if ans=="yes":
                print("IS YOUR CHILD BETWEEN 0-2 years")
                I_ans = input("yes/no :")
                if I_ans == "yes":
                    print("INFANT DIET :")
                    print("THE BASIC FOOD THAT SHOULD BE GIVEN :\n 1.Baked apples \n 2.Tomato and Carrot puree \n 3.Green Beans and banana puree \n NOTE:Please Ensure that you give soft food ")
                elif I_ans == "no":
                    print("CHILD DIET FOR AGE GROUP 2-12 years")
                    print()
                    print("DIET:")
                    print()
                    print("1.MILK \n 2.WHOLE WHEAT BREAD \n 3.Berries \n 4.Green Veggies")
            else:
                print("Thank you")
        elif ch4==3:
            print("Do you need a Doc?")
            dd_ans = input("yes/no: ")
            if dd_ans=="yes":
                print("DOCTORS LIST:")
                df4=pd.read_csv("csvfile.csv")
                print(df4)
            else:
                print("Try Again later")
        else:

            print("Some error occured")
    if ch1==6:
        print("WEBSITE LINK")
        webbrowser.open("http://www.google.com")
    elif ch1 == 2:
        aaa = 0
        import matplotlib.pyplot as pl
        print("Hello ! How has your Day been?")
        while aaa == 0:
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
            aaa = int(input("Enter 0 to go back to Teen health page:"))
            if aaa != 0:
                zz = input("Enter yes to go back to main page:")
        if a == 2:
            print("The harsh truth is that Teens tend to eat more and more junk rather healthy food.\nThis can lead to high risk of health issues.")
            print("To support your energy levels:\n1.Eat more grains rich in carbohydrates and proteins\n2.Eat more fibre\n3.A small cheat meal is healthy too!!")
            aaa = int(input("Enter 0 to go back to Teen health page:"))
            if aaa != 0:
                zz = input("Enter yes to go back to main page:")
        if a == 3:
            print()
            df=pd.read_csv('csvfile.csv')
            print("OUR DOCTORS LIST:")
            print(df)
            aaa = int(input("Enter 0 to go back to Teen health page:"))
            if aaa != 0:
                zz = input("Enter yes to go back to main page:")
        else :
            print("Error")
            aaa = int(input("Enter 0 to go back to Teen health page:"))
            if aaa != 0:
                zz = input("Enter yes to go back to main page:")
print("Thank you for Using WebDoc!!")
