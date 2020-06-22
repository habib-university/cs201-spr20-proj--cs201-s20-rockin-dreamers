class Rope(object):
    def __init__(self, data='', parent=None):
        # checks if input is a string
        if isinstance(data, list):
            if len(data) == 0:
                self.__init__()
            elif len(data) == 1:
                self.__init__(data[0], parent=parent)
            else:
                self.current = self
                # Round-up division (to match rope arithmetic associativity)
                idiv = len(data) // 2 + (len(data) % 2 > 0)
                self.left = Rope(data[:idiv], parent=self.current)
                self.right = Rope(data[idiv:], parent=self.current)
                self.parent = parent
                self.data = ''
                self.weight = len(self.data.join(data[:idiv]))
        elif isinstance(data, str):
            self.left = None
            self.right = None
            self.data = data
            self.weight = len(data)
            self.parent=parent 
            self.current = self
        else:
            raise TypeError('Only strings are currently supported')
        # Word iteration

    # checks if tree is balanced
    # def __eq__(self, other):
    #     if (self.left and self.right) and (other.left and other.right):
    #         return self.left == other.left and self.right == other.right
    #     elif (self.left and self.right) or (other.left and other.right):
    #         return False
    #     else:
    #         return self.data == other.data

    # #returns the weight of the string
    # def __len__(self):
    #     if self.left and self.right:
    #         return len(self.left.data) + len(self.right.data)
    #     else:
    #         return(len(self.data))

    def search(self, node, i):
        if node.weight <= i and node.right != None:
            return self.search(node.right, i-node.weight)
        elif node.left != None:
            return self.search(node.left, i)
        return node.data[i]

    def searchnode(self, node, i):
        if node.weight <= i and node.right != None:
            return self.searchnode(node.right, i-node.weight)
        elif node.left != None:
            return self.searchnode(node.left, i)
        return node,i
#Issue: if i>len(rope): returns the rightmost leaf
        # if node.weight == i:
        #     return node
        # else:a
        #     if node.weight <= i and node.right != None:
        #         return self.searchnode(node.right, i-node.weight)
        #     elif node.left != None:
        #         return self.searchnode(node.left, i)
    def search_words(self,node, words):
        wordlist=words.split()
        index=[]
        for i in wordlist:
            n,s,e=self.search_word(node,i)
            index.append((s,e))
        return index

    def search_word(self, node, word):
        return_node=None
        s=0
        e=0
        if node.data=="":
            return_node,s,e=self.search_word(node.left, word)
            if return_node==None:
                return_node,s,e=self.search_word(node.right, word)
        elif node.data==word:
            t=node
            index_s=0
            while t.parent!=None:
                if t.parent.right==t:
                    index_s+=t.parent.weight
                t=t.parent
            index_e=index_s+len(node.data)
            return node,index_s,index_e
        return return_node,s,e


    def splits(self,root,i):
        node,t=self.searchnode(root,i)
        node0=Rope(node.data[0:t])
        node1=Rope(node.data[t:])
        node.data=''
        node.weight=len(node0.data)
        node.left=node0
        node.right=node1
        node0.parent=node
        node1.parent=node
        l2=self.split(root,i)
        l1=self.split(root,0)
        return l1,l2

    def nuke(self,node):
        if node.parent.right==node:
            node.parent.right=None
        elif node.parent.left==node:
            node.parent.left=None
            node.parent.weight=node.parent.weight-node.weight
        node.parent=None

    def split(self,root, i, limit=None):
        arr=[]
        node,t=self.searchnode(root,i)
        #Chops off the required strings
        while node!=None:
            arr.append(node.data)
            self.nuke(node)
            i=i+node.weight
            node,t=self.searchnode(root,i)
            if node.data=="":
                node=None
            if i==limit:
                node=None
        r=Rope(arr)
        return r
    
    # def balance(self,node):
    #     if node.left!=None:
    #         self.balance(node.left)
    #     if node.right!=None:
    #         self.balance(node.right)
    #     if node.left == None and node.right==None:
    #             self.nuke(node)
    #     elif node.left == None and node.right != None:
    #         node.parent.right=node.right
    #         node.right.parent=node.parent
    #     elif node.left != None and node.right == None:
    #         node.parent.left=node.left
    #         node.left.parent=node.parent
        
        
        

        




    def concatenation(self, newrope, length, node1, node2):
        self.left = node1
        self.right = node2
        self.weight = length
        # self.current = self
        return self


s = "Hi we are friends Anas Ali"
s_split = s.split()
r=Rope(s_split)
r1,r2=r.splits(r,5)
node=r2.search_words(r2,'Anas')
print(node)
