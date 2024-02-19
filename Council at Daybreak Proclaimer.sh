#!/bin/bash
runmode=1
echo "Let's play 'Council at Daybreak!'"
spd-say "Let's play council at daybreak!"
sleep 3
clear
while [ $runmode -ne 3 ] ; do

#While the runmode variable is not 3, then this whole thing repeats.
if [ $runmode -eq 1 ] ; then
read -p "Do you want to have all the cards in the deck called out? [y/n]" callall
case $callall in
    "Y" | "y" | "Yes" | "yes" | "YES")
        catceb="y"
    schiz="y"
    clreg="y"
    parish="y"
    chari="y"
    cru="y"
    homsch="y"
    youth="y"
    conv="y"
    lauds="y";;
    *)

    read -p "Is the Catholic Celebrity card in play?(y/n)" catceb
        read -p "Is the Schismatic card in play?(y/n)" schiz
        read -p "Is/are the Cloistered Religious card(s) in play? [y/n]" clreg
        read -p "Is the Nosy Parish Worker card in play? (y/n)" parish
        read -p "Is the Charismatic card in play?(y/n)" chari
        read -p "Is the Crusader card in play?[y/n]" cru
        read -p "Is the Homeschooler card in play?[y/n]" homsch
        read -p "Is the Youth Group Kid in play?[y/n]" youth
        read -p "Is the Convert card in play? [y/n]" conv
        read -p "Is The One Who Prays Lauds card in play?[y/n]" lauds;;
esac
fi
clear
read -p "Press [enter] to start the game."
clear
if [ $catceb = "y" ] ; then
echo "CATHOLIC CELEBRITY"
spd-say "Catholic celebrity"
sleep 2
echo "Before the night, show everyone your card. Then lay it face-down in front of you."
spd-say "Before the night, show everyone your card. Then lay it face-down in front of you."
sleep 5
fi
echo "Everyone, go to sleep."
spd-say "Everyone, go to sleep."
sleep 3
clear
deck=("Heretics" "Schismatic" "Cloistered Religious" "Nosy Parish Worker" "Charismatic" "Crusader" "Homeschooler" "Youth Group Kid" "Convert" "The One Who Prays Lauds")


for person in "${deck[@]}";
do
    clear
    actiondone=0
    case $person in
        "Heretics")
            echo "HERITICS"
            spd-say "Heretics"
            sleep 2
            echo "Arise and find one another. Acknowledge each other with a silent signal."
            spd-say "Arise and find one another. Acknowledge each other with a silent signal."
            sleep 3
            actiondone=1;;
        "Schismatic")
        if [ $schiz = "y" ] ; then
            echo "SCHISMATIC"
            spd-say "Schismatic"
            sleep 2
            echo "Arise. Heretics, stick out your thumb to show the Schismatic who you really are."
            spd-say "Arise. Heretics, stick out your thumb to show the Schismatic who you really are."
            sleep 5
            echo "If only one thumb is up, then the other Heretic card is in the middle."
            spd-say "If only one thumb is up, then the other Heretic card is in the middle."
            sleep 3
            actiondone=1
            fi;;
        "Cloistered Religious")
        if [ $clreg = "y" ] ; then
            echo "CLOISTERED RELIGIOUS"
            spd-say "Cloistered Religious"
            sleep 2
            echo "Arise and silently Acknowledge one another."
            spd-say "Arise and silently Acknowledge one another."
            sleep 4
            echo "If no one else has arisen, then the other Cloistered Religious card is in the middle."
            spd-say "If no one else has arisen, then the other Cloistered Religious card is in the middle."
            sleep 3
            actiondone=1
            fi;;
        "Nosy Parish Worker")
        if [ $parish = "y" ] ; then
            echo "NOSY PARISH WORKER"
            spd-say "Nosy Parish Worker"
            sleep 2
            echo "Arise and choose one of the two options:"
            spd-say "Arise and choose one of the two options:"
            sleep 3
            echo "Look at one player's card"
            echo "OR"
            echo "look at two of the cards in the middle."
            spd-say "Look at one player's card or look at two of the cards in the middle."
            sleep 4
            actiondone=1
            fi;;
        "Charismatic")
        if [ $chari = "y" ] ; then
            echo "CHARISMATIC"
            spd-say "Charismatic"
            sleep 2
            echo "Arise and look at either the card of the player on your right or your left."
            spd-say "Arise and look at either the card of the player on your right or your left."
            sleep 3
            actiondone=1
            fi;;
        "Crusader")
        if [ $cru = "y" ] ; then
            echo "CRUSADER"
            spd-say "Crusader"
            sleep 2
            echo "Arise and take another player's card and switch it with your own."
            spd-say "Arise and take another player's card and switch it with your own."
            sleep 4
            echo "You may look at your new card (but you do not take their action during the night.)"
            spd-say "You may look at your new card but you do not take their action during the night."
            sleep 5
            echo "OR"
            echo "You can do nothing and remain the Crusader."
            spd-say "Or you can do nothing and remain the Crusader."
            actiondone=1
            fi;;
        "Homeschooler")
        if [ $homsch = "y" ] ; then
            echo "HOMESCHOOLER"
            spd-say "Homeschooler"
            sleep 2
            echo "Arise, sneak out of the house, and look at one card in the middle."
            spd-say "Arise, sneak out of the house, and look at one card in the middle."
            sleep 2
            actiondone=1
            fi;;
        "Youth Group Kid")
        if [ $youth = "y" ] ; then
            echo "YOUTH GROUP KID"
            spd-say "Youth Group Kid"
            sleep 2
            echo "Arise and switch two other players' cards."
            spd-say "Arise and switch two other players' cards."
            sleep 3
            echo "You do not get to look at the cards you are switching and you cannot switch your card with another's."
            spd-say "You do not get to look at the cards you are switching and you cannot switch your card with another's."
            sleep 3
            actiondone=1
            fi;;
        "Convert")
        if [ $conv = "y" ] ; then
            echo "CONVERT"
            spd-say "Cunvert"
            sleep 2
            echo "Arise and switch your card with one card in the middle. Do not look at your new card."
            spd-say "Arise and switch your card with one card in the middle. Do not look at your new card."
            sleep 3
            actiondone=1
            fi;;
        "The One Who Prays Lauds")
        if [ $lauds = "y" ] ; then
            echo "THE ONE WHO PRAYS LAUDS"
            spd-say "The One Who Prays Lauds"
            sleep 2
            echo "Arise and look at the card in front of you."
            spd-say "Arise and look at the card in front of you."
            sleep 1
            actiondone=1
            fi;;
    esac
    if [ $actiondone -eq 1 ] ; then
    sleep 3
    echo "Now, go back to sleep."
    spd-say "Now, go back to sleep."
    sleep 3
    fi
done
clear
echo "Now that the night is over, everybody WAKE UP!!!"
spd-say "Now that the night is over, everybody wake up!"
sleep 5
echo Now,\ let\'s\ get\ that\ heretic!
spd-say Now,\ let\'s\ get\ that\ heretic!
echo "----- Enter a number to select an option from this menu. -----"
echo "1 --------------------------- Play again with a different deck"
echo "2 ------------------------------ Play again with the same deck"
echo "3 ------------------------------------------------------- Quit"
read -p ">" runmode
done
