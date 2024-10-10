class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = ''
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            for string in strs[1:]:
                if i >= len(string) or string[i] != current_char:
                    return prefix
            prefix += current_char
        return prefix
