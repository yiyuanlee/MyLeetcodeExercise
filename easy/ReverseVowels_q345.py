class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = list(s)
        left, right = 0, len(s_list) - 1

        while left < right:
            # Find the next vowel from the left
            while left < right and s_list[left] not in vowels:
                left += 1
            
            # Find the next vowel from the right
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # If both pointers have found a vowel and haven't crossed, swap them
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return "".join(s_list)
