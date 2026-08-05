#create notes file
note=input("enter your notes:")
file=open("notes.txt","w")
file.write(note)
file.close()
print(f"your notes:{note}")

