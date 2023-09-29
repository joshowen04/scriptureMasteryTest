class Word:
    def __init__(self,word):
        self.text = word
        self.hidden = False
        self.displayText = self.text


    # def createText(self,text):
    #     return text.split()
    

    def isHidden(self):
        return self.hidden
        pass

    def hide(self):
        self.hidden = True
        textLength = len(self.text)
        hiddenText = ""
        for letter in range(textLength):
            hiddenText += "_"

        self.displayText = hiddenText

if __name__ == "__main__":
    newWord = Word("Baller")
    print(newWord.isHidden())

    print(newWord.displayText)

    newWord.hide();
    print(newWord.displayText)
    print(newWord.isHidden())

