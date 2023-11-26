from tkinter import *
from tkinter import filedialog
import random
testStr = " SOMETHING: Boom, boom \n SANTA ANA: Rats!"
Status = "Welcome to BroCColi Subtitle Creator!"
import time
import pickle
import sys
#global totaltimelapsed
global running
running = False
totaltimelapsed = 0
startTimes = []
endTimes = []
TextLines = []
nextline = 'Not working'
global StartTime
StartTime = 0
global TimeElapsed
TimeElapsed = 0
global Timestamp
Timestamp = "00:00:00,000"
def Time_convert(sec):
  mins = sec // 60
  hours = mins // 60
  mins = mins % 60
  sec = sec % 60
  if len(str(mins)) == 1:
      DisMins = "0" + str(mins)
      mins = DisMins
  if len(str(sec)) == 1:
      DisSecs = "0" + str(sec)
      sec = DisSecs
  if len(str(hours)) == 1:
      DisHrs = "0" + str(hours)
      hours = DisHrs
  

  return "{0}:{1}:{2},000".format(str(hours),str(mins),str(sec))

  

#input("Press Enter to start")
#start_time = time.time()
#input("Press Enter to stop")
#end_time = time.time()
#time_lapsed = end_time - start_time

WorkingDir = "c:\\users\\Joey Bailey\\Videos\\Current DVD Project Videos With Subtitles"
WorkingFile = "Not Specified"
def SaveTXT():
  if len(TextLines) ==0:
    info("There aren't any lines typed\nin yet.", True)
  else:
    WorkingFile = filedialog.asksaveasfilename(initialdir=WorkingDir, title = "Export Text lines", filetypes = (("Text files","*.txt"),("all files","*.*")))
    if WorkingFile != '':
        TotalLines = len(TextLines)
        SaveFile = open(WorkingFile+".txt", 'w')
        
        for x in range(0, TotalLines):
            
            SaveFile.write(TextLines[x])
            SaveFile.write('''\n\n''')
        SaveFile.close()
        info('Exported text lines\n to text file.', False)
def info(msg, err):
  global Status
  Status = msg
  if err == True:
    canvas.itemconfig(statmessage, text=Status, fill="red")
  else:
    canvas.itemconfig(statmessage, text=Status, fill="#00ff00")
  tk.update()
def add_new_text():
    NextLn1 = NewLineText.get("1.0", "1.10000")
    NextLn2 = NewLineText.get("2.0", "2.10000")
    if len(NextLn2)!=0 or len(NextLn1)!=0:
      if len(NextLn2)==0:
        NextText = NextLn1
      elif len(NextLn1)==0:
        NextText = NextLn2
      else:
        NextText = NextLn1 + "\n" + NextLn2
      TextLines.append(NextText)
      info('Added text line\n"'+NextText+'"', False)
      UpdateDisplay()
    else:
      info("There's no text in\nthe text box.", True)
def saveSRT():
    TotalLines = [len(TextLines), len(startTimes), len(endTimes)]
    FailReasons = "Couldn't export subtitles for these reasons:"
    if min(TotalLines) == 0:
      if len(TextLines) == 0:
        FailReasons = FailReasons+"\nThere aren't any text lines."
      if len(endTimes) == 0:
        FailReasons = FailReasons+"\nThere aren't any end times."
      if len(startTimes) == 0:
        FailReasons = FailReasons+"\nThere aren't any start times."
      info(FailReasons, True)
    else:
      WorkingFile = filedialog.asksaveasfilename(initialdir=WorkingDir, title = "Export Subtitles", filetypes = (("SubRip Text Subtitles","*.srt"),("all files","*.*")))
      if WorkingFile != '':
        if WorkingFile.endswith(".srt"):
            SaveFile = open(WorkingFile, 'w')
        else:
          SaveFile = open(WorkingFile+".srt", 'w')
        for x in range(0, min(TotalLines)):
            SaveFile.write(str(x+1)+"""
""")
            SaveFile.write("""%s --> %s
""" % (startTimes[x], endTimes[x]))
            SaveFile.write(TextLines[x])
            SaveFile.write(''' 

''')
        SaveFile.close()
        info('Exported subtitles.', False)
