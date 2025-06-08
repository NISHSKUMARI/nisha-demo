"""num=int(input("enter the number"))
fact=1
if num<0:
  print(" factorial of 0 does not exist")

elif num == 0:
        print(" factorial of 0 is:",1)

else num > 0:
      for i in range(1,num+1):  
        fact = fact*i
        print(fact)"""
num = int(input("Enter the number: "))
fact = 1

if num < 0:
    print("Factorial of negative numbers does not exist.")
elif num == 0:
    print("Factorial of 0 is: 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of", num, "is:", fact)

      