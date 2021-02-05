listA = [1,2,3,4,5,6,7,8]

class Node:
    def __init__(self, currentVal = None , cNodeNext = None):
        self.currentVal = currentVal
        self.cNodeNext = cNodeNext
head = Node(listA[0])
#1->None

for value in listA[1:]:
    newNode = Node(value)
    currentNode = head
    while currentNode.cNodeNext!=None:
        currentNode= currentNode.cNodeNext
    currentNode.cNodeNext = newNode

temp = head
while head:
    head.currentVal = 1
    head = head.cNodeNext
#while head:
 #   head.currentVal = 1
  #  head = head.cNodeNext

while temp:
    print(temp.currentVal)
    temp = temp.cNodeNext
# 1-> None
# 1->None    |||||||| 2->None
# currentNode = 1->2->None