def SaveDraft():
    global TextLines
    global startTimes
    global endTimes
    global totaltimelapsed
    if WorkingFile == "Not Specified":
      SaveDraftAs()
    else:
      saved_data = {"starts" : startTimes, "ends" : endTimes, "Texts" : TextLines, "time" : totaltimelapsed}
      save_file = open(WorkingFile, "wb")
      pickle.dump(saved_data, save_file)
      save_file.close()
      info('Saved draft', False)
      UpdateDisplay()
def SaveDraftAs():
    global TextLines
    global startTimes
    global endTimes
    global totaltimelapsed
    global WorkingFile
    WorkingFile = filedialog.asksaveasfilename(initialdir=WorkingDir, title = "Save Draft file",filetypes = (("BroCColi Drafts","*.dat"),("all files","*.*")))
    if WorkingFile != '':
      saved_data = {"starts" : startTimes, "ends" : endTimes, "Texts" : TextLines, "time" : totaltimelapsed}
      if WorkingFile.endswith(".dat"):
        save_file = open(WorkingFile, "wb")
      else:
        save_file = open(WorkingFile+".dat", "wb")
      pickle.dump(saved_data, save_file)
      save_file.close()
      info('Saved draft.', False)
      UpdateDisplay()
def Play(addingtimes):
    global running
    global StartTime
    canvas.itemconfig(PauseRec2, fill="")
    canvas.itemconfig(PauseRec1, fill="")
    canvas.itemconfig(PlayTriangle, fill="cyan")
    running = True
    StartTime = int(time.time())
    if addingtimes == True:
        AddTimes()
def loadDraft():
    global TextLines
    global startTimes
    global endTimes
    global totaltimelapsed

    global WorkingFile
    WorkingFile = filedialog.askopenfilename(initialdir=WorkingDir, title = "Open Draft file",filetypes = (("BroCColi Drafts","*.dat"),("all files","*.*")))
    if WorkingFile != '':
      load_file = open(WorkingFile, "rb")
      loaded_data = pickle.load(load_file)
      startTimes = loaded_data["starts"]
      endTimes = loaded_data["ends"]
      TextLines = loaded_data["Texts"]
      totaltimelapsed = loaded_data["time"]
      UpdateDisplay()
      load_file.close()
      info('Loaded draft from file:\n'+WorkingFile, False)
def ImportText():
  global TextLines
  WorkingFile = filedialog.askopenfilename(initialdir=WorkingDir, title = "Open Text file",filetypes = (("Text Files","*.txt"),("all files","*.*")))
  if WorkingFile != '':
    load_file = open(WorkingFile)
    LoadedText = load_file.read()
    ImpLines = LoadedText.splitlines()
    CurLn = ""
    CraftingTable = []
    Ln1 = 0
    for x in range(0, len(ImpLines)):
        if len(ImpLines[x])!=0:
          if len(ImpLines[x])>30:
            CraftingTable = ImpLines[x].split()
            ln1 = int(len(CraftingTable)/2)
            for y in range(0, len(CraftingTable)):
              if len(CurLn)==0:
                CurLn = CraftingTable[y]
              else:
                if y == int(len(CraftingTable)/2):
                  CurLn = CurLn+"\n"+CraftingTable[y]
                else:
                  CurLn = CurLn+" "+CraftingTable[y]
          else:
           if len(CurLn)==0:
             CurLn = ImpLines[x]
           else:
             CurLn = CurLn+"\n"+ImpLines[x]
          if x == len(ImpLines)-1:
            TextLines.append(CurLn)
            CurLn = ""
        else:
          TextLines.append(CurLn)
          CurLn = ""
    load_file.close()
    info("Imported text lines\nfrom file.", False)
    UpdateDisplay()
def New():
    global totaltimelapsed
    global startTimes
    global endTimes
    global TextLines
    totaltimelapsed = 0
    startTimes = []
    endTimes = []
    TextLines = []
    UpdateDisplay()
    info("Started new file", False)

