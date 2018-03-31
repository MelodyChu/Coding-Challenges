# def gradingStudents(grades):
    
#     new_grades = []
    
#     for i in range(1,len(grades)):
#         if grades[i] < 38:
#             new_grades.append(grades[i])
#         else: # 43 should go to 45
#             if grades[i] % 5 == 0:
#                 new_grades.append(grades[i])
#             elif (5*(int(grades[i] / 5) + 1)) - grades[i] < 3:
#                 new_grades.append(5*(int(grades[i]/5) + 1))
#             else:
#                 new_grades.append(grades[i])
                
#     for grade in new_grades:
#         print (grade)



# print gradingStudents([4, 73, 67, 38, 33])

from __future__ import print_function

import os
import sys

def gradingStudents(grades):

    
    new_grades = []
    
    for i in range(1,len(grades)):
        if grades[i] < 38:
            new_grades.append(grades[i])
        else: # 43 should go to 45
            if grades[i] % 5 == 0:
                new_grades.append(grades[i])
            elif (5*(int(grades[i] / 5) + 1)) - grades[i] < 3:
                new_grades.append(5*(int(grades[i]/5) + 1))
            else:
                new_grades.append(grades[i])
                
    for grade in new_grades:
        print (grade)
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
