science=input("enter science marks:")
maths=input("Enter maths marks:")
social=input("Entr social marks:")
computer=input("Enter computer marks:")
history=input("Enter history marks:")

science=int(science)
maths=int(maths)
social=int(social)
computer=int(computer)
history=int(history)

total= science+maths+social+computer+history
average=total/5
print("total marks is:",total)
print("average:",average)