def AddTimes():
        
        if len(startTimes) == len(endTimes) and len(startTimes) <= len(TextLines):
            
            startTimes.append(Timestamp)
            info('Added start time at:\n'+Timestamp, False)
        elif len(endTimes) <= len(TextLines):
            
            endTimes.append(Timestamp)
            info('Added end time at:\n'+Timestamp, False)
        UpdateDisplay()
def PausePlay():
    if running == False:
          Play(False)
    else:
        Pause(False)
def UpdateDisplay():
    global Timestamp
    global totaltimelapsed
    global TextLines
    global endTimes
    Timestamp = Time_convert(totaltimelapsed)
    #canvas.create_rectangle(0, 0, 200, 50, fill="black")
    #canvas.create_text(100, 15, text=Timestamp, fill="green", font=("Helvetica", 20))
    canvas.itemconfig(display, text=Timestamp)
    if len(endTimes) < len(TextLines):
      canvas.itemconfig(nxtln, text=TextLines[len(endTimes)])
    else:
      canvas.itemconfig(nxtln, text="<No More Lines>")
    tk.update()

def Pause(addingtimes):
    global totaltimelapsed
    global running
    global Timestamp
    global StartTime
    canvas.itemconfig(PauseRec2, fill="red")
    canvas.itemconfig(PauseRec1, fill="red")
    canvas.itemconfig(PlayTriangle, fill="")
    running = False
    timepassed = int(time.time()) - StartTime
    totaltimelapsed = totaltimelapsed + timepassed
    Timestamp = Time_convert(totaltimelapsed)
    if addingtimes == True:
        AddTimes()
    UpdateDisplay()
def Rewind():
    global totaltimelapsed
    totaltimelapsed = totaltimelapsed - 1
    UpdateDisplay()
def Ffwd():
    global totaltimelapsed
    totaltimelapsed = totaltimelapsed + 1
    UpdateDisplay()
def AddPp():
    global startTimes
    global endTimes
    global TextLines
    if running == True and  len(startTimes) > len(endTimes):
        Pause(True)
        if len(TextLines)>len(endTimes):
          Play(False)
          
    else:
        if running == True:
            Pause(False)
            Play(True)
        else:
            AddTimes()
def ViewLines():
    global startTimes
    global endTimes
    global TextLines
    print(startTimes)
    print(len(startTimes))
    print(endTimes)
    print(len(endTimes))
    print(TextLines)
    print(len(TextLines))
    info('Printed out lines in the console.', False)
def delTxt():
  global TextLines
  if len(TextLines) != 0:
    del TextLines[len(TextLines)-1]
    info('Deleted last text line', False)
    UpdateDisplay()
  else:
    info('There aren\'t any text\nlines to delete.', True)
def delTms():
  global startTimes
  global endTimes
  if len(startTimes) != 0:
    if len(startTimes) == len(endTimes):
      del endTimes[len(endTimes)-1]
      del startTimes[len(startTimes)-1]
      info('Deleted last start time\nand end time', False)
    else:
      del startTimes[len(startTimes)-1]
      info('Deleted last start time', False)
  else:
    info('There are no start/end times\nto delete', True)
# Style manipulation functions
def ToBrackets():
  global TextLines
  TotalLines = len(TextLines)
  for x in range(0, TotalLines):
    
    CurLn = TextLines[x]
    CurLn = CurLn.replace(")", "]")
    CurLn = CurLn.replace("(", "[")
    del TextLines[x]
    TextLines.insert(x, CurLn)
  info('All parentheses are\nconverted to square brackets.', False)
  UpdateDisplay()
def ToParens():
  global TextLines
  TotalLines = len(TextLines)
  for x in range(0, TotalLines):
    
    CurLn = TextLines[x]
    print(CurLn)
    CurLn = CurLn.replace("[", "(")
    CurLn = CurLn.replace("]", ")")
    del TextLines[x]
    TextLines.insert(x, CurLn)
  info('All square brackets are\nconverted to parentheses.', False)
  UpdateDisplay()
