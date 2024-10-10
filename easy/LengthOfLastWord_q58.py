class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cleaned_s = s.split()
        return(len(cleaned_s[-1]))