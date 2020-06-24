def search(string, index):
    return string[index]


print(search("hello", 4))


def concatenation(string1, string2):
    return string1 + " " + string2


print(concatenation("hello", "world"))


def split(string):
    j = 0
    split_lst = []
    for i in range(len(string)):
        if string[i] == " ":
            split_lst.append(string[j:i])
            j = i+1
    split_lst.append(string[j:])
    return split_lst


print(split("hello world goodbye world"))


def split_at_index(string, index):
    split_lst = []
    split_lst.append(string[:index+1])
    split_lst.append(string[index+1:])
    return split_lst


print(split_at_index("hello world", 3))


def insert(index, string1, string2):
    split_string = split_at_index(string1, index)
    return concatenation(concatenation(split_string[0], string2), split_string[1])


print(insert(4, "hello goodbye", "world"))


def deletion(string, index1, index2):
    return string[:index1+1] + string[index2:]


print(deletion("hello goodbye world", 5, 14))