def BrackID():
  global TextLines
  CurLns = []
  CurTXT = ""
  FullLine = ""
  for a in range(0, len(TextLines)):
    CurLns = TextLines[a].splitlines()
    for b in range(0, len(CurLns)):
      CurTXT = CurLns[b]
      if CurLns[b].startswith(" "):
        if CurLns[b].find(":")!=-1:
          CurTXT = CurTXT.replace(":","]",1)
          if CurLns[b].startswith(" - "):
            CurTXT = CurTXT.replace(" - "," - [",1)
          elif CurLns[b].startswith(" -"):
            CurTXT = CurTXT.replace(" -"," -[",1)
          else:
            CurTXT = CurTXT.replace(" "," [",1)
        elif CurLns[b].find("(")<=3:
          CurTXT = CurTXT.replace("(","[",1)
          CurTXT = CurTXT.replace(")","]",1)
      if FullLine == "":
          FullLine = CurTXT
      else:
          FullLine = FullLine + "\n"+CurTXT
    TextLines[a] = FullLine
    FullLine = ""
  info("Identifiers changed.\nPREVIEW:\n[Identifier] Message",False)
  UpdateDisplay()
def ParenID():
  global TextLines
  CurLns = []
  CurTXT = ""
  FullLine = ""
  for a in range(0, len(TextLines)):
    CurLns = TextLines[a].splitlines()
    for b in range(0, len(CurLns)):
      CurTXT = CurLns[b]
      if CurLns[b].startswith(" "):
        if CurLns[b].find(":")!=-1:
          CurTXT = CurTXT.replace(":",")",1)
          if CurLns[b].startswith(" - "):
            CurTXT = CurTXT.replace(" - "," - (",1)
          elif CurLns[b].startswith(" -"):
            CurTXT = CurTXT.replace(" -"," -(",1)
          else:
            CurTXT = CurTXT.replace(" "," (",1)
        elif CurLns[b].find("[")<=3:
          CurTXT = CurTXT.replace("[","(",1)
          CurTXT = CurTXT.replace("]",")",1)
      if FullLine == "":
          FullLine = CurTXT
      else:
          FullLine = FullLine + "\n"+CurTXT
    TextLines[a] = FullLine
    FullLine = ""
  info("Identifiers changed.\nPREVIEW:\n(Identifier) Message",False)
  UpdateDisplay()
def ColID():
  global TextLines
  CurLns = []
  CurTXT = ""
  FullLine = ""
  for a in range(0, len(TextLines)):
    CurLns = TextLines[a].splitlines()
    for b in range(0, len(CurLns)):
      CurTXT = CurLns[b]
      if CurLns[b].startswith(" "):
        if CurLns[b].find("[")<=3:
          CurTXT = CurTXT.replace("[","",1)
          CurTXT = CurTXT.replace("]",":",1)
        if CurLns[b].find("(")<=3:
          CurTXT = CurTXT.replace("(","",1)
          CurTXT = CurTXT.replace(")",":",1)
      if FullLine == "":
          FullLine = CurTXT
      else:
          FullLine = FullLine + "\n"+CurTXT
    TextLines[a] = FullLine
    FullLine = ""
  info("Identifiers changed.\nPREVIEW:\nIdentifier: Message",False)
  UpdateDisplay()
def CapsWithin():
  global TextLines
  CurLns = []
  CurWds = []
  CapMode = False
  CurLn1 = ''
  CurLn2 = ''
  for a in range(0, len(TextLines)):
    CurLns = TextLines[a].splitlines()
    for b in range(0, len(CurLns)):
      CurWds = CurLns[b].split()
      if CurLns[b].startswith(" "):
        CurWds[0] = " "+CurWds[0]
      for c in range(0, len(CurWds)):
          if CurWds[c].startswith("(") or CurWds[c].startswith('[')or CurWds[c].startswith('-(')or CurWds[c].startswith('-['):
            CapMode = True
          if CapMode == True:
            CurWds[c] = CurWds[c].upper()
          if CurWds[c].endswith(")") or CurWds[c].endswith("]"):
            CapMode = False
          if len(CurLn1)==0:
            CurLn1 = CurWds[c]
          else:
            CurLn1 = CurLn1+" "+CurWds[c]
      CurLns[b]=CurLn1
      CurLn1=""
      if len(CurLn2)==0:
        CurLn2 = CurLns[b]
      else:
        CurLn2 = CurLn2+'\n'+CurLns[b]
    TextLines[a] = CurLn2
    CurLn2 = ""
  info("Capitalized everything\ninside (PARENTHESES)\nand[SQUARE BRACKETS]",False)
  UpdateDisplay()
