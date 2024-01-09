#!/usr/bin/env python3
import random # Use random.choice(list_name) to randomly pick from lists. Example: random.choice(names)
# Use random.randint(low, high) with if statements to "roll the dice." Example: random.randint(0, 10)
# Material for story
import re
import subprocess
names = ["Aurora", "Ahmed", "Audrey", "Arden", "Andrea", "Augusta", "Augustus", "Absalom", "Adash", "Abraham", "Abby", "Alex", "Al", "Allen", "Alice", "Allistair", "Aaron", "Amanda", "Alan", "Anthony", "Andy", "Andrew", "Antonio", "Annie", "Anne",
         "Benedict", "Britanni", "Bree", "Bob", "Ben", "Bailey", "Blake", "Blossom", "Benjamin", "Beatrice", "Bill", "Billie", "Billy", "Bobbie", "Broccy", "Bailey", "Bryan", "Brian", "Bista", "Benny",
         "Charlie", "Candy", "Cameron", "Cameron", "Chris", "Courtney", "Charles", "Camila", "Charlotte", "Cheryl", "Chloe", "Cola", "Cole",
         "Dylan", "Diego", "Dorothy", "Dora", "Darell", "Daisy", "Darcy", "Dana", "Deanna", "Daniel", "Danielle", "Dan",
         "Ellen", "Edward", "Elvis", "Elvira", "Elvir", "Eduardo", "Ed", "Eddy", "Edith", "Elora", "Ellie", "Elliot", "Emery", "Ellen", "Eliza", "Elsa", "Elizabeth", "Ethan",
         "Flavia", "Francis", "Felix", "Flint", "Finn", "Flinton", "Fabian", "Finley", "Flynn", "Farnsworth", "Falco", "Fallon", "Flanigan", "Fairfax", "Freddie", "Fernando", "Farley", "Fred", "Felicity",
         "Gabriel", "Gabby", "Gabriella", "Gabrielle", "George", "Gustavo", "Georgia", "Garfield", "Georgia",
         "Hilary", "Hilda", "Hildegard", "Henry", "Halibut", "Haddock", "Hally", "Harley", "Hayes",
         "Isabel", "Izzy", "Issac", "Ishmael", "Isadore", "Isabelle",
         "Jackson", "Jacob", "Jake", "Josie", "Julie", "Jane", "Joseph", "Joey", "Jack", "Jill", "Jean", "Jumbo", "John", "Johnny", "Jose",
         "Kirk", "Kirby", "Kit", "Kiki", "Katy", "Kingsley", "Khalid", "Kay",
         "Lio", "Leo", "Leonard", "Leah", "Lily", "Lulu", "Lana", "Linda", "Logan",
         "Maisie", "Montana", "Madison", "Manuel", "Mario", "Mary", "Maria", "Maryanne", "Milton", "Mark", "Marc", "Micah", "Milton", "Murphy", "Mog", "Melody", "Matthew", "Matt", "Matthias", "Ma", "Macaulay",
         "Nina", "Nelson", "Norman", "Nancy", "Nana", "Nathan", "Nate", "Natalie",
         "Oren", "Oleg", "Owen", "Ollie", "Oliver", "Olive", "Olivia", "Olaf",
         "Polly", "Paul", "Pami", "Peter", "Pete", "Petey", "Pat", "Patrick", "Patricia", "Penelope", "Pipi", "Ponyo", "Percy", "Percival", "Pa", "Petra",
         "Quincy", "Quinn", "Queedie",
         "Ralph", "Rosemary", "Ron", "Robert", "Rosie", "Reynaldo", "Roy", "Ramone", "Rogan",
         "Sol", "Sam", "Samuel", "Samantha", "Sean", "Sheeta", "Simon",
         "Taylor", "Thomas", "Tom", "Tommy", "Taffeta", "Tina", "Theah", "Timothy", "Tim", "Timmy",
         "Umberto", "Umbert", "Uniqua", "Umi",
         "Vanellope", "Victor", "Viola", "Violet", "Victoria",
         "Wallace", "Wally", "William", "Willow", "Wanda", "Willy",
         "Xavier", "Xin", "Xaviera",
         "Yoshi", "Yoshie",
         "Zach", "Zoey", "Zinnia", "Zelda", "Zoe", "Zany", "Zane", "Zen"]
last_names = ["A.", "Anderson", "Allen", "Alexander", "Alony", "Aksenov", "Asimov", "Amato", "Anderson", "All", "Abrams", "Adams",
              "B.", "Black", "Brinkman", "Boyle", "Burger", "Boone", "Bell", "Beakman", "Beekman", "Beckman", "Buttz", "Butts", "Baron", "Butt-Holdsworth", "Barry", "Bailey", "Bailey", "Bailey", "Brook", "Burrows", "Blixt", "Boraldo", "Baker", "Bibrowski", "Beiger", "Brooks",
              "C.", "Campbell", "Coy", "Coales", "Canon", "Cash", "Clark", "Clardy", "Chomak", "Chalmers", "Cook", "Craft", "Cain",
              "D.", "Delgado", "Donovan", "Dupont", "Diaz", "Dodson", "Dent", "Dailey", "Douglas",
              "E.", "Emanuel", "Elzner", "Erhard", "Eggleston", "Esle", "Elzner", "Eagan",
              "F.", "Franklin", "Fredrick", "Foxx", "Fitzgerald", "Field", "Fowler", "Furze",
              "G.", "Gould", "Grant", "Gill", "Gusteau", "Green", "Garcia", "Garwood", "Gates", "Gray", "Grayson", "Grey", "Greyson", "Garcia", "Gardner", "Gonzales", "Goodwin", "Gardner", "Gazarov", "Greene", "Grant",
              "H.", "Humphrey", "Hendrix", "Henderson", "Hopkins", "Halls", "Houston", "Hoffman", "Hellinga", "Hasler", "Hemessy", "Hyder", "Hudson", "Hudson", "Hudson", "Helms", "Hobbs", "Hake", "Hatke", "Hoskins", "Hasler", "Higgins", "Haynie", "Haggerty",
              "I.", "Il",
              "J.", "Jobs", "Jones", "Jones", "Johansen", "Jarre", "Johnson", "Johnson", "Johnson", "Johnson", "Johnson", "Johnson", "Johnson", "Johnson", "Johnson", "Jones", "Jones", "Jones", "Jones", "Jones", "Jones", "Jones", "Jones", "Joel", "Jefferys", "Jackson",
              "K.", "Klose", "Knox", "Kennedy", "Kowalski", "Krawczyk", "Kerr", "Kern", "Kingshill", "Kendrick",
              "L.", "Lamb", "Lopes", "Lockwood", "Lock", "Lachiram", "Lamore", "Lehman", "Langley", "Lorenz", "Lowe", "Lincoln", "LeBlanc",
              "M.", "Mcintosh", "McMillan", "Miller", "Mansi", "McPhaul", "Macintosh", "Mustard", "Miyazaki", "Morris", "Miller", "Metzler", "McBryde", "Murphy", "Metzler", "Miller", "McAteer",
              "N.", "Nixon", "Noel", "Nichols", "Newby", "Nelson", "Nguyen",
              "O.", "Owens", "Oldfield", "Oden", "Odom", "Olive", "Orr", "Orts", "Otis",
              "P.", "Pacheco", "Powell", "Plum", "Peacock", "Petty", "Payne", "Potts", "Patton", "Peasley", "Price", "Peasley", "Perez", "Pickering", "Proctor",
              "Q.", "Quimby",
              "R.", "Rollins", "Rivera", "Robinson", "Reed", "Robinson", "Ransom", "Rector", "Rose", "Roe", "Ruth", "Richards", "Roberts",
              "S.", "Santiago", "Stevens", "Scarlet", "Sauter", "Silva", "Sauter", "Sousa", "Simmons", "Stubbs", "Sanders", "Seed", "Schaefer", "Simpson", "Song", "Silva", "See", "Smith", "Smith", "Smith", "Simons", "Swackhammer", "Smith", "Smith", "Smith", "Smith", "Schaffer", "Smiley", "Stephens", "Saikia", "Sum", "Shark", "Sternik", "Sides",
              "T.", "Trentsondale", "Thomas", "Takahata", "Trigg", "Tuck", "Taylor", "Thomas", "Thorne",
              "U.", "Ulfgood",
              "V.", "Vandermark",
              "W.", "Williams", "Waggoner", "Wilson", "Wilke", "Winn", "Wilson", "Wagner", "Washington", "Wright", "Wilkins", "Wiesner", "Weber", "Watson", "White",
              "X.", "Xavierson",
              "Y.", "Ying",
              "Z.", "Zhibing", "Zimmerhanzel", "Zurborg"]
CharacterType = ["Peck", "Daikini", "Human", "Alien", "Bandit", "Pirate", "Scientist", "Vampire", "Dragon", "Skeleton", "Robot", "Ghost", "zombie", "Astronaut", "Prince/princess", "Police officer", "Athlete", "Diver", "Knight", "Firefighter", "Cowboy/girl", "Doctor", "Clown", "Wizard", "Racecar driver", "Native"]
Vehicles = ["Time machine", "Rocket ship", "Car", "Van", "Bus", "Helicopter", "Bicycle", "Horse", "Boat", "Submarine", "Airplane", "Jetpack"]
Tools = ["Flashlight", "Invisibility potion", "money", "Fire lighter", "Parachute", "Giant Growth potion", "Key", "Ray gun", "Rope", "First aid kit", "Disguise", "Magic wand", "Shield", "Food", "Sword", "computer", "Cell phone", "Ladder", "Camera", "Music player", "Science kit", "Calculator", "Computer book", "Python Programming book"]
Prizes = ["medal", "Trophy", "Peace", "Knowledge", "kiss", "money", "treasure", "Freedom", "A Car", "Language knowledge"]
PlaceTypes = {"Japan":"country", "Bulgaria":"country", "Chernobyl":"outdoors", "Somalia":"country", "Death Valley":"outdoors", "the United States":"country", "church":"indoors", "jail":"indoors", "a castle":"indoors", "the Open ocean":"outdoors", "a Forest":"outdoors", "Outer space":"other", "a Haunted house":"indoors", "A desert":"outdoors", "a house":"indoors", "Minecraft":"other", "a cave":"indoors", "A lab":"indoors", "a school":"indoors", "a library":"indoors", "Glinthia":"country"}
Places = [ place for place in PlaceTypes.keys() ] #This line takes place names from the dictionary above.
Animals = ["guinea pig", "mouse", "rat", "dog", "cat", "duck", "bird", "spider", "tarantula", "bug", "bee", "insect", "horse", "mule", "elephant", "Giraffe", "Frog", "Goldfish", "Axolotl", "Shrimp", "Peacock", "Cardinal", "Zebra", "Jackalope", "Ladybug", "Shark", "Wolf", "Snake", "Pirhana"]
good_adjective = ["Enchanted", "Magical", "Joking", "Japanese", "Normal", "Fearless", "Brave", "Rational", "Happy", "Friendly", "Wondorous", "Nice", "Fit", "Fat", "Slightly Annoying", "Extreme", "Upside-down", "Good", "Holy", "Gentle", "courageous", "victorious", "Awesome", "Great", "self-controlled", "One and only"]
bad_adjective = ["quimpy", "stupid", "bad", "evil", "terrible", "terrifying", "creepy", "angry", "Crappy", "loser", "dubious", "Stinky", "Impatient", "Jerky", "Despicable", "Always Late", "Murderous", "Peckish", "Horrible", "Lying", "Theiving", "Jealous", "Lazy", "Smelly", "Oderous", "One and only"]
Foods = ["Blackroot", "Broccoli", "Gruel", "Spinnach", "Granola bar", "Cheeseburger", "Carrot", "Banana", "Candy", "Apple", "Soda can", "Yogurt", "Onion", "Jerky", "Wasabi", "Roast Beef", 'Lettuce', "Milk", "Boiled Liver", "Bean", "Horseradish", "Tilapia", "Sushi", "Noodle", "Watermelon", "Donut", "Cheese"]
death_terms = ["died", "kicked the bucket", "croaked", "passed away", "expired", "got buried"]
# Initializing data for the story.
last_list = "none"
good_guys = []
bad_guys = []
active_vehicles = []
inactive_good_guys = []
inactive_bad_guys = []
place = ""
X2repeat = random.randint(0,12)
goals = [] # Goals start with "Leave", "Take", "Destroy", "Visit",
# "Leave" goals mean that you have to leave that location.
# "Take" goals mean that you have to obtain an item. It could be an item that you can't start with.
# "Destroy" goals mean that you have to find an item and destroy it.
# "Visit" goals mean that you have to go to a certain place.
# "Meet" goals mean that you have to meet a good guy
# Define events that might happen in the story.
#Key events
said = input("Should this generated story be said? (It only works in Linux systems with the speach-dispatcher package installed.) [y/n]")
def storyprint(text, strend):
    global said
    print(text, end=strend)
    if said.lower().startswith("y"):
            subprocess.run(["spd-say", text])
            waittime = len(text)//10+1
            #print()
            subprocess.run(["sleep", str(waittime)])
#storyprint("Does this work?\nOne way to find out...", "\n")
def NewPlace():
    global place
    global Places
    global PlaceTypes
    if random.randint(0,1) == 1:
                    NewPlace = input("(type in a name of a place.) ")
                    if not NewPlace in PlaceTypes:
                        Places.append(NewPlace)
                        subject_type = input("(Type in \"indoors\" if that place you entered is indoors.) ")
                        if 'indoors' in subject_type:
                            subject_type = 'indoors'
                        elif 'outdoors' in subject_type:
                            subject_type = 'outdoors'
                        PlaceTypes[NewPlace] = subject_type
    else:
                    NewPlace = random.choice(Places)
    place = NewPlace
NewPlace()
def vehicle_check():
    """This function searches the inventory for vehicles. If any vehicles were found, they get transferred to the active_vehicles list."""
    global inventory
    global active_vehicles
    global Vehicles
    for x in Vehicles:
            while x in inventory:
                active_vehicles.append(x)
                inventory.remove(x)
def Animal():
        global good_guys
        global Animals
        if random.randint(0,1) == 1:
            animal = input("(What animal did the good guy(s) see?)")
            if not animal in Animals:
                Animals.append(animal)
        else:
            animal = random.choice(Animals)
        storyprint("  The good guy"+is_plural(good_guys)+" saw a(n) "+animal + ".", " ")
        if random.randint(0, 1) == 1:
            storyprint("They followed it.", " ")
        storyprint("Then, it disappeared.", "\n")
def is_plural(lyst):
    """This is used when a group of characters is mentioned in the story. This prevents the story from saying "good guys" when there's really 1 good guy. The lyst parameter in this function takes lists."""
    if len(lyst) > 1:
        return "s"
    return ""
def were_was(lyst):
    """returns were if there's more than one element in the list. If not, it returns was."""
    if len(lyst) > 1:
        return "were"
    return "was"
