#  Given a nested dictionary representing student data (e.g., names as keys and another dict of subject:marks),
#  how would you extract all students who scored more than 80 in Math?
student_data = {
    "name" : "Ram",
    "subject" : {
        "English" : 80,
        "Science" : 90,
        "Math" : 90
    }
}
student_subjects = student_data.get('subject')
# s = student_data.get('name') if student_subjects.get('Math') > 80 else 'no student has got over 80' 
#  print(s)
if student_subjects.get('Math') > 80:
    print(student_data.get('name'))
else:
    print("NO Student has got over the 80 marks.")