def LowerWithin():
  global TextLines
  CurLns = []
  CurWds = []
  CapMode = False
  CurLn1 = ''
  CurLn2 = ''
  Prefix = ""
  for a in range(0, len(TextLines)):
    CurLns = TextLines[a].splitlines()
    for b in range(0, len(CurLns)):
      CurWds = CurLns[b].split()
      if CurLns[b].startswith(" "):
        CurWds[0] = " "+CurWds[0]
      for c in range(0, len(CurWds)):
          if CurWds[c].startswith("(") or CurWds[c].startswith('[')or CurWds[c].startswith('-(')or CurWds[c].startswith('-['):
            CapMode = True
            if CurWds[c].startswith("("):
              Prefix = "("
            elif CurWds[c].startswith("-("):
              Prefix = "-("
            elif CurWds[c].startswith("["):
              Prefix = "["
            elif CurWds[c].startswith("-["):
              Prefix = "-["
            CurWds[c] = CurWds[c].replace(Prefix, "", 1)
          if CapMode == True:
            CurWds[c] = CurWds[c].capitalize()
            if Prefix != "":
              CurWds[c] = Prefix + CurWds[c]
          if CurWds[c].endswith(")") or CurWds[c].endswith("]"):
            CapMode = False
          if len(CurLn1)==0:
            CurLn1 = CurWds[c]
          else:
            CurLn1 = CurLn1+" "+CurWds[c]
      CurLns[b]=CurLn1
      CurLn1=""
      if len(CurLn2)==0:
        CurLn2 = CurLns[b]
      else:
        CurLn2 = CurLn2+'\n'+CurLns[b]
    TextLines[a] = CurLn2
    CurLn2 = ""
  info("LOWERCASED EVERYTHING\nINSIDE (parentheses)\nAND[square brackets]",False)
  UpdateDisplay()
def LowerID():
  global TextLines
  CurLns = []
  CurWds = []
  CapMode = False
  CurLn1 = ''
  CurLn2 = ''
  Prefix = ""
  for a in range(0, len(TextLines)):
    CurLns = TextLines[a].splitlines()
    for b in range(0, len(CurLns)):
      CurWds = CurLns[b].split()
      if CurLns[b].startswith(" "):
        CurWds[0] = " "+CurWds[0]
        CapMode = True
      for c in range(0, len(CurWds)):
          if CurWds[c].startswith("(") or CurWds[c].startswith('[')or CurWds[c].startswith('-(')or CurWds[c].startswith('-[')or CurWds[c].startswith("-"):
            
            if CurWds[c].startswith("("):
              Prefix = "("
            elif CurWds[c].startswith("-("):
              Prefix = "-("
            elif CurWds[c].startswith("["):
              Prefix = "["
            elif CurWds[c].startswith("-["):
              Prefix = "-["
            elif CurWds[c].startswith("-"):
              Prefix = "-"
            CurWds[c] = CurWds[c].replace(Prefix, "", 1)
          if CapMode == True:
            CurWds[c] = CurWds[c].capitalize()
            if Prefix != "":
              CurWds[c] = Prefix + CurWds[c]
          if CurWds[c].endswith(")") or CurWds[c].endswith("]")or CurWds[c].endswith(":"):
            CapMode = False
          if len(CurLn1)==0:
            CurLn1 = CurWds[c]
          else:
            CurLn1 = CurLn1+" "+CurWds[c]
      CurLns[b]=CurLn1
      CurLn1=""
      if len(CurLn2)==0:
        CurLn2 = CurLns[b]
      else:
        CurLn2 = CurLn2+'\n'+CurLns[b]
    TextLines[a] = CurLn2
    CurLn2 = ""
  info("Lowercased: IDENTIFIERS",False)
  UpdateDisplay()
  
