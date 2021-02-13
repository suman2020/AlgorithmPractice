"""
Dictionary                                      List
______________________________________________________________
Unordered                                       Ordered
Access via keys                                 Access via index
Collection of key value pairs                   Collection of elements
Preffered when you have unique key values       preffered when you have ordered data
no duplicate members                            alloe duplicate members

"""



# Dictionary
# it is a collection which is unordered, changeable and indexed


"""Creation of Dictionary in python"""
myDict = dict()
secondDict = { }

myDict = {1:'one',2:'dos',3:'tres',4:'quadro',5:'quadro'}
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
# adding multiple elements
newLis = {'focus':'family','children':2,'siblings':'1'}
mfd.update(newLis)
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

"""
Delete/Remove an element from the dictionary
"""
# removing using pop() method that takes key as an parameter and this method returns the corresponding value
name = mfd.pop('wiffe')
print(name)
print(mfd)

# using popitem() method removes any random item in the dictionary and returns the key value pair in the form of tuple
items = mfd.popitem()
print(items, type(items))
print(mfd)

# using clear() method empties the dictionar
# mfd.clear()
# print(mfd)

# using del() method
del mfd['name']
print(mfd)
# del mfd #can delete the entire dictionary as well.
# print(mfd)

# time complexity is generally : O(1) but in some cases it might take longer time to delete so we hace time complexity as : amortized O(n) and space complexity O(1)

"""
Dictionary methods.
    1. clear() : removes the entire dictionary items ---> dictionary-name.clear()
    2. copy() : copy the elements of the dictionary ---> dictionary_name.copy()
    3. fromkeys(keys,value) : returns a dictionary with the specified keys and the specified value (None if value is not given)
    4. get(index,value): returns the value for the specified key
    5. items() : return a key-value tuple pair
    6. keys() : displays the list of all keys in the dictionary
    7. values() : displays the list of all the valuee
    8. popitem() : remove an arbitrary key-value pair in the dictionary
    9. setdefault(key,value): search for a value with the given key, if not found makes a new dictionary key-value pair
    10. pop(key): removes the element with the given index
    11. update(): takes dictionary or tuple as a parameter
 """
# copy()
copydict = mfd.copy()
copydict['name']= 'Simon'
print(copydict)
print(mfd)

# fromkeys()
x = ('key1','key2','key3')
z = ['keya','keyb','keyc']
y = 0
a = [1,2,3]
newDict1 = dict.fromkeys(x,y)
newDict2 = dict.fromkeys(z,a)
print(newDict1)
print(newDict2)


# get()
  # returns the value associated with the key. if the value is not found it returns null
val = copydict.get('name')
print(val)
print(copydict)

# if the address is not found it returns the value passed alongside it but that key value pair wont be added to the dictionary
val2 = copydict.get('address')
print(val2)  #---> None
print(copydict)

val3 = copydict.get('address','America')
print(val3) #---> America
print(copydict)


# setdefault() looks out for the value with the specified key, if key is not present it adds that key along with the passed value as a dictionary item
val3 =  copydict.setdefault('name')
print(val3) #--> 'Simon'
val4 = copydict.setdefault('address','America')
print(val4) #-->'America'
print(copydict)

"""
Dictionary operatons/ built in functions
1. in operator : returns boolean 
2. for operator: traverse through the dictionary
3. all() : returns true if all the values of the key-value pair is true and vice versa , returns true if the dict is empty
4. any() : returns true if either one value in the key-value pair is true, retunrs false if the dict in empty
5. len() : returns the number of pairs
6. sorted() : returns list of keys ,sorts on the basis of ascendig order unless reverse = true (sorts on descendig order)
"""

result = 'name' in copydict
result2 ='Simon' in copydict.values()  # ---> time complexity is O(1)
print(result)
print(result2)

dicta = {0:False,1:True,2:False}
print(all(dicta))
print(any(dicta))

print(len(dicta))
print(sorted(copydict))
print(sorted(copydict, reverse= True))
print(sorted(copydict,key = len))
