import serial
import sys
import serial.tools.list_ports
import time
import keyboard
from arduinoTools import findArduino, getButtonStatus
from playsound import playsound
from configuration import *
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
#-------------------------------------------------------------------------
#Button Mapping
buttonOneMap = 'f2'
buttonTwoMap = 'f3'
buttonThreeMap = 'f4'
buttonFourMap = 'f5'
buttonFiveMap = 'f6'
buttonSixMap = 'f7'
buttonSevenMap = 'f8'
buttonEightMap = 'f9'


#-------------------------------------------------------------------------

#Private logic variables
fontSize = 30
labelWidth = 4
pressedButtonLogger = []
listOfNum = ["1","2","3", "4", "5", "6", "7", "8"]
scoreList = [0,0,0,0,0,0,0,0]
scoreDisplay = []
scoreConfig = []
currentPlayer = -1
unlocked = True
currentName = ""
arduinoPort = ""
status= ""
isBorder = True
#Delay from reset
resetDelay = 0.1
winLoseLock = True

#-------------------------------------------------------------------------
#detect arduino in windows port
arduino = findArduino()
#-------------------------------------------------------------------------

#Set names on display
def setText(name):
    textDisplay.set(name)

#-------------------------------------------------------------------------

#Get Button Numb last index
def getLastPressed():
    global pressedButtonLogger
    return pressedButtonLogger[-1]

def appendLastEntry(entry):
    global editArea
    editArea.config(state='normal')
    editArea.insert(END, ">" + entry + "\n")
    editArea.see(END)
    editArea.config(state='disabled')

#reset all button locks
def resetRound():
    #Connect function variable to global
    global unlocked
    global resetDelay
    global currentName
    global winButton
    global loseButton
    global resultPanel
    global scoreConfig
    global currentPlayer
    global backgroundColor
    #Disable win/lose buttons on the control panel
    winButton['state'] = 'disabled'
    loseButton['state'] = 'disabled'
    #Set original name label to no one
    setText("Who's Next!")
    #Reset Image
    #resultPanel.configure(image='')
    #Reset variables
    unlocked = True
    currentName = ""
    print("Reset!")
    time.sleep(resetDelay)
    scoreConfig[currentPlayer].config(bg=backgroundColor)

#Reset but players who pressed before cannot press again
def softReset():
    resetRound()
    appendLastEntry("Reset Partial")
    
#Reset all button input and all players can press
def hardReset():
    global pressedButtonLogger
    resetRound()
    appendLastEntry("Reset All")
    #Hard reset button logged
    pressedButtonLogger = []
#-------------------------------------------------------------------------

#Create control panel window, labels and buttons
def createControlPanel():
    global winButton
    global loseButton
    global selectedLabel
    global editArea
    
    top = Toplevel()
    top.title("Control Panel")
    top.wm_attributes("-topmost", 1)
    #Main name settings
    selectedLabel = Label(top, textvariable=textDisplay, width=20, font=("Arial", 30)).pack()
    #Reset buttons settings
    hardResetButton = Button(top, text="Reset All", width=20, height=5, padx=20, pady=20, command=hardReset)
    hardResetButton.pack(side=LEFT)
    softResetButton = Button(top, text="Reset Partial", width=20, height=5, padx=20, pady=20, command=softReset)
    softResetButton.pack(side=LEFT)
    #Win button settings
    winButton = Button(top, text="Win", width=20, height=5, padx=20, pady=20, command=winFunc)
    winButton.pack(side=LEFT)
    #Lose button settings
    loseButton = Button(top, text="Lose", width=20, height=5, padx=20, pady=20, command=loseFunc)
    loseButton.pack(side=LEFT)
    #Toggle Display Border
    #Lose button settings
    borderButton = Button(top, text="Toggle Border", width=20, height=5, padx=20, pady=20, command=toggleBorder)
    borderButton.pack(side=LEFT)
    #Quit button settings
    quitButton = Button(top, text="Quit", width=20, height=5, padx=20, pady=20, command=quit)
    quitButton.pack(side=LEFT)
    #Scrollable Text Field
    editArea = ScrolledText(
        master = top,
        wrap = WORD,
        width = 10,
        height = 5
    )
    editArea.config(state='disabled')
    #editArea.configure(state=DISABLED)
    editArea.pack(padx=10,pady=10,fill=BOTH,expand=False,side=RIGHT)
    #Reset win/lose buttons to 'disable'
    resetButtons()


