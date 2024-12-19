def num_of_stu():
    return int(input("Number of students in class:"))
def stu_infor():
    return (input("ID: "), input("Name: "), input("DoB: "))
def num_course():
    return int(input("Number of courses: "))
def cou_info():
    return input("Course ID: "), input("Course Name: ")
def select_co(courses):
    for i, course in enumerate (courses, 1):
        print(str(i) + course[1] + "ID:" + course[0] + ")")
    return courses[int(input("Select course number: ")) - 1][0]
def marks_course(course_id, students,marks):
    if course_id not in marks: #Kiểm tra nếu course id chưa tồn tại, tạo dict mới
        marks[course_id] = {}
    
    for student in students:
        marks[course_id][student[0]] = float(input("Mark for " + student[1] + " (Id:" + student[0] + "):")) 
    
def list_cou(courses): #print cou
    for course in courses:
        print("Id: " + course[0] + ",Name: " +course[1])
def list_student(students):
    for student in students:
        print("Id: " + student[0] + ",Name: " + student[1] + "Dob:" + student[2])
def show_student_marks(course_id, students, marks):
    if course_id in marks:
        for student in students:
            mark = marks[course_id].get(student[0], 'None')
            print("Id: "+ student[0]+ ",Name: " + student[1] + "Mark: "+ str(mark))

def main():
    students = [stu_infor() for _ in range (num_of_stu())]
    courses = [cou_info() for _ in range (num_course())]

    marks = {}
    while True:
        print("1.List students\n2.List courses\n3.Input marks\n4.Show marks\n5.End")
        choice = input("Choice: ")
        if choice == '1':
            list_student(students)
        elif choice == '2':
            list_cou(courses)
        elif choice == '3':
            marks_course(select_co(courses),students,marks)
        elif choice == '4':
            show_student_marks(select_co(courses),students,marks)
        elif choice == '5':
            break
        else:
            print("Invalid choice,select again.")

if __name__ == "__main__":