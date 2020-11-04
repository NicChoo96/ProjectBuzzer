import serial.tools.list_ports
import sys
listOfNum = ["1","2","3", "4", "5", "6", "7", "8"]

#list all ports and find arduino
#return arduino linkage
def findArduino():
	arduinoPort = ""
	ports = list(serial.tools.list_ports.comports())
	for p in ports:
		print(p)
		if "Arduino" in p[1]:
			arduinoPort = p[0];
		elif "USB-SERIAL CH340" in p[1]:
			arduinoPort = p[0];
	#if arduino is found, link arduino serial to python
	if arduinoPort != "":
		return serial.Serial(arduinoPort, 9600, timeout=0)
	else:
		print("Error 404, Arduino Not Found!")
		sys.exit()

#gets latest update from arduino
def getLatestStatus(thisArduino):
	status = ""
	while thisArduino.inWaiting() > 0:
		status = thisArduino.readline();
	return status;

#strip the raw data of their spaces
def cleanData(inputData): 
	if inputData == "": #bug patch between byte and str
		return "";
	else:
		return inputData.strip().decode()

#checks if the data has numbers in it from the input data
def checkListNum(data):
	for n in listOfNum:
		if n in data:
			return True;
	return False;

#extract out the numbers from the string
def extractNum(data):
	for n in listOfNum:
		if n in data:
			return n;
	return "";

def getButtonStatus(cArduino):
	return extractNum(cleanData(getLatestStatus(cArduino)))
