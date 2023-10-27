import matplotlib.pyplot as pl
print("Hello ! How has your Day been?")
a = int(input("1 : Stress Levels and Management\n2 : Nutrition\n3 : Consult a Doctor"))
if a == 1:
    aa = 0
    print("Please answer these few questions")
    print("*Please note that this is not a diagnostic tool. Only a professional can identify the real issue\n1:Never to 5:Always")
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
        if 10 < aa < 14 :
            print("A moderate stress is required and is healthy. Maintain your stress in this level")
        if 14 < aa < 21 :
            print("Though your levels seem to be moderate it is very close to high levels. Adopt habits like excercise,yoga and meditation.")
    if aa <=10 :
        print("You have LOW levels of stress")
        if 1 <= aa <= 6 :
            print("Though Low levels are healthy and compromising, a little stress is required to have you driven in your life.")
xx = [(aa*10/3),100]
pl.pie(xx,labels=["Your stress","Total"])
pl.show()

if a == 2:
