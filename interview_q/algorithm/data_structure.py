# Python 3
# coding:utf-8


class BasicTree(object):
    def __init__(self, root):
        self.root = root
        self.child = TreeRoom()
        self.father = None

    # def add_child(self, kid):
    #     pass

    # def __str__(self):
    #     return str(self.root)

    # def size(self):
    #     return len(self.child)+1

    def __repr__(self):
        return self.root


class Tree(BasicTree):
    def __init__(self, root):
        super().__init__(root)
        self.node = BasicTree(root)
        self.child = self.node.child

    def add_child(self, kid):
        kid_tree = BasicTree(kid)
        self.child.append(kid_tree)
        kid_tree.father = self.node

    def __str__(self):
        return ''


class TreeRoom(list):
    def __init__(self):
        super().__init__()
        self.room = []

    def __repr__(self):
        s = str(self.room[0])
        for x in self.room[1:]:
            s+= ' '+str(x)
        return s

    def append(self, tmp):
        self.room.append(tmp)

    def __len__(self):
        return len(self.room)


class BinaryTree(object):
    def __init__(self, root):
        self.room = [root]
        self.root = self.room[0]

    def add_child(self):
        pass


def main():
    t1 = Tree('a')
    t1.add_child('b')
    t1.add_child('c')
    print(len(t1.child))
    # print(t1.count)


if __name__ == "__main__":
    main()
