
"""INTERVIEW PRACTICE QUESTIONS
1. How to find the missing number in an interger array of 1 to 100 ?
hint: sum of n elements = 1+2+3+4+5+..... = n(n+1)/2
in our case let us suppose that we have a list of elements from 1 to 100 and there is a missing number 67


""""""
myList = [1,2,3,..............,99,100] # we have a missing number 67f
# we first find the sum of 100 elements in series
sum = 100(100+1)/2 -> we took n = 100
sum2 = sum(myList) -> gives the sum of 99 elements in our list
diff = sum-sum2  # difference gives the missing element in the list

// -> used for integer output
/ -> used for double/float output
"""
sum1 = (100 * 101 )/2
sum2 = 43
diff = sum2 - sum1
print(diff)

"""
2. Write a program to find all pairs of integers whose sum is equal to a given number
--> Does array contain only positive or negative numbers?
--> What if the same pair repeats twice, should we print it every time?
--> If the reverse of the pair is acceptable e.g. can we print both (4,1) and (1,4) if the given sum is 5
--> Do we need to print only distint pairs? Does (3,3) is a vaild pair forgiven sum of 6?
--> How big is the array?

"""
def findPirs(nums, target):
    pair = list()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if [nums[i],nums[j]] in pair: # we don't want any repeated pairs
                continue
            if nums[i] + nums[j] == target:
                pair.append([nums[i],nums[j]])
                print([nums[i],nums[j]])



list1 = [2,6,3,9,11,23,12,2,1,23,3,4,7,7,2]   # sum must be equal to 9
findPirs(list1, 9)


"""
3. How to check if an array contains a number in Python
    import numpy as np
    myArray = np.array([1,2,3,4,5,6,7])
    def findNumber(myArray,find_element):
        for i in range(len(myArrY)):
            if myArrY[i] == find_element:
                print(i)
                return True
        return False
"""
"""
4. Find the maximum product of two integers in the array where all elements are positive.
"""
import numpy as np

myArray = np.array([1,2,3,4,5,56,7,5,76,34,6,7,3,7,8,78])
maxP = 0

def maximumProduct(myArray, maxP):
    for i in range(len(myArray)):
        for j in range(i+1, len(myArray)):
            if  myArray[i] * myArray[j]>= maxP:
                maxP = myArray[i] * myArray[j]
                print([myArray[i],myArray[j]])


    return maxP
value = maximumProduct(myArray,maxP)
print(value)

"""
5. Implement an algorithm to determine if a list has all unique characters, using python lists
"""
myList = [1,2,3,4,5,5,65,667,78,78,4,23,45,767,8]


def Unique(myList):
    list2 = list()
    for i in myList:
        if i in list2:
            print(i)
            return False
        else:
            list2.append(i)
    return True

suman = Unique(myList)
print(suman)

"""
6. Given two strings decide if one is permutation of another
Permutation: all the possible combinations of a string. for exapmle : ABC BCA ACB and so on
"""
def Permuatation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1==list2:
        return True
    else:
        return False

listA = ['s','u','m','a','n']
listB = ['m','a','n','s','u']
stm = Permuatation(listA,listB)
print(stm)





def permuatation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        if str1 in str2:
            return True
        else:
            return False

    """
    can also be written as 
    list1 = sorted(str1) // sorts the string 1 and converts it into a list
    list2 = sorted(str2) // sorts the string 2 and converts it into a list
    if list1==list2:
        return True
        
    --> conversion of string to list
    list = list(str1.split("")
    
    """

str1 = 'suman'
str2 = 'mansu'

print(permuatation(str1,str2))


"""
7. Given an image represented by an N*N matrix write a method to rotate the image by 90 degrees

1 2 3                    7 4 1    
4 5 6     --------->     8 5 2   
7 8 9                    9 6 3 
"""
tDAr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(tDAr)

def rotateMatrix(tDAr):

    no_of_rows = len(tDAr)
    for layer in range(no_of_rows//2):
        first = layer # 0
        last = no_of_rows-layer-1 #2  # it indicates the now of times that particular layer runs in loop
        # to be clear according to the example we have one layer. SO in the first loop of that layer, element 1,3,7 and 9 are moved
        # in the second loop of that particuar layer, element 2, 6,8 and 4 are moved. So for complete rotation the first layer runs two times in a loop.
        for i in range(first, last): # 0 and 1 runs for two times
            # saving top element
            top = tDAr[layer][i]   # element 1 we didn't do tDar[i][layer]cause in the second loop we have to change the element at index [0][1]. So changing it to
            # [i][layer] gives [1][0] in the upcoming loop.
            # move left element to top
            tDAr[layer][i] = tDAr[-i-1][layer]   # element1 replaced by element 7 (-1 indiactes the last element/row or column)
            # similarly in this case also we didn't use tdar[-layer-1][i] because it gives [-1][1] in the second loop that i.e the element 8 instead of 4. so 2 is replaced
            # by 8 which we don't want
            # move bottom element to elft
            tDAr[-i-1][layer] = tDAr[-layer-1][-i-1]
            #move right to bottom
            tDAr[-layer-1][-i-1] = tDAr[i][-layer-1]
            # move to the right
            tDAr[i][-layer-1] = top


    return tDAr;

print(rotateMatrix(tDAr))
