# Dictionary
# it is a collection which is unordered, changeable and indexed

# creating a dictionary

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