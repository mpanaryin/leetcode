class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Given an input string s, reverse the order of the words.

        A word is defined as a sequence of non-space characters.
        The words in s will be separated by at least one space.

        Return a string of the words in reverse order concatenated by a single space.

        Note that s may contain leading or trailing spaces or multiple spaces between
        two words. The returned string should only have a single space separating the
        words. Do not include any extra spaces
        """
        s_list = s.strip().split(' ')
        s_list.reverse()
        print(s_list)
        s_list_length = len(s_list)
        new_str = ''
        for i in range(s_list_length):
            print(s_list[i])
            if s_list[i] != '':
                new_str += s_list[i]
                if i != s_list_length:
                    new_str += ' '
        return new_str

st = "the sky is blue"
s = Solution()
result = s.reverseWords(st)
print(result)
