import time

x = int(input("enter num: "))

while True:
    print(x)
    x -= 1
    # parantez içindeki değer kadar duraklatır
    time.sleep(1)
    if x == 0:
        print("finished")
        break
    elif x < 0:
        print("invalid num")
        break