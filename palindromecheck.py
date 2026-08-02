# palindrome = a word which reads same from reverse also

s=input("enter a word:")
reverse=s[::-1]
if reverse == s:
    print("It is a palindrome")
else :
    print(" it is not a palindrome")
