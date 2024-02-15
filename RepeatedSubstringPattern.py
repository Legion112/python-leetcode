class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for length in range(1, len(s) // 2 + 1):
            if len(s) % length != 0:
                continue
            substring = s[:length]
            if s == (substring * (len(s) // length)):
                return True
        return False
