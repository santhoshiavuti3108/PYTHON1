def calci():
#calci ani oka funtion create cheysnam
    print("---simplecalculator---")
    print("supports:addition(+),substraction(-),multiplication(*),division(/)")
    print("type:exit  to stop")
# opening lo emaina kavali ante print cheyskovadaniki and .\n new line
    
# condition undhi kabati while loop& true ayithe input adguthundhi
    while True:
        userinput=input("enter your input expression:")
            #userinput expression exit ayithe loop break avthundhi
        if userinput.lower()=="exit":
                print("exited")
                break
        #try and except keywords error osthai emo anapudu use cheystharu and exception kuda error 
        try:
            allowed="1234567890+-*/.()"  

            if all(char in allowed for char in userinput):
                    result=eval(userinput) 
                    #eval is evaluation math function
                    print(f"result:{result}")
            else:
                    print("error:invalid")
        except ZeroDivisionError:
                print("error:zero division error")
        except Exception:
                print("error:invalid")


calci()

        

