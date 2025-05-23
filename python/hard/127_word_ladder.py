import collections


class Solution:
    """
    Grade[Hard]
    Topics[Hash Table, String, Breadth-First Search]

    A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence
    of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
    Given two words, beginWord and endWord, and a dictionary wordList,
    return the number of words in the shortest transformation sequence from beginWord to endWord,
    or 0 if no such sequence exists.

    Constraints:
        1 <= beginWord.length <= 10
        endWord.length == beginWord.length
        1 <= wordList.length <= 5000
        wordList[i].length == beginWord.length
        beginWord, endWord, and wordList[i] consist of lowercase English letters.
        beginWord != endWord
        All the words in wordList are unique.
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """
        Time complexity: O(N * M^2)
        Space complexity: O(N * M)
        """
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
    