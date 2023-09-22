import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------
# CSCI 127, Lab 12                                |
# Nov 29, 2022                                    |
# Alex Ellingsen                                  |
# -------------------------------------------------

def read_file(file_name):
    enroll = open(file_name, 'r')
    college_old_names = []
    college_old_enrollments = []
    next(enroll)
    for i in enroll:
        stats = i.split(',')
        college_name = stats[1]
        new_name = college_name.strip()
        college_old_names.append(new_name)
        college_enrollment = stats[0]
        college_old_enrollments.append(college_enrollment)
    college_names = np.asarray(college_old_names)
    college_enrollments = np.asarray(college_old_enrollments)
    college_tuple = (college_names, college_enrollments)
    return college_tuple
    

# -------------------------------------------------

def main(file_name):
    college_names, college_enrollments = read_file(file_name)
    int_enrollments = []
    for i in college_enrollments:
        int_enrollments.append(int(i))
    plt.ylim(0, 5000)
    plt.figure("MSU Enrollments")
    plt.title("Fall 2020")
    plt.xlabel("College")
    plt.ylabel("Enrollment")
    plt.bar(college_names, int_enrollments, color = ['gold', 'blue', 'gold', 'blue', 'gold', 'blue', 'gold'])
    
    

    plt.show()
    

# -------------------------------------------------

main("fall-2020.csv")
