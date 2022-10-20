#This function generate the initial menu of the game
#Allow start the game, exit the game or show help about how to play the game
def show_menu():
    valid_asnwer = False
    player_input = input("1) 1 to start, \n2) 0 to exit, \n3) h to see help: ").lower()

    while valid_asnwer == False:
        if player_input == "1":
            print("\n---------------------")
            print("Your Adventure start!")
            print("---------------------")

            player_input = input("""
-----------------------------------------------------------------
You wake up in an unknown place,
With dificult you see a corridor in front of you.
You can WALK to the end of the corridor or you can YELL for help.
----------------------------------------------------------------- 
What do you choice?: """).lower()
            if validate_player_input(player_input, "walk", "yell") == "walk":
                player_input = input("""
-----------------------------------------------------------------------------
As you reach the end of the corridor,
you see some stone steps that are iluminate by torches.
You can TAKE a torch to figth against the beast or you can go DOWN the steps.
-----------------------------------------------------------------------------
Which do you choice?: """).lower()
                if validate_player_input(player_input, "take", "down") == "take":
                    print("""
------------------------------------------------
You activated a trap, 
Some floodgates open under your feet 
and you fall towards an uncertain destination...

You wake up in an unknown place...
------------------------------------------------""")
                    play_again()
                else:
                    player_input = input("""
------------------------------------------------------------------------
You have reached a destroyed bridge, 
In front of you there is a rope and on the other side there are 3 doors:
- One on the RIGHT
- One on the CENTER and 
- One on the LEFT,
Suddenly the steps turn into a ramp 
and a giant stone begins to quickly fall to your position!.
You have to jump or you will be crushed.
------------------------------------------------------------------------
Which door do you choice?: """).lower()
                    if validate_player_input(player_input, "rigth", "center", "left") == "right":
                        player_input = input("""
--------------------------------------------------------------------------------------
Almost about to reach the door,
you realize that the rope is not enough, 
you have to LET go of the rope and take advantage of the momentum to reach the door or 
HOLD on to the rope!.
--------------------------------------------------------------------------------------
What do you decide to do?: """).lower()
                        if validate_player_input(player_input, "let", "hold") == "let":
                            print("""
Oh no!!! You were going very fast and ended up crashing into the door, 
you have been very badly injured, 
you can't move and there is nowhere to go, 
remember there is a door in front of you! 
you get up with effort to open the door 
Then you realize that it is a drawing of a door... you have no way out.""")
                            play_again()
                        else:
                            player_input = input("""
You have realized too late that it is not a rope, 
it is a giant snake that you were holding on to, 
you can continue to HOLD on or let GO, what are you going to do?""").lower()
                            if validate_player_input(player_input, "hold", "go") == "hold":
                                print("""
Bad idea, the snake has had time to catch you and takes you to its nest, 
its young will survive one more cycle thanks to your sacrifice. 
Bye.""")
                                play_again()

                            else:
                                print("""
----------------------------------------------------------
It was close.
Fortunately you weren't that far off the ground.
Wait a minute! Do you hear it too?
The giant stone is falling and you have nowhere to escape.
----------------------------------------------------------""")
                                play_again()
                    elif validate_player_input(player_input, "rigth", "center", "left") == "center":
                        print("""
------------------------------------------------------
You open the door, it looks like a room,
you enter and see a sleeping man, 
you throw a vase, the man wakes up, 
he is your kidnapper, HA HA HA IT'S ME!!! >:D
and this time II will make sure you can't run away... 
it's game over for you.
------------------------------------------------------""")
                        play_again()
                    else:
                        player_input = input("""
-----------------------------------------------------------------------------
You open the door, and in the background you can see the exit to the outside, 
but wait, the road is full of tigers that haven't eaten in 100 days, 
you can RUN towards the exit, or SEARCH another way.
-----------------------------------------------------------------------------
what do you want to decide?: """).lower()
                        if validate_player_input(player_input, "run", "search") ==  "run":
                            print("""
-------------------------------------------------------------------------
Wow, you're smart, tigers are literally dead from not eating in 100 days. 
You arrive at the exit, you see sunrise, you are free !
Next time you won't be so lucky.
-------------------------------------------------------------------------""")

                            print("Thanks for playing!")
                            play_again()
                        else:
                            print("""
---------------------------------------------------------------------
You look at a passage, you decide to take it 
but when you're halfway there you step on a slab that triggers a trap
the walls start to close in, you have no way to escape... 
---------------------------------------------------------------------

Game Over.""")
                            play_again()
            else:
                player_input = input("""
-------------------------------------------------------------------------
You start hearing chains moving behind you, 
You have awakened an aggressive beast, you have no escape, 
You can try to RUN or you can SEARCH for something to distract the beast.
-------------------------------------------------------------------------
What do you do?: """).lower()
                if validate_player_input(player_input, "run", "search") == "run":
                    print("""
-----------------------------------------------------------------------
Although it seems like a good idea, 
I remind you that you don't see anything, 
You stumble and the beast catches up with you, you became his dinner... 
Thanks for feeding Firulais
-----------------------------------------------------------------------""")
                    play_again()
                else:
                    print("""
------------------------------------------------------------
You search in silence...
You feel yourself touching something furry,
Again you hear chains moving, 
You can only see their big yellow eyes that glow in the dark 
and that's the last thing you'll see...
------------------------------------------------------------""")
                    play_again()

            valid_asnwer = True
        elif player_input == "0":
            print("""
------------------
See you next time.
------------------""")
            valid_asnwer = True
        elif player_input == "h":
            print("""
--------------------------------------------
I will show you part of a situation,
you will find words in CAPITAL LETTERS,
these will be your options,
you have to write wisely...

With love,
Mastermind 
--------------------------------------------""")
            valid_asnwer = True
            show_menu()
        else:
            player_input = input(f"\nSorry, option '{player_input}' don't exist.\n1) 1 to start, \n2) 0 to exit, \n3) h to see help: ").lower()

#This function receive the user input and compare throught the diferents options.
def validate_player_input(
                        player_input = str, 
                        first_option = str, 
                        second_option = str, 
                        third_option = None
                        ) -> str:

    valid_asnwer = False
    while valid_asnwer == False:
        if player_input == first_option or player_input == second_option or player_input == third_option:
            valid_asnwer = True
        else:
            if third_option != None:
                player_input = input(f"\nYou must write {first_option.upper()}, {second_option.upper()} or {third_option.upper()}: ").lower()
            else:
                player_input = input(f"\nYou must write {first_option.upper()} or {second_option.upper()}: ").lower()

    return player_input

#This function ask the user if want play again.
def play_again():
    asnwer_yes = ["1", "yes", "y", "si"]
    asnwer_no = ["0", "no", "n"]
    player_input = input("Play again?: ").lower()
    valid_asnwer = False
    while valid_asnwer == False:
        if player_input in asnwer_yes:
            print("""
--------------------------------
Let the Adventure start again!!!
--------------------------------""")
            show_menu()
            valid_asnwer = True
        elif player_input in asnwer_no:
            print("""
-------------------
Thanks for playing!
-------------------""")

            valid_asnwer = True
            break
        else:
            player_input = input("\nYes or No?: ").lower()

def main():
    print("""
--------------------------
Welcome to ADVENTURE GAME!)
--------------------------""")
    show_menu()

if __name__ == "__main__":
    main()