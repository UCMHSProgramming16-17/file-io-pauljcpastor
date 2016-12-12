file = open('mylist.txt', 'w') #open file

#TODO: add items to file
file.write('test\n')
file.write('test2')

file.write(input("What should I add to the list?"))
#close file
file.close()