#!/usr/bin/env python3
import csv
import os
def ls():
    """Lists the names of the files of the current working directory and the path to the current working directory."""
    contents = os.listdir(os.getcwd())
    
    print("Total: "+str(len(contents)))
    contents = sorted(contents)
    
    for x in contents:
        print(x)
    print("Directory: "+os.getcwd())
##def by_dept_reader():
##    """Reads the by_department.csv file."""
##    with open("by_department.csv") as csvfile:
##        csv_reader = csv.reader(csvfile)
##        row_index = 0
##        for row in csv_reader:
##            if len(row) > 0:
##                full_name, username, department = row
##                if row_index >= 1:
##                   print("{} works in {} with the user name {}.".format(full_name, department, username))
##            row_index += 1\
CSV_file = ""
def read_CSV(filename):
    """Reads CSV file, returns the non-empty lines of the CSV file as a list of lists."""
    with open(filename, "r") as csv_file:
        rows = []
        reader = csv.reader(csv_file)
        for row in reader:
            if len(row) > 0:
                rows.append(row)
    return rows
def insert_to_CSV(data, filename, index):
    """Inserts a new row into a CSV file in desired index. data parameter is a list, filename is a string, and index is an integer."""
    rows = read_CSV(filename)
    rows.insert(index, data)
    write_to_CSV(rows, filename)
    printCSV(filename)
def del_from_CSV(filename, index):
    """Deletes row from CSV file. filename is a string, and index is an integer."""
    rows = read_CSV(filename)
    del rows[index]
    write_to_CSV(rows, filename)
    printCSV(filename)
def replace_in_CSV(data, filename, index):
    """Replaces row from CSV file. Data is a list, filename is a string, and index is an integer."""
    rows = read_CSV(filename)
    rows[index] = data
    write_to_CSV(rows, filename)
    printCSV(filename)
