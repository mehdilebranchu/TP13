def printValues(self):
        print(self.__root.getVal())
        self.__root.getLeft()
        if self.__root.getRight() == None and self.__root.getLeft() == None:
            return
        if self.__root.getLeft() != None :
            print(self.__root.getLeft().getVal())
        b = binaryTree(self.__root.getRight())
        return b.printValues()
