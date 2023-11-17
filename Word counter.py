#!/usr/bin/env python3
import os
# Uncomment line 4 if you're using Windows. If not, uncomment line 5. Edit the path it points to. This script won't work if you don't.
#file_path = "C:\\Windows\\Path\\to\\wordcount.txt"
#file_path = "/linux/or/MacOS/path/to/word_count_file.txt"

#Setting up other variables.
wordcounts = []
days_to_do = 30
goal = 50000

#Prints a little guy with the title of this script.
print("  /\_/\  \n ( o   o ) \n==(   )== \n  /   \   \nNaNoWriMo Word Counter")

def writeFile():
    """Writes to the file that contains the word counts."""
    global wordcounts
    with open(file_path, 'w') as file:
        for x in wordcounts:
            file.write(str(x)+"\n")
def addCounts():
    """Returns the total of all the word counts."""
    global wordcounts
    total = 0
    for x in wordcounts:
        total += x
    return total
def counts_table():
    """Prints a table of how many words are on each chapter and progress report."""
    global wordcounts
    global days_to_do
    global goal

    #Prints the table of word counts.
    head = "Chapter | Word Count"
    print(head+"\n--------|-----------")
    for i, x in enumerate(wordcounts):
        print(str(i+1).rjust(len("Chapter"))+" | "+str(x))
    total = addCounts()
    
    if total >= goal:
        #If the goal is met, then it just prints "GOAL MET" and the total words written.
        print("GOAL MET")
        print(str(total)+" words")
    else:
        #If the goal isn't met, then print a progress report.
        print("-"*len(head)+"\nTotal words: "+str(total)+" out of "+str(goal)) #Prints the total words and the goal.
        print(str(total/goal*100)+"% through") #Prints the percentage.
        quota = goal//days_to_do+1 #Calculates how much words to write in a day.
        days_done = total//quota #Calculates the days done
        words_till = total #This line and the while loop that follows, the number of words to write to finish a day will be calculated.
        while words_till > quota:
            words_till -= quota
        words_till = quota - words_till
        #Prints how many days are done. Note that if you do one day of writing, it doesn't say "1 days done."
        if days_done == 1:
            print("1 day done out of "+str(days_to_do))
        else:
            print(str(days_done)+" days done out of "+str(days_to_do))
        print(str(words_till)+" words to finish next day\n"+str(goal-total)+" words to goal.") #Prints how many words left to do

#If the word count file exists, then this script will read from it. Otherwise, the script will create a file and write "0" to it to start with.
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            wordcounts.append(line)
        for i, n in enumerate(wordcounts):
            strNum = n.replace('\n', '')
            wordcounts[i] = int(strNum)
else:
    with open(file_path, "w") as file:
        file.write('0')

#Main loop
answer = "a" #The main loop runs while this variable doesn't start with the letter Q.
while not answer.lower().startswith('q'):
    counts_table()
    answer = input("What do you want to do: \n Add line,\nUpdate line,\nRemove line,\nor Quit?") #Input prompt
    if answer.lower().startswith('q'):
        #If you want to quit, the program asks you if you want to quit. If you do want to quit, the loop breaks by setting the answer variable to "q".
        answer = input("Are you sure you want to quit? (Y/N)")
        if answer.lower().startswith('y'):
            answer = "q"
    elif answer.lower().startswith('a'):
        #Adds a new count in the line. The if statement checks if the input is an integer, the action cancels if you don't type in an integer.
        line = input("What's the new count in that line?")
        if line.isdigit():
                        wordcounts.append(int(line))
                        writeFile()
        else:
                        print("Input must be an integer.")
    elif answer.lower().startswith('u'):
        #This is the most commonly used command in this program. It first asks if you which line to update and what the new count is.
        #Like the add command, the action cancels if you don't respond to any of the prompts with an integer.
        #Note: The index corresponds to the chapter number in the table you see onscreen. If you want to change chapter 1's word count, you respond with 1, not 0.
        ln = input("Which line to update?")
        if ln.isdigit():
                try:
                    ln = int(ln) #translates to integer
                    ln2update = wordcounts[ln-1]
                    line = input("What's the new count in that line?")
                    if line.isdigit():
                        ln2update = int(line)
                        wordcounts[ln-1] = ln2update
                        writeFile()
                    else:
                        print("Input must be an integer.")
                except IndexError:
                    print("Index out of range")

        else:
                print("That is not a number.")
    elif answer.lower().startswith('r'):
        answer = input("Are you sure you want to remove a line? (Y/N)") #First, the program asks if you're sure if you want to remove an entry.
        if answer.lower().startswith('y'):
            ln = input("Which line to remove?")#if yes, it asks which index you want to remove. If you answer "yes" in the previous prompt, then you don't have to panic. You can just enter a non-number to cancel the action.
            if ln.isdigit():
                try:
                    ln = int(ln)
                    del wordcounts[ln-1]
                    writeFile()
                except IndexError:
                    print("Index out of range")
            else:
                print("That is not a number.")
