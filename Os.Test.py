oldlist = [[],[],[],[],[],[]]
newlist = []

def base(resp): #used as the base for input from the user
    z = 0
    if resp == "A": #resp is response
        template = 'NewFile.txt'
    elif resp == 'B':
        template = 'Test_Picture.txt'
    # Old picture, used for template.
    with open(template, 'r') as f:
        for line in f:
            z = z + 1
            print(line, end='')
            oldlist[z-1].append(line)
    print(' \n')
    #This section of code is used to slice the words in each columm up to their characters
    for x in range(len(oldlist)):
        y = oldlist[x][0]
        list_of_letters = list(y)
        newlist.append(list_of_letters)

#print(newlist)
text = str(input("Would you rather want a new template(A) to begin with or would you like to use an already existing template(B)? "))
base(text)
#This prints out the changed picture
for i in range(len(newlist)):
    for j in range(len(newlist[i])):
        print(newlist[i][j], end='')


  
