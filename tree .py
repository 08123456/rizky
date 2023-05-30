#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import QueueLinkedList as queue


# In[ ]:


class AVLNode:
    def__init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.heigth = 1


# In[ ]:


def preOrderTRaversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightChild)
    
def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
    
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isempty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.vaue.leftChild)
            if root.value.right is not None:
                customQueue.enqueue(root.value.rightChild)
                
                
def searchNode(rootNode, nodevalue):
    if rootNode.data == nodeValue:
        print("The Value is found")
        elif nodeValue < rootNode.data:
            if rootNode.leftChild.data == nodeValue:
                print("The value is found")
            else:
                searchNode(rootNode.leftChild, nodeValue)
                
            else:
                if rootNode.rightChild.data == nodevalue:
                    print("The value is found")
                else:
                    searchNode(rootNode.rightChild, nodeValue)
                    
def getHeight(rootNode):
    if not rootNode:
        return 0 
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot


def getbalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue)

                    
        

