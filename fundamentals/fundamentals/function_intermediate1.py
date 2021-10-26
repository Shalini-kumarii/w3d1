#1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)
students[0]['last_name']='Bryant'
print(students)
sports_directory['soccer'][0]='Andres'
print(sports_directory)
z[0]['y']=30
print(z)

#2
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(listkeyvalue):
    for x in range(len(listkeyvalue)):
        for key,value in listkeyvalue[x].items():
            print(f"{key} - {value}")
    
iterateDictionary(students) 

#3
def iterateDictionary2(key_name, some_list):
    sortedlist=[]
    for x in range(len(some_list)):
        for key,value in some_list[x].items():
            if key_name == key:
                sortedlist.append(value)
    for y in range(len(sortedlist)):
        print(sortedlist[y])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict_list):
    for key,value in dict_list.items():
        print("")
        print(f"{len(value)} {key}")
        for x in range(len(value)):
            print(value[x])

printInfo(dojo)

