import random
# you can set system limit for guess number
limit = int(input("Set the limit for system to guess a number : "))
guess = int(random.randint(0,limit))
turns = int(input("Set your turn for play that you want : "))


t = 0
while t < turns:
    t += 1
    ans = int(input("Enter What could be the guess number : "))
    if guess == ans:
        print(f"Congratulations🎉🎉 You won \n you won in {t} turns ")
        # when you won this programm will not run anymore we use break
        break
    elif guess > ans:
        print("You should enter some big number")
    elif guess < ans:
        print("You should enter some small number")


    if turns-t != 0 and guess != ans:
         print(f"you have only {turns-t} turns left")
    elif turns-t == 0 and guess != ans:
        print("You Lose! your all Turns have been finished")
