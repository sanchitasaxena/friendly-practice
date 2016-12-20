# object orientated implementation of a binary tree

class BinaryTree(object):

    # attributes
    def __init__(self,rootObj):

        #root sometimes called key
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        # simply adding node to tree if no left child
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        # left child exists, insert the node and push the existing child
        # to the next level of the tree
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):

        # simply adding node to tree if no right child
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        # left child exists, insert the node and push the existing child
        # to the next level of the tree
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            # to not accidentally over write something before you set it
            self.rightChild = t

    # methods for accessing
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    #setting roote value
    def setRootVal(self, obj):
        self.key = obj

    # get root value -- get's instance of binary tree
    # <__main__.BinaryTree object at 0x1005dea10>
    def getRootVal(self):
        return self.key