def test_events():
    """This function is for testing new functions without having to type the functions over and over again."""
    global place
    global Tools
    global inventory
    global good_guys
    global inactive_good_guys
    global inactive_bad_guys
    global bad_guys
    global Vehicles
    global active_vehicles
    global Places
    for x in range(10):
        active_vehicles.append(random.choice(Vehicles))
    #to_test = [ "conversation()"]
    to_test = ["fight(False)", "NewPlace()", "location_specific()", "use_item()", "goto()"]
    print("######TEST######")
    # Test location_specific() and use_item() on separate runs.
    # To Test:
    # all functions
    # location_specific()
    # use_item()
    for z in to_test:
        print("---------| "+z+" |-----------")
        for x in range(10):
            #place = y
            if len(bad_guys) == 0:
                bad_guys.extend(["bad guy "+str(x) for x in range(10)])
            if len(inactive_bad_guys) == 0:
                inactive_bad_guys.extend(["inactive bad guy "+str(x) for x in range(10)])
            if len(inactive_good_guys) == 0:
                inactive_good_guys.extend(["inactive good guy "+str(x) for x in range(10)])
            if len(good_guys) == 0:
                good_guys.extend(["good guy "+str(x) for x in range(10)])
            inventory = Tools
            print("Iteration "+str(x+1)+"/10")
            inventory.append(random.choice(Vehicles))
            exec(z)
            good_guy_check()
    print("#######END TEST########")
