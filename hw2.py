class Homework2:
    def get_students_taking_all_courses(self,students_courses, all_courses):
        names = []
        count = []
        students = []
        course_count = len(all_courses)
        for i in range(len(students_courses)):
            if students_courses[i][0] in names:
                count[names.index(students_courses[i][0])] += 1
            else:
                names.append(students_courses[i][0])
                count.append(1)

        for i in range(len(names)):
            if count[i] == course_count:
                students.append(names[i])

        return students
        #return the list of students
        

# For testing your code uncomment below lines.

# students_courses = [('Alice', 'Math'), ('Bob', 'Math'), ('Bob', 'Physics'),('Alice', 'Physics'), ('Charlie', 'Physics')]
# all_courses = ['Math', 'Physics']

# l=Homework2()
# result = l.get_students_taking_all_courses(students_courses, all_courses)
# print(result)

# Comment or delete the above test code before submitting.