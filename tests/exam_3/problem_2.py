import numpy as np
# -------------------------------
class Course:
    def __init__(self, rubric, number):
        self.rubric = rubric
        self.number = number

    def __str__(self):
        return self.rubric + " " + str(self.number)

class Course_Schedule:
    def __init__(self, num_classes):
        self.num_classes = num_classes
        self.courses = np.ndarray(num_classes, dtype=Course)
        self.counter = 0

    def add(self, course):
        self.courses[self.counter] = course
        self.counter += 1
    def __str__(self):
        result = "My schedule\n"
        result += "-------\n"
        for courses in self.courses:
            result += str(courses) + "\n"
        return result
# -------------------------------
def main():
    my_courses = Course_Schedule(3)
    course_1 = Course("CSCI", 127)
    my_courses.add(course_1)
    course_2 = Course("M", 171)
    my_courses.add(course_2)
    course_3 = Course("WRIT", 101)
    my_courses.add(course_3)
    print(my_courses)
# -------------------------------
main()
