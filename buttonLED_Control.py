import serial

def onButtonOne(arduino):
	arduino.write('a')

def onButtonTwo(arduino):
	arduino.write('b')

def onButtonThree(arduino):
	arduino.write('c')

def onButtonFour(arduino):
	arduino.write('d')

def onButtonFive(arduino):
	arduino.write('e')

def onButtonSix(arduino):
	arduino.write('f')

def onButtonSeven(arduino):
	arduino.write('g')

def onButtonEight(arduino):
	arduino.write('h')

def resetButtons(arduino):
	arduino.write('i')

switcher = {"1":onButtonOne, "2":onButtonTwo, "3":onButtonThree, "4":onButtonFour, "5":onButtonFive, "6":onButtonSix, "7":onButtonSeven, "8":onButtonEight}

def controlButton(arduino, buttonNumb, isOn):
	if isOn:
		switcher[buttonNumb](arduino)
	else:
		#Off All
		resetButtons(arduino);