def UpperID():
  global TextLines
  CurLns = []
  CurWds = []
  CapMode = False
  CurLn1 = ''
  CurLn2 = ''
  for a in range(0, len(TextLines)):
    CurLns = TextLines[a].splitlines()
    for b in range(0, len(CurLns)):
      CurWds = CurLns[b].split()
      if CurLns[b].startswith(" "):
        CurWds[0] = " "+CurWds[0]
        CapMode = True
      for c in range(0, len(CurWds)):
          
            
          if CapMode == True:
            CurWds[c] = CurWds[c].upper()
          if CurWds[c].endswith(")") or CurWds[c].endswith("]")or CurWds[c].endswith(":"):
            CapMode = False
          if len(CurLn1)==0:
            CurLn1 = CurWds[c]
          else:
            CurLn1 = CurLn1+" "+CurWds[c]
      CurLns[b]=CurLn1
      CurLn1=""
      if len(CurLn2)==0:
        CurLn2 = CurLns[b]
      else:
        CurLn2 = CurLn2+'\n'+CurLns[b]
    TextLines[a] = CurLn2
    CurLn2 = ""
  info("[UPPERCASED] identifiers",False)
  UpdateDisplay()
def SpaceHyphen():
  global TextLines
  CurLns = []
  CurTXT = ""
  FullLine = ""
  for a in range(0, len(TextLines)):
    CurLns = TextLines[a].splitlines()
    for b in range(0, len(CurLns)):
      CurTXT = CurLns[b]
      if CurLns[b].startswith("-") or CurLns[b].startswith(" -"):
        CurTXT = CurTXT.replace("-","- ",1)
      if FullLine == "":
          FullLine = CurTXT
      else:
          FullLine = FullLine + "\n"+CurTXT
      TextLines[a] = FullLine
    FullLine = ""
  info("Added spaces after hyphens.\nPREVIEW:\n- Message",False)
  UpdateDisplay()
def UnSpaceHyphen():
  global TextLines
  CurLns = []
  CurTXT = ""
  FullLine = ""
  for a in range(0, len(TextLines)):
    CurLns = TextLines[a].splitlines()
    for b in range(0, len(CurLns)):
      CurTXT = CurLns[b]
      if CurLns[b].startswith("- ") or CurLns[b].startswith(" - "):
        CurTXT = CurTXT.replace("- ","-",1)
      if FullLine == "":
          FullLine = CurTXT
      else:
          FullLine = FullLine + "\n"+CurTXT
      TextLines[a] = FullLine
    FullLine = ""
  info("Removed spaces after hyphens.\nPREVIEW:\n-Message",False)
  UpdateDisplay()
def Surprise():
  global TextLines
  Brackets = ["ToBrackets()", "ToParens()"]
  Upper1 = ["CapsWithin()", "LowerWithin()"]
  IDtype = ["ColID()", "BrackID()", "ParenID()"]
  Upper2 = ["UpperID()", "LowerID"]
  HyphenStyle = ["UnSpaceHyphen()", "SpaceHyphen()"]
  newStyle = []
  Preview = ""
  newStyle.append(random.choice(Brackets))
  newStyle.append(random.choice(Upper1))
  newStyle.append(random.choice(IDtype))
  newStyle.append(random.choice(Upper2))
  newStyle.append(random.choice(HyphenStyle))
  for x in range(0, len(newStyle)):
    exec(newStyle[x])
  if newStyle[4] == "UnSpaceHyphen()":
    Preview = "-"
  else:
    Preview = "- "
  if newStyle[2] == "BrackID()":
    Preview = Preview + "["
  elif newStyle[2] == "ParenID()":
    Preview = Preview + "("
  if newStyle[3] == "UpperID()":
    Preview = Preview + "IDENTIFIER"
  else:
    Preview = Preview + "Identifier"
  if newStyle[2] == "BrackID()":
    Preview = Preview + "]"
  elif newStyle[2] == "ParenID()":
    Preview = Preview + ")"
  else:
    Preview = Preview + ":"
  Preview = Preview + " Message\n"
  if newStyle[4] == "UnSpaceHyphen()":
    Preview = Preview + "-"
  else:
    Preview = Preview + "- "
  if newStyle[0] == "ToBrackets()":
    Preview = Preview + "["
  else:
    Preview = Preview + "("
  if newStyle[1] == "CapsWithin()":
    Preview = Preview + "SOUND EFFECT"
  else:
    Preview = Preview + "Sound Effect"
  if newStyle[0] == "ToBrackets()":
    Preview = Preview + "]"
  else:
    Preview = Preview + ")"
  print(len(Preview))
  Preview = Preview + "\nYour subtitle style has\nbeen randomized."
  
  info(Preview, False)
