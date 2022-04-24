names = [['ilovebabies'],['ihatebabies']]
newlist = []
for x in range(len(names)):
    y = names[x][0]
    list_of_letters = list(y)
    newlist.append(list_of_letters)

print(newlist)
newlist[0][0] = 'm'
print(newlist)