score=0
ans_1=input("QUESTION:1 \nIn which year Pakistan won the World Cup? \na. 1997 \nb. 1992 \nc. 2002 \nANSWER: ")
if (ans_1 == "b") or (ans_1 == "1992"):
    score+=1
    print("CORRECT!! \nScore=",score)
else:
    print("INCORRECT!! The answer is 1992 \nScore=",score)
ans_2=input("\nQUESTION:2 \nWhict team was defeated by Pakistan in World Cup Final? \na. India \nb. Srilanka \nc. England \nANSWER: ")
if (ans_2 == "c") or (ans_2 == "England"):
    score+=1
    print("CORRECT!! \nScore=",score)
else:
    print("INCORRECT!! The answer is England \nScore=",score)
ans_3=input("\nQUESTION:3 \nWhen did Pakistan won the World T20 Cup? \na. 2009 \nb. 2007 \nc. 2005 \nANSWER: ")
if (ans_3=="a") or (ans_3=="2009"):
    score+=1
    print("CORRECT!! \nScore=",score)
else:
    print("INCORRECT!! The answer is 2009 \nScore=",score)
ans_4=input("\nQUESTION:4 \nWho was the captain of Pakistan when the team won the World T20 Final? \na. Shoaib Malik \nb. Shahid Afridi \nc. Younis Khan \nANSWER: ")
if (ans_4=="c") or (ans_4=="Younis Khan"):
    score+=1
    print("CORRECT!! \nScore=",score)
else:
    print("INCORRECT!! The answer is Younis khan \nScore=",score)
ans_5=input("\nQUESTION:5 \nWhich team was defeated by Pakistan in Champions Trophy Final 2017? \na. South Africa \nb. India \nc. England \nANSWER: ")
if (ans_5 == "b") or (ans_5=="India"):
    score+=1
    print("CORRECT!! \nScore=",score)
else:
    print("INCORRECT!! The answer is India \nScore=",score)
print("YOUR SCORE:",score)
if score ==5:
    print("YOU ARE AMAZING!!!")

    
