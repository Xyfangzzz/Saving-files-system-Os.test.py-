#line 28 is giving out an error saying list is out of index. reread the code and fix that.
import os
import re
oldlist = [[],[],[],[],[],[]]
newlist = []
newtemplate = ''
template = ''
with open('template.txt', 'r') as rl:
            for line in rl:
                template = line
print(line)



def newfilecopy(newtemplate):
    os.chdir('C:/Users/katom/Downloads/Python2/Save_Files')
    z = 0
    y = 0
    list_of_letters = '0'
    with open('Newfile0.txt', 'r') as rf:
        with open(newtemplate, 'w') as wf:
            for line in rf:
                wf.write(line)
                z = z + 1
                oldlist[z-1].append(line)

    print(os.listdir())
    print(oldlist)
    for x in range(len(oldlist)): # for loop used to cut the txt docuemnt into lines that we can even cut furthur to control each indivual character.
            y = oldlist[x][0]
            list_of_letters = list(y)
            newlist.append(list_of_letters) # Line of code connects to lines 46-49
        
def base(resp): #used as the base for input from the user
    os.chdir('C:/Users/katom/Downloads/Python2/Save_Files')
    numberfinder = re.compile(r'(Newfile)(\d|\d\d|\d\d\d)(.txt)')
    global template
    dir = os.listdir()
    temp = ''
    z = 0
    newtemp = ''
    x = 0
    foundnumber = numberfinder.search(dir[x])
    if resp == "A": #resp is response to answer
        for x in range(len(dir)):
            # lines ## - ## is expermental code for  when template index is the certain file type, but the file has not been found, due to removance, name changed, etc, 
            # temp means temporary
            if template == dir[x]:
                print(dir[x])
                temp = int(foundnumber.group(2)) + 1
                newtemplate = 'Newfile'+ str(temp) + '.txt'
                newfilecopy(newtemplate)
                os.chdir('C:/Users/katom/Downloads/Python2') 
                with open('template.txt', 'w') as wf:
                    wf.write(newtemplate)
                print(newtemplate)
            if temp == 10:
                    print("10 is the limit. pls rewrite or delete the previous files/filename.")
            elif resp == 'B':
                print("Choose from the list:")
                for file in range(len(dir)):
                    print(dir[file], end = ' ')
    
                

            
    
    
    
    
    # Old picture, used for template.
    #This prints out the changed picture
    for i in range(len(newlist)):
        for j in range(len(newlist[i])):
            print(newlist[i][j], end='')

          
    print(' \n')


<<<<<<< HEAD
#print(newlist)
#This prints out the changed picture
for i in range(len(newlist)):
    for j in range(len(newlist[i])):
        print(newlist[i][j], end='')
=======
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#print(newlist)
text = str(input("Would you rather want a new template(A) to begin with or would you like to use an already existing template(B)? "))
base(text)

>>>>>>> test



  
