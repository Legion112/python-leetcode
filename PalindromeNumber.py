class Solution:
    def isPalindrome(self, number: int) -> bool:
        divisor = 1
        while number // divisor >= 10:
            divisor *= 10

        while number != 0:
            leading = number // divisor
            trailing = number %  10
            if leading != trailing:
                return False
            number = (number % divisor) // 10
            divisor /= 100 # removing two digits

        return True