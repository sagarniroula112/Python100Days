import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

a = time.strftime('%H')
b = int(a)

if(b>=4 and b<12):
    print("Good Morning Sir!")
elif(b>=12 and b<=5):
    print("Good Afternoon Sir!")
else:
    print("Good Night Sir!")
