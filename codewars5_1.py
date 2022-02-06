#implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

#[]                                -->  "no one likes this"
#["Peter"]                         -->  "Peter likes this"
#["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
#["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
#["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

list1=['Alex', 'Jacob', 'Mark', 'Max']
answr=''
if len(list1) == 0:
    answr = 'no one likes this'

print(len(list1))

for i in range(len(list1)):
    if i==0:
        answr = answr +  list1[i]
    elif len(list1)==2 and i==1:
        answr = answr + ' and ' + list1[i]
    elif len(list1)>2 and i==1:
        answr = answr + ', ' + list1[i]
    elif len(list1) ==3 and i == 2:
        answr = answr + ' and ' + list1[i]
    elif len(list1) > 3 and i == 2:
        answr = answr + ' and ' + str(len(list1)-2)+ ' others'

if len(list1)>1:
    answr=answr+ ' like this'
else:
    answr = answr + ' likes this'

print (answr)
