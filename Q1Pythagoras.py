import math 
a = True
while a == True:
    try:
        A = float(input("Triangle leg 1 length "))
    except:
        print("please use a number")
        exit()
    try:
        B = float(input("Triangle leg 2 length "))
    except:
        print("please use a number")
        exit()
    a=False
A = A*A 
B = B*B 
C = A+B 
C = math.sqrt(C)
print("The length of the hypotenuse is ",C,". Thank you for using this simple calculator.")