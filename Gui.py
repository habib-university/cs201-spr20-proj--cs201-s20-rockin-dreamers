from tkinter import *


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
            self.parent = parent
            self.current = self
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
        if node.weight <= i and node.right != None:
            return self.search(node.right, i-node.weight)
        elif node.left != None:
            return self.search(node.left, i)
        return node.data[i]

    def searchnode(self, node, i):
        if node.weight < i and node.right != None:
            return self.searchnode(node.right, i-node.weight)
        elif node.left != None:
            return self.searchnode(node.left, i)
        return node, i

    def search_word(self, node, word):
        return_node = None
        if node.data == "":
            return_node = self.search_word(node.left, word)
            if return_node == None:
                return_node = self.search_word(node.right, word)
        elif node.data == word:
            return node
        return return_node

    def concatenation(self, newrope, length, node1, node2):

        self.left = node1
        self.right = node2
        self.weight = length
        # self.current = self
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


app = Tk()

# Text Widget + Font Size
txt = Text(app, font=('Verdana', 8))
txt.pack()


def update_rope(newtxt):
    text = newtxt.get("1.0", "end")
    print(text)
    new_rope = Rope(text.split())
    final_rope = Rope()
    final_r = final_rope.concatenation(final_rope, length_text -
                                       split_len + 1, currentrope, new_rope)
    # Label1 = Label(next_window, text=text_in_textbox+text)
    # Label1.pack()
    print(final_r.search(final_r, 8))


def add_text():
    # newtxt = Text(newWindow, font=('Verdana', 8))
    # next_window
    next_window = Toplevel(app)
    newtxt = Text(next_window, font=('Verdana', 8))
    newtxt.pack()
    btn = Button(next_window, text='Update',
                 command=lambda: update_rope(newtxt))
    btn.pack()


def edit_window():
    # global newWindow
    newWindow = Toplevel(app)
    btn = Button(newWindow, text='Add', command=add_text)
    btn.pack()
    btn = Button(newWindow, text='Delete', command=getText)
    btn.pack()

# def getoptions():
#     btn = Button(app, text='Add', command=add_text)
#     btn.pack()
#     btn = Button(app, text='Delete', command=getText)
#     btn.pack()


def getText():
    global text_in_textbox
    text_in_textbox = txt.get("1.0", "end")

    global length_text
    length_text = len(text_in_textbox)
    global currentrope
    global split_len
    split_len = len(text_in_textbox.split())
    currentrope = Rope(text_in_textbox.split())
    print(text_in_textbox)
    # Label1 = Label(app, text=text_in_textbox)
    btn = Button(app, text=text_in_textbox, command=edit_window)
    btn.pack()
    # w = Label(master, text="Hello, world!")
    # Label1.pack()
    txt.delete(1.0, END)
    # return text_in_textbox


# Delete Button
btn = Button(app, text='Save Text', command=getText)
btn.pack()

# : txt.delete(1.0, END))
btn = Button(app, text='Edit Text', command=edit_window)
btn.pack()
btn = Button(app, text='New Text', command=lambda: txt.delete(1.0, END))
btn.pack()
app.mainloop()
