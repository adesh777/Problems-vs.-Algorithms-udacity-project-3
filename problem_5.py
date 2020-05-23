class TrieNode:
    def __init__(self, val=''):

        self.value = val
        self.next = {}
    
    def insert(self, char):

        self.next[char] = self.next.get(char, TrieNode(char))



class Trie:
    def __init__(self):

        self.root = {}

    def insert(self, word):

        word = word
        self.root[word[0]] = self.root.get(word[0], TrieNode(word[0]))
        current = self.root[word[0]]
        for i in range(1, len(word)):
            current.insert(word[i])
            current = current.next[word[i]]

    def find(self, prefix):

        if not prefix:
            return self.root
        
        if prefix[0] not in self.root:
            return None
        
        current = self.root[prefix[0]]
        if current:
            for i in range(1,len(prefix)):
                if prefix[i] not in current.next:
                    return None
                current = current.next[prefix[i]]
        return current

class TrieNode:
    def __init__(self, val=''):
        self.value = val
        self.next = {}
    
    def insert(self, char):
        self.next[char] = self.next.get(char, TrieNode(char))
        
    def suffixes(self, suffix = ''):

        suffix_list = []
        for values in self.next:
            if self.next[values].next:
                suffix_list.extend(self.next[values].suffixes(suffix+values))
            elif values == '\x00':
                suffix_list.append(suffix)
        return suffix_list

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word+'\0')

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='')

