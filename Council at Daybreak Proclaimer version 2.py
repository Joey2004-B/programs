#!/usr/bin/env python3
import subprocess
import random
def talk(message, secs, said):
    print(message)
    if len(str(said)) == 0:
        subprocess.run(["spd-say", message.lower()])
    else:
        subprocess.run(["spd-say", said])
    subprocess.run(["sleep", str(secs)])
def clearscreen():
    subprocess.run(["clear"])
#talk("Let's play council at daybreak!", 3, "")
clearscreen()
runmode = 1
print("Let's play \"Council at Daybreak!\"")
cast = ["Catholic Celebrity", "Heretics", "Schismatic", "Cloistered Religious", "Nosy Parish Worker", "Charismatic", "Crusader", "Homeschooler", "Youth Group Kid", "Convert", "The One who Prays Lauds"]
while runmode < 3:
    if runmode == 1:
        cards = []
        callall = input("Do you want to have all of the cards in the deck to be called out? [y/n]")
        if callall.lower().startswith("y"):
            cards = cast
        else:
            for x in cast:
                if x != "Heretics":
                    print(x)
                    want = input("Is this in play?(y/n)")
                    if want.lower().startswith("y"):
                        cards.append(x)
                else:
                    cards.append(x)
    randomizecards = input("Do you want the cards to be called at random? (y/n)")
    if randomizecards.lower().startswith("y"):
        #print(cards)
        random.shuffle(cards)
        #print(cards)
    input("Press [enter] to start.")
    clearscreen()
    if cards[0] != "Catholic Celebrity":
        talk("Everyone, go to sleep.", 3, "")
    for i, x in enumerate(cards):
        if x == "Catholic Celebrity":
            talk("CATHOLIC CELEBRITY", 2, "Catholic celebrity")
            if i == 0:
                talk("Before the night, show everyone your card. Then lay it face-down in front of you.", 5, "")
            else:
                talk("Everyone, wake up for now. Catholic Celebrity, show everyone your card. Then lay it face down in front of you.", 7, "")
        elif x == "Heretics":
            talk("HERETICS", 2, "Heretics")
            talk("Arise and find one another. Acknowledge each other with a silent signal.", 6, "")
        elif x == "Schismatic":
            talk("SCHISMATIC", 2, "Schismatic")
            talk("Arise. Heretics, stick out your thumbs to show the schismatic who you really are.", 5, "")
            talk("If only one thumb is up, then the other Heretic card is in the middle.", 6, "")
        elif x == "Cloistered Religious":
            talk("CLOISTERED RELIGIOUS", 2, "Cloistered Religious")
            talk("Arise and silently acknowledge one another.", 4, "")
            talk("If no one else has arisen, then the other Cloistered Religious card is in the middle.", 6, "")
        elif x == "Nosy Parish Worker":
            talk("NOSY PARISH WORKER", 2, "Nosy Parish Worker")
            talk("Arise and choose one of the two options:", 3, "")
            talk("Look at one player's card\nOR\nlook at two of the cards in the middle.", 7, "Look at one player's card or look at two of the cards in the middle.")
        elif x == "Charismatic":
            talk("CHARISMATIC", 2, "Charismatic")
            talk("Arise and look at either the card of the player on your right or your left.", 6, "")
        elif x == "Crusader":
            talk("CRUSADER", 2, "Crusader")
            talk("Arise and take another player's card and switch it with your own.", 4, "")
            talk("You may look at your new card, but you do not take their action during the night.", 5, "")
            talk("OR\nyou can do nothing and remain the Crusader.", 6, "Or you can do nothing and remian the Crusader.")
        elif x == "Homeschooler":
            talk("HOMESCHOOLER", 2, "Homeschooler")
            talk("Arise, sneak out of the house, and look at one card in the middle.", 5, "")
        elif x == "Youth Group Kid":
            talk("YOUTH GROUP KID", 2, "Youth Group Kid")
            talk("Arise and switch two other players' cards.", 3, "")
            talk("You do not get to look at the cards you are switching, and you cannot switch your card with another's.", 7, "")
        elif x == "Convert":
            talk("CONVERT", 2, "Cunvert")
            talk("Arise and switch your card with one card in the middle. Do not look at your new card.", 7, "")
        elif x == "The One who Prays Lauds":
            talk("THE ONE WHO PRAYS LAUDS", 2, "")
            talk("Arise and look at the card in front of you.", 4, "")
        talk("Now, go to sleep.", 3, "")
        clearscreen()
    talk("Now that the night is over, everyone WAKE UP!!!",5,"")
    talk("Now, let's get that heretic!",3,"")
    print("----- Enter a number to select an option from this menu. -----\n1 --------------------------- Play again with a different deck\n2 ------------------------------ Play again with the same deck\n3 ------------------------------------------------------- Quit")
    picked = False
    while picked == False:
        new_runmode = input(">")
        if new_runmode == "1" or new_runmode == "2" or new_runmode == "3":
            runmode = int(new_runmode)
            picked = True
        else:
            print("Invalid option.")
clearscreen()
