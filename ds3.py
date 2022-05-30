class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    def PrintLinkedList(self):
        if self.head is None:
            print("Your LinkedList is Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref
    def addBegin(self,data):
        newNode=Node(data)
        newNode.ref=self.head
        self.head=newNode
    def addEnd(self,data):
            newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newNode




ll1=LinkedList()
ll1.addBegin(10)
ll1.addBegin(20)
ll1.addBegin(30)
print(ll1.head)
ll1.PrintLinkedList()