from collections import Counter


class Solution:
    """
    The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

    For example, "ACGAATTCCG" is a DNA sequence.
    When studying DNA, it is useful to identify repeated sequences within the DNA.

    Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that
    occur more than once in a DNA molecule. You may return the answer in any order.
    """
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sequences_of_nucleotides = list()
        str_length = len(s)
        if str_length < 10:
            return []
        for i in range(str_length-9):
            sequences_of_nucleotides.append(s[i:i+10])
        sequences_of_nucleotides_counter = Counter(sequences_of_nucleotides)
        return [seq for seq, number in sequences_of_nucleotides_counter.items() if number >= 2]


s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s2 = "AAAAAAAAAAAAA"
s3 = "AAAAAAAAAAA"
sol = Solution()
result = sol.findRepeatedDnaSequences(s3)
print(result)