##def AppendByDept(dicts):
##    """Appends to the by_department.csv file."""
##    with open("by_department.csv", "a") as csv_file:
##        new_users = dicts
##        writer = csv.DictWriter(csv_file, fieldnames=["name","username","department"])
##        writer.writerows(new_users)
def printCSV(filename):
    """Outputs the CSV file in a neat table."""
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        cell_lengths = []
        row_index = 0
        for row in csv_reader:
            if row_index == 0:
                for x in range(len(row)):
                    cell_lengths.append(0)
            for z, x in enumerate(row):
                if len(cell_lengths) <= z:
                    cell_lengths.append(0)
                if cell_lengths[z] < len(x):
                    cell_lengths[z] = len(x)
            row_index += 1
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for i, row in enumerate(csv_reader):
            if len(row) > 0:
                index = str(i//2)
                spaces = 9 - len(index)
                print(" "*9,end="")
                for x in cell_lengths:
                    print("+",end="")
                    print("-"*x,end="")
                print("+")
                print(" "*spaces, end=index)
                for z, x in enumerate(row):
                    print("|", end="")
                    print(x,end="")
                    cell_len = cell_lengths[z] - len(row[z])
                    print(" "*cell_len,end="")
                print("|")
        print(" "*9,end="")
        for x in cell_lengths:
            print("+",end="")
            print("-"*x,end="")
        print("+\n^Indexes^|   "+filename)
def write_to_CSV(data, filename):
        """Writes a CSV file using a list of lists containing strings. Warning: It overwrites a file if it already exists! Be careful when executing this commmand!"""
        with open(filename, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)
#printCSV("hosts.csv")
def openCSV():
    global CSV_file
    CSV_file = ""
    changedDir = True
    done = False
    while done == False:
        if changedDir == True:
            ls()
            changedDir = False
        CSV_file = input("What CSV file do you want to open? (Type in \"cd\" to change or make a directory. >")
        if CSV_file.lower() == "cd":
            new_dir = input("Which directory do you want to go to? (Type in\"..\" to go to parent directory.>")
            if os.path.exists(new_dir) and os.path.isdir(new_dir):
                os.chdir(new_dir)
                changedDir = True
            elif not os.path.exists(new_dir):
                makedir = input("This directory doesn't exist. Make directory? (y/n)>")
                if makedir.lower() == "y" or makedir.lower().startswith("yes"):
                    os.mkdir(new_dir)
                    os.chdir(new_dir)
                    changedDir = True
        if os.path.exists(CSV_file) and os.path.isfile(CSV_file):
            if not CSV_file.lower().endswith(".csv"):
                sure = input("This file does not end with the .csv extention. Are you sure about opening it? >")
                if sure.lower() == "y" or sure.lower().startswith("yes"):
                   printCSV(CSV_file)
                else:
                    CSV_file = ""
            else:
                printCSV(CSV_file)
                done = True
        elif os.path.isdir(CSV_file):
            os.chdir(CSV_file)
            changedDir = True
        elif CSV_file != "cd":
            print("The file, {} does not exist.".format(CSV_file))
            create = input("Create new file? (y/n) >")
            if create.lower() == "y" or create.lower().startswith("yes"):
                if not CSV_file.lower().endswith(".csv"):
                    CSV_file = CSV_file + ".csv"
                row = []
                new_row = input("What data should you add to the CSV file? (Tip: use this line for headers separated by commas.) >")
                first_row = new_row.split(",")
                row[1] = first_row
                write_to_CSV(row, CSV_file)
                print("File saved as "+CSV_file)
                printCSV(CSV_file)
                done = True
action = ""
openCSV()

while action.lower() != "quit":
    action = input("What do you want to do? >")
    if action.lower().startswith("insert"):
        repData = input("What data do you want to insert? >")
        repIndex = int(input("Which index do you want to write that data? (first entry = 0, last entry = -1) > "))
        sure = input("Are you sure? (y/n) >")
        if sure.lower() == "y" or sure.lower().startswith("yes"):
            Data = repData.split(",")
            insert_to_CSV(Data, CSV_file, repIndex)
            #printCSV(CSV_file)
    elif action.lower() == "delete":
        DelIndex = int(input("Which index do you want to write that data? (first entry = 0, last entry = -1) > "))
        sure = input("Are you sure? (y/n) >")
        if sure.lower() == "y" or sure.lower().startswith("yes"):
            del_from_CSV(CSV_file, DelIndex)
            #printCSV(CSV_file)
    elif action.lower() == "replace":
        repIndex = int(input("Which index do you want to replace? (first entry = 0, last entry = -1) > "))
        repData = input("What data do you want to put there? >")
        print("You're about to put "+repData+" in index "+str(repIndex)+", overwriting the data that was there.")
        sure = input("Are you sure? (y/n) >")
        if sure.lower() == "y" or sure.lower().startswith("yes"):
            Data = repData.split(",")
            replace_in_CSV(Data, CSV_file, repIndex)
            #printCSV(CSV_file)
    elif action.lower() == "help":
        print("CSV files are text files that are lists with multiple values separated by commas, this program can display those files as a table.\nThis program can be used to manipulate and read CSV files.\nCommands:\nnew          creates new CSV file\ndelete       deletes desired line of CSV file.\nopen         opens a CSV file\nhelp         shows this screen\nquit         exits the program\ninsert       Inserts desired data at desired index.\n         Use commas if you want the data in separate cells.\nreplace       Does the same as the insert command, but the data at the desired index is overwritten.\nprint file   shows the file in a table.")
    elif action.lower() == "new":
        sure = input("Are you sure? (y/n)>")
        if sure.lower() == "y" or sure.lower().startswith("yes"):
            changedDir = True
            DoneMaking = False
            while DoneMaking == False:
                if changedDir == True:
                    changedDir = False
                    ls()
                new_file = input("What do you want to name your new CSV file? (type in \"cd\" to change or make directories.) >")
                if new_file.lower() == "cd":
                    new_dir = input("Which directory do you want to go to? (Type in\"..\" to go to parent directory.>")
                    if os.path.exists(new_dir) and os.path.isdir(new_dir):
                        os.chdir(new_dir)
                        changedDir = True
                    elif not os.path.exists(new_dir):
                        makedir = input("This directory doesn't exist. Make directory? (y/n)>")
                        if makedir.lower() == "y" or makedir.lower().startswith("yes"):
                            os.mkdir(new_dir)
                            os.chdir(new_dir)
                            changedDir = True
                elif os.path.isdir(new_file):
                    os.chdir(new_file)
                    changedDir = True
                elif os.path.exists(new_file):
                        print("The file, {} already exists.".format(new_file))
                        sure = input("Overwrite the file? (y/n)>")
                        if sure.lower() == "y" and sure.lower().startswith("yes"):
                                if not CSV_file.lower().endswith(".csv"):
                                    CSV_file = CSV_file + ".csv"
                                row = []
                                new_row = input("What data should you add to the CSV file? (Tip: use this line for headers separated by commas.) >")
                                first_row = new_row.split(",")
                                row[1] = first_row
                                write_to_CSV(row, CSV_file)
                                print("File saved as "+CSV_file)
                                printCSV(CSV_file)
                                DoneMaking = True
                else:
                    if not CSV_file.lower().endswith(".csv"):
                        CSV_file = CSV_file + ".csv"
                    row = []
                    new_row = input("What data should you add to the CSV file? (Tip: use this line for headers separated by commas.) >")
                    first_row = new_row.split(",")
                    row[1] = first_row
                    write_to_CSV(row, CSV_file)
                    print("File saved as "+CSV_file)
                    printCSV(CSV_file)
                    DoneMaking = True
    elif action.lower() == "open":
        sure = input("Are you sure? (y/n)>")
        if sure.lower() == "y" or sure.lower().startswith("yes"):
            openCSV()
    elif action.lower() == "quit":
        sure = input("Are you sure? (y/n)>")
        if sure.lower() == "y" or sure.lower().startswith("yes"):
            action = "quit"
    elif action.lower() == "print file":
        printCSV(CSV_file)
    else:
        print("Unknown command. Try typing in \"help\" for a list of commands.")
