"""
            Student Management Information System
            -------------------------------------

This is the main file for the CASE STUDY Project of NCERT CS Class 11 and Class 12 TextBooks.
Additions are being made on basis of the prompts given at the end of each chapter.

Schools use “Student Management Information System” (SMIS) to manage student-related data. This system provides
facilities for:
• recording and maintaining personal details of students.
• maintaining marks scored in assessments and computing results of students.
• keeping track of student attendance.
• managing many other student-related data. Let us automate this process step by step.
"""

SchoolName = "IIT Bombay"

'''
Required Inputs:
    Roll No.
    Student Name
    Class
    Section
    Address
    City
    Pincode
    Parent/Guardian's Contact No.
'''
# Taking Input:
RollNo = input("Enter your roll number: ")
StudentName = input("Enter your name: ")
Class = int(input("Enter your class: "))
Section = input("Enter your section: ")
AddressLine1 = input("Enter the first line of your address: ")
AddressLine2 = input("Enter the second line of your address: ")
City = input("Enter your city: ")
Pincode = int(input("Enter your area's pincode: "))
PhoneNo = int(input("Enter your parent's/guardian's phone number: "))


# Approximate as \t is unpredictable.
def id_card(roll_no, name, student_class, student_section, address_line1, address_line2, city, pincode, phone_no):
    global SchoolName
    print("_____________________________________________________________________________")
    print("\t\t\t\t\t\t", SchoolName)
    print("Student Name: ", name, "\t\t\t\t\t\t", "Roll No: ", roll_no, sep="")
    print("Class: ", student_class, "\t\t\t\t\t\t\t\t\t", "Section: ", student_section, sep="")
    print("Address: ", address_line1, sep="")
    print("\t\t ", address_line2, sep="")
    print("City: ", city, "\t\t\t\t\t\t\t\t", "Pincode: ", pincode, sep="")
    print("Parent's/Guardian's Contact No:", phone_no)
    print("_____________________________________________________________________________")


id_card(RollNo, StudentName, Class, Section, AddressLine1, AddressLine2, City, Pincode, PhoneNo)

# No. of working days in which the student is present, assuming that it is calculated by other modes.
StudentAttendance = 0


# For short attendance
def is_short_attendance(total_working_days):
    global StudentAttendance
    if StudentAttendance / total_working_days < 0.78:
        return True
    else:
        return False
