import random
def compc():
  game1=["S","W","G"]
  return random.choice(game1)
i1=10
i=0
comp_wins  =0
user_wins =0
draws =0
invalid_input = 0
while i<i1 :
    var = compc()
    print(f"-----------------SNAKE WATER GUN GAME================= ")
    print("Enter your choice (S for Snake, W for Water, G for Gun):")
    user = input().upper()#so that if user enters lower case by mistake
    print(f"Computer chose: {var}")
    if user == 'S' and var == 'G'or user == 'W' and var == 'S'or user == 'G' and var == 'W':
        print(f"computer wins:1\nuser loses:0")
        comp_wins=comp_wins+1
    elif user == 'S' and var == 'W' or user == 'W' and var == 'G'or user == 'G' and var == 'S':
        print(f"user wins:1\ncomputer loses :0")
        user_wins=user_wins+1
    elif user == 'S' and var == 'S'or user == 'W' and var == 'W' or user == 'G' and var == 'G':
        print("Draw")
        draws = draws + 1
    else:
        print("INVALID INPUT")
        invalid_input=invalid_input+1
    i=i+1
    print(f"No. of chances left : {i1-i}")
print(f"Number of the computer wins : {comp_wins}")
print(f"Number of times user wins: {user_wins}")
print(f"Number of draws {draws}")
print(f"NUMBER OF INVALID INPUTS : {invalid_input}")
if comp_wins>user_wins:
    print("FINAL WINNER IS THE COMPUTER")
elif user_wins>comp_wins:
    print("FINAL WINNER IS USER")
else:
    print("BOTH WON EQUAL NUMBER OF TIMES")
