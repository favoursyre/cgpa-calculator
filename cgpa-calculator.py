#I want to create a CGPA calculator
import numpy as np

#name = input ("What's your name? ").title()

#this is to get how many sessions I would be calculating for

#session = input ("What's the session? (yyyy/yyyy) ")
sessionCGPA = []
grade = []
unit = []
sumgradeunit1 = []
sumgradeunit2 = []
sumunit1 = []
sumunit1 = []
totalunit1 = []
new = []
unitload = []

#this is to get how many semesters I would calculating for
semesterNum = int(input("How many semesters are you calculating for? "))
if semesterNum == 2:
    semester = ["First", "Second"]
else :
    semester = ["this"]

position = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th",  "15th"]

for semesters in range (semesterNum):
    print("\n")
    coursenum = int(input("How many courses did you offer in " + semester[semesters] + " semester? "))
    
    for steps in range (coursenum):
            #coursename = input("What's the name of the " + position[steps] + " course? ")
        courseunit = int(input("What's the unit load of " + position[steps] + " course? "))
        coursegrade = input("What's the grade of " + position[steps] + " course? " ).title()

        if coursegrade == "A":
            newcoursegrade = 5 
        elif coursegrade == "B":
            newcoursegrade = 4 
        elif coursegrade == "C":
            newcoursegrade = 3 
        elif coursegrade == "D":
            newcoursegrade = 2
        elif coursegrade == "E":
            newcoursegrade = 1
        elif coursegrade == "F":
            newcoursegrade = 0
    
        unit.append(courseunit) #this puts all the unitload of each course in a list
        grade.append(newcoursegrade) #this puts all the course grade of each course in a list
        coursegradeunit1 = [unit * grade for unit,grade in zip (unit, grade)] #this puts all the grade * units of each course in a list

        a = np.array(coursegradeunit1) #this puts all the grade * unit of each course in an array
        b = np.array(unit) #this puts all the unit of each course in an array
        if semesterNum == 2:
            lengthA = len(a) - coursenum
            lengthB = len(b) - coursenum
        else :
            lengthA = len(a)
            lengthB = len(b) 
    
        sumgradeunit1 = sum(a[:lengthA]) #this sums the grade * unit of the first semester
        sumgradeunit2 = sum(a[(coursenum-1):len(a)]) #this sums the grade * unit of the second semester
        sumunit1 = sum(b[:lengthB]) #this sums the unit of the first semester
        sumunit2 = sum(b[(coursenum-1):len(b)]) #this sums the unit of the second semester

if semesterNum == 2:
    gpa1 = sumgradeunit1 / sumunit1
    gpa2 = sumgradeunit2 / sumunit2
    Totalcgpa = (gpa1 + gpa2) / semesterNum
else :
    Totalcgpa = sumgradeunit1 / sumunit1
    

print("\n")
print("Your CGPA is ", Totalcgpa)
#print(sumunit2)



#print(eachgradeunit)
#print(eachunit)
       
