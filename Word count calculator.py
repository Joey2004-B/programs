import os
file_path = "C:\\Users\\Joey Bailey\\Documents\\Stories\\Penguins in the Sky\\wordcount.txt"
wordcounts = []
days_to_do = 30
goal = 50000
print("  /\_/\  \n ( o   o ) \n==(   )== \n  /   \   \nNaNoWriMo Word Counter")

def writeFile():
    global wordcounts
    with open(file_path, 'w') as file:
        for x in wordcounts:
            file.write(str(x)+"\n")
def addCounts():
    global wordcounts
    total = 0
    for x in wordcounts:
        total += x
    return total
def counts_table():
    global wordcounts
    global days_to_do
    global goal
    head = "Chapter | Word Count"
    print(head+"\n--------|-----------")
    for i, x in enumerate(wordcounts):
        print(str(i+1).rjust(len("Chapter"))+" | "+str(x))
    total = addCounts()
    print("-"*len(head)+"\nTotal words: "+str(total)+" out of "+str(goal))
    print(str(total/goal*100)+"% through")
    if total >= goal:
        print("GOAL MET")
    else:
        quota = goal//days_to_do+1
        days_done = total//quota
        words_till = total
        while words_till > quota:
            words_till -= quota
        words_till = quota - words_till
        if days_done == 1:
            print("1 day done out of "+str(days_to_do))
        else:
            print(str(days_done)+" days done out of "+str(days_to_do))
        print(str(words_till)+" words to finish next day\n"+str(goal-total)+" words to goal.")
            
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

answer = "a"
while not answer.lower().startswith('q'):
    counts_table()
    answer = input("What do you want to do: \n Add line,\nUpdate line,\nRemove line,\nor Quit?")
    if answer.lower().startswith('q'):
        answer = input("Are you sure you want to quit? (Y/N)")
        if answer.lower().startswith('y'):
            answer = "q"
    elif answer.lower().startswith('a'):
        line = input("What's the new count in that line?")
        if line.isdigit():
                        wordcounts.append(int(line))
                        writeFile()
        else:
                        print("Input must be an integer.")
    elif answer.lower().startswith('u'):
        ln = input("Which line to update?")
        if ln.isdigit():
                try:
                    ln = int(ln)
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
        answer = input("Are you sure you want to remove a line? (Y/N)")
        if answer.lower().startswith('y'):
            ln = input("Which line to remove?")
            if ln.isdigit():
                try:
                    ln = int(ln)
                    del wordcounts[ln-1]
                    writeFile()
                except IndexError:
                    print("Index out of range")
            else:
                print("That is not a number.")
