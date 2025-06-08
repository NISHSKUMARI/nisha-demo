"""print("the number is divisible by 13")
for i in range (1,100):
  if i%13==0:
    print(i)"""

    # second solution
l=[39,50,26,65,91,117]
result=list(filter(lambda x : x%13==0,l))
print("the number divisible by 13:",result)
