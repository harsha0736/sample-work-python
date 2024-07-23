import random
print("choose from: ROCK,SCISSORS,PAPER")
user_choice=input().upper()
computer_choice=random.choice(["PAPER","SCISSORS","ROCK"])
if user_choice=="PAPER" and computer_choice=="ROCK":
    print("PAPER WIN")
if user_choice=="PAPER" and computer_choice=="SCISSORS":
    print("SCISSORS WIN")
if user_choice=="ROCK" and computer_choice=="SCISSORS":
    print("ROCK WIN")
if user_choice=="ROCK" and computer_choice=="PAPER":
    print("PAPER WIN")
if user_choice=="SCISSORS" and computer_choice=="ROCK":
     print("SCISSORS WIN")
