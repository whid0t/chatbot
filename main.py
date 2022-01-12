import time
from tkinter import *


#the worlists with the commands
wordlist_greeting = ("hello", "hi", "greetings", "sup", "what's up", "yo")
wordlist_help = ("help", "wordlists", "help chatbot", "wordlist")
wordlist_time = ("time", "what time", "say time", "localtime")
wordlist_math = ("math", "sum", "do math", "help math")
math_problems = ("sum", "devide", "multiply")
wordlist_chat = ("exit", "new")
wordlist_game = ("rps", "guess")
wordlist_credit = ("credits", "creator")
vreme = time.asctime( time.localtime(time.time()) )




print('Hi! This is my first big project. Please if you find any problems let me know here or email me at whid0t@abv.bg. Thank you!')


name = input("\nHi! My name is Richard the Great chatbot. Please tell me your name so i know how should i call you.\nYour name: ")
print("Hi %s, nice to meet you!" %name)
print("If you need help you can type \"help\"")
time.sleep(1.5)




def purvo():
        def back(x):
                if x == "back":
                        purvo()
        
        import time
        first_c = input("Command: ")
        if first_c.isalpha():
        #greetings
                if first_c in wordlist_greeting:
                        print("Thanks for greeting me. Now you can ask me to do something")
                        time.sleep(1.0)
                        purvo()

        #time
                elif first_c in wordlist_time:
                        print("Local current time is: ", vreme)
                        time.sleep(1.0)
                        purvo()

        #help
                elif first_c in wordlist_help:
                        import time
                        print("For greeting message you can type these ones: ")
                        for index, x in enumerate(range(len(wordlist_greeting))):
                                print(index + 1, "".join(wordlist_greeting[x]))
                                time.sleep(1.0)
                        print("\nFor time request you can type these ones: ")
                        for index, x in enumerate(range(len(wordlist_time))):
                                print(index + 1, "".join(wordlist_time[x]))
                                time.sleep(1.0)
                        print("\nFor math functions and help type these ones: ")
                        for index, x in enumerate(range(len(wordlist_math))):
                                print(index + 1, "".join(wordlist_math[x]))
                                time.sleep(1.0)
                        print("\nFor games type these ones: ")
                        for index, x in enumerate(range(len(wordlist_game))):
                                print(index + 1, "".join(wordlist_game[x]))
                                time.sleep(1.0)
                        purvo()

        #exit and new section
                elif first_c in wordlist_chat[0]:
                        print("It was nice talking to you! Bye!")
                        time.sleep(1.5)
                        exit

                elif first_c in wordlist_chat[1]:
                        print("New chat incoming...")
                        time.sleep(1.5)
                        purvo()

        #math section
                elif first_c in wordlist_math:
                        import time
                        print("Math functions: \n", " ".join(math_problems))
                        math_inp = input("Your math problem: ")
                        time.sleep(1.0)
                        back(math_inp)

                        #sum
                        if math_inp in math_problems[0]:
                                sum_help = int(input("Tell me how many numbers you will sum: "))
                                total = 0
                                for num in range(sum_help):
                                        sum_num = int(input("Tell me the number you want to sum: \n"))
                                        total += sum_num
                                print("Your result is: ", total)
                                time.sleep(2)
                                print("You will need to type \"math\" again to use it again")
                                purvo()

                        #devide
                        elif math_inp in math_problems[1]:
                                devide1 = input("Tell me the number to be devided: \n")
                                devide2 = input("Tell me  the deviding number: \n")
                                print(int(devide1) / int(devide2))
                                purvo()

                        #multiply
                        elif math_inp in math_problems[2]:
                                multi1 = input("Tell me the first number: \n")
                                multi2 = input("Tell me the second number: \n")
                                print(int(multi1) * int(multi2))
                                purvo()


        #credits
                elif first_c in wordlist_credit:
                        print("Created by whid0t 2020. For any questions you can e-mail my at \"whid0t@abv.bg\"")
                        purvo()




        #rock, paper, scissors game
                elif first_c in wordlist_game[0]:
                        import time
                        import random
                        from random import choice

                        #variables and start of the game
                        neshta = ["rock", "paper", "scissors"]

                        print("Please choose one:")
                        time.sleep(1.5)
                        for x in range(len(neshta)):
                                print (neshta[x])

                        #user input
                        while True:
                            try:
                                izb_igrach = input("Choice: ")
                                if izb_igrach == neshta[0]:
                                        a = 8.0
                                elif izb_igrach == neshta[1]:
                                        a = 4.0
                                elif izb_igrach == neshta[2]:
                                        a = 1.0
                                back(izb_igrach)
                        #input check
                            except ValueError:
                                print("Please make a available choice...")
                                continue
                            else:
                                print("You chose: %s" %izb_igrach)
                                time.sleep(3.0)
                                break

                        #input check again
                        while True:

                            if izb_igrach not in ('rock', 'paper', 'scissors'):
                                print("Please choose one from them")
                                break

                        #random choice for the computer
                            else:
                                print("3")
                                time.sleep(1.5)
                                print("2")
                                time.sleep(1.5)
                                print("1")
                                time.sleep(1.5)
                                izbor_comp = random.choice(neshta)
                                print("My choice is ", izbor_comp)
                                if izbor_comp == neshta[0]:
                                        b = 8.0
                                elif izbor_comp == neshta[1]:
                                        b = 4.0
                                elif izbor_comp == neshta[2]:
                                        b = 1.0
                                time.sleep(2.0)
                
                        #seeing who wins
                
                                c = a / b
                                win = [4.0, 2.0, 0.125]
                                lose = [8.0, 0.5, 0.25]
                                draw = 1.0
                                float(draw)
                                if c in win:
                                    print("I win")
                                elif c in lose:
                                    print("You win")
                                else:
                                    print("Draw")

                                time.sleep(1.5)
                                print("Good game. Type \"rps\" if you want to play again")
                                purvo()
                                break

        #guess the number

                elif first_c in wordlist_game[1]:
                    import random
                    rang = int(input("Tell me from 0 to what number should i choose one: "))
                    back(rang)
                    nums = range(0,rang)
                    computer_num = random.choice(nums)
                    print("I'm ready with choosing my number from 0 to {}. Now you have 3 tries to guess it!".format(rang))
                    #trying to guess
                    for i in range(0,3):
                        user_guess = int(input("Your guess: "))
                        if user_guess != computer_num:
                            print("Try again.")
                            continue
                        elif user_guess == computer_num:
                            print("Congrats you guessed it!")
                            break
                    purvo()

                else:
                        print("You chose a command that isn't in our lists. Type 'help' to see the wordlists.")
                        purvo()


        #error print
        else:
                print("Sorry i didn't understand that. Type \"help\" to display the wordlists. \nType \"exit\" to exit the chat or \"new\" to renew the chat.")
                purvo()


purvo()


