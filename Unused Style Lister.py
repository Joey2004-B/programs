#!/usr/bin/env python3
import os
import re
import subprocess
oldDir = os.getcwd()
homeDir = os.getenv("HOME")
#Step 1: Collect information about styles

## Cursors
os.chdir(os.path.join(homeDir, ".icons"))
contents = os.listdir(os.getcwd())
cursors = {}
for x in contents:
    os.chdir(os.path.join(homeDir, ".icons"))
    try:
        os.chdir(x)
        with open("index.theme", "r") as cfgfile:
            data = cfgfile.readlines()
        for y in data:
            if y.startswith("Name="):
                name = y.replace("Name=", "")
                cursors[x] = name
    except:
        cursors[x] = x + "\n"
#print(cursors)


## Icons
os.chdir(os.path.join(homeDir, ".local/share/icons"))
contents = os.listdir(os.getcwd())
icons = {}
for x in contents:
    os.chdir(os.path.join(homeDir, ".local/share/icons"))
    try:
        os.chdir(x)
        with open("index.theme", "r") as cfgfile:
            data = cfgfile.readlines()
        for y in data:
            if y.startswith("Name="):
                name = y.replace("Name=", "")
                icons[x] = name
    except:
        icons[x] = x + "\n"
#print(icons)

## Color Schemes
os.chdir(os.path.join(homeDir, ".local/share/color-schemes"))
contents = os.listdir(os.getcwd())
colors = {}
for x in contents:
        name = ""
        with open(x, "r") as cfgfile:
            filename = x.replace(".colors", "")
            data = cfgfile.readlines()
        for y in data:
            if y.startswith("Name="):
                name = y.replace("Name=", "")
        if len(name) == 0:
            colors[filename] = x + "\n"
        else:
            colors[filename] = name
#print(colors)

## Plasma Styles
os.chdir(os.path.join(homeDir, ".local/share/plasma/desktoptheme"))
contents = os.listdir(os.getcwd())
plasma = {}
for x in contents:
    os.chdir(os.path.join(homeDir, ".local/share/plasma/desktoptheme"))
    try:
        os.chdir(x)
        with open("metadata.desktop", "r") as cfgfile:
            data = cfgfile.readlines()
        for y in data:
            if y.startswith("Name="):
                name = y.replace("Name=", "")
                plasma[x] = name
    except:
        plasma[x] = x + "\n"
#print(plasma)

## Window Decorations
os.chdir(os.path.join(homeDir, ".local/share/aurorae/themes"))
contents = os.listdir(os.getcwd())
winDecor = {}
for x in contents:
    os.chdir(os.path.join(homeDir, ".local/share/aurorae/themes"))
    try:
        os.chdir(x)
        with open("metadata.desktop", "r") as cfgfile:
            data = cfgfile.readlines()
        for y in data:
            if y.startswith("Name="):
                name = y.replace("Name=", "")
                winDecor[x] = name
    except:
        winDecor[x] = x + "\n"
#print(winDecor)

print(len(cursors))
#Step 2: Go through the global themes and see if there are any styles that aren't used.
os.chdir(os.path.join(homeDir, ".local/share/plasma/look-and-feel"))
contents = os.listdir(os.getcwd())
for x in contents:
        os.chdir(os.path.join(homeDir, ".local/share/plasma/look-and-feel"))
        os.chdir(x)
        #print(x)
        os.chdir("contents")
        #print(os.getcwd())
        if os.path.exists("defaults"):
            #print("Reading file")
            with open("defaults", "r") as cfgfile:
                    data = cfgfile.readlines()
                    prevline = ""
                    for y in data:
                        #print(prevline)
                        #Cursors
                        if y.startswith("cursorTheme=") and prevline == "[kcminputrc][Mouse]\n":
                            name = y.replace("cursorTheme=", "")
                            #print(name)
                            if name.strip() in cursors:
                                cursors.pop(name.strip())
                        #Color schemes
                        if y.startswith("ColorScheme=") and prevline == "[kdeglobals][General]\n":
                            name = y.replace("ColorScheme=", "")
                            #print(name)
                            if name.strip() in colors:
                                colors.pop(name.strip())
                        # Window Decorations
                        if y.startswith("theme=") and prevline.startswith("library="):
                            name = re.sub(r"^theme=.*__", "", y)
                            #print(name)
                            if name.strip() in winDecor:
                                winDecor.pop(name.strip())
                        #Plasma styles
                        if y.startswith("name=") and prevline.startswith("[plasmarc][Theme]"):
                            name = re.sub(r"^name=", "", y)
                            print(name)
                            if name.strip() in plasma:
                                plasma.pop(name.strip())
                        #Icons
                        if y.startswith("Theme=") and prevline == "[kdeglobals][Icons]\n":
                            name = y.replace("Theme=", "")
                            #print(name)
                            if name.strip() in icons:
                                icons.pop(name.strip())

                        if len(y) > 0:
                            prevline = y
#print(len(cursors))
#Step 3: Output unused styles.
subprocess.run(["clear"])
if len(plasma) == 0:
    print("\nAll Plasma styles used.")
else:
    print("\n ----- PLASMA STYLES ----- ")
    for x,y in plasma.items():
        print(y, end="")

if len(colors) == 0:
    print("\nAll color schemes used.")
else:
    print("\n ----- COLOR SCHEMES ----- ")
    for x,y in colors.items():
        print(y, end="")



if len(winDecor) == 0:
    print("\nAll window decorations used.")
else:
    print("\n ----- WINDOW DECORATIONS ----- ")
    for x,y in winDecor.items():
        print(y, end="")

if len(icons) == 0:
    print("\nAll icon styles used.")
else:
    print("\n ----- ICON STYLES ----- ")
    for x,y in icons.items():
        print(y, end="")

if len(cursors) == 0:
    print("\nAll cursor styles used.")
else:
    print("\n ----- CURSORS ----- ")
    for x,y in cursors.items():
        print(y, end="")
os.chdir(oldDir)
#print(colors)
