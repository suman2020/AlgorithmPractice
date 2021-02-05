# listA = [1,2,3,4,5,6,7,8]
#
# class Node:
#     def __init__(self, currentVal = None , cNodeNext = None):
#         self.currentVal = currentVal
#         self.cNodeNext = cNodeNext
# head = Node(listA[0])
# #1->None
#
# for value in listA[1:]:
#     newNode = Node(value)
#     currentNode = head
#     while currentNode.cNodeNext!=None:
#         currentNode= currentNode.cNodeNext
#     currentNode.cNodeNext = newNode
#
# #temp = head
# # while temp:
# #     temp.currentVal = 1
# #     temp = temp.cNodeNext
# #while head:
#  #   head.currentVal = 1
#   #  head = head.cNodeNext
#
# while head:
#     print(head.currentVal)
#     head = head.cNodeNext
# # 1-> None
# # 1->None    |||||||| 2->None
# # currentNode = 1->2->None
#

# LinkedList
# Creating a Node class
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

#Creating a Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
# method to inset a new element in the beginning
    def insert_at_beginning(self, data):

        if self.head is None:
            self.head = Node(data)
            return
        newNode = Node(data,self.head)
        self.head = newNode

# insert a new node at the last
    def insert_at_end(self,data):
        NewNode = Node(data,None)
        if self.head is None:
            self.head = NewNode
            return
        itr = self.head

        while itr.next:
            itr = itr.next
        itr.next = NewNode
# method to insert multiple values i.e elements in a list
    def insert_list(self,list):
        # self.head = None
        for data in list:
            self.insert_at_end(data)
        """
        the above function can also be written as
    def insert_list(self,list):
        self.head = Node(list[0], None)

        for value in list[1:]:
            currentNode = Node(value)
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = currentNode
        """
 # method to print the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

        """
    def print_list(self):
        temp = self.head
        while temp.next:
            print(temp.data)
            temp = temp.next
            
    # these two functions above prints the same value
    # the difference is 
    in the second case: we iterated through the next node the current node points to
    # A->B->C->none   A has value 1, B has 2 and C has 3 
    # first iteration           # second iteration                # third iteration
    temp = A                     temp = B                          temp = C
    while loop runs              while loop runs                   loop doesnot run because temp.next or C->next is null
    prints 1                     prints 2                          loop ends
    temp = B                     temp = C                          print function prints the value in C node i.e 3
    
    In the first case: we iterated through the current nodes
    # A->B->C->none   A has value 1, B has 2 and C has 3 
    # first iteration           # second iteration                # third iteration
    temp = A                     temp = B                          temp = C
    while loop runs              while loop runs                   while loop runs
    prints 1                     prints 2                          prints 3
    temp = B                     temp = C                          temp = None After this the loop ends. But if we try to print after this
                                                                   it gives non type error
    
    
    
    
    
    
    """
# method to count the list
    def count_list(self):
        count = 0
        curr = self.head
        while curr:
            count+=1
            curr = curr.next
        return count
# method to reverse the linked list
    def reverse_list(self):
        previousNode = None
        currentNode = self.head
        while currentNode is not None:
            temp_currentNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = temp_currentNode
        self.head = previousNode

    def remove_node_withValue(self,value):
        currentNode = self.head

        while currentNode:
            if currentNode.data == 3:
                print('This node is to be removed')
                tempNode = previousNode
                previousNode= currentNode.next
                currentNode = tempNode
                currentNode.next = previousNode
                break;
            previousNode = currentNode
            currentNode = currentNode.next

    def remove_node_withIndex(self,index):
        currentNode = self.head
        count = 0
        if index == 0:
            self.head= self.head.next
        while currentNode:
            if count == index -1 :
                print("Removal with index given")
                currentNode.next = currentNode.next.next
                break;
            currentNode = currentNode.next
            count += count

    def insert_newNode_WithIndex(self, index, value):
        if index < 0 and index >=self.count_list():
            raise Exception('Invalid index')
        newNode = Node(value)
        if index ==0:
            newNode.next = self.head
            self.head = newNode.next
        else:
            currentNode = self.head
            count = 0
            while currentNode:

                if count == index:

                    newNode.next = currentNode
                    currentNode = previousNode
                    currentNode.next = newNode
                    break

                """
                 can also be written as 
                 if count == index-1:
                    
                    newNode.next = currentNode.next
                    currentNode.next =  newNode
                    break
                
                """
                count +=1
                previousNode = currentNode
                currentNode = currentNode.next

    def middleNode(self):
        node_storage = {}
        i = 0
        while self.head:
            node_storage[i] = self.head
            self.head = self.head.next
            i += 1
        target = int(i/2)
        for e in range(target,i):
            print(node_storage[e].data)





if __name__ == '__main__':
    list = [1,2,3,4,5,6,7,8,9,10]
    list1 = LinkedList()
    # list1.insert_at_end(5)
    # list1.insert_at_end(10)
    # list1.insert_at_end(15)
    list1.insert_at_beginning(12)
    list1.insert_at_beginning(13)
    list1.insert_list(list)
    print("Before reverse")
    list1.print_list()
    print("Count")
    print(list1.count_list())

    print("After Reverse")
    list1.reverse_list()
    list1.print_list()

    print("Removal of a node")
    list1.remove_node_withValue(2)

    list1.print_list()
    list1.remove_node_withIndex(1)
    list1.print_list()

    print("\nInsertion of a new node with index")
    list1.insert_newNode_WithIndex(3,59)
    list1.print_list()

    print("\nPrinting from the middle node")
    list1.middleNode()