#-------------------------------------------------------------------------
#Win Lose Display Logic
def winFunc():
    global currentName
    global resultPanel
    global correctImage
    
    #Add points and update scoreboard
    updateScoreBoard(1)
    flashLabel(scoreConfig[currentPlayer], "green", True, 6, 150)

    #Display correct animation
    #resultPanel.configure(image=correctImage)
    #resultPanel.image = correctImage
    
    #setText(currentName + "\nanswered correct!")
    
    resetButtons()   #Reset win/lose buttons to 'disable'
    #Log into control panel display
    appendLastEntry(getLastPressed() + " correct")
    playsound('sound/Correct.wav', False)

def loseFunc():
    global currentName
    global resultPanel
    global wrongImage
    
    #Deducts points and update scoreboard
    updateScoreBoard(-1)
    flashLabel(scoreConfig[currentPlayer], "red", True, 4, 300)


    #Display Wrong Animation
    #resultPanel.configure(image=wrongImage)
    #resultPanel.image = wrongImage
    
    #setText(currentName + "\nanswered wrong...")
    
    resetButtons()   #Reset win/lose buttons to 'disable'
    #Log into control panel display
    appendLastEntry(getLastPressed() + " wrong")
    playsound('sound/Wrong.wav', False)

#-------------------------------------------------------------------------
    
#Change win/lose button back to disabled
def resetButtons():
    global winLoseLock
    winButton['state'] = 'disabled'
    loseButton['state'] = 'disabled'
    winLoseLock = True

#-------------------------------------------------------------------------
#Quit program
def quit():
    root.destroy()
    sys.exit()

#-------------------------------------------------------------------------
#Toggling Display Windows Border
def toggleBorder():
    global root
    global isBorder
    if isBorder:
        isBorder = False
        root.overrideredirect(1)
    else:
        isBorder = True
        root.overrideredirect(0)

#-------------------------------------------------------------------------
#Manual inputs
def debugKeyInputs():
    global buttonNumb
    #Keyboard inputs for Reset and Quit
    try:
        if keyboard.is_pressed('k') and not winLoseLock: #reset button pressed
            winFunc()
        else:
            pass
        if keyboard.is_pressed('l') and not winLoseLock: #reset button pressed
            loseFunc()
        else:
            pass
        if keyboard.is_pressed('r'): #reset button pressed
            hardReset()
        else:
            pass
        if keyboard.is_pressed('s'): #reset button pressed
            softReset()
        else:
            pass
        if keyboard.is_pressed('q'): #quit game
            print("Button Smashing Quit!")
            quit()
        else:
            pass
        if keyboard.is_pressed(buttonOneMap): #reset button pressed
            buttonNumb = "1"
        else:
            pass
        if keyboard.is_pressed(buttonTwoMap): #reset button pressed
            buttonNumb = "2"
        else:
            pass
        if keyboard.is_pressed(buttonThreeMap): #reset button pressed
            buttonNumb = "3"
        else:
            pass
        if keyboard.is_pressed(buttonFourMap): #reset button pressed
            buttonNumb = "4"
        else:
            pass
        if keyboard.is_pressed(buttonFiveMap): #reset button pressed
            buttonNumb = "5"
        else:
            pass
        if keyboard.is_pressed(buttonSixMap): #reset button pressed
            buttonNumb = "6"
        else:
            pass
        if keyboard.is_pressed(buttonSevenMap): #reset button pressed
            buttonNumb = "7"
        else:
            pass
        if keyboard.is_pressed(buttonEightMap): #reset button pressed
            buttonNumb = "8"
        else:
            pass
    except:
        quit()

def checkButtonNotPressedBefore(buttonNumb):
    for bN in pressedButtonLogger:
        if bN == buttonNumb:
            return False
    return True

