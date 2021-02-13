"""
Tuples:
a tuple is an immutable sequence of python objects
tuples are also comparable and hashable

"""
"""
Creating a tuple
"""
newTuple = ('a','b','c','p','e')
newTuple1 = ('a',) # if comma is not written, then it's just gonna return a string
newTuple2 = tuple('qweerrty')
print(newTuple)
print(newTuple1)
print(newTuple2)


"""
Location of tuples in memory:
    - elements are stored cotigouosly
    - can be indexed 
"""

"""
accessing elements of the tuple
"""
print(newTuple[::-1])
print(sorted(newTuple))

"""
traversing the elements in tuple: time complexity: O(n) and space complexity is 0(1)
"""
for element in newTuple:

    print(newTuple.index(element),element)


"""
searching elements in the tuple
"""
print('b' in newTuple)
print('fuck' in newTuple) #---> time complexity would be 0(1)

def searchElelment(newTuple, element):
    for i in newTuple:    #---> time complexity would be 0(n)
        if i==element:
            return True
    return False
print(searchElelment(newTuple,'c'))

"""
Tuple operatons and functions
"""
# concatenate multiple tuples
finalTuple = newTuple + newTuple2
print(finalTuple)

# star operation
print(finalTuple * 2) # multiplies the element of the tuple by the written value

#count method
  # counts the number of times the element is repeated
print(finalTuple.count('a'))
# index method
print(finalTuple.index('e'))

# len method
print(len(finalTuple))

# converting list to tuple
bitch = tuple([1,2,3,4,5,6])
print(bitch)


"""
Tuples vs Lists
Common functions: len(), max(), min(),sum(),any(),all(),sorted(), count(), index()
Methods that can't be applied on tuples: append(). insert(). remove(), pop(),clear(), sort(), reverse()
Tuples can be stored in lists
Lists can be stored in tuples

- We generally use tuples for heterogeneous(different) data types and lists for homogeneous (similar) data types
- iterating through a tuple is faster than with list
- tuples that contain immutable elements can be used as a key for a dictionary
- if we have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected 

"""
list1 = [(1,2),(9,0),(3,4)]
tuple1 = ([1,2],[3,4],[5,6])
tuple2 = ((1,2),(3,4),(5,6))
print(list1)
print(tuple1)
print(tuple2)

"""
Time and space complexity in python tuples
 Operations                           Time Complexity                 Space COmplexity
1. Creating a tuple\                    O(1)                           O(n) 
2. Traversing a given tuple             O(n)                           O(1)
3. Accessing a given element            O(1)                           O(1)
4. Searching a given element            O(n)                           O(1)
"""