print('***ACRONYM GENERATOR***')
print("-------PLEASE FOLLOW THE INSTRUCTIONS TO OBTAIN YOUR RESULT-------")
p=0
while p==0:   
    print("1. Start Conversion")
    print("2. Exit Program")
    ch=input("Enter your choice : ")  
    if ch=="1" or "y":
        t=1
        x=input('How many Sentences would you like to convert: ')
        if str(x) not in "1234567890":
            print("Invalid Input,Please Try Again")
        else:
            x=int(x)
            while t<=x:
                sentence=list(input('Enter Sentence to be converted to acronym: ').split(" "))
                final_acro=""
                temp=[]
                for i in sentence:
                    if i in ["of","Of","on","On","in","In"]:
                        continue
                    else:
                        final_acro+=i[0].upper()
                        temp+=[i]
                print("Final Acroynm: ",final_acro)
                for j in range(len(final_acro)):
                    print(final_acro[j],"------",temp[j])
                t=t+1
            print('The total number of sentences has been reached:',x,'times')
            print('THANK YOU')
           
            p=1
    elif ch=="2":
        print('THANK YOU')
    
        p=1
    else:
        print("Invalid Input,Please Try Again")
    
print("The following semster project has been completed by:-\nAvjot Singh--(12200643)\nChodiphilli Ramesh--(12207110)\nTimmareddy Nareshreddy--(12205919) ")

        

