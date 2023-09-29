class Reference:
    def __init__(self,book, chapter,verseStart, verseEnd = ""):
        self.book = book
        self.chapter = chapter
        self.verseStart = verseStart
        self.verseEnd = verseEnd
    
        
    def displayReference(self):
        if self.verseEnd:
            referenceText = f"{self.book} {self.chapter}:{self.verseStart}-{self.verseEnd}"
        else:
            referenceText = f"{self.book} {self.chapter}:{self.verseStart}"
        return referenceText
    
    def setBook(self, book):
        self.book = book
    def setChapter(self, chapter):
        self.chapter = chapter
    def setVerseStart(self, verseStart):
        self.verseStart = verseStart
    def setVerseEnd(self, verseEnd):
        self.verseEnd = verseEnd

    