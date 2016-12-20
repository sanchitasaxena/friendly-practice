# you traverse the tree by checking if the tree exists

################################################################################
class BinaryTree(object):

    def __init__(self,rootObj):

        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):

        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):

        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key
################################################################################

# externally implementing it is better because you'll be wanting to do something
# while traversing rather than having the method built in

#preorder - visit the root node first, the left subtree, then right
def preorder(tree):
    if tree:
        print tree.getRootVal()
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

#postorder - visit the left subtree, the right subtree, then root node
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print tree.getRootVal()

#postorder - visit the left subtree, the root node, then right subtree
def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print tree.getRootVal()
        inorder(tree.getRightChild())





















