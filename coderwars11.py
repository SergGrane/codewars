# This function should return a number (final grade). There are four types of final grades:
# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases


def final_grade (exam: int, projects: int):
    if exam > 90 or projects >10:
        return 100
    elif  75 < exam and 5 <= projects:
        return  90
    elif 50 < exam and 2 <= projects:
        return 75
    else:
        return 0

print(final_grade(55, 15))
