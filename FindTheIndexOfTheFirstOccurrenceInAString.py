class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for startIndex, _ in enumerate(haystack):
            if len(haystack) - startIndex < len(needle):
                return -1
            matched = True
            for offset, needed in enumerate(needle):
                if haystack[startIndex + offset] != needed:
                    matched = False
                    break
            if matched:
                return startIndex
        return -1

