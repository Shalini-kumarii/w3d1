#1
def countdown(num):
    countlist=[]
    for x in range(num,0,-1):
        countlist.append(x)
    return countlist

value = countdown(5)
print(value)

#2

def print_and_return(numlist):
    print(numlist[0])
    return numlist[1]

value= print_and_return([1,2])
print(value)

#3
def first_plus_length(numlist):
    listlength=len(numlist)
    sum = listlength+numlist[0]
    return sum

returnsum= first_plus_length([1,2,3,4,5])
print(returnsum)

#4
def values_greater_than_second(numlist):
    temp= numlist[1]
    newlist=[]
    for x in range(len(numlist)):
        if temp < numlist[x]:
            newlist.append(numlist[x])
    return newlist

returnlist = values_greater_than_second([5,2,3,2,1,4])
print(returnlist)

#5
def length_and_value(size,value):
    listval =[]
    for x in range(size):
        listval.append(value)
    return listval

returnvalue = length_and_value(4,7)
print(returnvalue)