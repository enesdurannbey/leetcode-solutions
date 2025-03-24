class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels =["a","e","i","o","u","A","E","I","O","U"]
        chars = list(s)
        captured = []
        for char in chars:
            if char in vowels:
                captured.append(char)
        captured.reverse()
        vowel_index = 0
        for i,char in enumerate(chars):
            if char in vowels:
                chars[i] = captured[vowel_index]
                vowel_index += 1
        return "".join(chars)