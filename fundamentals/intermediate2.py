#1
print('QUESTION 1')
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
print(students[0]['last_name'])

sports_directory['soccer'][0]='Andres'
print(sports_directory['soccer'][0])

z[0]['y']=30
print(z)

#2
print('QUESTION 2')
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def sportsDict(list):
    for i in range(0,len(list),1):
        print (list[i])
print(sportsDict(students))

#3
print('QUESTION 3')
def iterateDict(key_name, list):
    for i in range(0,len(list),1):
        print(list[i][key_name])
print(iterateDict('first_name', students))

def iterateDict2(key_name, list):
    for i in range(0,len(list),1):
        print(list[i][key_name])
print(iterateDict('last_name', students))

#4
print('QUESTION 4')
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}




def printInfo(some_dict):
    for key in some_dict:
        print('\n'+ str(len(some_dict[key])) + ' ' + key.upper())
        for i in some_dict[key]:
            print(i)

printInfo(dojo)   
