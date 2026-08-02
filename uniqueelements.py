# print unique elements

numbers=list(map(int,input("enter the values with spaces:").split()))
for i in numbers:
    if numbers.count(i)==1:
        print(i,end=" ")