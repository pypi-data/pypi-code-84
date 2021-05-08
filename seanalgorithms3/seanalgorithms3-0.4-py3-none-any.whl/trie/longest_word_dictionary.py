'''
Given a list of strings words representing an English Dictionary, find the longest word in words that 
can be built one character at a time by other words in words. If there is more than one possible answer, 
return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is 
lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
'''

from collections import defaultdict, deque
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = 0
        self.word = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, x):
        current = self.root 
        for char in x:
            current = current.children[char]
        current.end += 1
        current.word = x

    def bfs(self):
        que = deque([self.root])
        result = ''
        while que:
            current = que.popleft()
            for char in current.children.values():
                if char.end:
                    que.append(char)
                    if len(char.word) > len(result) or char.word < result:
                        result = char.word 

        return result 

def longest_word(words):
    trie = Trie()
    for word in words: trie.insert(word)
    return trie.bfs()


