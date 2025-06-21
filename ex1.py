#print the number of times a number is divisble by 2 till we gget a number lesser than 2
num=(int(input("Enter a number greater than 2 ")))
count=0
i=1
for i in range(num):
    num=num//2 
    count+=1
    if num<2:
       break
print("The number must be divided", count ,"times to get a number less than 2.")