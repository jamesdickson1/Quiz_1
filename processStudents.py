''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv

# create a file object to open the file in read mode

infile = open("students.csv",'r')

# create a csv object from the file object

outfile = open("processedStudents.csv",'a')

#skip the header row

next(infile)

#create an outfile object for the pocessed record

stufile = csv.reader(infile, delimiter=",")

#create a new dictionary named 'student_dict'

student_dict = {}

#use a loop to iterate through each row of the file

for i in stufile:
    #check if the GPA is below 3.0. If so, write the record to the outfile
    if float(i[8]) < 3.0:
        outfile.write(i[0] + "," + i[2] + "," + i[3] + "," + i[6] + ',' + i[7] + "," + i[8] + "\n")
        
        student_dict.update({i[0]:i[8]})

        
    


    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA
    





#print the entire dictionary
print(student_dict)

#Print the student id 

print(student_dict["124567890"])

#print out the corresponding GPA from the dictionary


#close the outfile

outfile.close()







