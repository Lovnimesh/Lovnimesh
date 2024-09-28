questions=[["What is the biological name of the human is ","Homoshapians","Humanosorus", "peoplosorus","Humangasorus",1,["Homoshapians","peoplosorus"] ],
           ["what is the name of first president of india","Dr Sarevapalli Radhakrisnan","Dr Rajendra Prasad",
            "JwaharLaal Nehru","Dr. Bheem Rao Ambedkar",2,["Dr. Rajendra Prasad","Dr. Sarvapalli Radhakrisnan"]],
           ["Who is the father of constitution of india",'Dr.Bheemrao Ambedkar','Mahatma Gandhi','Jwaharlaal Nehru'
           ,"Dr. Rajendra Prasad",1,["Dr Bheem Rao Ambedkar","Mahatma Gandhi"]]]
money=[1000,2000,5000,10000,20000,50000,100000]
public_vote=[{1:"46%",2:"7%",3:"40%",4:"7%"},{1:"35%",2:"40%",3:"15%",4:"10%"},{1:"39%", 2:"36%", 3:"13%",4:"12%"}]
for i in range (0,len(questions)):
    question=questions[i]
    print(f"for Rs. {money[i]} your question is......' {question[0]}'")
    print(f"a.{question[1]}       b.{question[2]}    c.{question[3] }   d.{question[4]}/n")

    a=int(input("write your ans in integer(if you dont know the ans you can use help line by typing 0): "))
    
    if a==0:
        print("""
        Type 1 for public vote
         Type 2 for 50-50
         Type 3 for Call your frnd
         Type 4 for Surprise
        """ )
        hl=int(input("Type: "))
        if hl==1:
            print(public_vote[i])
        elif hl==2:
            print(question[6])
        elif hl==3:
            print('call your friend through your mobile')
        elif hl==4:
            print("there is no option 4, ulloo banaya bda maja aaya")
        v=int(input("Now give the ans: "))
        if v==question[5]:
            print(f"you have won Rs.{money[i]},congrats\n\n")
        else:
             print("sorry you Lost")
             break

    elif a==question[5]:
        print(f"you have won {money[i] }, congrats\n\n")
    else:
        print("sorry you lost")
        break

if i<5:

 print(" since you haven't reached till level 5 you lost your winning amount")

p=input("Feedback: ")
print(p)