def convert_character(in_closing):
    """This function randomly makes a good guy a bad guy, a bad guy a good guy, and could also make characters go away from the main action."""
    global good_guys
    global bad_guys
    global inactive_bad_guys
    global inactive_good_guys
    global Places
    parties = [good_guys, bad_guys, inactive_good_guys, inactive_bad_guys]
    startParty = random.choice(parties)
    parties.remove(startParty)
    if in_closing == True:
         if bad_guys in parties:
             parties.remove(bad_guys)
         if inactive_bad_guys in parties:
             parties.remove(inactive_bad_guys)
    endParty = random.choice(parties)
    if len(startParty) > 0 and startParty != endParty:
        print(" ",end=" ")
        convertee = random.choice(startParty)
        endParty.append(convertee)
        startParty.remove(convertee)
        if startParty == bad_guys:
            if endParty == good_guys:
                storyprint(convertee + " soon learned that what evil he/she was doing was wrong. So he/she joined the good guy"+is_plural(good_guys)+".", "\n")
            elif endParty == inactive_bad_guys:
                storyprint(convertee + " retreated.", "\n")
            else:
                storyprint(convertee + " made a hasty retreat. Soon after he/she retreated, he/she turned his/her back on doing evil deeds.", "\n")
        elif startParty == good_guys:
            if endParty == bad_guys:
                if len(good_guys) > 0:
                    storyprint(convertee + " did not want to do what the other good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" doing, so he/she turned bad.", "\n")
                else:
                    storyprint(convertee + ", the last good guy turned evil.", "\n")
            elif endParty == inactive_good_guys:
                if len(good_guys) > 0:
                    storyprint(convertee + " started puffing and said, \"I need a break. You guy"+is_plural(good_guys)+" can go on without me. I'll catch up with you sometime.\" And so, the good guy"+is_plural(good_guys)+" continued without him/her.", "\n")
                else:
                    storyprint(convertee + " just left and went to "+random.choice(Places)+". It's more peaceful there.", "\n")
            else:
                if len(good_guys) > 0:
                    storyprint(convertee + " thought the good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" a little bit weird in their thinking, so he/she turned his/her back on them and left.", "\n")
                else:
                    storyprint(convertee + " thought that doing good is worth nothing. So he/she left and turned bad.", "\n")
        elif startParty == inactive_good_guys:
            if endParty == inactive_bad_guys:
                storyprint("Meanwhile, " + convertee + " had an idea. He/she would go against the good guy"+is_plural(good_guys)+" because he/she thought that they "+were_was(good_guys)+" being silly. And so, he/she turned bad.", "\n")
            elif endParty == good_guys:
                storyprint("The good guy"+is_plural(good_guys)+" suddenly ran across good old " + convertee + ". What a surprise!", "\n")
            else:
                storyprint("Suddenly, mean old " + convertee + " appeared with an angry face. Wait, WHAT?! he/she TURNED BAD?!?", "\n")
        else:
            if endParty == inactive_good_guys:
                storyprint("Meanwhile, " + convertee + " thought about what he/she was doing. \"You know what?\" he thought out loud. \"I think those good guy"+is_plural(good_guys)+" got it right.\" And so, he/she turned good.", "\n")
            elif endParty == good_guys:
                storyprint(convertee + " showed up. The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" alarmed. \"I'm sorry for being a bad guy. I know, I'm a stinkbrain.\" " + convertee + " said. \"I wanna join you now.\" And so, he/she was with the good guy"+is_plural(good_guys)+".", "\n")
            else:
                storyprint("Suddenly, " + convertee + " emerged. The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" ready for battle.", "\n")
def conversation():
    """Makes the characters talk"""
    global good_guys
    global bad_guys
    global inactive_good_guys
    global inactive_bad_guys
    global inventory
    rep = random.randint(1,10)
    askReply = False
    overPhone = False
    party = ""
    for x in range(rep):
        print(" ", end=" ")
        overPhone = False
        if random.randint(0,3) == 1 and len(bad_guys) > 0:
            storyprint(random.choice(bad_guys), " ")
            overPhone = False
            party = "bad"
        elif random.randint(0,2) == 1 and len(bad_guys) > 0  and len(inactive_bad_guys) > 0:
            storyprint(random.choice(inactive_bad_guys), " ")
            overPhone = True
            party = "bad"
        elif random.randint(0,1) == 1 and len(inactive_good_guys) > 0  and "Cell phone" in inventory:
            storyprint(random.choice(inactive_good_guys), " ")
            overPhone = True
            party = "good"
        else:
            storyprint(random.choice(good_guys), " ")
            overPhone = False
            party = "good"
        if askReply == True:
                    storyprint("replied", '')
        else:
                    storyprint("said", '')
        saying = input(", \" (what did he/she say?)")
        if re.search(r'"$', saying):
            saying = re.sub(r'"$', "", saying)
        storyprint(saying+'"', "\n")
        if re.search(r"\?$", saying):
            askReply = True
        else:
            askReply = False
        if x == rep - 1 and askReply == True:
            rep += 1
def kill_character():
        """Kills off a character"""
        global good_guys
        global bad_guys
        global inventory
        global Tools
        global death_terms
        good_guy_check()
        victimParty = "---"
        party = random.randint(0, 1)
        if len(good_guys) > 0 and party == 1:
            victim = random.choice(good_guys)
            victimParty = "good"
            good_guys.remove(victim)
        elif len(bad_guys) > 0:
            victim = random.choice(bad_guys)
            victimParty = "bad"
            bad_guys.remove(victim)
        if victimParty != "---":
            print(" ",end=" ")
            if len(bad_guys) > 0 and len(good_guys) > 0:
                if victimParty == "good":
                    weapon = random.choice(Tools)
                    murderer = random.choice(bad_guys)
                else:
                    if len(inventory) > 0:
                        weapon = random.choice(inventory)
                    else:
                        weapon = "bare hands"
                    murderer = random.choice(good_guys)
                storyprint(murderer + " killed " + victim + " with (a) " + weapon, "\n")
            else:
                r = random.randint(0, 3)
                if r == 1:
                    storyprint(victim + " was satisfied with the length of his/her days. He/she "+random.choice(death_terms)+" of old age.", "\n")
                elif r == 2:
                    storyprint(victim + " was sick with a serious illness.", " ")
                    i = random.randint(0, 1)
                    if i == 1:
                        storyprint("He/she got an injection. his/her friends hoped that he/she would be alright, but he/she "+ random.choice(death_terms) + ".", "\n")
                    else:
                        storyprint("The sickness was so serious, he/she "+ random.choice(death_terms) +".", "\n")
                elif r == 3:
                    storyprint(victim+" had a fatal fall. he/she "+ random.choice(death_terms) + " from it.", "\n")
                else:
                    storyprint(victim+" was poisoned", "")
                    if len(bad_guys) > 0:
                        storyprint(" by "+ random.choice(bad_guys), "")
                    storyprint(". And so, "+victim+" "+random.choice(death_terms)+".", "\n")
def fight(inClosing):
    """If there are active good guys and active bad guys, then it starts a fight between good guys and bad guys. If the inClosing parameter is True, it's a fight to the death."""
    global bad_guys
    global good_guys
    global inventory
    global Tools
    global Prizes
    global inactive_good_guys
    global inactive_bad_guys
    good_guy_check()
    turn = 0
    if len(good_guys) > 0 and len(bad_guys) > 0:
        storyprint("  The good guy"+is_plural(good_guys)+" and the bad guy"+is_plural(bad_guys)+" started a fight.", " ")
        while len(good_guys) > 0 and len(bad_guys) > 0:
                print(" ",end=" ")
                attacker = random.choice(good_guys)
                good_turn = random.randint(0, 10)
                victim = random.choice(bad_guys)
                if len(inventory) == 0:
                    item = "bare hands"
                else:
                    item = random.choice(inventory)
                if good_turn < 2 and turn > 0 and inClosing == False:
                    storyprint("The good guy"+is_plural(good_guys)+" fled from battle.", "\n")
                    inactive_bad_guys.extend(bad_guys)
                    bad_guys.clear()
                    break
                else:
                    storyprint(attacker + " attacked " + victim + " with " + item + ".", " ")
                    if random.randint(0,2) == 2:
                        storyprint(victim + " was defeated.","\n")
                        bad_guys.remove(victim)
                        if len(bad_guys) == 0:
                            storyprint("  The good guy"+is_plural(good_guys)+" won!", "\n")
                            break
                    elif random.randint(0,1) == 1:
                        storyprint(victim + " blocked the attack with a " + random.choice(Tools) + ".", "\n")
                    elif random.randint(0,1) == 0:
                        storyprint("Missed.", "\n")
                    else:
                        print("")
                if len(good_guys) > 0 and len(bad_guys) > 0:
                    print(" ",end=" ")
                    attacker = random.choice(bad_guys)
                    bad_turn = random.randint(0, 10)
                    attacker = random.choice(bad_guys)
                    victim = random.choice(good_guys)
                    item = random.choice(Tools)
                    if bad_turn < 2 and turn > 0 and inClosing == False:
                        storyprint("The bad guy"+is_plural(bad_guys)+" fled from battle.", "\n")
                        inactive_bad_guys.extend(bad_guys)
                        bad_guys.clear()
                        break
                    else:
                        storyprint(attacker + " attacked " + victim + " with " + item + ".", " ")
                        if "Shield" in inventory and random.randint(0,2) < 2:
                            storyprint(victim + " blocked the attack with a shield."," ")
                            if random.randint(0,2) == 2:
                                inventory.remove("Shield")
                                storyprint(victim + "'s shield broke from the attack.", "\n")
                            else:
                                print('')
                        elif random.randint(0,2) == 2:
                            storyprint(victim + " was defeated.", "\n")
                            good_guys.remove(victim)
                            if len(good_guys) == 0:
                                storyprint("  The bad guy"+is_plural(bad_guys)+" won.", "\n")
                                break
                        elif random.randint(0,1) == 1:
                            if len(inventory) == 0:
                                storyprint("Missed.", "\n")
                            else:
                                storyprint(victim + " blocked the attack with (a) " + random.choice(inventory)+ ".", "\n")
                        else:
                            print('')
                turn += 1
def introduce_bad_guy():
    """Introduces bad guy"""
    global bad_guys
    global inactive_bad_guys
    global inactive_good_guys
    global good_guys
    global Places
    global PlaceTypes
    global Tools
    global place
    good_guy_check()
    isActive = random.randint(0, 1)
    r = random.randint(0, 3)
    s = random.randint(0,1)
    crimes = ["stole a", "was vandalizing", "was trying to murder", "was robbing a bank", "was robbing a store", "was smuggling", "killed someone", "was commiting sins", "was stealing stuff", "was stealing stuff from"]
    crime = random.choice(crimes)

    if isActive == False:
                NewPlace()
    if isActive == 1 and r == 1:
        introduce(bad_guys, True)
        if crime == "was trying to murder" or crime == "was stealing stuff from":
            if len(inactive_good_guys) > 0 and s == 0 and r == 1:
                introduce(good_guys, True)
        elif crime == "was smuggling" or crime == "stole a":
                    if s == 1 and r == 1:
                        thing = input("( Type in an item )")
                        if not thing in Tools:
                            Tools.append(thing)
                    else:
                        thing = random.choice(Tools)
        print(" ",end=" ")
        if r == 1:
            storyprint("Around the corner, " + bad_guys[-1] + " appeared. He/she ", "")
            storyprint(crime, "")
            if crime == "was trying to murder" or crime == "was stealing stuff from":
                if len(inactive_good_guys) > 0 and s == 1:
                    new_guy = random.choice(inactive_good_guys)
                    good_guys.append(new_guy)
                    inactive_good_guys.remove(new_guy)
                    print(" "+new_guy+".")
                else:
                    storyprint(" "+good_guys[-1] + ".", "\n")
            elif crime == "was smuggling" or crime == "stole a":
                storyprint(" "+thing+".", "\n")
            elif crime == "was vandalizing":

                storyprint(" "+place+".", "\n")
            else:
                print(".")
            storyprint("  \"Hey! Stop that!\" " + random.choice(good_guys) + " shouted at " + bad_guys[-1] + ".", "\n")
            if random.randint(0,1) == 1:
                fight(False)
            else:
                storyprint("  "+bad_guys[-1] + " saw the good guy"+is_plural(good_guys)+". He/she ran away.", "\n")
                retreated = bad_guys[-1]
                inactive_bad_guys.append(retreated)
                bad_guys.remove(retreated)
        elif r == 2:
            storyprint("Suddenly, " + bad_guys[-1] + " jumped behind the good guy"+is_plural(good_guys)+" and took them by surprise.", "\n")
            fight(False)
        elif r == 3:
            storyprint("The good guy"+is_plural(good_guys)+" found " + bad_guys[-1] + ".", "\n")
        else:
            storyprint(bad_guys[-1] + " was having a pleasant walk. It wasn't pleasant for long, as soon as " + bad_guys[-1] + " saw the good guy"+is_plural(good_guys)+", his/her walk immediately became the worst one he/she ever had.", "\n")
    else:
        introduce(bad_guys, False)
        storyprint("  Meanwhile, at " + random.choice(Places), ", ")
        r = random.randint(0, 2)
        if r == 1:
            storyprint(inactive_bad_guys[-1] + " was planning his/her next evil deed. He/she cackled evilly. \"This is the most evil thing I've ever planned! You know what? I'm just gonna do it!\" And so, he/she went out to do it. I'm not telling you. It's a secret.", "\n")
        elif r == 2:
            storyprint(inactive_bad_guys[-1] + " saw the good guy"+is_plural(good_guys)+" out the window. \"Uh-oh. I need to deal with them.\" He/she looked out the window again. \"Oh, drat! They're gone! Oh, well. I'm just gonna go after them.\" That was what he/she did.", "\n")
        else:
            storyprint(inactive_bad_guys[-1] + " was enjoying him/herself. He/she was thinking about all the evil deeds he/she had done in the past. \"You know what?\" he/she said. \"I'm going to go out and do some more evil deeds so that I'll have more deeds for me to think about.\" And so, he/she went out to do some more evil deeds for him/her to think about.", "\n")
def good_guy_check():
    """Checks if there are active good guys. If not, then this function will introduce or re-introduce good guys."""
    global good_guys
    global inactive_good_guys
    if len(good_guys) == 0:
        if len(inactive_good_guys) > 0:
            good_guys = inactive_good_guys
            inactive_good_guys.clear()
            while len(good_guys) == 0:
                r = random.randint(1,10)
                for x in range(r):
                    introduce(good_guys, True)
            storyprint("  There were no good guys left. But some other good guy"+is_plural(good_guys)+" came to do the right thing.", " ")
            list_party(good_guys, "Those good guys were")
        else:
            storyprint("  The good guys were gone. But some more good guys came to the scene.", "\n")
            for x in range(random.randint(2, 13)):
                introduce(good_guys, True)
            list_party(good_guys, "  The new good guys were")
def findGoal(Gtype):
    """This function is used to check if a certain type of goal is in the goals list."""
    global goals
    if len(goals) > 0:
        for goal in goals:
            if goal.startswith(Gtype):
                return True
    return False
def goto():
    """This function is used when the good guys go somewhere."""
    global place
    global Places
    global PlaceTypes
    global goals
    global active_vehicles
    global inactive_bad_guys
    global bad_guys
    good_guy_check()
    if findGoal("Visit") and random.randint(0,1) == 1:
        for goal in goals:
            if goal.startswith("Visit"):
                subject = goal.replace("Visit ", "")
                break
    else:
        if random.randint(0,1) == 1:
                    subject = input("(type in a name of a place.) ")
                    if not NewPlace in PlaceTypes:
                        Places.append(NewPlace)
                        subject_type = input("(Type in \"indoors\" if that place you entered is indoors.) ")
                        if 'indoors' in subject_type:
                            subject_type = 'indoors'
                        elif 'outdoors' in subject_type:
                            subject_type = 'outdoors'
                        PlaceTypes[NewPlace] = subject_type
        else:
                    subject = random.choice(Places)
    print(" ", end=" ")
    if subject == "Outer space" and "Rocket ship" in active_vehicles:
        active_vehicles = ["Rocket ship"]
        place = subject
        storyprint("3, 2, 1, BLAST OFF! The good guy"+is_plural(good_guys)+" blasted off into space in a rocket ship!", "\n")
        if len(bad_guys) > 0:
            left_behind = bad_guys
            bad_guys.clear()
            inactive_bad_guys.extend(left_behind)
    else:
        if subject == "Outer space" and not "Time machine" in active_vehicles:
            while subject ==  "Outer space" or subject == place:
                subject = random.choice(Places)
        place = subject
        storyprint("The good guy"+is_plural(good_guys)+" went to "+place+" by ", "")
        if len(active_vehicles) == 0:
            storyprint("foot.", "\n")
        else:
            storyprint(random.choice(active_vehicles)+".", "\n")
        if len(bad_guys) > 0:
            left_behind = bad_guys
            bad_guys.clear()
            inactive_bad_guys.extend(left_behind)
def introduce(party, isactive):
    """This function introduces a character with a randomly generated name."""
    global names
    global last_names
    global CharacterType
    global Animals
    global Foods
    global good_adjective
    global bad_adjective
    global inactive_good_guys
    global inactive_bad_guys
    if random.randint(0,1) == 1:
        prefixes = ["Mr.", "Madame", "Monseiur", "Ms.", "Leutenant", "General", "Colonel", "Mrs.", "Mr.", "Miss", "Ms.", "Herr", "Col.", "King", "Queen", "Dr.", "Doctor", "Prof.", "Professor"]
        firstNameType = random.randint(1,6)
        midNameType = random.randint(0,1)
        lastNameType = random.randint(0,3)
        if firstNameType == 1:
            newCharName = random.choice(names)[:1] + "."
        elif firstNameType == 2:
            newCharName = ""
        else:
            newCharName = random.choice(names)
        if firstNameType < 3:
            newCharName = random.choice(prefixes)+" "+newCharName
        if midNameType == 1:
            MidInitial = ""
        else:
            MidInitial = random.choice(names)[:1]
        if lastNameType == 1 and MidInitial != "" and firstNameType != 2:
            newLastName = ""
        elif lastNameType == 2:
            newLastName = random.choice(last_names)[:1] + "."
        elif lastNameType == 3:
            newLastName = random.choice(names)[:1] + "."
        else:
            newLastName = random.choice(last_names)
        WhatIsIt = random.randint(0, 5)
        if WhatIsIt == 1:
            newCharType = random.choice(Animals)
        elif WhatIsIt == 2:
            newCharType = random.choice(CharacterType)
        elif WhatIsIt == 3:
            newCharType = random.choice(CharacterType)
        elif WhatIsIt == 4:
            newCharType = random.choice(Animals)
        elif WhatIsIt == 5:
            if party == good_guys:
                newCharType = input("(This good guy is what?)")
            else:
                newCharType = input("(This bad guy is what?)")
            if not newCharType in Animals and not newCharType in CharacterType and not newCharType in Foods:
                what = input("(Is this an animal, food, or something else?)")
                if "food" in what.lower():
                    Foods.append(newCharType)
                elif "animal" in what.lower():
                    Animals.append(newCharType)
                else:
                    CharacterType.append(newCharType)
        else:
            newCharType = random.choice(Foods)
        if party == good_guys:
            if random.randint(0,1) == 1:
                newCharAdj = random.choice(good_adjective)
            else:
                newCharAdj = input("(Type in a good adjective.)")
                if not newCharAdj in good_adjective:
                    good_adjective.append(newCharAdj)
        else:
            if random.randint(0,1) == 1:
                newCharAdj = random.choice(bad_adjective)
            else:
                newCharAdj = input("(Type in a bad adjective.)")
                if not newCharAdj in bad_adjective:
                    bad_adjective.append(newCharAdj)
        newCharType = newCharType.capitalize()
        newCharAdj = newCharAdj.capitalize()
        if len(MidInitial) == 0:
            fullNewname = newCharName.strip() + " " + newLastName
        else:
            fullNewname = newCharName.strip() + " " + MidInitial + ". " + newLastName
        fullNewname = fullNewname.strip() + " the "+ newCharAdj + " " + newCharType
    else:
        if party == good_guys:
            fullNewname = input("(Please type a name for a good guy) ")
        else:
            fullNewname = input("(Please type a name for a bad guy) ")
    if isactive:
        party.append(fullNewname)
    else:
        if party == good_guys:
            inactive_good_guys.append(fullNewname)
        else:
            inactive_bad_guys.append(fullNewname)
def print_inventory():
    """Prints the good guys' inventory, and how much of a certain item."""
    global inventory
    global good_guys
    global last_list
    if last_list != "inventory":
        last_list = "inventory"
        good_guy_check()
        inventory_dictionary = {}
        for item in inventory:
            if item in inventory_dictionary:
                inventory_dictionary[item] += 1
            else:
                inventory_dictionary[item] = 1
        storyprint("  The good guy"+is_plural(good_guys)+" had ", "")
        printed_inventory = []
        for item, quantity in inventory_dictionary.items():
            if quantity == 1:
                printed_inventory.append("a(n) " + item)
            else:
                if item.endswith("s"):
                    printed_inventory.append(str(quantity) + " " + item + "es")
                else:
                    printed_inventory.append(str(quantity) + " " + item + "s")
        for index, item in enumerate(printed_inventory):
            if index == len(printed_inventory)-1:
                storyprint("and " + item.lower() + ".", "\n")
            else:
                storyprint(item.lower(), ", ")
def list_vehicles():
    """Lists good guys' vehicles."""
    global active_vehicles
    global last_list
    if last_list != 'vehicles':
        last_list = 'vehicles'
        if len(active_vehicles) == 0:
            return "foot"
        elif len(active_vehicles) == 1:
            return "a(n) "+active_vehicles[0]
        else:
            to_return = ""
            for index, vehicle in enumerate(active_vehicles):
                if index == len(active_vehicles) - 1:
                    to_return += "and a(n) "+ vehicle
                else:
                    to_return += vehicle + ", a(n) "
        return to_return
    else:
        return "... You know what vehicles the good guy"+is_plural(good_guys)+" had."
def list_party(lyst, start):
    """Prints all the string items in a list. Most of the time, it's used to list the names of the good guys."""
    global last_list
    if not start.startswith("Our hero") or not start.startswith("The good"):
        last_list = "none"
    if last_list != 'party':
        if start.startswith("Our hero") or start.startswith("The good"):
            last_list = "party"
        storyprint(start," ")
        for index, person in enumerate(lyst):
            if index == len(lyst)-1 and len(lyst) != 1:
                storyprint("and " + person, "")
            else:
                storyprint(person, "")
            if person.endswith("Holy Ghost"):
                storyprint("(he/she isn't THE Holy Ghost, but a ghost that is holy)","")
            if index == len(lyst)-1:
                print(".")
            else:
                print(",", end=" ")
def location_specific():
    """This function does something different, depending on the location."""
    global goals
    global Tools
    global inventory
    global Places
    global PlaceTypes
    global good_adjectives
    global good_guys
    global bad_guys
    global bad_adjective
    global Animals
    global Vehicles
    global inactive_good_guys
    global inactive_bad_guys
    global Prizes
    global Foods
    global death_terms
    global place
    global names
    good_guy_check()
    if place == "Chernobyl":
        storyprint("  The radiation in Chernobyl was intense! The good guy"+is_plural(good_guys)+" needed to get out of Chernobyl!", "\n")
        if not "Leave Chernobyl" in goals:
            goals.append("Leave Chernobyl")
        if random.randint(0,2) == 1:
            victim = random.choice(good_guys)
            good_guys.remove(victim)
            print(" ", end=" ")
            storyprint(victim + " couldn't stand the radiation, so he/she "+random.choice(death_terms)+" from it.", "\n")
            if random.randint(0,1) == 1 and len(good_guys) > 0:
                storyprint("  After "+victim+" died from radiation, the other good guy"+is_plural(good_guys)+" slowly "+random.choice(death_terms)+" from the radiation. One by one.", "\n")
                good_guys.clear()
            good_guy_check()
        if len(bad_guys) > 0 and random.randint(0, 1) == 1:
            victim = random.choice(bad_guys)
            bad_guys.remove(victim)
            print(" ", end=" ")
            storyprint(victim + " couldn't stand the radiation, so he/she "+random.choice(death_terms)+" from it.", "\n")
            if random.randint(0,1) == 1 and len(bad_guys) > 0:
                storyprint("  After "+victim+" died from radiation, the other bad guy"+is_plural(bad_guys)+" slowly "+random.choice(death_terms)+" from the radiation. One by one.", "\n")
                bad_guys.clear()
    elif place == "Death Valley":
        storyprint("  Death Valley is called \"Death Valley\" for a reason.", " ")
        if random.randint(0,2) == 1 and len(good_guys) > 0:
            victim = random.choice(good_guys)
            good_guys.remove(victim)
        elif random.randint(0,1) == 1 and len(bad_guys) > 0:
            victim = random.choice(bad_guys)
            bad_guys.remove(victim)
        else:
            victim = "Nobody"
        storyprint(victim + " "+random.choice(death_terms)+".", "\n")
    elif place == "church":
        print(" ", end=" ")
        if random.randint(0,1) == 1:
            storyprint("A priest was saying Mass.", "\n")
        else:
            storyprint("The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" praying.", "\n")
        if len(bad_guys) > 0:
            good_guys.extend(bad_guys)
            bad_guys.clear()
            storyprint("  The bad guy(s) at church learned that what they "+were_was(bad_guys)+" doing was so bad. And so, there were more good guys.", "\n")
            list_party(good_guys, "  Now, the good guys were")
        if random.randint(0,1) == 1:
            new_mission()
            storyprint("  That might have been an answer to the good guy"+is_plural(good_guys)+"'s prayers!", "\n")
            if goals[-1] == "Visit Outer space" and not "Rocket ship" in inventory:
                inventory.append("Rocket ship")
                storyprint("  Since the good guy"+is_plural(good_guys)+"'s mission was to go to space, they recieved a rocket ship for them to blast off into space in.", "\n")
    elif place == "jail":
        print(" ", end=" ")
        if random.randint(0,1) == 1:
            storyprint("The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" just visiting the jail. They did nothing wrong.", "\n")
            if len(inactive_bad_guys) > 0 or len(bad_guys) > 0:
                if len(bad_guys) > 0:
                    if random.randint(0,1) == 1:
                        inactive_bad_guys.extend(bad_guys)
                    bad_guys.clear()
                storyprint("  The bad guy"+is_plural(inactive_bad_guys)+" "+were_was(inactive_bad_guys)+" behind bars. They wouldn't be doing any more evil for a long time.", "\n")
        else:
            storyprint("The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" behind bars. They needed to escape."," ")
            goals.append("Leave jail")
            if len(inventory) > 0:
                storyprint("So, they tried to escape with a "+random.choice(inventory)+".", "\n")
                if random.randint(0,1) == 1:
                    NewPlace()
                    storyprint("  They managed to escape! They were now in "+place+".", "\n")
                else:
                    storyprint("  The plan to escape didn't work.", "\n")
            else:
                storyprint("The good guy"+is_plural(good_guys)+" had nothing to escape from jail with.", "\n")
    elif place == "the Open ocean":
        r = random.randint(0, 1)
        if r == 1:
            for x in range(random.randint(3, 15)):
                if random.randint(0,1) == 1:
                    bad_guys.append(random.choice(names) + " the Pirate")
                else:
                    pirate_name = input("(Give a pirate a name.) ")
            storyprint("  Pirates attacked the good guy"+is_plural(good_guys), "")
            if "Boat" in active_vehicles:
                storyprint("'s ship","")
            print("!")
            bad_guys.append(pirate_name + " the Pirate")
            if "Boat" in active_vehicles:
                list_party(bad_guys, "The bad guys on the ship were")
            else:
                list_party(bad_guys, "The bad guys here were")
            fight(True)
        elif not "Boat" in active_vehicles:
            storyprint("  The good guy"+is_plural(good_guys)+" had to swim.", " ")
            victim = random.choice(good_guys)
            while victim.endswith("Diver") or victim != "Nobody" or "fish" in victim.lower():
                if random.randint(0, 1) == 1:
                    victim = random.choice(good_guys)
                else:
                    victim = "Nobody"
                    good_guys.append("Nobody")
                    break
            good_guys.remove(victim)
            storyprint(victim + " drowned because he/she wasn't good at swimming.", "\n")
        else:
            victim = random.choice(good_guys)
            storyprint(victim + " fell overboard! The good guy"+is_plural(good_guys)+" tried to rescue him/her,", "")
            s = random.randint(0, 2)
            if s == 1 and not victim.endswith("Diver"):
                storyprint(" but he/she drowned.", "\n")
                good_guys.remove(victim)
            elif s == 2:
                storyprint(" but he/she disappeared under the water.", "\n")
                good_guys.remove(victim)
                inactive_good_guys.append(victim)
            else:
                storyprint(" and he/she was saved!", "\n")
    elif place == "Outer space":
        print(" ", end=" ")
        if random.randint(0, 2) == 1 and "Rocket ship" in active_vehicles:
            storyprint("  An asteroid crashed into the good guy"+is_plural(good_guys)+"'s rocket ship."," ")
            if random.randint(0,1) == 1:
                storyprint('Luckily, '+random.choice(good_guys)+ " fixed it. Now, the good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" journeying through space.", "\n")
            else:
                storyprint("The damage couldn't be fixed. The good guy"+is_plural(good_guys)+" had to get back to earth fast!", "\n")
                if random.randint(0,1) == 1:
                    NewPlace()
                    storyprint("  They flew to "+place+".", " ")
                    if place == "Outer space":
                        storyprint("Wait, WHAT?!? They were STILL IN SPACE??? Since space was so big, and the good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" so far from Earth, they were still in space.", "\n")
                        goals.append("Leave Outer space")
                    else:
                        storyprint("It was good to be back on Earth. The good guy"+is_plural(good_guys)+" threw their damaged space ship away. It was now on top of a big mountain of trash in the dump where everyone passing by could see it.", "\n")
                        active_vehicles.remove("Rocket ship")
        elif random.randint(0,1) == 1:
            victim = random.choice(good_guys)
            storyprint("  "+victim + " ran out of air. So, he/she "+random.choice(death_terms)+".", "\n")
            good_guys.remove(victim)
        else:
            nice = random.randint(0,1)
            if nice == 1:
                alien_name = input("(Name the friendly alien.) ")
                good_guys.append(alien_name+" the Friendly Alien")
                storyprint("  The"+is_plural(good_guys)+" met "+good_guys[-1]+". That alien was friendly and followed the good guy"+is_plural(good_guys)+".", "\n")
            else:
                alien_name = input("(Name the hostile alien.) ")
                bad_guys.append(alien_name+" the Hostile Alien")
                storyprint("  The"+is_plural(good_guys)+" met "+bad_guys[-1]+" That alien wasn't happy. It had a laser gun pointed at the good guy"+is_plural(good_guys)+".", "\n")
                fight(False)
    elif place == "a Haunted house":
        if random.randint(0,1) == 1:
            alien_name = input("(Name the friendly ghost.) ")
            good_guys.append(alien_name+" the Friendly Ghost")
            storyprint("  The good guy(s), met "+good_guys[-1]+". It was friendly, so it followed them around.", "\n")
        else:
            alien_name = input("(Name the unfriendly ghost.) ")
            bad_guys.append(alien_name+" the Unfriendly Ghost")
            goals.append("Leave a Haunted house")
            storyprint("  The good guy"+is_plural(good_guys)+" heard a mysterious voice from nowhere saying, \"Goooo aaaawwaaayyy. Yooou're nooot weelcooome heeere.\"\n  The good guy"+is_plural(good_guys)+" continued walking down the hallway of the haunted house, with the floorboards creaking for every step they take.\n  Suddenly, they saw a ghost! \"I told you to go away!\" the ghost shouted. \"Or my name isn't "+bad_guys[-1]+"!\"", "\n")
    elif place == "A desert":
        storyprint("  The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" thirsty.")
        if "Food" in inventory:
            if random.randint(0,1) == 1:
                snack = random.choice(Foods)
            else:
                snack = input("(Type in a food.)")
                if not snack in Foods:
                    Foods.append(snack)
            storyprint("  The good guy"+is_plural(good_guys)+" had (a) "+snack+". Somehow, they felt refreshed. But not for long.", "\n")
            if random.randint(0,1) == 1:
                inventory.remove("Food")
            goals.append("Leave A desert")
        else:
            NewPlace = place
            while NewPlace == place:
                NewPlace = random.choice(Places)
            storyprint("  "+random.choice(good_guys)+" saw "+NewPlace+". \"Hey!\" he/she said. \"There's probably water there!\"", "\n")
            storyprint("  \"Yeah!\" "+random.choice(good_guys) + " said. \"Let's go!\"", "\n")
            if random.randint(0,5) == 5:
                storyprint("That " +NewPlace+" place was real. The good guys made it safely there, out of the desert.", "\n")
                place = NewPlace
            else:
                storyprint("When the good guy"+is_plural(good_guys)+" went over to where that place was, or where they thought it was, it disappeared. It was a mirage.\n  \"We need to get out of here!\" "+random.choice(good_guys)+" said.", "\n")
                goals.append("Leave A desert")
    elif place == "Minecraft":
        if random.randint(0,1) == 1:
            storyprint("  Since the good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" in Minecraft, the game where people build things out of blocks. The good guy"+is_plural(good_guys)+" decided to build something in Minecraft.\n  Later, the good guy"+is_plural(good_guys)+" built "+random.choice(Places)+" in Minecraft!", "\n")
        else:
            for x in range(random.randint(2,10)):
                 if random.randint(0,1) == 1:
                     bad_guys.append("Creeper "+str(x+1))
                 else:
                     creeper_name = input("(Give a creeper a name.) ")
                     if not "Creeper" in creeper_name:
                         creeper_name = creeper_name + " the Creeper"
                     bad_guys.append(creeper_name)
            storyprint("  Suddenly, some creepers appeared. When I say creepers when I'm also talking about Minecraft, I'm not talking about plants that climb up trees and stuff. I'm talking about blocky, mottled-green creatures with no arms and four little legs that it scuttles with, ready to explode in your face.", "\n")
            if random.randint(0,1) == 1:
                victim = random.choice(good_guys)
                storyprint("  A creeper crept up and blew "+victim+" up. That was the last of him/her.", "\n")
                good_guys.remove(victim)

            storyprint("  The creepers were ready for battle!", "\n")
            fight(False)
    elif place == "a cave":
        print(" ", end=" ")
        if random.randint(0,1) == 1:
            storyprint("The good guy"+is_plural(good_guys)+" went mining.", end=" ")
            if random.randint(0,3) == 2:
                storyprint("They found gold!", "\n")
                inventory.append("money")
                if random.randint(0,1) == 1:
                    inventory.append("treasure")
            else:
                storyprint("They didn't mine anything interesting.", "\n")
        else:
            storyprint("The ceiling caved in. The good guy"+is_plural(good_guys)+" picked at the wall that kept them inside the cave. Would they make it out?", "\n")
            NewPlace()
            if random.randint(0,1) == 1:
                storyprint("  The good guy"+is_plural(good_guys)+" made it out! They were now at "+place+".", "\n")
            else:
                storyprint("  The good guy"+is_plural(good_guys)+" suffocated.", "\n")
                good_guys.clear()
                good_guy_check()
                storyprint("The other good guy"+is_plural(good_guys)+' "+were_was(good_guys)+" at '+place+".", "\n")
    elif place == "a school":
        storyprint("  Life in school was boring. The lessons were long. The lunches there were bland and tasteless. The good guy"+is_plural(good_guys)+" needed to get out of there.", "\n")
        goals.append("Leave a school")
def new_mission():
    """This function gives the good guys a goal to work towards."""
    global goals
    global Tools
    global inventory
    global Places
    global good_adjectives
    global good_guys
    global bad_guys
    global bad_adjective
    global Animals
    global Vehicles
    global inactive_good_guys
    global inactive_bad_guys
    global Prizes
    global Foods
    global place
    global PlaceTypes
    good_guy_check()

    missionTypes = ["Leave", "Take", "Destroy", "Visit", "Meet"]
    mission_kind = random.choice(missionTypes)
    if mission_kind == "Leave":
        if not "Leave "+ place in goals:
            goals.append("Leave " + place)

    elif mission_kind == "Take" or mission_kind == "Destroy":
        r = random.randint(0, 4)
        if r == 0:
                item = random.choice(Tools)
        elif r == 1:
                item = random.choice(Tools)
        elif r == 2:
                item = random.choice(Vehicles)
        elif r == 3:
                item = random.choice(Foods)
        elif r == 4:
                item = random.choice(Prizes)
        if "" in inventory:
            inventory.remove("")
        r = random.randint(0,2)
        if mission_kind == "Take":
            if r == 1:
                item = random.choice(good_adjective) + " " + item + " of " + random.choice(Places)
            elif r == 2:
                item = input("(Type in a name of an item for the good guys to get.) ")

        else:
            if r == 1:
                item = random.choice(bad_adjective) + " " + item + " of " + random.choice(Places)
            elif r == 2:
                item = input("(Type in a name of an item for the good guys to destroy.) ")


        if not mission_kind + " " + item in goals:
            goals.append(mission_kind + " " + item)
    elif mission_kind == "Visit":
        if random.randint(0,1) == 1:
            Place2GoTo = place
            while Place2GoTo == place:
                Place2GoTo = random.choice(Places)
        else:
            Place2GoTo = input("(type in a name of a place.) ")
        if not Place2GoTo in PlaceTypes:
            Places.append(Place2GoTo)
            subject_type = input("(Type in \"indoors\" if that place you entered is indoors.) ")
            if 'indoors' in subject_type:
                subject_type = 'indoors'
            elif 'outdoors' in subject_type:
                subject_type = 'outdoors'
            PlaceTypes[Place2GoTo] = subject_type

        if not "Visit "+Place2GoTo in goals:
            goals.append("Visit "+Place2GoTo)
    else:
        introduce(good_guys, False)

        if not "Meet "+inactive_good_guys[-1] in goals:
            goals.append("Meet "+inactive_good_guys[-1])
            to_meet = inactive_good_guys[-1]
    if "computer" in inventory and random.randint(0,1) == 1:
        introduce(good_guys, False)
        storyprint("  The good guy"+is_plural(good_guys)+" got an email from "+inactive_good_guys[-1]+" saying that they need to", " ")
    elif "Cell phone" in inventory and random.randint(0,1) == 1:
        introduce(good_guys, False)
        storyprint("  The good guy"+is_plural(good_guys)+" had a phone call from "+inactive_good_guys[-1]+" saying that they need to", " ")
    elif random.randint(0,2) == 1:
        storyprint("  The good guy"+is_plural(good_guys)+" found a piece of paper saying that they need to", " ")
    elif random.randint(0,2) == 2:
        introduce(good_guys, False)
        storyprint("  {} told the good guy{} to".format(inactive_good_guys[-1], is_plural(good_guys)), " ")
    else:
        introduce(good_guys, True)
        storyprint("  {} came and told the good guy{} to".format(good_guys[-1], is_plural(good_guys)), " ")
    if mission_kind == "Take":
        storyprint("find a/the " + item + ".", "\n")
    elif mission_kind == "Destroy":
        storyprint("find and destroy a/the " + item + ".", "\n")
    elif mission_kind == "Visit":
        storyprint("go to "+Place2GoTo + ".", "\n")
    elif mission_kind == "Leave":
        storyprint("leave (the) {}.".format(place), "\n")
    else:
        storyprint("meet {}.".format(to_meet), "\n")
    goal_check()
def elevator():
    """When this function is called, the good guys take an elevator ride. Who will they find in there?"""
    global Places
    global PlaceTypes
    global good_guys
    global bad_guys
    global inactive_good_guys
    global inactive_bad_guys
    good_guy_check()
    doors = "closed"
    elev_directions = ["up", "down"]
    direction = random.choice(elev_directions)
    tripLen = random.randint(1, 10)
    left = False
    something_happened = True
    storyprint("  The good guy"+is_plural(good_guys)+" found an elevator and took a ride in it.", "\n")
    for x in range(tripLen):
        if something_happened == True:
            something_happened = False
            storyprint("  The elevator was going "+direction+".", "\n")
        if random.randint(0,1) == 1:
            direction = random.choice(elev_directions)
        if random.randint(0,4) == 1 and len(inactive_good_guys) > 0:
            new_character = random.choice(inactive_good_guys)
            inactive_good_guys.remove(new_character)
            good_guys.append(new_character)
            storyprint("  The doors opened and "+new_character+" entered the elevator.", "\n")
            doors = "opened"
            something_happened = True
        elif random.randint(0,3) == 1 and len(inactive_bad_guys) > 0:
            new_character = random.choice(inactive_bad_guys)
            inactive_bad_guys.remove(new_character)
            bad_guys.append(new_character)
            storyprint("  The doors opened and "+new_character+" entered the elevator.", "\n")
            doors = "opened"
            something_happened = True
        elif random.randint(0,2) == 1:
            introduce(good_guys, True)
            storyprint("  The doors opened and "+good_guys[-1]+' entered the elevator.', "\n")
            doors = "opened"
            something_happened = True
        elif random.randint(0,1) == 0:
            introduce(bad_guys, True)
            storyprint("  The doors opened and "+bad_guys[-1]+' entered the elevator.', "\n")
            doors = "opened"
            something_happened = True
        if random.randint(0,2) == 1 and len(bad_guys) > 0:
            quitter = random.choice(bad_guys)
            bad_guys.remove(quitter)
            inactive_bad_guys.append(quitter)
            print(" ",end=" ")
            if doors == "closed":
                doors = "opened"
                storyprint("The doors opened."," ")
            storyprint(quitter+" stepped out of the elevator.", "\n")
            something_happened = True
        elif random.randint(0,1) == 1:
            quitter = random.choice(good_guys)
            good_guys.remove(quitter)
            inactive_good_guys.append(quitter)
            print(" ",end=" ")
            if doors == "closed":
                doors = "opened"
                storyprint("The doors opened."," ")
            storyprint(quitter+" stepped out of the elevator.", "\n")
            something_happened = True
            if len(good_guys) == 0 or random.randint(0,1) == 1:
                if len(good_guys) == 0:
                    good_guys = inactive_good_guys
                    inactive_good_guys.clear()
                left = True
                break
        if doors == "opened" and x < tripLen - 1:
            storyprint("  The doors closed, and the elevator continued moving.", "\n")
            doors = "closed"
            direction = random.choice(elev_directions)
        if len(bad_guys) > 0 and random.randint(0,1) == 1:
            fight(True)
        good_guy_check()
    if left == False and random.randint(0,1) == 1:
        storyprint("  The elevator stopped abruptly. It was broken down. The good guy"+is_plural(good_guys)+ " needed to get out of there. "+random.choice(good_guys)+" tried to open the doors.", "\n")
        if random.randint(0,1) == 1:
            storyprint("  The doors were stuck. The good guy"+is_plural(good_guys)+" waited for help to arrive.", "\n")
            introduce(good_guys, True)
            storyprint("  Later, the doors were opened from the outside by "+good_guys[-1]+".", "\n")
        else:
            storyprint("  Later, "+random.choice(good_guys)+" tried to open the doors. This time, he/she succeeded!", "\n")
    storyprint("  The good guy"+is_plural(good_guys)+" left the elevator.", "\n")
    if len(bad_guys) > 0:
        inactive_bad_guys.extend(bad_guys)
        bad_guys.clear()
    if random.randint(0,5) == 1:
                    NewPlace()
                    storyprint("  They were now at "+place+".", "\n")
#Good events
def use_item():
    global inventory
    global place
    global PlaceTypes
    global good_guys
    global bad_guys
    global inactive_good_guys
    global goals
    global inactive_bad_guys
    global death_terms
    good_guy_check()
    if len(inventory) > 0:
        used_item = random.choice(inventory)
        if used_item == "Flashlight":
            if PlaceTypes[place] == "outdoors" or random.randint(0,1) == 1:
                storyprint("  It was nighttime."," ")
            else:
                storyprint("  It was dark."," ")
            storyprint(random.choice(good_guys)+" took out his/her flashlight and lit the way.", "\n")
            if random.randint(0,1) == 1:
                storyprint("  Later, the flashlight stopped working because it ran out of battery power.", "\n")
                if used_item in inventory:
                    inventory.remove(used_item)
        elif used_item == "Invisibility potion" and len(bad_guys) > 0:
            list_party(bad_guys,"  The bad guys here were")
            storyprint("  The good guy"+is_plural(good_guys)+" needed to sneak past the bad guy"+is_plural(bad_guys)+".", " ")
            inventory.remove(used_item)
            storyprint("They drank their invisibility potion and snuck away from the bad guy"+is_plural(bad_guys)+".", "\n")
            inactive_bad_guys.extend(bad_guys)
            bad_guys.clear()
        elif used_item == "money":
            if random.randint(0,2) == 1:
                get_vehicle()
            elif random.randint(0,1) == 1 and len(good_guys) > 1:
                goodGuy = random.choice(good_guys)
                goodGuy2 = goodGuy
                if random.randint(0,3) == 1:
                    new_tool = random.choice(Tools)
                elif random.randint(0,2) == 1 and len(inventory) > 0:
                    new_tool = random.choice(Tools)
                elif random.randint(0,1) == 1:
                    new_tool = input("(Type in an item.)")
                    if not new_tool in Tools:
                        Tools.append(new_tool)
                    storyprint("a(n) "+new_tool+".", "\n")
                    inventory.append(new_tool)
                    if random.randint(0,1) == 1:
                        inventory.remove("money")
                else:
                    new_tool = "money"
                while goodGuy == goodGuy2:
                    goodGuy2 = random.choice(good_guys)
                storyprint("  "+goodGuy+" gave "+goodGuy2+" a(n) "+new_tool+".", "\n")
                inventory.append(new_tool)
                if random.randint(0,1) == 1:
                        inventory.remove("money")

            else:
                get_tool()
        elif used_item == "Fire lighter":
            print(" ", end=" ")
            if len(bad_guys) > 0:
                victim = random.choice(bad_guys)
                attacker = random.choice(good_guys)
                storyprint(attacker+" set "+victim+" on fire with a fire lighter.", " ")
                if random.randint(0,1) == 1:
                    storyprint("That was the last of "+victim+".", " ")
                    bad_guys.remove(victim)
            else:
                storyprint("The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" feeling cold, so they used their fire lighter to make a little fire to keep them comfy and cozy."," ")
            if random.randint(0,1) == 1:
                storyprint("The firelighter had lit its last fire.", "\n")
                inventory.remove(used_item)
            else:
                print("")
            if PlaceTypes[place] == "indoors" and random.randint(0,1) == 1:
                    storyprint("  The good guy"+is_plural(good_guys)+" made a mistake. They accidentally set "+place+" on fire. They needed to get out of here.", "\n")
                    if random.randint(0,1) == 1:
                          for x in range(random.randint(1, len(good_guys))):
                              victim = random.choice(good_guys)
                              storyprint("  "+victim +" didn't make it out.", "\n")
                              good_guys.remove(victim)
                    if len(bad_guys) > 0:
                        storyprint("  The bad guy"+is_plural(bad_guys)+" also wanted to get out.", "\n")
                        if random.randint(0,1) == 1:
                            for x in range(random.randint(1, len(bad_guys))):
                              victim = random.choice(bad_guys)
                              storyprint("  "+victim +" didn't make it out.", "\n")
                              bad_guys.remove(victim)
                    NewPlace()
                    if len(good_guys) > 0:
                        storyprint("  The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" now at "+place+".", "\n")
        elif used_item == "Giant Growth potion":
            if len(goals) > 0 or len(bad_guys)>0:
                print(" ",end=" ")
                inventory.remove(used_item)
                user = random.choice(good_guys)
                storyprint(user+" drank up a giant growth potion and grew super tall.", "\n")
                if len(goals) > 0:
                    storyprint("  "+user+" saw something that would help accomplish one of the good guy"+is_plural(good_guys)+"'s goals.", "\n")
                    goal_resolve()
                if len(bad_guys) == 1:
                          storyprint("  "+user+" tried to squish "+bad_guys[0]+"."," ")
                          if random.randint(0,1) == 1:
                              bad_guys.clear()
                              storyprint(user+" squashed the bad guy!", "\n")
                          else:
                              if random.randint(0,1) == 1:
                                storyprint("But "+user+" missed.", "\n")
                              else:
                                storyprint("But "+bad_guys[0]+" dodged.", "\n")
                elif len(bad_guys) > 0:
                    print("")
                    for x in range(random.randint(1,len(bad_guys))):
                        victim = random.choice(bad_guys)
                        bad_guys.remove(victim)
                        storyprint("  "+user+" squashed "+victim+".", "\n")
        elif used_item == "Key":
            if random.randint(0,1) == 1 and PlaceTypes[place] == "indoors":
                storyprint("  The good guy"+is_plural(good_guys)+" found a door. It was locked. They tried to unlock the door with a key.", "\n")
                if random.randint(0,1) == 1:
                    storyprint("  The door was unlocked.", "")
                    if random.randint(0,1) == 1 and len(bad_guys) > 0:
                        inactive_bad_guys.extend(bad_guys)
                        bad_guys.clear()
                    if random.randint(0,4) == 4:
                        storyprint("The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" in another room.", "\n")
                    else:
                        print('')
                        NewPlace()
                        storyprint("  The good guy"+is_plural(good_guys)+' '+were_was(good_guys)+" now in "+place+".", "\n")
                else:
                    storyprint("  The key didn't unlock the door.", "\n")
                if random.randint(0,1) == 1:
                    storyprint("  The key was stuck in the door's keyhole. So, the good guy"+is_plural(good_guys)+" left it in the keyhole.", "\n")
                    inventory.remove(used_item)
            elif len(bad_guys) > 0:
                victim = random.choice(bad_guys)
                storyprint("  There was a cage, and the good guy"+is_plural(good_guys)+" managed to get "+victim+" inside.", " ")
                if random.randint(0,1) == 1:
                    storyprint("\n  Before "+random.choice(good_guys)+" could lock the cage, "+victim+" escaped.", "\n")
                else:
                    bad_guys.remove(victim)
                    inactive_bad_guys.append(victim)
                    storyprint(random.choice(good_guys)+" locked the cage with "+victim+" inside of it.", "\n")
                    if random.randint(0,1) == 1:
                        storyprint("  The key was stuck in the door's keyhole. So, the good guy"+is_plural(good_guys)+" left it in the keyhole.", "\n")
                        inventory.remove(used_item)
        elif used_item == "Ray gun" and len(bad_guys) > 0:
            victim = random.choice(bad_guys)
            storyprint("  "+random.choice(good_guys)+" pointed his/her ray gun at "+victim+".\n  ZAP!"," ")
            if random.randint(0,1) == 1:
                storyprint("Direct hit! "+victim+" was no more!", "\n")
                bad_guys.remove(victim)
            else:
                storyprint(victim+" missed!", "\n")
            if random.randint(0,1) == 1:
                inventory.remove(used_item)
                storyprint("  The ray gun ran out of power.", "\n")
        elif used_item == "Rope":
            print(" ",end=" ")
            if random.randint(0,1) == 1:
                storyprint("The good guy"+is_plural(good_guys)+" climbed down a rope","")
                if len(bad_guys) > 0:
                    storyprint("and got away from the bad guy"+is_plural(bad_guys)+".", "\n")
                    inactive_bad_guys.extend(bad_guys)
                    bad_guys.clear()
                else:
                    print(".")
                NewPlace()
                storyprint("  The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" now at "+place+".", "\n")
            elif len(bad_guys) > 0:
                storyprint("The good guy"+is_plural(good_guys)+" tied the bad guy"+is_plural(bad_guys)+" up with the rope.", "\n")
                inventory.remove(used_item)
                if random.randint(0,1) == 1:
                    storyprint("  The rope wasn't tied properly. The bad guy"+is_plural(bad_guys)+" managed to escape from the rope trap.", "\n")
                else:
                    inactive_bad_guys.extend(bad_guys)
                    bad_guys.clear()
            else:
                print('')
        elif used_item == "First aid kit":
            storyprint("  "+random.choice(good_guys)+" was hurt. Good thing that the good guy"+is_plural(good_guys)+" had a first aid kit. He/she was healed.", " ")
            if random.randint(0,1) == 1:
                storyprint("The good guy"+is_plural(good_guys)+" used up the last of their first aid kit.", "\n")
                inventory.remove(used_item)
            else:
                print("")
        elif used_item == "Disguise" and len(bad_guys) > 0:
            user = random.choice(good_guys)
            storyprint("  "+user + " put on a disguise. The bad guy"+is_plural(bad_guys)+" thought that he/she was a fellow bad guy.\n  \"I would like another person to come with me on my quest,\" "+user+" said.\n "," ")
            if random.randint(0,1) == 1 or len(bad_guys) == 1:
                lucky = random.choice(bad_guys)
                storyprint(lucky+" was interested. \"Yes!\" he/she said. \"I would like to be on your quest.\"", "\n")
            else:
                lucky = "all"
                multiple_bad_guys = is_plural(bad_guys)
                storyprint("All the bad guys were interested in joining "+user+" on his/her quest.", "\n")
            if lucky == "all":
                    good_guys.append(bad_guys)
                    bad_guys.clear()
            else:
                    bad_guys.remove(lucky)
                    good_guys.append(lucky)
            if len(good_guys) > 1:
                storyprint("  "+user+" took ", "")
                if lucky == "all":
                    storyprint("the bad guy"+multiple_bad_guys," ")
                else:
                    storyprint(lucky, " ")
                storyprint("to see the other good guy(s).\n  \"Wait,\" one of the bad guys said. \"Aren't those our enemies?\"\n  \"Not really,\" "+user+" said.\n  The bad guy(s) said that they would like to be on the good guy(s)'s quest. After thinking a bit, they joined the good guy(s).", "\n")
        elif used_item == "Magic wand":
            user = random.choice(good_guys)
            w = random.randint(0,1)
            ani = random.randint(0,1)
            if ani == 1 and w == 1 and len(bad_guys) > 0:
                    animal = random.choice(Animals)
            elif w == 1 and len(bad_guys) > 0:
                    animal = input("(Type in an animal.)")
                    if not animal in Animals:
                        Animals.append(animal)
            storyprint("  "+user+" used his/her magic wand to", " ")
            if len(bad_guys) > 0 and w == 1:
                storyprint("turn the bad guy","")
                if len(bad_guys) == 1:
                    storyprint(" into a(n) "+animal+".", "\n")
                else:
                    storyprint("s into "+animal+"s.", "\n")
                    for index, baddie, in enumerate(bad_guys):
                        #The following piece of code can be copied for using a future transform command.
                        if 'the' in baddie:
                            bad_guys[index] = re.sub(r'^(.*)the .*$', r'\1the '+animal.capitalize(), baddie)
                        else:
                            bad_guys[index] = baddie + " the " + animal.capitalize()
            elif len(goals) > 0 and random.randint(0,1) == 1:
                goal = random.choice(goals)
                if goal.startswith("Visit") or goal.startswith("Leave"):
                    if goal.startswith("Visit"):
                        subject = goal.replace("Visit ", "")
                        place = subject
                    else:
                        subject = goal.replace("Leave ", "")
                        while place == subject:
                            place = random.choice(Places)
                    storyprint("go to "+place+".", "\n")
                    if len(bad_guys) > 0:
                        inactive_bad_guys.extend(bad_guys)
                        bad_guys.clear()
                elif goal.startswith("Take") or goal.startswith("Destroy"):
                    if goal.startswith("Take"):
                        subject = goal.replace("Take ", "")
                    else:
                        subject = goal.replace("Destroy ", "")
                    inventory.append(subject)
                    storyprint("get the "+subject+".", ' ')
                    if goal.startswith("Destroy"):
                        storyprint("The good guy"+is_plural(good_guys)+" destroyed it with magic.", "\n")
                    else:
                        print('')
                else:
                    subject = goal.replace("Meet ", "")
                    storyprint("summon "+subject+".", "\n")
                    good_guys.append(subject)
            else:
                storyprint("do some magic."," ")
                trick = random.randint(0,9)
                if trick == 1:
                    print("")
                    victim = random.choice(good_guys)
                    if random.randint(0,1) == 1:
                        animal = random.choice(Animals)
                    else:
                        animal = input("(Type in an animal.)")
                        if not animal in Animals:
                            Animals.append(animal)
                    victim = random.choice(good_guys)
                    good_guys.remove(victim)
                    if 'the' in victim:
                            good_guys.append(re.sub(r'^(.*)the .*$', r'\1the '+animal.capitalize(), victim))
                    else:
                            good_guys.append(victim + " the " + animal.capitalize())
                    storyprint("  Poof! "+victim+" turned into a(n) "+animal+".", "\n")
                elif trick == 2 and len(bad_guys) > 0:
                    victim = random.choice(bad_guys)
                    storyprint("Poof! "+victim+" disappeared.", "\n")
                    bad_guys.remove(victim)
                    if random.randint(0,1) == 1:
                        inactive_bad_guys.append(victim)
                elif trick == 3:
                    victim = random.choice(good_guys)
                    if victim == user:
                        storyprint(user+" made him/herself disappear.", "\n")
                    else:
                        storyprint(user+" made "+victim+" disappear.", "\n")
                    good_guys.remove(victim)
                    if random.randint(0,1) == 1:
                        inactive_good_guys.append(victim)
                elif trick == 4 and len(active_vehicles) > 0:
                    victim = random.choice(active_vehicles)
                    storyprint(user+" made their "+victim+" disappear.", "\n")
                    active_vehicles.remove(victim)
                elif trick == 5 and len(inventory) > 0:
                    victim = random.choice(inventory)
                    storyprint(user+" made their "+victim+" disappear.", "\n")
                    inventory.remove(victim)
                elif trick == 6:
                    print('')
                    if random.randint(0,1) == 1:
                        inventory.append(random.choice(Tools))
                    else:
                        new_item = input("(What did the good guys get?)")
                        if not new_item in Tools:
                            Tools.append(new_item)
                        inventory.append(new_item)
                    storyprint("  Using magic, the good guy"+is_plural(good_guys)+" got a "+inventory[-1]+".", "\n")
                elif trick == 7:
                    print('')
                    if random.randint(0,1) == 1:
                        active_vehicles.append(random.choice(Vehicles))
                    else:
                        new_vehicle = input("(Type in a vehicle.)")
                        if not new_vehicle in Vehicles:
                            Vehicles.append(new_vehicle)
                        active_vehicles.append(new_vehicle)
                    storyprint("  The good guy"+is_plural(good_guys)+" got a "+active_vehicles[-1]+' from using magic.', "\n")
                elif trick == 8:
                    inventory.remove(used_item)
                    storyprint("Poof! The magic wand disappeared.", "\n")
                elif trick == 9 and len(inactive_bad_guys) > 0:
                    baddie = random.choice(inactive_bad_guys)
                    inactive_bad_guys.remove(baddie)
                    bad_guys.append(baddie)
                    storyprint("Poof! "+baddie+" appeared.", "\n")
                elif len(inactive_good_guys) > 0:
                    convertee = random.choice(inactive_good_guys)
                    inactive_good_guys.remove(convertee)
                    good_guys.append(convertee)
                    storyprint("Poof! "+good_guys[-1]+" appeared.", "\n")
                else:
                    print("")
                    introduce(good_guys, True)
                    storyprint("Poof! "+good_guys[-1]+" appeared.", "\n")
        elif used_item == "Shield" and len(bad_guys) > 0:
            storyprint("  "+random.choice(bad_guys)+" attacked "+random.choice(good_guys)+" with a "+random.choice(Tools)+'. But he/she used a shield to block the attack.', " ")
            if random.randint(0,1) == 1:
                storyprint("The shield broke on impact.", "\n")
                inventory.remove(used_item)
            else:
                print("")
        elif used_item == "Food":
            if random.randint(0,1) == 1 and len(good_guys) > 1:
                user = random.choice(good_guys)
            else:
                user = "The good guys"
            fchoice = random.randint(0,1)
            if fchoice == 1:
                food = random.choice(Foods)
            else:
                food = input("(What did the good guy(s) eat?)")
                if not food in Foods:
                    Foods.append(food)
            storyprint("  "+user+" got hungry. So,", " ")
            if user == "The good guys":
                storyprint("they ate some "+food+".", "\n")
            else:
                storyprint("He/she ate some "+food+".", "\n")
            if random.randint(0,1) == 1:
                inventory.remove(used_item)
        elif used_item == "Sword" and len(bad_guys) > 0:
            victim = random.choice(bad_guys)
            storyprint("  "+random.choice(good_guys)+" attacked "+victim+" with a sword.", " ")
            if random.randint(0,1) == 1:
                storyprint("Direct hit!", " ")
                if random.randint(0,1) == 1:
                    bad_guys.remove(victim)
                    storyprint(victim+" was defeated.", "\n")
                if random.randint(0,1) == 1:
                    storyprint("The sword shattered.", "\n")
                    inventory.remove(used_item)
                else:
                    print("")
            else:
                storyprint("Missed..", "\n")
        elif used_item == "computer":
            print(" ", end=" ")
            if random.randint(0,1) ==1 and len(inactive_good_guys) > 0:
                visitor = random.choice(inactive_good_guys)
                storyprint(random.choice(good_guys)+" sent an email to "+visitor+".", "\n")
                if random.randint(0,1) == 1:
                      storyprint("  Later, "+visitor+" came.", "\n")
                      inactive_good_guys.remove(visitor)
                      good_guys.append(visitor)
                else:
                    storyprint("  Later, nobody came.", "\n")
            else:
                if 'Python Programming book' in inventory:
                    storyprint(random.choice(good_guys)+" was programming in Python.", "\n")
                else:
                    storyprint(random.choice(good_guys)+" used their computer to do stuff, like planning on what to do next.", "\n")
            if random.randint(0,1) == 1:
                storyprint("  Later, the computer stopped working.", "\n")
                if used_item in inventory:
                    inventory.remove(used_item)
        elif used_item == "Cell phone" and len(inactive_good_guys) > 0:
            visitor = random.choice(inactive_good_guys)
            storyprint("  "+random.choice(good_guys),"used his/her cell phone to call "+visitor+" to come over to "+place+" with the good guy"+is_plural(good_guys)+".", "\n")
            if random.randint(0,1) == 1:
                storyprint("  Later, "+visitor+" came!", "\n")
                inactive_good_guys.remove(visitor)
                good_guys.append(visitor)
            else:
                storyprint("  Later, nobody came.", "\n")
            if random.randint(0,1) == 1:
                storyprint("  The cell phone stopped working.", "\n")
                inventory.remove(used_item)
        elif used_item == "Ladder":
            storyprint("  The good guy"+is_plural(good_guys)+" used a ladder to climb out of "+place+".", "\n")
            NewPlace()
            storyprint("  The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" now at "+place+".", "\n")
            if len(bad_guys) > 0:
                    inactive_bad_guys.extend(bad_guys)
                    bad_guys.clear()
        elif used_item == "Camera":
            storyprint("  The good guy"+is_plural(good_guys)+" took a picture of", " ")
            if len(bad_guys) > 0 and random.randint(0,1) == 1:
                storyprint(random.choice(bad_guys)+".", "\n")
            elif len(inventory) > 0 and random.randint(0,1) == 1:
                storyprint(random.choice(inventory)+".", "\n")
            elif random.randint(0,1) == 1:
                storyprint(place+".", "\n")
            else:
                storyprint(random.choice(good_guys)+".", "\n")
            if random.randint(0,1) == 1:
                reasons_to_stop = ("  The camera stopped working.", "  Somebody lost the camera.", "  The camera's SD card ran out of room", "  The camera's batteries ran out.", "  The camera ran out of film.")
                storyprint(random.choice(reasons_to_stop), "\n")
                inventory.remove(used_item)
        elif used_item == "Music player":
            storyprint("  The good guy"+is_plural(good_guys)+" listened to some music.", "\n")
            if len(inactive_bad_guys) > 0 and random.randint(0,1) == 1:
                storyprint("  The bad guys"+is_plural(inactive_bad_guys)+" heard the music and rushed over to the good guy"+is_plural(good_guys)+" and their music.", "\n")
                bad_guys.extend(inactive_bad_guys)
                inactive_bad_guys.clear()
            if random.randint(0,1) == 1:
                storyprint("  Soon, the music stopped. It was because the music player stopped working.", "\n")
                inventory.remove(used_item)
        elif used_item == "Science kit":
            user = random.choice(good_guys)
            storyprint("  "+user+ " did some science-y stuff with his/her science kit.", " ")
            if random.randint(0,1) == 1 and len(bad_guys) > 0:
                storyprint(user+" made some slime, with it. ", '')
                if random.randint(0,1) == 1:
                    storyprint("The bad guy"+is_plural(bad_guys)+" got stuck in that slime and they suffocated in it.", "\n")
                    bad_guys.clear()
                else:
                    victim = random.choice(bad_guys)
                    storyprint(victim+" got stuck in slime and he/she suffocated in it.", "\n")
                    bad_guys.remove(victim)
            else:
                print(" ",end=" ")
                NewPlace()
                storyprint("  The good guy"+is_plural(good_guys)+" made a cannon using baking soda and vinegar, and they got blasted away to "+place+".", "\n")
                if len(bad_guys) > 0:
                    inactive_bad_guys.extend(bad_guys)
                    bad_guys.clear()
            if random.randint(0,1) == 1:
                storyprint("  The good guy"+is_plural(good_guys)+" used the last of their science kit.", "\n")
                inventory.remove(used_item)
        elif used_item == "Calculator":
            storyprint("  "+random.choice(good_guys)+" did some math on a calculator.", " ")
            total_bads = len(bad_guys) + len(inactive_bad_guys)
            total_goods = len(good_guys) + len(inactive_good_guys)
            if total_bads > total_goods:
                storyprint("According to their calculations, the good guy", "")
                if total_goods > 1:
                    storyprint("s were outnumbered. There were "+str(total_goods)+" good guys", " ")
                else:
                    storyprint(" was outnumbered. There was only one good guy", " ")
                storyprint(" and there were "+str(total_bads)+" bad guys.")
            elif total_goods > total_bads and total_bads > 0:
                storyprint("According to their calculations, the bad guy", "")
                if total_bads > 1:
                    storyprint("s were outnumbered. There were "+str(total_bads)+" bad guys", " ")
                else:
                    storyprint(" was outnumbered. There was only one bad guy", " ")
                storyprint(" and there were "+str(total_goods)+" good guys.", "\n")
            else:
                storyprint("There were "+str(len(good_guys))+" good guy"+is_plural(good_guys)+" at "+place+". Counting the good guy"+is_plural(inactive_good_guys)+" that weren't there, "+str(total_goods)+" good guys overall.\n  The good guy"+is_plural(good_guys)+" had "+str(len(inventory))+" items.", "")
                if len(active_vehicles) > 0:
                    storyprint("The good guy"+is_plural(good_guys)+" had "+str(len(active_vehicles))+" vehicles.", "\n")
                else:
                    print('')
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            print(' ', end=" ")
            if random.randint(0,3) == 3:
                    storyprint("Also, "+str(a)+" + "+str(b)+" = "+str(a+b)+".", "\n")
            elif random.randint(0,2) == 2:
                storyprint("Also, "+str(a)+" - "+str(b)+" = "+str(a-b)+".", "\n")
            elif random.randint(0,1) == 1:
                storyprint("Also, "+str(a)+" times "+str(b)+" is equal to "+str(a*b)+".", "\n")
            else:
                storyprint("Also, "+str(a)+" divided by "+str(b)+" is equal to "+str(a//b), "")
                if a % b == 0:
                    print(".")
                else:
                    storyprint(" with a remainder of "+str(a%b)+".", "\n")
            if random.randint(0,1) == 1:
                storyprint("  Later, the calculator stopped working.", "\n")
                inventory.remove(used_item)
        elif used_item == "Computer book":
            storyprint("  The good guy"+is_plural(good_guys)+" read about computers because they wanted to read something, and they somehow had that book. Now, they knew more about computers.", "\n")
        elif used_item == "Python Programming book":
            storyprint("  The good guy"+is_plural(good_guys)+" read about Python programming because they wanted to read something, and they had that book. Now, they knew more about programming in Python.", "\n")
def get_vehicle():
    """Gives the good guys a vehicle to travel with.\nIt is true that the good guys can travel anywhere on foot, but that would be hard in real life."""
    global Vehicles
    global active_vehicles
    global inventory
    global good_guys
    global goals
    good_guy_check()
    r = random.randint(0, 1)
    if "Visit Outer space" in goals:
        new_vehicle = "Rocket ship"
    elif random.randint(0,1) == 1:
        new_vehicle = input("(Type in a vehicle) ")
    else:
        new_vehicle = random.choice(Vehicles)
    print(' ',end=' ')
    if r == 1:
        storyprint("The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" shopping for a " + new_vehicle + ".", " ")
        if "money" in inventory and random.randint(0,1) == 1:
            if random.randint(0,1) ==1:
                storyprint("The good guys found it and bought it.", "\n")
                active_vehicles.append(new_vehicle)
            else:
                storyprint("They didn't find one.", "\n")
        else:
            if random.randint(0,1) == 1:
                storyprint("They found one, but they didn't have enough money.", "\n")
            else:
                storyprint("They didn't find one. Besides, they didn't have enough money for one anyway.", "\n")
    else:
        storyprint("The good guy"+is_plural(good_guys)+" found an abandoned "+new_vehicle+".", " ")
        if random.randint(0,1) ==1:
            storyprint("It worked. So, the good guy"+is_plural(good_guys)+" took it.", "\n")
            active_vehicles.append(new_vehicle)
        else:
            storyprint("It was broken.", " ")
            if random.randint(0,1) ==1:
                storyprint("But "+random.choice(good_guys)+" fixed it. Now, the good guy"+is_plural(good_guys)+" got the "+new_vehicle+".", "\n")
                active_vehicles.append(new_vehicle)
            else:
                storyprint("It was no good. Nobody could fix it. So, the good guy"+is_plural(good_guys)+" left it behind.", "\n")
def get_tool():
    """Gives the good guys a tool."""
    global Tools
    global inventory
    global good_guys
    good_guy_check()
    if findGoal("Take") and random.randint(0,1) == 1:
        for goal in goals:
            if goal.startswith("Take"):
                new_tool = goal.replace("Take ", "")
                break
    elif findGoal("Destroy") and random.randint(0,1) == 1:
        for goal in goals:
            if goal.startswith("Destroy"):
                new_tool = goal.replace("Destroy ", "")
                break
    elif random.randint(0,1) == 1:
        new_tool = input("(Type in a name of an item) ")
    else:
        new_tool = random.choice(Tools)
    print(' ',end=' ')
    if random.randint(0, 1) == 1 and "money" in inventory:
        storyprint("The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" shopping. They found (a) " +new_tool+"."," ")
        if random.randint(0,2) != 2:
            inventory.append(new_tool)
            if random.randint(0,1) == 1:
                inventory.remove("money")
            storyprint("The good guy"+is_plural(good_guys)+" got it.", "\n")
        else:
            storyprint("But they didn't have enough money.", "\n")
    else:
        storyprint("The good guy"+is_plural(good_guys)+" found (a) "+new_tool+".", "\n")
        inventory.append(new_tool)
    goal_check() #Just in case if somebody had already finished the goal all along.
def new_guy():
    """Introduces a good guy in the middle of the story."""
    global good_guys
    good_guy_check()
    global inactive_good_guys
    introduce(good_guys, True)
    print(' ',end=' ')
    if random.randint(0,1) == 1:
        storyprint(good_guys[-1]+" came over and joined the good guy(s).", "\n")
    else:
        storyprint("The good guy(s) met "+good_guys[-1]+".", "\n")
def goal_check():
    """Checks if any goals are completed."""
    global goals
    global Tools
    global inventory
    global Places
    global good_adjectives
    global good_guys
    global bad_guys
    global bad_adjective
    global Animals
    global Vehicles
    global inactive_good_guys
    global inactive_bad_guys
    global Prizes
    global Foods
    global place
    global active_vehicles
    good_guy_check()
    finished_goals = []
    for goal in goals:
        if goal.startswith("Meet"):
            subject = goal.replace("Meet ", "")
            if subject in good_guys:
                if not goal in finished_goals:
                    finished_goals.append(goal)
        elif goal.startswith("Leave"):
            subject = goal.replace("Leave ", "")
            if place != subject:
                if not goal in finished_goals:
                    finished_goals.append(goal)
        elif goal.startswith("Take"):
            subject = goal.replace("Take ", "")
            if subject in inventory or subject in active_vehicles:
                if not goal in finished_goals:
                    finished_goals.append(goal)
        elif goal.startswith("Destroy"):
            subject = goal.replace("Destroy ", "")
            if subject in inventory:
                if not goal in finished_goals:
                    finished_goals.append(goal)
                inventory.remove(subject)
            elif subject in active_vehicles:
                if not goal in finished_goals:
                    finished_goals.append(goal)
                active_vehicles.remove(subject)
        else:
            subject = goal.replace("Visit ", "")
            if subject == place:
                if not goal in finished_goals:
                    finished_goals.append(goal)
    for goal in finished_goals:
        if goal.startswith("Meet"):
            subject = goal.replace("Meet ", "")
            verb = "meeting"
        elif goal.startswith("Leave"):
            subject = goal.replace("Leave ", "")
            verb = "leaving"
        elif goal.startswith("Take"):
            subject = goal.replace("Take ", "")
            verb = "taking a/the"
        elif goal.startswith("Destroy"):
            subject = goal.replace("Destroy ", "")
            verb = "destroying a/the"
        else:
            subject = goal.replace("Visit ", "")
            verb = "visiting"
        goals.remove(goal)
        new_prize = random.choice(Prizes)
        inventory.append(new_prize)
        if new_prize == "kiss":
                        introduce(good_guys, True)
        storyprint("  The good guy"+is_plural(good_guys)+" got (a)", " ")
        if new_prize == "kiss":
            storyprint(" kiss(es) from " + good_guys[-1], " ")
        else:
            storyprint(new_prize," ")
        storyprint("for "+verb+" "+subject+".", "\n")
def goal_resolve():
    """This function resolves a goal if there are any goals."""
    global goals
    global Tools
    global inventory
    global Places
    global good_adjectives
    global good_guys
    global bad_guys
    global bad_adjective
    global Animals
    global Vehicles
    global inactive_good_guys
    global inactive_bad_guys
    global Prizes
    global Foods
    global place
    good_guy_check()
    solved = True
    if len(goals) > 0:
        solved_goal = random.choice(goals)
        print(' ',end=' ')
        if solved_goal.startswith("Meet"):
            subject = solved_goal.replace("Meet ", "")
            storyprint("The good guy"+is_plural(good_guys)+" met "+subject+".", "\n")
            good_guys.append(subject)
            if subject in inactive_good_guys:
                inactive_good_guys.remove(subject)
        elif solved_goal.startswith("Leave"):
            subject = solved_goal.replace("Leave ", "")
            if place == subject:
                while place == subject:
                    NewPlace()
                storyprint("  The good guy"+is_plural(good_guys)+" left "+subject+". They were now at "+place+".", "\n")
        elif solved_goal.startswith("Take") or solved_goal.startswith("Destroy"):
            if solved_goal.startswith("Take"):
                subject = solved_goal.replace("Take ", "")
            else:
                subject = solved_goal.replace("Destroy ", "")
            storyprint("The good guys found (a) "+subject,"")
            if random.randint(0,1) == 1:
                storyprint(" at a store.", ' ')
                if "money" in inventory:
                    storyprint("The good guy"+is_plural(good_guys)+" bought it.", " ")
                    inventory.append(subject)
                else:
                    storyprint("The good guy"+is_plural(good_guys)+" didn't have any money. Now, their goal was to find some money.", " ")
                    goals.append("Take money")
                    solved = False
            else:
                    storyprint(". The good guy"+is_plural(good_guys)+" got it.", " ")
                    inventory.append(subject)
            if subject in inventory and solved_goal.startswith("Destroy"):
                storyprint("The good guy"+is_plural(good_guys)+" also destroyed it.", "\n")
                inventory.remove(subject)
            else:
                print('')
        else:
            subject = solved_goal.replace("Visit ", "")
            if subject == "Outer space" and not "Rocket ship" in inventory:
                storyprint("The good guy"+is_plural(good_guys)+" needed a rocket ship to go to space.", " ")
                if random.randint(0,1) == 1:
                    storyprint("They ended up finding a rocket ship that they could use. So, they blasted off into space!", "\n")
                    active_vehicles.append("Rocket ship")
                    place = subject
                else:
                    print('')
            else:
                place = subject
                storyprint("The good guy"+is_plural(good_guys)+" went to "+subject+".", "\n")
    goal_check()
#Bad events
def hunger():
    global good_guys
    global inventory
    global Foods
    global death_terms
    good_guy_check()
    if "Food" in inventory or "money" in inventory:
        if random.randint(0,1) == 1:
            food = random.choice(Foods)
        else:
            food = input("(Type in a food.) ")
            if not food in Foods:
                Foods.append(food)
    if random.randint(0,1) == 1 and len(good_guys) > 1:
        victim = "The good guys"
    else:
        victim = random.choice(good_guys)
    storyprint("  "+victim+" got hungry.", " ")
    if victim == "The good guys":
            storyprint("They", " ")
    else:
            storyprint("He/she"," ")
    if "Food" in inventory:
        storyprint("had some {}(s) to eat.".format(food), "\n")
        if victim == "The good guys" or random.randint(0,1) == 1:
            inventory.remove("Food")
    elif "money" in inventory:
        storyprint("had some money. They bought some {}(s) to eat.".format(food), "\n")
        if random.randint(0,1) == 1:
            inventory.remove("money")
    else:
        if random.randint(0,1):
            storyprint("fasted.", "\n")
        elif random.randint(0,1) == 1 and len(inventory) > 0:
            item = random.choice(inventory)
            storyprint("ate their "+item+".", "\n")
            inventory.remove(item)
        else:
            storyprint(random.choice(death_terms)+" from hunger.", "\n")
            if victim == "The good guys":
                good_guys.clear()
                good_guy_check()
            else:
                good_guys.remove(victim)
def destroy_vehicle():
    """Destroys a vehicle. Some good guys may die from the crash."""
    global good_guys
    global death_terms
    global active_vehicles
    good_guy_check()
    if len(active_vehicles) > 0:
        print(' ', end=" ")
        wrecked_vehicle = random.choice(active_vehicles)
        active_vehicles.remove(wrecked_vehicle)
        if random.randint(0,1) == 1 and wrecked_vehicle != "Horse":
            storyprint("Suddenly, the good guy"+is_plural(good_guys)+"'s "+wrecked_vehicle+" broke down.", "\n")
        elif wrecked_vehicle == "Horse":
            storyprint("The good guy"+is_plural(good_guys)+"'s horse "+random.choice(death_terms)+".", "\n")
        else:
            storyprint("The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" riding in their "+wrecked_vehicle+". Suddenly, it crashed.", ' ')
            if random.randint(0,1) == 1:
                victim = random.choice(good_guys)
                storyprint(victim+" "+random.choice(death_terms)+" when the "+wrecked_vehicle+" crashed.", "\n")
                good_guys.remove(victim)
            else:
                storyprint("Luckily, nobody was hurt.", "\n")
def lose_item():
    global inventory
    global good_guys
    global bad_guys
    good_guy_check()
    if len(inventory) > 0 :
        lost_item = random.choice(inventory)
        inventory.remove(lost_item)
        print(' ',end=' ')
        if random.randint(0,2) == 1 and len(bad_guys) > 0:
            storyprint(random.choice(bad_guys)+" stole (a) "+lost_item+" from the good guy"+is_plural(good_guys)+".", " ")
            if random.randint(0,1) == 1:
                storyprint("he/she destroyed the "+lost_item+".", "\n")
            else:
                print('')
        elif random.randint(0,1) == 1:
            storyprint("The good guy"+is_plural(good_guys)+"'s "+lost_item+" broke.", "\n")
        else:
            storyprint("The good guy"+is_plural(good_guys)+" lost their "+lost_item+".", "\n")
def natural_disaster():
    """Makes a random natural disaster happen."""
    global place
    global Places
    global good_guys
    global bad_guys
    global death_terms
    global inactive_bad_guys
    global PlaceTypes
    good_guy_check()
    startPlace = place
    disaster = random.randint(0, 6)
    starts = ("  Suddenly,","  Then,", "  All of a sudden,")
    start = random.choice(starts)
    safe = False
    if disaster == 0:
        storyprint(start+" there was an earthquake.", "\n")
        if PlaceTypes[place] == "indoors":
            if random.randint(0,1) == 1:
                storyprint("  The good guy"+is_plural(good_guys)+" hid under a doorway.", "\n")
                safe = True
        if PlaceTypes[place] == "outdoors" and random.randint(0,1) == 1:
            safe = True
        if safe == False and random.randint(0,2) != 1 and len(good_guys) > 1:
            for x in range(random.randint(1,len(good_guys))):
                if len(good_guys) > 0 and random.randint(0,1) == 1:
                    victim = random.choice(good_guys)
                    good_guys.remove(victim)
                    storyprint("  "+victim+" "+random.choice(death_terms)+" from being crushed by falling building parts.", "\n")
        if len(bad_guys) > 1 and random.randint(0,1) == 1:
            for x in range(random.randint(1,len(bad_guys))):
                if len(bad_guys) > 0 and random.randint(0,1) == 1:
                    victim = random.choice(bad_guys)
                    bad_guys.remove(victim)
                    storyprint("  "+victim+" "+random.choice(death_terms)+" from being crushed by falling building parts.", "\n")
        storyprint("  Later, the earthquake stopped.", "\n")
    elif disaster == 1:
        storyprint(start+" "+place+" got flooded!", "\n")
        if random.randint(0,1) == 1:
            place = "the Open ocean"
            storyprint("  The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" washed away to sea.", "\n")
        if safe == False and random.randint(0,2) != 1 and len(good_guys) > 1:
            for x in range(random.randint(1,len(good_guys))):
                if len(good_guys) > 0 and random.randint(0,1) == 1:
                    victim = random.choice(good_guys)
                    if not 'diver' in victim.lower() or not "fish" in victim.lower():
                        good_guys.remove(victim)
                        storyprint("  "+victim+" drowned.", "\n")
        if len(bad_guys) > 1 and random.randint(0,1) == 1:
            for x in range(random.randint(1,len(bad_guys))):
                if len(bad_guys) > 0 and random.randint(0,1) == 1:
                    victim = random.choice(bad_guys)
                    if not 'diver' in victim.lower() or not "fish" in victim.lower():
                        bad_guys.remove(victim)
                        storyprint("  "+victim+" drowned.", "\n")
        if place != "the Open ocean":
            storyprint("  The waters went down.", "\n")
            NewPlace()
            storyprint("  The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" now at "+place+".", "\n")
    elif disaster == 2:
        storyprint(start+" a tornado appeared!", "\n")
        if PlaceTypes[place] == "outdoors" and random.randint(0,1) == 1:
            safe = True
        if safe == False and random.randint(0,2) != 1 and len(good_guys) > 1:
            for x in range(random.randint(1,len(good_guys))):
                if len(good_guys) > 0 and random.randint(0,1) == 1:
                    victim = random.choice(good_guys)
                    good_guys.remove(victim)
                    storyprint('  '+victim+" got sucked up by the tornado.", "\n")
        if len(bad_guys) > 1 and random.randint(0,1) == 1:
            for x in range(random.randint(1,len(bad_guys))):
                if len(bad_guys) > 0 and random.randint(0,1) == 1:
                    victim = random.choice(bad_guys)
                    bad_guys.remove(victim)
                    storyprint("  "+victim+" got sucked up by the tornado.", "\n")
        if safe == False and random.randint(0,2) != 1 and len(good_guys) > 1:
            for x in range(random.randint(1,len(good_guys))):
                if len(good_guys) > 0 and random.randint(0,1) == 1:
                    victim = random.choice(good_guys)
                    good_guys.remove(victim)
                    storyprint("  "+victim+" "+random.choice(death_terms)+" from being crushed by falling building parts.", "\n")
        if len(bad_guys) > 1 and random.randint(0,1) == 1:
            for x in range(random.randint(1,len(bad_guys))):
                if len(bad_guys) > 0 and random.randint(0,1) == 1:
                    victim = random.choice(bad_guys)
                    bad_guys.remove(victim)
                    storyprint("  "+victim+" "+random.choice(death_terms)+" from being crushed by falling building parts.", "\n")
        if random.randint(0,4) > 0:
            storyprint("  That tornado destroyed the {}.".format(place), "\n")
            NewPlace()
            storyprint("  The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" now at "+place+".", "\n")
        storyprint("  Later, the tornado was no more.", "\n")
    elif disaster == 3:
        storyprint(start+" it was raining, and our heroes heard thunder!", ' ')
        if PlaceTypes[place] != "indoors":
            storyprint("The good guy"+is_plural(good_guys)+" needed to find a place to wait out the storm in.", "\n")
            x = 0
            rep = random.randint(3, 5)
            while x < rep or PlaceTypes[place] != "indoors":
                NewPlace()
                if len(bad_guys) > 0:
                    inactive_bad_guys.extend(bad_guys)
                    bad_guys.clear()
                storyprint("  They went to "+place+".", " ")
                if PlaceTypes[place] == "outdoors":
                    storyprint("But they weren't out of the rain yet.", "\n")
                else:
                    safe = True
                    storyprint("The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" safe from the storm.", "\n")
                x += 1
            if safe == False and random.randint(0, 10) == 10:
                    victim = random.choice(good_guys)
                    storyprint("  "+victim+" was struck by lightning.", "\n")
                    good_guys.remove(victim)
        else:
            storyprint('Good thing they were inside.', "\n")
        storyprint("  Later, the storm passed.", "\n")
    elif disaster == 4:
        storyprint(start+" a volcano erupted! The good guy"+is_plural(good_guys)+" tried to outrun the lava.", "\n")
        if len(good_guys) > 1:
            for x in range(random.randint(1, len(good_guys))):
                if random.randint(0,1) == 1 and len(good_guys) > 0:
                    if len(good_guys) > 0 and random.randint(0,1) == 1:
                        victim = random.choice(good_guys)
                        storyprint("  "+victim+" tried to outrun the lava, but he/she was consumed by the lava.", "\n")
                        good_guys.remove(victim)
        if len(bad_guys) > 1:
            for x in range(random.randint(1, len(bad_guys))):
                if random.randint(0,1) == 1 and len(bad_guys) > 0:
                    if len(bad_guys) > 0 and random.randint(0,1) == 1:
                        victim = random.choice(bad_guys)
                        storyprint("  "+victim+" tried to outrun the lava, but he/she was consumed by the lava.", "\n")
                        bad_guys.remove(victim)
        NewPlace()
        if len(good_guys) == 0:
            storyprint("  "+place+".", "\n")
            good_guy_check()
        else:
            storyprint("  The good guy"+is_plural(good_guys)+" outran the lava.", " ")
            if len(bad_guys) > 0:
                storyprint("The bad guy"+is_plural(bad_guys)+" outran the lava, too.", ' ')
            storyprint("They were now at "+place+".", "\n")
    elif disaster == 5:
        storyprint(start+" a blizzard blew in!", " ")
        if PlaceTypes[place] != "indoors":
            storyprint("The good guy"+is_plural(good_guys)+" needed to find a place to wait out the storm in.", "\n")
            NewPlace()
            if len(bad_guys) > 0:
                    inactive_bad_guys.extend(bad_guys)
                    bad_guys.clear()
            storyprint("  They went to "+place+".", " ")
            if PlaceTypes[place] == "indoors":
                    storyprint("They were safe.", "\n")
                    safe = True
            else:
                storyprint("They were still in the storm.", "\n")
        else:
                    storyprint("The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" safe.", "\n")
                    safe = True
        if len(good_guys) > 1:
            for x in range(0, random.randint(1, len(good_guys))):
                if safe == False and random.randint(0, 2) == 0 and len(good_guys) > 0:
                        victim = random.choice(good_guys)
                        storyprint("  "+victim+" "+random.choice(death_terms)+" from frostbite.", "\n")
                        good_guys.remove(victim)
        storyprint("  Later, the snowstorm passed.", "\n")
    else:
        storyprint(start+" hailstones fell!", "\n")
        if PlaceTypes[place] == "outdoors":
            storyprint("  The good guy"+is_plural(good_guys)+" needed to find a place to wait out the storm in.", "\n")
            NewPlace()
            if len(bad_guys) > 0:
                    inactive_bad_guys.extend(bad_guys)
                    bad_guys.clear()
            storyprint("They went to "+place+".", ' ')
            if PlaceTypes[place] != "outdoors":
                if random.randint(0,5) < 5:
                    storyprint("They were safe.", "\n")
                    safe = True
                else:
                    print('')
                    storyprint(random.choice(starts)+" a hailstone crashed through the roof.", "\n")
            else:
                storyprint("They were still in the hailstorm.", "\n")
        else:
                    storyprint("  The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+" safe because they were in "+place+".", "\n")
                    safe = True
        if len(good_guys) > 1:
            for x in range(0, random.randint(1, len(good_guys))):
                if safe == False and random.randint(0, 2) == 0 and len(good_guys) > 0:
                        victim = random.choice(good_guys)
                        storyprint("  "+victim+" was struck by a hailstone.", "\n")
                        good_guys.remove(victim)
        storyprint("  Later, the hailstones stopped falling.", "\n")
def trapped():
    """A good guy gets trapped in this function."""
    global good_guys
    global inactive_good_guys
    global place
    global last_list
    global Places
    global PlaceTypes
    global inventory
    good_guy_check()
    free = False
    if random.randint(0,1) == 1 and len(good_guys) > 1:
        victim = "The good guys"
    else:
        victim = random.choice(good_guys)
    storyprint("  "+victim+" got trapped in", " ")
    if random.randint(0,1) ==1 and PlaceTypes[place] == "indoors":
        storyprint("a room.", "\n")
        trap = "room"
    else:
        storyprint("a cage.", "\n")
        trap = "cage"
    if "Key" in inventory:
        storyprint("  "+random.choice(good_guys)+" tried to unlock the door to the "+trap+" with a key.", ' ')
        if random.randint(0,1) == 1:
            free = True
            storyprint("The door was unlocked! ","")
            if victim == "The good guys":
                storyprint("The good guys were free.", "\n")
            else:
                storyprint(victim+" was free.", "\n")
        elif random.randint(0,1) == 1:
            storyprint("The key didn't fit in the lock.", "\n")
        else:
            storyprint("The key fit the lock, but the door didn't unlock.", "\n")
    if random.randint(0,1) == 1 and len(inventory) > 1 and free == False:
        storyprint("  "+random.choice(good_guys)+" tried to release "+victim+" from the "+trap+" using (a) "+random.choice(inventory)+"."," ")
        if random.randint(0,1) == 1:
            storyprint("It worked.",' ')
            if victim == "The good guys":
                storyprint("The good guys were free.", "\n")
            else:
                storyprint(victim+" was free.", "\n")
            free = True
        else:
            storyprint("It didn't work.", "\n")
    if victim == "The good guys" and free == False:
        NewPlace()
        storyprint("  Meanwhile, at "+place+", ", "")
        if len(inactive_good_guys) > 0:
            in_between = inactive_good_guys
            inactive_good_guys = good_guys
            good_guys = in_between
        else:
            inactive_good_guys = good_guys
            good_guys.clear
            for x in range(random.randint(1, 12)):
                introduce(good_guys, True)
        list_party(good_guys, "there were")
        last_list = "party"
    elif free == False and victim != "The good guys":
        storyprint("  The other good guy(s) had to leave "+victim+" behind.", "\n")
        good_guys.remove(victim)
        inactive_good_guys.append(victim)
def lost():
    """The good guys get lost in this function."""
    global good_guys
    global place
    global Places
    global PlaceTypes
    global inactive_good_guys
    global inactive_bad_guys
    global bad_guys
    good_guy_check()
    print(' ',end=' ')
    if place == "a Forest":
        storyprint("The good guy"+is_plural(good_guys)+" turned around and found that they were lost in the woods.", "\n")
    else:
        storyprint("The good guy"+is_plural(good_guys)+" got lost and they didn't know where to go.", "\n")
    rep = random.randint(1, 10)
    for c in range(rep):
        evnt = random.randint(0, 6)
        storyprint("  The good guy"+is_plural(good_guys)+" wandered around", " ")
        if PlaceTypes[place] == "indoors":
            storyprint("the hallways of", " ")
        storyprint("(the) "+place+".", "\n")
        if evnt == 1 and len(good_guys) > 1:
            convertee = random.choice(good_guys)
            storyprint("  "+convertee+" wandered off.", "\n")
            good_guys.remove(convertee)
            inactive_good_guys.append(convertee)
        elif evnt == 2 and len(inactive_good_guys) > 0:
            convertee = random.choice(inactive_good_guys)
            storyprint("  The good guy"+is_plural(good_guys)+" found "+convertee+".", "\n")
            good_guys.append(convertee)
            inactive_good_guys.remove(convertee)
        elif evnt == 3 and len(inactive_bad_guys) > 0:
            convertee = random.choice(inactive_bad_guys)
            storyprint("  "+convertee+" emerged from the darkness.", "\n")
            bad_guys.append(convertee)
            inactive_bad_guys.remove(convertee)
        elif evnt == 4 and len(bad_guys) > 0:
            convertee = random.choice(bad_guys)
            storyprint("  "+convertee+" retreated to the shadows.", "\n")
            inactive_bad_guys.append(convertee)
            bad_guys.remove(convertee)
        elif evnt == 5:
            introduce(good_guys, True)
            storyprint("  The good guy"+is_plural(good_guys)+" met "+good_guys[-1]+".", "\n")
        elif evnt == 6:
            introduce(bad_guys, True)
            storyprint("  "+bad_guys[-1],"emerged.", "\n")
        else:
            NewPlace()
            storyprint("  The good guy"+is_plural(good_guys)+" found themselves at "+place+".", " ")
            if random.randint(0,1) == 1:
                storyprint("However, they were still lost.", "\n")
            else:
                print('')
                break
    storyprint("  The good guy"+is_plural(good_guys)+" "+were_was(good_guys)+"n't lost anymore.", "\n")
def confused():
    """Not finished yet"""
    global good_guys
    global bad_guys
    global inactive_bad_guys
    global inactive_good_guys
    good_guy_check()
    """The good guys get confused in this function."""
    storyprint("  The good guy"+is_plural(good_guys)+" got confused.", "\n")
    if len(bad_guys) > 0:
        victim = random.choice(good_guys)
        storyprint(victim+" thought that "+random.choice(bad_guys)+" was his/her friend. So, he/she went on the bad guy's side.", "\n")
        good_guys.remove(victim)
        bad_guys.append(victim)
def pit():
    """Not finished yet"""
    global good_guys
    good_guy_check()
# Start the story.
for x in range(X2repeat+1):
    introduce(good_guys, True)
X2repeat = random.randint(1,5) * len(good_guys)
inventory = [random.choice(Tools) for x in range(X2repeat)]
test_events() #This line is temporary.
storyprint("  Once upon a time, there", " ")
if len(good_guys) == 1:
    storyprint("was " + good_guys[0] + "."," ")
    if good_guys[0].endswith("Holy Ghost"):
        storyprint("He/she isn't THE Holy Ghost, but a ghost that is holy.", "\n")
    else:
        print('')
else:
    b = ["good neighbors", "good guys", "heroes", "people", "good people", "neighbors"]
    storyprint("were " + str(len(good_guys)) +" "+ random.choice(b), ". ")
    list_party(good_guys, "They were ")
sentence_starts = ["They were born in ", "They lived in ", "They were going through ", "They were sent to ", "They went to ", "They were going on vacation to "]
senStart = "  "+random.choice(sentence_starts)
if PlaceTypes[place] == "country":
    storyprint(senStart + place.capitalize() + ".", "\n")
else:
    storyprint(senStart + place.lower() + ".", "\n")
if senStart == "  They were sent to ":
    storyprint("  Why were they sent to "+place.lower()+"?"," ")
    r = random.randint(0, 2)
    if r == 0:
        storyprint("Because they were being naughty. They want to find a way out of {}.".format(place.lower()), "\n")
        goals.append("Leave " + place)
    elif r == 1:
        introduce(bad_guys, False)
        if place.lower() == "a school":
            storyprint("Because {} thought they were so stupid, they needed to go to school".format(inactive_bad_guys[-1]), "\n")
        else:
            storyprint("Because {} kidnapped them and left them there so that they could not escape.".format(inactive_bad_guys[-1]), "\n")
        goals.append("Leave " + place)
    else:
        storyprint('Because...', "\n")
        new_mission()
X2repeat = random.randint(0,1)
if len(good_guys) > 5:
    X2repeat += random.randint(0,1)
if len(good_guys) > 10:
    X2repeat += random.randint(0,1)
if X2repeat > 0:
    active_vehicles = [random.choice(Vehicles) for x in range(X2repeat)]
else:
    active_vehicles = []
if senStart == "  They were sent to ":
    storyprint("  They got to "+place+" by " + list_vehicles() + ".", "\n")
else:
    storyprint("  They got there by "+list_vehicles()+".", "\n")
print_inventory()
total_bad_guys = len(inactive_bad_guys) + len(bad_guys)
#Opening
possible_events = ["Animal()","conversation()", 'convert_character(False)', 'introduce_bad_guy()', 'good_guy_check()', 'goto()', 'print_inventory()', 'list_vehicles()', 'new_mission()', 'get_vehicle()', 'get_tool()', 'new_guy()', 'use_item()', 'hunger()', 'lose_item()', 'trapped()', 'lost()', "new_guy()", "get_tool()", "get_vehicle()", "new_mission()", "goto()", "convert_character(False)", "print_inventory()", "introduce_bad_guy()", "list_party(good_guys, \"  The good guys here were\")", "list_vehicles()"]
while total_bad_guys == 0 and len(goals) == 0:
    if random.randint(0, 6) == 5 and len(active_vehicles) > 0 and last_list != "vehicles":
        storyprint("  The good guys had " + list_vehicles(), "\n")
        last_list = "vehicles"
    if random.randint(0,1) == 1:
        event = random.choice(possible_events)
        exec(event)
        if not event.lower().startswith("list"):
            last_list = "none"
    elif random.randint(0,1) == 1:
        new_mission()
    good_guy_check() #Even though there weren't any events that kill the good guys in this loop, it's still possible to have the good_guys list down to 0.
    total_bad_guys = len(inactive_bad_guys) + len(bad_guys)
    vehicle_check()
#Middle
possible_events = ["Animal()","conversation()", "goal_resolve()", "new_guy()", "get_tool()", "location_specific()", "kill_character()",  "fight(False)", "get_vehicle()", "new_mission()", "goto()", "convert_character(False)", "print_inventory()", "introduce_bad_guy()", "list_party(good_guys, \"  Our heroes were\")", 'convert_character(False)', 'kill_character()', 'fight(True)', 'introduce_bad_guy()', 'goto()', 'print_inventory()', 'list_vehicles()', 'list_party(good_guys, "  The good guys were")', 'new_mission()', 'location_specific()', 'elevator()', 'get_vehicle()', 'get_tool()', 'new_guy()', 'goal_resolve()', 'use_item', 'destroy_vehicle()', 'hunger()', 'lose_item()', 'natural_disaster()', 'trapped()', 'lost()']
repeatLimit = random.randint(20, 50)
Rep = 0
while Rep <= repeatLimit:
        if random.randint(0, 6) == 5 and len(active_vehicles) > 0 and last_list != "vehicles":
            storyprint("  The good guys had " + list_vehicles(), "\n")
            last_list = "vehicles"
        else:
            event = random.choice(possible_events)
            try:
                exec(event)
            except:
                pass
            if not event.lower().startswith("list") or event != "print_inventory()":
                last_list = "none"
        good_guy_check()
        vehicle_check()
        Rep += 1
        total_bad_guys = len(inactive_bad_guys) + len(bad_guys)
        goal_check()
#Closing
possible_events = ["Animal()","conversation()", 'convert_character(True)', 'kill_character()', 'fight(True)', 'good_guy_check()', 'goto()', 'print_inventory()', 'list_vehicles()', 'list_party(good_guys, "  The good guys were")', 'elevator()', 'get_vehicle()', 'get_tool()', 'new_guy()', 'goal_check()', 'goal_resolve()', 'use_item()', 'destroy_vehicle()', 'hunger()', 'lose_item()', 'natural_disaster()', 'trapped()']
chance = 2
while total_bad_guys > 0:
    if random.randint(0,chance) > 0:
        convert_character(True)
    if len(bad_guys) > 0 and random.randint(0,chance) != 1:
        fight(True)
    elif len(inactive_bad_guys) > 0 and random.randint(0,chance) != 1:
        list_party(inactive_bad_guys, "  These bad guys came over to fight the good guy"+is_plural(good_guys)+":")
        bad_guys.extend(inactive_bad_guys)
        inactive_bad_guys.clear()
        fight(True)
    elif len(goals) > 0 and random.randint(0,chance) != 1:
        goal_resolve()
    else:
        event = random.choice(possible_events)
        exec(event)
        if not event.lower().startswith("list"):
                last_list = "none"
    good_guy_check()
    vehicle_check()
    goal_check()
    total_bad_guys = len(bad_guys) + len(inactive_bad_guys)
    if random.randint(0,chance) == 1:
        chance += 1
while len(goals) > 0:
    if len(goals) > 0 and random.randint(0,2) < 2:
        goal_resolve()
    else:
        event = random.choice(possible_events)
        try:
            exec(event)
        except:
            pass
        if not event.lower().startswith("list"):
                last_list = "none"
    good_guy_check()
    vehicle_check()
    goal_check()
storyprint("The end.", "\n")
input("(Press [enter] to exit.)")
