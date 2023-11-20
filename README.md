# PYTHON SCRIPTS!
This repository is my first GitHub repository. This one contains Python programs that I made. They all work well on Windows (I use that OS.), and maybe Linux and MacOS (unless otherwise noted).
Feel free to review any of the code in this repository. Reviews are appreciated. They help code get better.
## Word counter
 >Uploaded!
 
 You use commands to interact with this program. This is quite useful if you want to write a 50,000 word novel in a month and if you store the different chapters in separate files.
You might have to make some changes to the file before running it for the first time.
>FOR FIRST TIME USING THIS SCRIPT: You need to first edit the path to the file this script keeps the word counts in. Please note that the script won't work properly before you configure the variable that stores the path to the file the script will store the word counts in. (The line to edit is near the top of the file, you don't need to scroll down.)
>
>Windows path example: `'C:\\Users\\Username\\Documents\\Novel\\wordcounts.txt"`
>
>MacOS path example: `'/Users/Username/Documents/Novel/wordcounts.txt'`
>
>Linux path example: `'/home/Username/Documents/Novel/wordcounts.txt'`
>
>On the first time you run the script after changing the file path near the top of the file, it will automatically create the file. You should see a table with only one entry. That entry should be `0`.

 How to use:
 In the first prompt, there are some commands you can type in, `add`, `remove`, `update`, or `quit`. You can just type in the first letter of those commands, and the script knows what you mean.
 >Important note: Most of the prompts in this script accepts only numbers. If you type in a non-number in any of these prompts, the action cancels. Pretty handy if you accidentally type in a command you didn't mean to type in.
>
>Another important note: When a prompt asks for an index, you have to enter the number shown on the table, not the proper Python index for the word count. For example, if you want to change the word count for chapter 1, you type in `1`, not `0`.

- `add` command adds a word count to the table. The script asks you what the word count for the new chapter is. You'll need to click on the `Word Count` option in your word processor program you're writing your novel in.
- `remove` command removes a word count from the table. Useful if you accidentally added a word count to the table.
- `update` command is the most used one. It first asks the user which word count you want to change. Then, it will ask what's the new word count for that chapter.
- `quit` command exits the program. It asks if you really want to leave. If you type in `y`, then the script finishes.
 ## Story Generator
 >Not uploaded yet
 I need to fix some bugs on this one.

 This program is what you'll get if you combine Mad Libs with Rory Story Cubes or Storytime Dice.
 - It randomly generates stories.
 - It sometimes give the user opportunities to fill in some blanks with some input prompts.

Before I add this script to my repository, I have to fix these bugs. Please let me know if you want to fix them.
- [ ] For every time that the `input()` function or any function that calls that function, have any `print()` functions called after all the `input()` functions, except for the `conversation()` function.
- [ ] Change the wording in some of the functions defined in it. (like in `elevator()`, and `convert_character()`)
- [ ] Fix a problem with blank lines being added in the `fight()`. I want all the paragraphs the code outputs to start with two spaces and no newline characters until the next paragraph.
- [ ] Make it possible to print a random expression meaning that someone died in `fight()`
- [ ] In `good_guy_check()`, if one good guy was introduced after all the good guys are gone, it should have proper grammar.
- [ ] In `elevator()`, if the good guys lose a fight, make the story either continue with new characters entering the elevator or have the story continue in a different place.
- [ ] In `lost()`, it's possible to have multiple paragraphs start with "`  The good guys`," if that paragraph was supposed to start with that phrase, and the previous paragraph also started with that phrase, it should start with "`  They`" instead.
- [ ] In `conversation()`, if someone asks a question at the end of the loop, let someone answer that question.
- [ ] In `natural_disaster()`, there is a loop in the thunderstorm part, and as soon as the good guys were safe, the loop should break.
- [ ] in `kill_character()`, make it possible to start a fight by calling the `fight()` function.
- [ ] In `list_vehicles()`, use a dictionary to count them.
- [ ] Make a `new_place()` function where it changes the place the good guys are at in the story into a random place, or let the user type in the place.
 ## Subtitle Creator
 >Not uploaded yet
 - Creates SRT subtitles
 - You can write transcripts of videos in .txt files and import them into the program.
 - Has options to capitalize and uncapitalize text inside parentheses or square brackets.
 - Also has options to randomly choose what brackets would be used and whether the text inside is capitalized or not.
 - Window is always on top of the video player window if you are watching the video you want to add subtitles to maximized.
 ## CSV editor
 >Not uploaded yet
 This is a command-line interface tool that creates and edits CSV files.
 You type in commands to use it. It displays the contents of the CSV file you're working on in a neat table.
 
 ## And maybe more.
example.py file (I had to make it for doing a QwikLab exercise on a course on using Git and GitHub. I might have to delete it some day).
