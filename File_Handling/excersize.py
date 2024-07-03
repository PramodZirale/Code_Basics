# student_marks.csv contains the marks and other details for some students. Write a python program to:

# Open the file in read mode
# Create a dictionary from the given data
# Add a new field to the dictionary total\_marks and store the total marks of the students.
# Add a new field to the dictionary Average and store the average marks of the students.
# Create a new file and write this information to the new file
# (https://www.kaggle.com/arunkumar413/student-marks)

with open("student_marks.csv","r") as s:
    student_data = s.readlines()
    print(student_data)
    
headers = student_data[0].strip().split(",")

student_details = []

for student in student_data[1:]:
    student = student.strip().split(",")
    row_dict = dict(zip(headers, student))
    student_details.append(row_dict)
    
print(student_details)  
    
    