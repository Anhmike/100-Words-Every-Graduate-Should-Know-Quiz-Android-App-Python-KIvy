from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from VocabBuilder import VocabBuilder
from time import sleep

'''
100 Words Every Graduate Should Know
By Troy J. Watson
Wed Aug  5 09:31:32 AEST 2015

A simple quiz to help a student expand their vocabularly.
This program is made for Android using Kivy-Python
'''

# Mon Oct 12 19:10:42 AEDT 2015
#TODO add padding to buttons to make them easy to press for mobile phones
#TODO split answer text to two lines to make it compatible for mobile phones

# Thu Oct  8 16:18:05 AEDT 2015
#TODO add button to reset program
#TODO use screen manager to show a list of high scores

class ExternalLayout(BoxLayout):
        
        def loadLibraries(self):
                # loads a new object, thus only runs at the start of a new quiz
                self.idleMode = False
                self.vocabBuilder = VocabBuilder() # new object of VocabBuilder created
                self.vocabBuilder.loadQuestion()
                self.progressLabel.text = str(self.vocabBuilder.currentWord) + "/100"
                self.questionLabel.text = self.vocabBuilder.question
                self.aLabel.text = self.vocabBuilder.answers[0]
                self.bLabel.text = self.vocabBuilder.answers[1]
                self.cLabel.text = self.vocabBuilder.answers[2]
                self.dLabel.text = self.vocabBuilder.answers[3]
                self.eLabel.text = self.vocabBuilder.answers[4]
                
        def showTopScore(self):
                # aka IDLE MODE
                self.vocabBuilder = VocabBuilder()
                self.idleMode = True
                self.progressLabel = self.ids['progress_label']
                self.statusLabel = self.ids['status_label']
                self.scoreLabel = self.ids['score_label']
                self.questionLabel = self.ids['question_label']
                self.titleLabel = self.ids['title_label']
                self.aLabel = self.ids['a_label']
                self.bLabel = self.ids['b_label']
                self.cLabel = self.ids['c_label']
                self.dLabel = self.ids['d_label']
                self.eLabel = self.ids['e_label']
                self.progressLabel.text = "100/100"
                self.questionLabel.text = "Top Score: " + str(self.vocabBuilder.highScore)
                self.statusLabel.text = ""
                self.titleLabel.text = "100 Words Every Graduate Should Know"
                self.aLabel.text = "press any button to start..."
                self.bLabel.text = ""
                self.cLabel.text = ""
                self.dLabel.text = ""
                self.eLabel.text = ""

        def chooseAnswer(self, reply, *args):
                # if the user was in idleMode and they clicked a button
                # then load up a new session
                if self.idleMode:
                        self.statusLabel.text = ""
                        self.idleMode = False
                        self.loadLibraries()
                
                # if the user is not in idle mode
                # then run this ElSE block
                else:
                        print self.vocabBuilder.currentWord
                        self.progressLabel.text = str(self.vocabBuilder.currentWord + 1) + "/100"
                        self.vocabBuilder.addScore(int(reply) - 1)

                        # if answer correct display CORRECT on screen
                        if (self.vocabBuilder.isCorrect(int(reply) - 1)):
                                print 'Correct'
                                self.titleLabel.text = "[color=00ff08]Correct[/color] "  + self.vocabBuilder.question + " = \n" + self.vocabBuilder.answer
                                self.scoreLabel.text = str(self.vocabBuilder.getScore()) + " correct"
                                
                        # if answer is incorrect display INCORRECT on screen
                        else:
                                print 'Incorrect'
                                print 'Answer', self.vocabBuilder.answer
                                print 'Current score', str(self.vocabBuilder.getScore())
                                self.titleLabel.text = "[color=ff0000]Incorrect[/color] " + self.vocabBuilder.question + " = \n" + self.vocabBuilder.answer
                                self.scoreLabel.text = str(self.vocabBuilder.getScore()) + " correct"

                        # when there are no more questions display score, save score
                        # and go to idle mode
                        if self.vocabBuilder.noMoreLeft():
                                # Thu Oct  8 16:19:35 AEDT 2015
                                #TODO go to the scores screen
                                print 'Questions correct', str(self.vocabBuilder.getScore()), 'out of 100'
                                self.vocabBuilder.saveHighScore()
                                self.showTopScore() # this is idle mode

                        # if there are more questions to go, load a new question
                        else:
                                self.vocabBuilder.loadQuestion() # this loads the new questions
                                # the actual answer is stored in self.vocabBuilder.answer
                                self.questionLabel.text = self.vocabBuilder.question
                                self.aLabel.text = self.vocabBuilder.answers[0]
                                self.bLabel.text = self.vocabBuilder.answers[1]
                                self.cLabel.text = self.vocabBuilder.answers[2]
                                self.dLabel.text = self.vocabBuilder.answers[3]
                                self.eLabel.text = self.vocabBuilder.answers[4]
                                             
class KivyStuff(App):

	def build(self):
                
                Builder.load_file('main.kv')
                externalLayout = ExternalLayout()
                externalLayout.showTopScore()
                return externalLayout
              
def main():
	KivyStuff().run()

if __name__ == '__main__':main()
