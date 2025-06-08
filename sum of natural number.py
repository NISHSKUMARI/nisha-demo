num=int(input("enter the number:"))
if num<0:
  print(" plese enter the positive number:")
else:
  sum=0
  while num>0:
    sum +=num
    num -=1
    print(sum)