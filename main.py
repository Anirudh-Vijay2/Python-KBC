questions = [
    "Who is the current prime minister of India?",
    "Which team won the FIFA world cup 2022?",
    "Who is the richest prson in India?",
    "Which is the largest planet in our solar system?",
    "Who is the father of Atomic bomb",
    "\"A way of reffering to a country's working population in terms of their existing productive skills and abilities\" is known as?",
    "Which is the most densely populated state in India?",
    "Who is the current prime minister of United Kingdom(England)?",
    "FCI stands for?",
    "Have you subscribed to Code With Harry youtube channel?"
]

options = [
    " A: Rahul Gandhi    B: Priyanka Gandhi \n C: Narendra Modi    D: Aravind Kejariwal",
    " A: Portugal    B: India \n C: Argentina    D: France",
    " A: Ratan Tata    B: Gautham Adani \n C: Anil Ambani    D: Mukesh Ambani",
    " A: Earth    B: Jupiter \n C: Mars    D: Saturn",
    " A: Robert Oppenheimer    B: CV Raman \n C: Issac Newton    D: J.J Thomson",
    " A: Working people    B: People as Resource \n C: Workers    D: Employed people",
    " A: Uttar Pradesh    B: Kerala \n C: Maharashtra    D: Bihar",
    " A: Rishi Sunak    B: Boris Johnson \n C: Liz Truss    D: Hugh O'Leary",
    " A: Food Corporation of India    B: Funding Cost Inning\n C: Fantastic Coporation of India    D: Forme Cord of India", 
    " A: Yes    B: No \n C: Maybe    D: Will Do",
    
]

answers = [
    "c",
    "c",
    "b",
    "b",
    "a",
    "b",
    "d",
    "a",
    "a",
    "a"
]

print("Welcome to KBC. Do you want to play KBC?")
start = input("Enter y to play or n to quit (y/n): ")

