a=(input("enter the values"))
x,y,z=a.split(",")
n1=int(x)
n2=int(y)
n3=int(z)
great=0
if n1>n2:
    if n1>n3:
        great=n1
    else:
        great=n3
elif n2>n1:
    if n2>n3:
        great=n2
    else:
        great=n3
elif n3>n1:
    if n3>n2:
        great=n3
    else :
        great=n2
print(f"the grestest number :{great}")



    




