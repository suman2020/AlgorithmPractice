# # creating a list of elements
# listA = []
# listA.append(elementname)
#
# # converting a list of numbers to string
#
# list1 = map(str, listA) # first the numbers are converted to string
# desiredString = ''.join(list1)
#
# desiredString = ''.join(listA) # if the list consists of string elemenets
#
# # converting a binary number to string

listA = [1,2,3,4,5]
count = 0
for element in listA:
    for ele in listA[1:]:
        count+=1
        print('hello ',count)

