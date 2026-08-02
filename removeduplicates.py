#remove duplicates from a list
#list = values store chyesthadhi
#map = converts every value / input lo una prathi value ni int ki convert cheysthadhi

 
numbers=list(map(int,input("enter the values with spaces:").split()))

# oka unique list ni create cheyali
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print("list after removing duplicates:",unique)


