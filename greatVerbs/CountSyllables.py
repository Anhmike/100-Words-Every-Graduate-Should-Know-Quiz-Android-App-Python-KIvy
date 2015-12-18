
'''                                                                                                                 
Count Syllables v1.0

A simple class to count syllables using a dictionary method

This class will attempt to calculate syllables of words not found in dictionary
'''

class CountSyllables(object):

        def __init__(self):
		# variables- instantiated
                x = 0

        def generateDict(self):
                # converts a pronunciation dictionary into a syllable count dictionary
                fileName = open("dict.txt", 'r')
                print 'openning file...'
                data = fileName.read()
                fileName.close()

                print 'splitting up data by entries...'
                words = data.split("\n")

                outputFile = open("syllables.txt", 'w')
                for entry in words:
                        entry = entry.split("  ")
                        word = entry[0]
                        pronunciation = entry[1]
                        sections = pronunciation.split(" ")
                        count = 0
                        for section in sections:
                                if self.isVowel(section):
                                        count+=1
                        if count == 0: count = 1
                        
                        outputFile.write(word.lower() + ',' + str(count) + '\n')
                outputFile.close()


        def isVowel(self, word):
                # a simple function to find whether a word contains a vowel or not
                word = word.lower()
                if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:
                        return True
                else: return False

        def count(self, word):
                # count syllables using dictionary method
                fileName = open('syllables.txt', 'r')
                data = fileName.read()
                fileName.close()
                
                lines = data.split('\n') 
                for line in lines:
                        entry = line.split(',')
                        if entry[0] == word.lower(): 
                                # returns number of syllables
                                return int(entry[1])
                # if dictionary method can't find it returns -1
                return -1               
                        
        def oldCount(self, word):
                # an old way to count syllables
                # to be used if the dictionary method fails
                # Thu Sep  3 07:05:09 AEST 2015
                vowels = "aeiou"
                count = 0
                for v in vowels:
                        count += word.lower().count(v)
                if count < 1: return 1
                else: return count
        
def main():
	test = CountSyllables()
	print test.count('elephant')

if __name__ == '__main__':main()
