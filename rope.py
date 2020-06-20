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
            self.data = data+' '
            self.weight = len(data)
            self.parent = parent
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
        if node.weight < i and node.right != None:
            return self.search(node.right, i-node.weight)
        elif node.left != None:
            return self.search(node.left, i)
        return node.data[i]

    def searchnode(self, node, i):
        # if node.weight == i:
        #     return node
        # else:
        if node.weight < i and node.right != None:
            return self.searchnode(node.right, i-node.weight)
        elif node.left != None:
            return self.searchnode(node.left, i)
        return node, i

    def concatenation(self, newrope, length, node1, node2):

        self.left = node1
        self.right = node2
        self.weight = length

        return self

    def printrope(self, rootnode):
        if (rootnode.right == None and rootnode.left == None):
            if rootnode.data != None:
                print(rootnode.data)
        elif rootnode.left == None:
            self.printrope(rootnode.right)
        elif rootnode.right == None:
            self.printrope(rootnode.left)
        else:
            self.printrope(rootnode.left)
            self.printrope(rootnode.right)

    def splitnode(self, node, splitindex: int):
        datar = node.data
        newnode1 = Rope(datar[:splitindex])
        newnode2 = Rope(datar[splitindex:])
        return newnode1, newnode2

    def split(self, rootnode, index):
        target, i = self.searchnode(rootnode, index)
        if target.parent == None:
            # split node at specific index
            return self.splitnode(target, i)
        elif target.parent != None:
            # split node
            if i != 0:
                split1, split2 = self.splitnode(target, i)
                target.left = split1
                target.right = split2
                target.weight = len(split1.data)
                rightnode = target.right
                target.right = None
                target.parent.weight -= len(rightnode.data)

            # remove link between right leaf and target


phrase = "This code is by Aaron."
phrase2 = "This code is by Umme."
array_phrase = phrase.split()
array_phrase2 = phrase2.split()
rope = Rope(array_phrase)
rope2 = Rope(array_phrase2)
# newrope = Rope()
# length_left = len(phrase)-len(array_phrase)+1
# r = newrope.concatenation(newrope.current, length_left, rope, rope2)
# print(r.search(r.current, 32)
somenode = rope2.searchnode(rope2.current, 6)
# print(somenode)
# rope.printrope(rope.current)
# print(rope.search(rope.current, 7))
# rope2.split(rope2.current, 4)
phrase3 = "yes"
phrase3 = phrase3.split()
rope3 = Rope(phrase3)
#rope3.split(rope3, 2)
rope2.split(rope2.current, 3)
