class Rope(object):

    def __init__(self, data=''):
        #checks if input is a string
        if isinstance(data, list):
            if len(data) == 0:
                self.__init__()
            elif len(data) == 1:
                self.__init__(data[0])
            else:
                # Round-up division (to match rope arithmetic associativity)
                idiv = len(data) // 2 + (len(data) % 2 > 0)
                self.left = Rope(data[:idiv])
                self.right = Rope(data[idiv:])
                self.data = ''
                self.length = self.left.length     
        elif isinstance(data, str):
            self.left = None
            self.right = None
            self.data = data
            self.length = len(data)   
        else:
            raise TypeError('Only strings are currently supported')
        # Word iteration
        self.current = self

    #checks if tree is balanced
    def __eq__(self, other):
        if (self.left and self.right) and (other.left and other.right):
            return self.left == other.left and self.right == other.right
        elif (self.left and self.right) or (other.left and other.right):
            return False
        else:
            return self.data == other.data

    #returns the length of the string
    def __len__(self):
        if self.left and self.right:
            return len(self.left.data) + len(self.right.data)
        else:
            return(len(self.data))

    def search(self,node,i):
        if node.weight<i and node.right!=None:
            return search(node.right,i-node.weight)
        elif node.left!=None:
            return search(node.left,i)
        return node.value[i]

