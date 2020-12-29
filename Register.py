number = int(input("Enter how many students are registering: "))
ofile = open('idNum', 'w+') #writing the user input to the file
for students in range(number): # the number of students entered in line 1
  idNum = int(input("Enter ID Numbers : "))
  ofile.write("idNum")# write   idNum to ofile 
ofile.close()#close file ""