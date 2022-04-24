oldlist = [[],[],[],[],[],[]]
newlist = []
z = 0
# Old picture, used for template.
with open('Test_Picture.txt', 'r') as f:
    
    for line in f:
        z = z + 1
        print(line, end='')
        oldlist[z-1].append(line)
print(' \n')

#print(oldlist)
#print(z)

#This section of code is used to slice the words in each columm up to their characters
for x in range(len(oldlist)):
    y = oldlist[x][0]
    list_of_letters = list(y)
    newlist.append(list_of_letters)

#print(newlist)

#This prints out the changed picture
for i in range(len(newlist)):
    for j in range(len(newlist[i])):
        print(newlist[i][j], end='')


  
