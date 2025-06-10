# Text-Based-Rpg: Jumanji
# Welcome user to the game and ask their name
name = input("Hello, welcome to the game... What is your name? ")
print(f"Welcome to Jumanji {name} \n")

# Start game
# Describe the starting scene
print("One day, you decided to play a video game called Jumanji. All of a sudden, you were sucked into the TV screen! Lying on the ground, you looked up to see towering trees overhead, signaling the start of your wild adventure…")
print("")
print("[S]tand up and take in your surrondings.")
print("Stand up and [g]o towards the water.")
ans1 = input("Choice: ").lower().strip()
# Check their answer
if ans1 == "s":
    print("You got up and slowly walked around, noticing you were in a jungle. A screen popped up which said 'Game began.' ")
    print("")
    print("[Y]ou go look for other people.")
    print("You go [a]cross the river.")
    ans2 = input("Choice: ").lower().strip()
    # Check their answer
    if ans2 == "y":
        print("As you were walking, you stumbled upon a person! You had no idea who they were, until they explained their story and they were your best friend in another body!?")
        print("")
        print("You and your best friend take separate [p]aths to explore.")
        print("You and your [b]est friend explore together.")
        ans3 = input("Choice:  ").lower().strip()
    
        # Check their answer
        if ans3 == "b":
            print("You decide to explore together and find yourself at a camp, it seems to be not too old, as if someone had just left…")
            print("")
            print("You both sneak [t]owards the camp to loot it")
            print("You both wait to see if anyone [m]ight arrive")
            ans4 = input("Choice:  ").lower().strip()
            
            if ans4 == "m":
                print("Your waiting had saved you as armoured men soon came, some having trained dogs walking alongside them. You heard them talking.")
                print("")
                print("You listen [i]n for more information.")
                print("You [q]uietly leave.")
                ans5 = input("Choice :   ").lower().strip()
        
                if ans5 == "i":
                    print("You listen and over hear they are going to be finding outlanders and eliminating them, your heart starts to race. You remember, it just might be a game…")
                    print("")
                    print("You decide to [c]onfront them.")
                    print("You [d]ecide to attack them.")
                    ans6 = input("Choice :   ").lower().strip()
             
                    if ans6 == "c":
                         print("You approach them with your hands in the air. You spoke asking “Is this just a game?” They stared. Suddenly you were stabbed from behind, the last words you heard were “You won”, everything went blank and then you woke up… just a game?")
                         
             
                    elif ans6 == "d":
                         print("Before you realized it was too late, fists against guns? What were you thinking? You had gotten shot multiple times. So close yet so far. ‘Game over.’")
                    else:
                         print("Not a option you fool... 'game' over.")
             
                elif ans5 == "q":
                    print("Your attempt to leave had failed as they saw the movement in the bushes and immediately shot you both… “Game over” were the last words you heard.")
                else:
                    print("Not a option you fool... 'game' over.")
            elif ans4 == "t":
                print("You heard footsteps and looked in that direction. When you looked back your best friend was gone, that's when you felt a stab. The knife going through your chest. You drop, dead. ‘Game over’…")
            else:
                print("Not a option you fool... 'game' over.")
        
        elif ans3 == "p":
            print("You took separate paths but just a few minutes later you heard a scream. You rushed to find your best friend's corpse being eaten by a tiger, and you were next. There you both laid at the end of the ‘game’…")
        else:
            print("Not a option you fool... 'game' over.")
    elif ans2 == "a":
        print("You decide to go across the river nearby the waterfall, you use the big rocks but then your foot slips! You fell down the waterfall, hit the rocks below hard… and had a fatal injury, dying from constant bleeding.  ")
    else:
        print("Not a option you fool... 'game' over.")
elif ans1 == "g":
    print("You got up and slowly walked towards the water, suddenly a hippo emerged from the water, and you a fool went closer and was chopped, eaten to death.")
else:
    print("Not a option you fool... 'game' over.")