#-------------------------------------------------------------------------
#Create Scoreboard
def createScoreBoard():
    #global numberOfPlayers
    #global root
    global scoreDisplay
    #global backgroundColor
    #global fontColor
    global scoreConfig
    for x in range(numberOfPlayers):
        display = StringVar()
        scoreDisplay.append(display)
        s_config = Label(root, textvariable=scoreDisplay[x],
                      width=labelWidth, bg=backgroundColor, fg=fontColor, font=("Arial", fontSize))
        s_config.pack(side=LEFT)
        scoreConfig.append(s_config)
        scoreDisplay[x].set(str(x+1) + "\n" + str(scoreList[x]))
        
def updateScoreBoard(points):
    global currentPlayer
    global scoreList
    global scoreDisplay
    if not (points < 0 and scoreList[currentPlayer] == 0):
        scoreList[currentPlayer] += points
        scoreDisplay[currentPlayer].set(
        str(listOfNum[currentPlayer]) + "\n" + str(scoreList[currentPlayer]))

def flashLabel(flashingLabel, color, isSelected, times, delay):
    if getLabelColor(flashingLabel) == backgroundColor:
        setLabelColor(flashingLabel, color)
    else:
        setLabelColor(flashingLabel, backgroundColor)
    times = times - 1
    if times >= 0:
        flashingLabel.after(delay, flashLabel, flashingLabel, color, isSelected, times, delay)
    else:
        if isSelected:
            setLabelColor(flashingLabel, color)
        else:
            setLabelColor(flashingLabel, backgroundColor)

#get set label color
def getLabelColor(labelName):
    return labelName.cget('bg')
def setLabelColor(labelName, color):
    labelName.config(bg=color)
    
#-------------------------------------------------------------------------
def main():
    global unlocked
    global currentName
    global winButton
    global loseButton
    global buttonNumb
    global pressedButtonLogger
    global currentPlayer
    global winLoseLock
    #Assign values from arduino serial output
    buttonNumb = getButtonStatus(arduino) #Decode arduino output from \r\n'1'
    if debugging:
        debugKeyInputs()
    if buttonNumb != "" and unlocked and checkButtonNotPressedBefore(buttonNumb):
        #Logged button pressed to prevent pressing of the same button
        pressedButtonLogger.append(buttonNumb)
        #Button Pressed feedback sound
        playsound('sound/ButtonPressed.wav', False)
        #Lock button
        unlocked = False
        winLoseLock = False
        #Set name selected from nameList, from arduino output
        currentName = nameList[int(buttonNumb)-1]
        #Set current player to press button
        currentPlayer = int(buttonNumb) - 1
        #Highlight the player who press the button
        flashLabel(scoreConfig[currentPlayer], selectedColor, True, 5, 200)
        #Set display to name
        setText(currentName)
        #Enable win lose buttons
        winButton['state'] = 'active'
        loseButton['state'] = 'active'
        #Debug steps
        print(buttonNumb)
        appendLastEntry(buttonNumb + " has pressed")
        print("Lock Engaged")
    #Loop main display window
    root.after(10, main)
    
#-------------------------------------------------------------------------
#Instantiate main display window
root = Tk()
root["bg"] = backgroundColor

createScoreBoard()
root.title(displayTitle)
root.geometry(displayWindowSize) #Size of window
#ttk.Style().configure('TFrame', background=backgroundColor)
#backgroundFrame = ttk.Frame(root)
#backgroundFrame.pack(fill="both", expand=True)
#Import all images
correctImage = PhotoImage(file="image/Tick.png")
correctImage = correctImage.zoom(imageSize)
correctImage = correctImage.subsample(32)
wrongImage = PhotoImage(file="image/Cross.png")
wrongImage = wrongImage.zoom(imageSize)
wrongImage = wrongImage.subsample(32)

#Control panel display variable
textDisplay = StringVar()
#selectedLabel = Label(root, textvariable=textDisplay,
                      #width=20, font=("Arial", 35)).pack()
#Default who's next text
setText("Who's Next!")

resultPanel = Label(root)
resultPanel.pack(side="left", fill="both", expand="yes")

createControlPanel()
#createScorePanel()
#Always on top of all other windows program
root.wm_attributes("-topmost", 1)
root.after(1000, main)
root.mainloop()
