
import random 
random.seed()
A = random.randint(1,100)
B = random.randint(1,100)
C = A + B
print("beep boop\ndoing number stuff\n. . .\n......")
D = int(input(str(A) + " + " + str(B) + " = ? "))
if D == C:
    print("Correct ur so cool")
else:
    print("Sandly wrong and uncool")