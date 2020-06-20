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
            self.weight = len(data) + 1
            self.parent = parent
            if data == "":
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
        if node.weight < i and node.right != None:
            return self.search(node.right, i-node.weight)
        elif node.left != None:
            return self.search(node.left, i)
        return node.data[i]

    def searchnode(self, node, i):
        if node.weight == i:
            return (node)
        else:
            if node.weight < i and node.right != None:
                return self.searchnode(node.right, i-node.weight)
            elif node.left != None:
                return self.searchnode(node.left, i)

    def concatenation(self, newrope, length, node1, node2):

        self.left = node1
        self.right = node2
        self.weight = length
        # self.current = self
        return self

    # def splitnode(self, node, splitindex: int):
    #     datar = node.data.split()
    #     newnode1 = Rope(datar[:splitindex])
    #     newnode2 = Rope(datar[splitindex:])
    #     print(newnode1.data)

    # def split(self, rootnode, index):
    #     target = searchnode(rootnode, index)
    #     # case01
    #     if target.p == None:
    #         return target.left, target.right
    #     if target.p != None:

    #         right_tree = Rope()


s = "Hi we are friends"
s_split = s.split()
r = Rope(s_split)
s2 = "okay thats great"
s2_split = s2.split()
r2 = Rope(s2_split)
print(s_split, s2_split)
print(r.search(r.current, 3))
# print(r2.search(r2.current, 2))
newrope = Rope()
len_left = len(s)-len(s_split) + 1
newrope = newrope.concatenation(newrope, len_left, r, r2)
print(newrope.search(newrope.current, 19))
