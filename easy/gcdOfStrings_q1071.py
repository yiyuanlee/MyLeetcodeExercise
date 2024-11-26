class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Return empty string if either input is empty
        if not str1 or not str2:
            return ""
        
        # Find the length of the shorter string
        min_length = min(len(str1), len(str2))
        
        # Iterate through all possible substring lengths (starting with the largest)
        for length in range(min_length, 0, -1):
            # Candidate substring for the common divisor
            candidate = str1[:length]
            
            # Check if the candidate divides both strings
            if str1 == candidate * (len(str1) // length) and str2 == candidate * (len(str2) // length):
                return candidate
        
        return ""
