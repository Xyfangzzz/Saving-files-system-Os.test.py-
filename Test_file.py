listnumber = 2
list1 = [0,1,2]
z = 0
print(list1)
print(listnumber-1)
for x in list1:
   if listnumber != list1[x]:
      print('hello')
      z = z + 1
      if (listnumber - 1) == list1[x]:
         print(listnumber, list1[x])
         list1.append(listnumber)
         break
   if listnumber == list1[x]:
         list1.append(x+1)
         print(list1[x])
         z = z + 1
listnumber = list1[z]

#print(z)
print(list1)
print(listnumber)



#import os #we'll use the os module to search if we have a type of file. If if a filename is already made, then it should make a copy of the file but with a number added to it.
#import re
#newtextfile = 'Newfile1.txt'
#numberfinder = re.compile(r'(Newfile)(\d|\d\d|\d\d\d)(.txt)')  #used to find the number of the copy of the file
#temp = ''
#print(newtextfile[0])
#print(os.listdir())
#os.chdir('C:/Users/katom/Downloads/Python2/Save_Files')
#print(os.getcwd())
#print(os.listdir())
#dir = os.listdir()
#for x in range(len(dir)):
 #   if newtextfile == dir[x]:
  #      foundnumber = numberfinder.search(dir[x])
   #     temp = int(foundnumber.group(2)) + 1
    #    newtextfile = 'Newfile'+ str(temp) + '.txt'
     #   if temp == 10:
      #      print("10 is the limit. pls rewrite or delete the previous files/filename.")
            
        
   

#with open('Newfile1.txt', 'r') as rf:
 #   with open(newtextfile, 'w') as wf:
  #      for line in rf:
   #         wf.write(line)

#print(os.listdir())


# Test Code for changing the indivisual character
#names = [['ilovebabies'],['ihatebabies']]
#newlist = []
#for x in range(len(names)):
 #   y = names[x][0]
  #  list_of_letters = list(y)
   # newlist.append(list_of_letters)

#print(newlist)
#newlist[0][0] = 'm'
#print(newlist)