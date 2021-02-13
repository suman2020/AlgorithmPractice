# Dictionary
# it is a collection which is unordered, changeable and indexed


"""Creation of Dictionary in python"""
myDict = dict()
secondDict = { }

myDict = {1:'one',2:'dos',3:'tres',4:'quadro'}
print(myDict)
print(myDict[4])

# time complexity for excesssing element of an dictionary is O(1)

"""
Dictionary in memory:
    Python dictonaries are implemented using hash table. It is an array whose index is obtained by passing keys into the hash functions. 
    A hash table is a way of doing key-value lookups. the key value pair is stored as an element of the array and index is determined by using ha
    hash function. 
    
    key --> hashFunction(key) --> gives index 
    
    engtoSpan = {'one':'uno','two':'des','three':'tres'}
    in the memory it is stored as:
    one -->hash() --> index = 1
    two -->hash() --> index = 3
    index   value    
    0
    1       one|uno
    2
    3       two|des
    4
    there might be  a situation where the hash function might point to the same index:
    three --> hash() --> index = 1 , in such cases collison happpens. so the element are added in the form of linkedlist 
    
    1      one|uno ---->  three|tres
    

"""
"""
Inserting and updating an element in a Dictionary
"""
mfd = {'name':'Suman','age':34}
mfd['age'] = 38
print(mfd['age'])
# adding a new element
mfd['wiffe'] = 'Albina'
print(mfd)

# time complexity of insertion of element = O(1) and space complexity is : amortized O(1)

"""
Traversing through a dictionary:
"""
def traverseDict(mfd):
    # traversing through keys
    for key in mfd: # can also be written as mfd.keys()
        print(key)
    # traversing through values
    for values in mfd.values():
        print(values)
    # traversing through pairs

    for key, value in mfd.items():
        print(key, value)
        """
        can also be written as:
        for pairs in mfd.items():
        print(pairs[0],pairs[1])
        """

traverseDict(mfd)

# time complexity is: O(n)  and space complexity is: 0(1) cause we are not adding or using any space in the memory.
"""
Searching for an element in the dictionary
"""
def searchDict(dict, value):
    for key in dict.keys():
        if dict[key]==value:
            return key,value  # returns tuple
            # return [key, value] ---> returns list
            # return key      --> return str

    return "Value not found"

suman = searchDict(mfd,'Albina')
print(type(suman))
# if the value is same for two different keys, then while retruning its gonna return the first key
# time complexity is: O(n) and space complexity is: O(1)