def grading_students(grades):

    n = int(input('Please enter the total number of students: ')) #number of students

    grades = []  # an array for the former grades
    final_grades = []  # an array for the final grades
    grade= 0


    for x in range(n):

        #while 1<=n<=60 and 0<=grade<=100: # considering the constraints for number of students and grade value

        if n>60 or n<1: #The student number should be more than or equal to 1 and less than or equal to 60
            print('The student number should be more than or equal to 1 and less than or equal to 60')
            break #break if the student number is out of range

        if grade <0 or grade > 100: #The grade should be greater or equal to zero or less than or equal to 100
            print('The grade should be greater or equal to zero or less than or equal to 100')
            break#break if the grade number is out of range


        grade = int(input('Enter the students grade, one grade per line : ')) #grades for students
        grades.append(grade)

        if grade >= 38 and grade%5 >= 3: # if the grade is less than 38 or its remainder when divided by 5 is greater or equal to 3
            final_grade = grade + (5 - (grade%5))# the final grade is then added to the result of 5 minus the remainder
            final_grades.append(final_grade)  # adding the final grade to the array of final grades


        else:
            final_grade = grade  # final grade isn't modified
            final_grades.append(final_grade)




    print('These are the original grades: ' + str(grades))
    print('These are the final grades: ' + str(final_grades))

grades = []
grading_students(grades)


