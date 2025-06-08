"""num= 4
if num == 1:
  print("it is not prime num:")   
  if num>1: 
     for i in range (2,num):
        if num%i == 0:
          print("it is not prime num:")   
        break    
     else:  
            print(" it is a prime, num:")
  else:
    print("Invalid input. Enter a positive integer.")"""    
num = int(input("Enter a number: "))
if num == 1:
         print("It is not a prime number.")  # 1 is not a prime number
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print("Invalid input. Please enter a positive number.")
