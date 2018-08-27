class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
   
        paragraph = self.removePunctionCharacters(paragraph)
        paragraph = paragraph.lower()
        paragraph = paragraph.split()
        mapWordToOccurences = {}
        for value in paragraph:
            if value not in banned and value is not " ":
                if value in  mapWordToOccurences:
                     mapWordToOccurences[value] +=1
                else:
                     mapWordToOccurences[value] = 1
        
        maxOccurrence = max( mapWordToOccurences.values())
        return self.getMaxOccurrenceWord(mapWordToOccurences, maxOccurrence)
    



    def removePunctionCharacters(self, paragraph):
        removeChars = "!?',;."
        for char in removeChars:
            paragraph = paragraph.replace(char,"")
        return paragraph
    
    def getMaxOccurrenceWord(self, mapWordToOccurences, maxOccurrence):
        for key, value in  mapWordToOccurences.items():
            if value == maxOccurrence:
                return key



