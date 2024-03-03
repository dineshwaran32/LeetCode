class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            l1 = haystack.index(needle)
        except ValueError:
            l1 = -1
        return l1
