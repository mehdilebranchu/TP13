class node:
    def __init__(self,a,b,c):
        self.__val = a
        self.__right = b
        self.__left = c
    def getVal(self):
        return self.__val
    def getRight(self):
        return self.__right
    def getLeft(self):
        return self.__left
    def setRight(self,a):
        self.__right = a
    def setLeft(self,a):
        self.__left = a


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

    print(n1.getLeft())
