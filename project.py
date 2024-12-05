from operator import truediv

# menu หลัก
def mainmenu():
    print("\n[เมนูหลัก]")
    print("1.ชา")
    print("2.นม")
    print("3.น้ำผลไม้")    
    print("4.กาแฟ")    
    print("5.สมูตตี้") 

#menu 1 ชา
def menu1():
    while True:
        print("\n ชา")
        print("1.ชาเขียว")
        print("2.ชาดำ")
        print("3.ชาเย็น")
        print("4.ชานม")
        print("5.ชากุหลาบ")
        print("6.ชามะลิ")
        print("9.กลับเมนูหลัก")
        print("0.ออกจากโปรแกรม")
        work=int(input("เลือก :"))
        if work == 9 :
            return 9
        elif work == 0 :
            return 0
        elif work == 1:
            print("ชาเขียว")
        elif work == 2 :
            print("ชาดำ")
        elif work == 3:
            print("ชาเย็น")
        elif work == 4:
            print("ชานม")
        elif work == 5:
            print("ชากุหลาบ")
        elif work == 6:
            print("ชามะลิ")
        else:
            pass

#menu 2 นม
def menu2():
    while True:
        print("\n นม")
        print("1.นมโอวัลติน")
        print("2.นมไวท์มอลต์")
        print("3.นมสด")
        print("4.นมชมพู")
        print("9.กลับเมนูหลัก")
        print("0.ออกจากโปรแกรม")
        work=int(input("เลือก :"))
        if work== 9:
            return 9
        elif work==0:
            return 0
        elif work==1:
            print("นมโอวัลติน")
        elif work==2:
            print("นมไวท์มอลต์")
        elif work==3:
            print("นมสด")
        elif work==4:
            print("นมชมพู")
        else :
            pass

#menu 3 น้ำผลไม้
def menu3():
    while True:
        print("\n น้ำผลไม้")
        print("1.น้ำสตอเบอรี่")
        print("2.น้ำกีวี")
        print("3.น้ำสัปปะรด")
        print("4.น้ำกระเจี๊ยบ")
        print("5.น้ำแตงโมง")
        print("6.น้ำส้ม")
        print("9.กลับเมนูหลัก")
        print("0.ออกจากโปรแกรม")
        work=int(input("เลือก :"))
        if work== 9:
            return 9
        elif work==0:
            return 0
        elif work==1:
            print("น้ำสตอเบอรี่")
        elif work==2:
            print("น้ำกีวี")
        elif work==3:
            print("น้ำสัปปะรด")
        elif work==4:
            print("น้ำกระเจี๊ยบ")
        elif work==5:
            print("น้ำแตงโม")
        elif work==6:
            print("น้ำส้ม")
        else :
            pass
        
#mune 4 กาแฟ
def menu4():
    while True:
        print("\n กาแฟ")
        print("1.อเมริกาโน")
        print("2.เอสเปซโซ")
        print("3.คาปูชิโน")
        print("4.กาแฟดำ")
        print("5.ลาเต้")
        print("6.มอคคา")
        print("9.กลับเมนูหลัก")
        print("0.ออกจากโปรแกรม")
        work=int(input("เลือก :"))
        if work== 9:
            return 9
        elif work==0:
            return 0
        elif work==1:
            print("อเมริกาโน")
        elif work==2:
            print("เอสเปซโซ")
        elif work==3:
            print("คาปูชอโน")
        elif work==4:
            print("กาแฟดำ")
        elif work==5:
            print("ลาเต้")
        elif work==6:
            print("มอคคา")
        else :
            pass

#menu 5 สมูตตี้
def menu5():
    while True:
        print("\n สมูตตี้")
        print("1.สมูทตี้อะโวคาโดกล้วยมะนาว")
        print("2.สมูทตี้สตอเบอร์รี่โยเกิร์ต")
        print("3.สมูทตี้ส้มมะม่วง")
        print("9.กลับเมนูหลัก")
        print("0.ออกจากโปรแกรม")
        work=int(input("เลือก :"))
        if work== 9:
            return 9
        elif work==0:
            return 0
        elif work==1:
            print("สมูทตี้อะโวคาโดกล้วยมะนาว")
        elif work==2:
            print("สมูทตี้สตอเบอร์รี่โยเกิร์ต")
        elif work==3:
            print("สมูทตี้ส้มมะม่วง")
        else :
            pass

while True :
    mainmenu()
    work=int(input("เลือกเมนูที่ต้องการ : "))
    if work == 0 :
        break

    elif work==1:
        if menu1() == 0:
            break
    elif work==2:
        if menu2() == 0:
            break
    elif work==3:
        if menu3() == 0:
            break
    elif work==4:
        if menu4() == 0:
            break
    elif work==5:
        if menu5() == 0:
            break
    else :
        pass