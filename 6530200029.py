## นาย กิตติธร ทองตุ้ม 6530200029 ##
sum=0
for number in range(50,101):
    if number %7 ==0:
        print("number is",number)
        sum=sum+1
else:
    print("มีทั้งหมด=",sum)
#are divisible by 7!!
sum=0
for number in range(50,101):
    if number %11 ==0:
        print("number is",number)
        sum=sum+1
else:
    print("มีทั้งหมด=",sum)
#are divisible by 11!!
sum=0
for number in range(50,101):
    if (number %11==0) and (number %7 ==0):
        print("number is",number)
        sum=sum+1
else:
    print("มีทั้งหมด=",sum)
#are divisible by 7,11!!
