import random 
random.seed()
c = True
while c == True:
    try:
        a = int(input("number 1 "))
    except:
        print("please use a number")
        exit()
    try:
        b = int(input("number 2 "))
    except:
        print("please use a number")
        exit()
    c = False
if a > b:
    c = True
    print("first number must be smaller!")
print("Heres a random number ",random.randint(a,b))
