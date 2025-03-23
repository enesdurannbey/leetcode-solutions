class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1) == len(word2):
            combined = ""
            for i in range(len(word1)):
                combined += word1[i]+word2[i]
            return combined
        elif len(word1) < len(word2):
            combined = ""
            for i in range(len(word1)):
                combined += word1[i] + word2[i]
            combined += word2[(len(word1)):]
            return combined
        elif len(word1) > len(word2):
            combined = ""
            for i in range(len(word2)):
                combined += word1[i] + word2[i]
            combined += word1[(len(word2)):]
            return combined
            



        