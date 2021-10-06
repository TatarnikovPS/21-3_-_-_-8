c=""
arrow=0
while (arrow!="2") and (arrow!="8"):
    arrow=input("Осуществить перевод числа в 2 (двоичную СС) или в 8 (восьмеричную СС): ")
if arrow=="2":
    while True:
        try:
            a=int(input("Введите ваше число: "))
        except:
            False
        else:
            break
    while a>0:
        b=""
        b=str(a%2)+b
        a=a//2
        c+=b
    print("Ваше число в 2 системе: ",c[::-1])
if arrow=="8":
    while True:
        try:
            a=int(input("Введите ваше число: "))
        except:
            False
        else:
            break
    while a>0:
        b=""
        b=str(a%8)+b
        a=a//8
        c+=b
    print("Ваше число в 8 системе: ",c[::-1])
