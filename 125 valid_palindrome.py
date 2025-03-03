class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''.join([letter for letter in s.lower() if letter.isalpha()])
        print('clean_str: ', clean_str)
        if clean_str == clean_str[::-1]:
            return True
        return False

s = "A man, a plan, a canal: Panama"
sol = Solution()
sol.isPalindrome(s)
