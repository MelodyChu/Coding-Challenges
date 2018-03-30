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



print gradingStudents([4, 73, 67, 38, 33])