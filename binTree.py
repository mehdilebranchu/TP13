from ex1 import *
class binaryTree:
    def __init__(self,r):
        self.__root = r
    def getRoot(self):
        return self.__root
    def isRoot(self,n):
        if n.getVal() == 12:
            return True
        else:
            return False
    def size(self,node):
        n = 1
        if node.getRight() == None :
            return n
        b = binaryTree(node.getRight())
        return n + b.size(node.getRight())
    def printValues(self):
        if self.getRoot().getRight() == None:
            return self.getRoot().getRight().printNode()
        b = binaryTree(self.getRoot().getRight())
        return b.printValues()


if __name__ == '__main__':
    n6 = node(6,None,None)
    n7 = node(21,None,None)
    n8 = node(18,None,None)
    n9 = node(3,None,None)
    n5 = node(4,None,n9)
    n4 = node(19,n7,n8)
    n3 = node(17,n4,None)
    n2 = node(5,n6,n5)
    n1 = node(12, n3, n2)
    b1 = binaryTree(n1)
    print(b1.isRoot(n2))
    print(b1.size(n1))
    b1.printValues()