def AddPp2x():
 global startTimes
 global endTimes
 AddPp()
 if len(startTimes)==len(endTimes):
   AddPp()
   info("Added end time\nand start time.", False)
from tkinter import *
from tkinter import ttk
tk = Tk()
tk.title("BroCColi Subtitle Creator")
tk.wm_attributes("-topmost", 1)
#AddBtn = Button(tk, text="Add Start and end Times", command=AddPp2x)
#AddBtn.pack()
AddBtn2 = Button(tk, text="Add Start/end Times", command=AddPp)
AddBtn2.pack()

PausePlayBtn = Button(tk, text="Pause/Play", command=PausePlay)
PausePlayBtn.pack()
canvas = Canvas(tk, width=250, height=150)
canvas.pack()
canvas.create_rectangle(0, 0, 250, 150, fill="black")
PauseRec1 = canvas.create_rectangle(5, 5, 15, 25, fill="red")
PauseRec2 = canvas.create_rectangle(20, 5, 30, 25, fill="red")
PlayTriangle = canvas.create_polygon(5, 5, 5, 25, 30, 15, fill="")
display = canvas.create_text(150, 15, text=Timestamp, fill="#00ff00", font=("Helvetica", 20))
statmessage = canvas.create_text(125, 75, text=Status, fill="#00ff00")
nxtln = canvas.create_text(125, 125, text="The next text lines will\nappear here if text lines are\nentered first.", fill="white")
menu = Menu(tk)
tk.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label='New', command=New)
filemenu.add_command(label='Open Draft...', command=loadDraft)
filemenu.add_command(label='Save Draft As...', command=SaveDraftAs)
filemenu.add_command(label='Save Draft', command=SaveDraft)
filemenu.add_separator()
filemenu.add_command(label='Import lines from text file...', command=ImportText)
filemenu.add_separator()
filemenu.add_command(label='Export to SRT file...', command=saveSRT)
filemenu.add_command(label='Export lines to text file...', command=SaveTXT)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=tk.destroy)
editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="Delete last start/end times", command=delTms)
editmenu.add_command(label="Delete last text line", command=delTxt)
editmenu.add_separator()
editmenu.add_command(label="Replace () with []", command=ToBrackets)
editmenu.add_command(label="Replace [] with ()", command=ToParens)
editmenu.add_command(label="Capitalize everything inside [] and ()", command=CapsWithin)
editmenu.add_command(label="Lowercase everything inside [] and ()", command=LowerWithin)
editmenu.add_separator()
editmenu.add_command(label="Identifier type 1: [abc] def", command=BrackID)
editmenu.add_command(label="Identifier type 2: (abc) def", command=ParenID)
editmenu.add_command(label="Identifier type 3: abc: def", command=ColID)
editmenu.add_command(label="Lowercase Identifier", command=LowerID)
editmenu.add_command(label="Uppercase Identifier", command=UpperID)
editmenu.add_separator()
editmenu.add_command(label="Add spaces after hyphens", command=SpaceHyphen)
editmenu.add_command(label="Remove spaces after hyphens", command=UnSpaceHyphen)
editmenu.add_separator()
editmenu.add_command(label="Surprise me!", command=Surprise)
viewMenu = Menu(menu)
menu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label="View Text lines", command=ViewLines)
RewBtn = Button(tk, text="<<", command=Rewind)
RewBtn.pack()
FfwdBtn = Button(tk, text=">>", command=Ffwd)
FfwdBtn.pack()
NewLineText = Text(tk, height=2, width=42)
NewLineText.pack()
Nextlinebutton = Button(tk, text="Add line", command=add_new_text)
Nextlinebutton.pack()
tk.update()
#tk.mainloop()

