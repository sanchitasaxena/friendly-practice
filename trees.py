# using a list of lists to implement a tree
# root node - 1st element
# left subtree - 2nd element
# right subtree - 3rd element
def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,newBranch):
    t = root.pop(1)
    # if the left subTree has a left child, we make it the new left
    # child - installing the old left child the left child of the new one
    # new node at any position 
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        # index 2 is the right side of the tree
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root
# get the root
def getRootVal(root):
    return root[0]
# chage the root value
def setRootVal(root, newVal):
   root[0] = newVal

def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]