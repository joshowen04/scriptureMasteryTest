from Word import Word
from Reference import Reference
class Scripture:
    def __init__(self,text="This is a test"):
        self.text = text
        self.textList = self.createText(self.text)
        self.wordList = self.createWords(self.textList)
        
    def setText(self,text):
        self.text = text
        self.textList = self.createText(self.text)
        self.wordList = self.createWords(self.textList)

    def setReference(self,reference):
        self.reference = reference


    def createText(self,text):
        return text.split()
    
    def makeWord(self,word):
        newWord = Word(word)
        #print(newWord.displayText)
        #print(newWord.isHidden())
        return newWord

    def createWords(self, textList):
        wordList = map(self.makeWord,textList)
        wordList = list(wordList)
        return wordList
        
        
    
    def displayText(self):
        newText = ""
        for word in self.wordList:
            newText += f"{word.displayText} "

        return newText

if __name__ == "__main__":
    newScripture = Scripture()
    # print(newScripture.text)
    # print(newScripture.textList)
    #print(newScripture.wordList)
    print(newScripture.displayText())

    newScripture.wordList[3].hide()
    print(newScripture.displayText())
    newScripture.setText("I am the way, the truth and the light.")
    print(newScripture.displayText())

    newScripture.wordList[2].hide()
    print(newScripture.displayText())
    newReference = Reference("1 Nephi",10,25)
    newScripture.setReference(newReference)
    print(newScripture.reference.displayReference())