moneyEarned = 0
if start.lower() == "y":
    print("Here is your first question for 10$")
    print("Your current earning is 0.00$")
    print(questions[0])
    print(options[0])
    ans = input("Enter your option which you have selected here or enter q if you dont know the answer: ")
    if ans.lower() == answers[0]:
        print("The answer is correct")
        print("You earn 100$")
        moneyEarned = moneyEarned+100
        print("Your total earning is ",moneyEarned,"$")
        nxt = input("Are you ready for your next question? (y/n)")
    elif ans.lower == "q":
        print("You quitted")
        print("you earned ",moneyEarned,"$")    
    else:
        print("The Answer is wrong.")
        print("The correct answer is option",options[0].upper())
        print("you earned ",moneyEarned,"$") 
        print("Better luck next time")
    if nxt.lower() == "y":
        print("here is your second question for 200$")
        print(questions[1])
        print(options[1])
        ans = input("Enter your option which you have selected here or enter q if you dont know the answer: ")
        if ans.lower() == answers[1]:
            print("The answer is correct.")
            print("You earn 200$")
            moneyEarned = moneyEarned+200
            print("Your total earning is ",moneyEarned,"$")
            nxt = input("Are you ready for your next question? (y/n) ")
        elif ans.lower == "q":
            print("You quitted")
            print("you earned ",moneyEarned,"$")    
        else:
            print("The Answer is wrong.")
            print("The correct answer is option",options[1].upper())
            print("you earned ",moneyEarned,"$") 
            print("Better luck next time")
        if nxt.lower() == "y":
            print("here is your third question for 400$")
            print(questions[2])
            print(options[2])
            ans = input("Enter your option which you have selected here or enter q if you dont know the answer: ")
            if ans.lower() == answers[2]:
                print("The answer is correct.")
                print("You earn 400$")
                moneyEarned = moneyEarned+400
                print("Your total earning is ",moneyEarned,"$")
                nxt = input("Are you ready for your next question? (y/n) ")
            elif ans.lower == "q":
                print("You quitted")
                print("you earned ",moneyEarned,"$")    
            else:
                print("The Answer is wrong.")
                print("The correct answer is option",options[2].upper())
                print("you earned ",moneyEarned,"$") 
                print("Better luck next time")
            if nxt.lower() == "y":
                print("here is your fourth question for 800$")
                print(questions[3])
                print(options[3])
                ans = input("Enter your option which you have selected here or enter q if you dont know the answer: ")
                if ans.lower() == answers[3]:
                    print("The answer is correct.")
                    print("You earn 800$")
                    moneyEarned = moneyEarned+800
                    print("Your total earning is ",moneyEarned,"$")
                    nxt = input("Are you ready for your next question? ")
                elif ans.lower == "q":
                    print("You quitted")
                    print("you earned ",moneyEarned,"$")    
                else:
                    print("The Answer is wrong.")
                    print("The correct answer is option",options[3].upper())
                    print("you earned ",moneyEarned,"$") 
                    print("Better luck next time")
            if nxt.lower() == "y":
                print("here is your fifth question for 1600$")
                print(questions[4])
                print(options[4])
                ans = input("Enter your option which you have selected here or enter q if you dont know the answer: ")
                if ans.lower() == answers[4]:
                    print("The answer is correct.")
                    print("You earn 1600$")
                    moneyEarned = moneyEarned+1600
                    print("Your total earning is ",moneyEarned,"$")
                    nxt = input("Are you ready for your next question? ")
                elif ans.lower == "q":
                    print("You quitted")
                    print("you earned ",moneyEarned,"$")    
                else:
                    print("The Answer is wrong.")
                    print("The correct answer is option",options[4].upper())
                    print("you earned ",moneyEarned,"$") 
                    print("Better luck next time")  
            if nxt.lower() == "y":
                print("here is your sixth question for 3200$")
                print(questions[5])
                print(options[5])
                ans = input("Enter your option which you have selected here or enter q if you dont know the answer: ")
                if ans.lower() == answers[5]:
                    print("The answer is correct.")
                    print("You earn 3200$")
                    moneyEarned = moneyEarned+3200
                    print("Your total earning is ",moneyEarned,"$")
                    nxt = input("Are you ready for your next question? ")
                elif ans.lower == "q":
                    print("You quitted")
                    print("you earned ",moneyEarned,"$")    
                else:
                    print("The Answer is wrong.")
                    print("The correct answer is option",options[5].upper())
                    print("you earned ",moneyEarned,"$") 
                    print("Better luck next time")
            if nxt.lower() == "y":
                print("here is your seventh question for 6400$")
                print(questions[6])
                print(options[6])
                ans = input("Enter your option which you have selected here or enter q if you dont know the answer: ")
                if ans.lower() == answers[6]:
                    print("The answer is correct.")
                    print("You earn 6400$")
                    moneyEarned = moneyEarned+6400
                    print("Your total earning is ",moneyEarned,"$")
                    nxt = input("Are you ready for your next question? ")
                elif ans.lower == "q":
                    print("You quitted")
                    print("you earned ",moneyEarned,"$")    
                else:
                    print("The Answer is wrong.")
                    print("The correct answer is option",options[6].upper())
                    print("you earned ",moneyEarned,"$") 
                    print("Better luck next time")
            if nxt.lower() == "y":
                print("here is your eight question for 12800$")
                print(questions[7])
                print(options[7])
                ans = input("Enter your option which you have selected here or enter q if you dont know the answer: ")
                if ans.lower() == answers[7]:
                    print("The answer is correct.")
                    print("You earn 12800$")
                    moneyEarned = moneyEarned+12800
                    print("Your total earning is ",moneyEarned,"$")
                    nxt = input("Are you ready for your next question? ")
                elif ans.lower == "q":
                    print("You quitted")
                    print("you earned ",moneyEarned,"$")    
                else:
                    print("The Answer is wrong.")
                    print("The correct answer is option",options[7].upper())
                    print("you earned ",moneyEarned,"$") 
                    print("Better luck next time") 
            if nxt.lower() == "y":
                print("here is your ninth question for 25600$")
                print(questions[8])
                print(options[8])
                ans = input("Enter your option which you have selected here or enter q if you dont know the answer: ")
                if ans.lower() == answers[8]:
                    print("The answer is correct.")
                    print("You earn 25600$")
                    moneyEarned = moneyEarned+25600
                    print("Your total earning is ",moneyEarned,"$")
                    nxt = input("Are you ready for your next question? ")
                elif ans.lower == "q":
                    print("You quitted")
                    print("you earned ",moneyEarned,"$")    
                else:
                    print("The Answer is wrong.")
                    print("The correct answer is option",options[8].upper())
                    print("you earned ",moneyEarned,"$") 
                    print("Better luck next time")
            if nxt.lower() == "y":
                print("here is your Jackpot question for 15000$")
                print(questions[9])
                print(options[9])
                ans = input("Enter your option which you have selected here or enter q if you dont know the answer: ")
                if ans.lower() == answers[9]:
                    print("The answer is correct.")
                    print("You earn 15000$")
                    moneyEarned = moneyEarned+15000
                    print("Congratulations you have earned", moneyEarned,"$")
                elif ans.lower == "q":
                    print("You quitted")
                    print("you earned ",moneyEarned,"$")    
                else:
                    print("The Answer is wrong.")
                    print("The correct answer is option",options[9].upper())
                    print("you earned ",moneyEarned,"$") 
                    print("Better luck next time")
                   