a = 0
b = 1
num =int(input("enter the number  of fibonacci"))

if num == 1:
  print(a)
else:
  print(a)
  print(b)

for i in range(1,num+1):
  
  c = a+b
  a=b
  b=c
  print(c)