num=int(input("enter a number:"))
factorial=1
if num<0:
    print("factorial is not defined for negative values.")
elif num==0 or num==1:
    print(f"factorial={factorial}")
else:
   for i in range(2,num+1):
    factorial*=i
print(f"factorial={factorial}")

