class Solution:
    _romanMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        result = sum(
            self._romanMap[s[i]] if self._romanMap[s[i]] >= self._romanMap[s[i + 1]]else -self._romanMap[s[i]]
            for i in range(len(s) - 1)
        ) + self._romanMap[s[-1]]
        return result
