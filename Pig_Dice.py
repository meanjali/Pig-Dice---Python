import random

turn=1
score=0
score_this_turn=0
turn_over=False
game_over=False



def main():
    print_rules()
    play_game()

def print_rules():
    print("Let's Play")
    print("================================================")
    print("*Let's see in how many turns you get score 20*")
    print("*Turn ends when you hold or roll a 1*")
    print("*If you roll 1, you will loose all points for the turn*")
    print("*If you hold, you will save all points for the turn*")
    print()

def play_game():
    while not game_over:
        take_turn()
    print()
    print("Game Over")


def take_turn():
    global take_turn
    print "TURN",turn
    turn_over=False
    while not turn_over:
        c = raw_input ("Roll or hold (r/h) ")
        print "c: ",c
        if c== "r":
            roll_dice()
        elif c== "h":
            hold_dice()
        else:
            print("Invalid choice, Try again!!")

def roll_dice():
    global turn,turn_over,score_this_turn
    die=random.randint(1,6)
    print "DIE:",die
    if die==1:
        score_this_turn=0
        turn+=1
        print("Turn Over!!")
        turn_over=True
    else:
        score_this_turn+=die

def hold_dice():
        global turn,turn_over,score_this_turn,game_over
        print("Score for this turn : ",score_this_turn)
        score=score_this_turn
        score_this_turn=0
        print("Total Score:",score)
        turn_over=True
        if score>=20:
            game_over=True
            print("You finished in ",turn,"turns!!")
        turn+=1

    
if __name__ == "__main__":
    main()