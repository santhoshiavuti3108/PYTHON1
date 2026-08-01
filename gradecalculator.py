# grade calculator 
#subjects , sum , avg , percentage , grade
name=input("enter name :")
math=int(input("enter math marks:"))
eng=int(input("enter eng marks:"))
sci=int(input("enter sci marks:"))
sum=math+eng+sci
avg=sum/3
percentage=sum/300*100
grade=0
if sum >= 90:
    grade="A"
elif sum >= 80 and sum < 90:
    grade="B"
elif sum >= 65 and sum < 80:
    grade="C"
elif sum>= 35 and sum < 65:
    grade="PASS"
else :
    grade="FAIL"
print(f"name={name}.\n total  marks={sum}.\n avg={avg}.\n percentage={percentage}.\n grade={grade}")


