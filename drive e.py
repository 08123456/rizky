#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import QueueLinkedList as queue


# In[ ]:


class BTSNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        


# In[ ]:


def insertNode(rootNode, nodeValue):
    if rootNode.data == None
       rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootnode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
            
        else:
            if rootNode.rightChild None:
                rootNode.rightChild = BSTNode(nodeValue)
        return "The node has been successfully inserted"
    
def preOrder Traversal(rootNode):
    if not rootNode:
         return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rooNode.data)
    inOrderTraversal(rootNode.rightChild)
    
def levelOrderTraversal(rootNode):
    if not rootNode:

