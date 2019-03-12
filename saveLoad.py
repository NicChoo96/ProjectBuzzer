import json
import os

def saveState(playerScores):

	data = {}
	data['player'] = []
	for i in range(len(playerScores)):
		data['player'].append(playerScores[i])
with open('data.txt','w') as outfile:
	json.dump(data,outfile)

def loadState():
	playerScores = []
	if os.path.isfile('./data.txt'):
		with open('data.txt') as json_file:
		    data = json.load(json_file)
		    for p in data['player']:
		        playerScores.append(p)
	return playerScores