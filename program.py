#print("hello world")
#type coversion
#implict
'''a=100
b=45.8
c=a+b
print (c)
print (type(b))
'''
#explicit 
'''a=100
a=float(a)
print(a)
print (type(a))'''
'''a='1'
a=int(a)
print(type(a))'''
#ascii values
'''char="R"
santhu=ord(char)
print (santhu)
'''
'''char="s"
santhu=ord(char)
print(santhu)'''
'''ascii_value=88
santhu=chr(ascii_value)
print(santhu)'''
#operators
'''a=10
b=20
c=a+b
print(c)'''
'''a=10
b=20
a+=b
print(a)

'''
#input
'''age=float(input("give your age:"))
print(age)
'''
#output
'''a=input("give a:")
b=input("give b:")
print(a,b)
'''
'''a=input("give a:")
b=input("give b:")
print(a,b,sep="&",end="ended here!")'''
'''name=input("give your name:")
print("hello",name,sep=",",end="!")
'''
'''input=int(input("give a number:"))
print("you entered: ", input, end="!")
'''
# multipule inputs in single line
'''a=input("give values:")
x,y,z= a.split(" ")
sum=int(x)+int(y)+int(z)
print(sum)'''
 
'''name=input("enter name:")
age=input("enter age:")
print("name:",name,"age:",age ,sep=" ")'''

#comparison operator
'''x,y=input("enter x and y:").split(",")
a=int(x)
b=int(y)
print(a>b,a<b,a==b,a!=b,sep=",")'''

#f string
'''x,y=input("enter name and age:").split(",")
print(f"name:{x},age:{y}years")'''
# area of circle
'''radius=int(input("give radius:"))
a=3.14*radius*radius
print(f"area of circle:{a}")'''
#quadratic equation
'''a=float(input("give a value:"))
b=float(input("give b value:"))
c=float(input("give c value:"))
d=b**2-4*a*c

root1=-b+(d*0.5)/2*a
root2=-b-(d*0.5)/2*a

print(f"root1={root1},root2={root2}")'''
#if else statments
'''w=input()
if w=="sunny":
    print("play cricket")
elif w=="rainy":
    print("play indoor")
else :
    print("sleep")
print("code ended here!")
#'''
#strings
'''str="SANTHOSHI"
print(str)
print(str[-2])
print(str[2:])

'''
#vowel counter
'''s=input("give input:")
s2=s.lower()
a = s2.count("a")
e = s2.count("e")
i = s2.count("i")
o = s2.count("o")
u = s2.count("u")
print(f"no of vowels={a+e+i+o+u}")'''
#marks calculation
'''math=int(input("give math marks:"))
sci=int(input("give sci marks:"))
eng=int(input("give eng marks:"))
sum=math+sci+eng
print(f"total marks:{sum}")
avg=sum/3
print(f"average marks:{avg}")
percentage=(sum/300*100)
print(f"percentage={percentage}")
grade=percentage
if grade > 90:
    print(f"grade:A")
elif grade <= 90 and grade > 80:
    print(f"grade:B")
elif grade <= 80 and grade > 70:
    print(f"grade:c")
else :
    print(f"grade:F")

'''
n=input("enter your name:")
a=int(input("enter your age:"))
print(f"name:{n} and age:{a}")














    




























