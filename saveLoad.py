import json
import os

def saveState(playerScores, fileName):

	data = {}
	data['player'] = []
	for i in range(len(playerScores)):
		data['player'].append(playerScores[i])
	with open(fileName+'.txt','w') as outfile:
		json.dump(data,outfile)

def loadState(fileName):
	playerScores = []
	if os.path.isfile('./'+fileName+'.txt'):
		with open(fileName+'.txt') as json_file:
		    data = json.load(json_file)
		    for p in data['player']:
		        playerScores.append(p)
	return playerScores