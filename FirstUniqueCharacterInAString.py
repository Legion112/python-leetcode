from typing import Dict, Set


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seenTwice: Set[str] = set()
        seenOne: Dict[str, int] = dict()
        for pos, char in enumerate(s):
            if char in seenTwice:
                continue
            if char in seenOne:
                seenOne.pop(char)
                seenTwice.add(char)
                continue
            seenOne[char] = pos
        for pos in seenOne.values():
            return pos

        return -1

