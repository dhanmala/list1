question_list=["how many continent are there?",
              "what is the capital of India?",
              "NG mein kaunse course padhaya jaata hai?"]
option_list=[["four","nine","seven","eight"],
            ["chandigarh","bhopal","chennai","delhi"],
            ["software engineering","counseling","tourism","agriculture"]] 
solution=[3,4,1]
lifeline_option=[["1.flour","2.seven"],["1.chandigarh","2.delhi"],["1.software enginerring","2.tourism"]]
solution_lifeline=[2,2,1]
a=0
count=1
amount=0
while a<len(question_list):
    print(question_list)
    j=0
    while j<len(option_list[a]):
        print(option_list[a][j])
        j=j+1
    if count<=1:
        lifeline=input("do you want lifeline")
        if lifeline_option=="yes":
            b=0
            while b<len(lifeline_option[a]):
                print(lifeline_option[a][b])
                b=b+1
            c=int(input("please choose lifeline amount"))
            if c==solution_lifeline[a]:
                amount=amount+2000
                print("you are right",amount)
            else:
                print("you are wrong",amount)
                break
            count+=1
        q=int(input("please choose your answer"))
        if q==solution[a]:
            amount=amount+2000
            print("you are right",amount)
        else:
            print("you are wrong",amount)
            break
        count+=1
    else:
        q=int(input("please choos your answer"))
        if q==solution_lifeline[a]:
            amount=amount+1
            print("you are right")
        else:
            print("you are wrong")
            break
        q=q+1
a=a+1                  

