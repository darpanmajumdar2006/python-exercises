d=input('Is it a leap year? Enter "yes" or "no".\n')
k=int(input("Enter number of people in the room\n"))
fact=1
fact1=1
fact2=1
fact3=1
if d=="no":
    n=365
    b=365-k
    vt=365**k
    for i in range(1, n + 1):
        fact *= i
    for i in range(1, b + 1):
            fact1 *= i
    vnr=fact/fact1
    pa=vnr/vt
    pb=1-pa
    print("probability of the people having the same birthdays is: ",pb)
if d=="yes":
    n2=366
    c=366-k
    vt2=366**k
    for i in range(1, n2 + 1):
         fact2 *= i
    for i in range(1, c + 1):
            fact3 *= i
    vnr2=fact2/fact3
    pa2=vnr2/vt2
    pb2=1-pa2
    print("probability of the people having the same birthdays is: ",pb2)
