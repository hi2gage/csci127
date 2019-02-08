# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Gage Halverson
# Last Modified: January 25, 2019 
# ---------------------------------------
# Asks for how many credits being taken then uses a
# while loop to ask for the grade and how
# many credits that grade is worth. It then calls
# translate to translate the letter grade to
# to integer value. A list for grades and
# credits is built then once the loop is over
# A dot product fuction is called to multiple the
# grade and credit values together. That is then
# divied by the sum of the credits list and
# displayed as calulated GPA
# ---------------------------------------
import sys

#dot product fuction
def dot(v1, v2):
    return sum(x*y for x,y in zip(v1,v2))

def translate(grade):
#Dictionary of weights
    dic_weights = {
# Uppercase Keys
        "A": 4,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "F": 0,
# Lowercase Keys
        "a": 4,
        "a-": 3.7,
        "b+": 3.3,
        "b": 3.0,
        "b-": 2.7,
        "c+": 2.3,
        "c": 2.0,
        "c-": 1.7,
        "d+": 1.3,
        "d": 1.0,
        "f": 0
        }
#returns the integer value for string verison of the grade
    return dic_weights[grade]

def main():    
#Lists of grades and weights
    grades = []
    weights = []
    
#prompts User for # of Classes taken
    number_classes = int(input("Enter the number of courses you are taking:"))
    i = 0

#Loops through and asks weight and grades for the # of classes taken and inserts it into 2 lists
    i = 1
    while i <= number_classes:

        grade_str = input("Enter grade for course " + str(i) +":")
        
        grade_int = translate(grade_str)
        grades.insert(i, grade_int)

        weight = int(input("Enter credits for course " + str(i) +":"))
        weights.insert(i, weight)

        print()
        i += 1
#Calls Dot product function then divides by the sum of weights 
    gpa = dot(weights, grades)/sum(weights)
    print(format(gpa, '.2f'))

    
main()

