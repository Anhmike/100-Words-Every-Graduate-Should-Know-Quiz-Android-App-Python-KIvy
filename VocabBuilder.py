from random import randint
from random import shuffle
import re
'''                                                                                                    
VocabBuilder v1.0

By Troy J. Watson
Wed Aug  5 09:30:54 AEST 2015
An object to organize a multiple choice quiz. 
'''

#TODO weed out vestigial features

class VocabBuilder(object):

        def __init__(self):
		self.currentWord = 0
		self.anyMore = True
		self.score = 0
                self.highScore = self.getHighScore()
		self.words = []
		self.loadWords()		
		self.loadDict()

	def loadWords(self):
		# gets list of 100 words and 100 meanings
		fileName = open("gradWords.txt", "r")
		data = fileName.read()
		fileName.close()
		self.words = data.split("\n")
		self.words = filter(None, self.words)
		self.shuffleWords()
	
	def loadDict(self):
		# loads dictionary to create random words
		fileName = open("dict.txt", "r")
		data = fileName.read()
		fileName.close()
		self.dict = data.split("\n")
		
	def getRandomWord(self):
		# gets a random number from the dictionary
		while (True):			
			number = randint(1, len(self.dict)-1)
			newWord = self.dict[number]
			if len(newWord) > 1: return newWord
		

	def shuffleWords(self):
		# shuffles words and meanings
		shuffle(self.words)
		
	def loadQuestion(self):
		# creates a question, answer and answers variables
		# it keeps the real answer separate to be able to remember which one is correct
		entry = self.words[self.currentWord].split(',')
		#print entry
		#print self.currentWord
		question = entry[0]
		answer = entry[1]
		answers = [self.getRandomWord(), self.getRandomWord(), self.getRandomWord(), self.getRandomWord(), answer]
		self.question = question
		self.answer = answer
		shuffle(answers)
		self.answers = answers
		self.currentWord += 1

	def noMoreLeft(self):
		# is there more to go in the quiz?
		if self.currentWord > 99: return True
		else: return False

	def isCorrect(self, selection):
		# returns True if user got last question correct
		if self.answers[selection] == self.answer: return True
		else: return False

	def addScore(self, selection):
		# give the number position of answer- 0,1,2,3,4
		# if the number pos is the same as the real answer than add a score
		if self.answers[selection] == self.answer:
			self.score += 1

	def getScore(self):
		# get the current score
		return self.score

	def deleteHighScoreFile(self):
		# create the high scores file and delete anything already there
		fileName = open('highScores.txt', 'w')
		fileName.write("High Scores\n")
		fileName.close()


        def saveHighScore(self):
                # save a new highscore
                if self.score > self.getHighScore():
                        fileName = open('highScores.txt', 'w')
                        #print str(self.score)
                        fileName.write(str(self.score))
                        fileName.close()

	def getHighScore(self):
		# gets all of the highscore
		fileName = open('highScores.txt', 'r')
		data = fileName.read()
		fileName.close()
		temp =  int(re.sub("[^0-9]", "", data))
                #print str(temp)
                return temp
