f = open('DOB.txt', 'r')
name = f"Name \n "
dob = f"Date Of Birth \n"
print("\nDOB 2: ")
for line in f:
  string = line.split()
  name += f"{string[0]} {string[1]} \n" 
  dob += f"{string[2]} {string[3]} {string[4]} \n" 
print(name)
print(dob)
                         


                