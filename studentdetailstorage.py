# students details storage
# dictionary = { key : value }

student = {}

student["Name"]=input("enter student name:")
student["age"]=input("enter student age:")
student["class"]=input("enter student class:")
student["percentage"]=input("enter student percentage:")
student["phn number"]=input("enter student phn number:")

print("--student details--")
print(f"name:{student["Name"]}")
print(f"age:{student["age"]}")
print(f"class:{student["class"]}")
print(f"percentage:{student["percentage"]}")
print(f"phn number:{student["phn number"]}")
