class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0