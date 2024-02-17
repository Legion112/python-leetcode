from typing import List, Optional


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        minString: Optional[str] = min(strs, key=lambda s: len(s))
        if minString == "":
            return minString
        maxPrefixLength = 0
        stop = False
        for index, char in enumerate(minString):
            for string in strs:
                if char != string[index]:
                    stop = True
                    break
            if stop:
                return minString[0:maxPrefixLength]
            else:
                maxPrefixLength += 1
        return minString


