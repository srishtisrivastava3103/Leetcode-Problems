class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Operations:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for i in word:
            if i in curr.children:
                curr = curr.children[i]
                continue
            else:
                curr.children[i] = TrieNode()
                curr = curr.children[i]
        curr.children[word[-1]] = TrieNode()
        curr.children[word[-1]].endOfWord = True
        
    def search(self,word):
        curr = self.root
        for i in word:
            if i not in curr.children:
                return "Not Present"
            curr = curr.children[i]
        if word[-1] not in curr.children:
            return "Absent"
        curr = curr.children[word[-1]]
        if curr.endOfWord ==True:
            return "Present"
        return "Absent"
    def delete(self,word):
        curr = self.root
        st = []
        for i in word:
            if i not in curr.children:
                return "Not Present"
            st.append(curr)
            curr = curr.children[i]
        curr = curr.children[word[-1]]
        st.append(curr)
        i = len(st)-1
        while i>=0:
            if st[i].children=={}:
                st.pop(-1)
                i-=1
            else:
                break
            if len(st)>0:
                st[-1].children.pop(word[i])
            i-=1
        
            
                

if __name__=="__main__":
    trie = Operations()
    keys = ["the","a","there","anaswe","any","by","their"]
    
    for i in keys:
        trie.insert(i)
    for i in keys:
        print(trie.search(i))
    print(trie.search("th"))
    trie.delete("their")
    print(trie.search("their"))
    print(trie.search("there"))

    