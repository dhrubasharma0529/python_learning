#  Given two dictionaries with overlapping keys,
#  how would you combine them by summing the values of common keys ?
student_marks1 = {
    "name" : "Ram",
    "Math" : 80,
    "Science":95,
    "Health": 65,
    "English":70
}
student_marks2 = {
    "name" : "hari",
    "Math": 75,
    "English":80,
    "Nepali":65,  
    "Optional_Maths":90
}
student_marks_total = {}
if student_marks1.get('name') != None and student_marks2.get('name') != None:
    student_marks_total['name'] = student_marks1.get('name') + ' and '+ student_marks2.get('name')
elif student_marks1.get('name') == None and student_marks2.get('name') != None:
    student_marks_total['name'] = student_marks2.get('name')
elif student_marks1.get('name') != None and student_marks2.get('name') == None:
    student_marks_total['name'] = student_marks1.get('name')

student_marks_total['Math'] = student_marks1.get('Math',0) + student_marks2.get('Math',0) 
student_marks_total['Science'] = student_marks1.get('Science',0) + student_marks2.get('Science',0) 
student_marks_total['Health'] = student_marks1.get('Health',0) + student_marks2.get('Health',0) 
student_marks_total['Nepali'] = student_marks1.get('Nepali',0) + student_marks2.get('Nepali',0) 
student_marks_total['Otional_Maths'] = student_marks1.get('Optional_Maths',0) + student_marks2.get('Optional_Maths',0) 
print(student_marks_total)
