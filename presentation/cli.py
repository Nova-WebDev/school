from business.area.area_service import AreaService
from business.school.school_service import SchoolService
from business.class_room.class_service import ClassroomService
from business.student.student_service import StudentService
from business.subject.subject_service import SubjectService
from business.grade.grade_service import GradeService

from business.area.area_report import area_report
from business.school.school_report import school_report
from business.class_room.class_report import class_report
from business.student.student_report import student_report
from business.subject.subject_report import subject_report


menu_school_system = """

School Management System 

1) Reports
   11) Area
   12) School
   13) Class
   14) Student
   15) Subject

2) View
   21) View Area
   22) View School
   23) View Class
   24) View Student
   25) View Subject
   26) View Grade

3) Insert
   31) Insert Area
   32) Insert School
   33) Insert Class
   34) Insert Student
   35) Insert Subject
   36) Insert Grade

4) Update
   41) Update Area
   42) Update School
   43) Update Class
   44) Update Student
   45) Update Subject
   46) Update Grade

5) Delete
   51) Delete Area
   52) Delete School
   53) Delete Class
   54) Delete Student
   55) Delete Subject
   56) Delete Grade

0) Exit

"""


def cli_loop():
    while True:
        print(menu_school_system)
        choice = input("Select option: ").strip()

        if choice == "11":
            pk = int(input("Enter area pk: "))
            area_report(pk)
        elif choice == "12":
            pk = int(input("Enter school pk: "))
            school_report(pk)
        elif choice == "13":
            pk = int(input("Enter class pk: "))
            class_report(pk)
        elif choice == "14":
            pk = int(input("Enter student pk: "))
            student_report(pk)
        elif choice == "15":
            pk = int(input("Enter subject pk: "))
            subject_report(pk)

        elif choice == "21":
            print(AreaService.list_areas())
        elif choice == "22":
            pk = int(input("Enter area pk: "))
            print(SchoolService.list_schools_by_area(pk))
        elif choice == "23":
            pk = int(input("Enter school pk: "))
            print(ClassroomService.list_classrooms_by_school(pk))
        elif choice == "24":
            pk = int(input("Enter class pk: "))
            print(StudentService.list_students_by_classroom(pk))
        elif choice == "25":
            print(SubjectService.list_subjects())
        elif choice == "26":
            pk = int(input("Enter student pk: "))
            print(GradeService.list_grades_by_student(pk))

        elif choice == "31":
            name = input("Enter area name: ")
            AreaService.create_area(name)
        elif choice == "32":
            name = input("Enter school name: ")
            area_id = int(input("Enter area pk: "))
            SchoolService.create_school(name, area_id)
        elif choice == "33":
            name = input("Enter class name: ")
            school_id = int(input("Enter school pk: "))
            ClassroomService.create_classroom(name, school_id)
        elif choice == "34":
            name = input("Enter student name: ")
            class_id = int(input("Enter class pk: "))
            StudentService.create_student(name, class_id)
        elif choice == "35":
            name = input("Enter subject name: ")
            SubjectService.create_subject(name)
        elif choice == "36":
            score = float(input("Enter grade score: "))
            student_id = int(input("Enter student pk: "))
            subject_id = int(input("Enter subject pk: "))
            GradeService.create_grade(student_id, subject_id, score)

        elif choice == "41":
            pk = int(input("Enter area pk: "))
            name = input("Enter new name (or leave empty): ").strip() or None
            AreaService.update_area(pk, name)
        elif choice == "42":
            pk = int(input("Enter school pk: "))
            name = input("Enter new name (or leave empty): ").strip() or None
            area_id = input("Enter new area pk (or leave empty): ").strip()
            area_id = int(area_id) if area_id else None
            SchoolService.update_school(pk, name, area_id)
        elif choice == "43":
            pk = int(input("Enter class pk: "))
            name = input("Enter new name (or leave empty): ").strip() or None
            school_id = input("Enter new school pk (or leave empty): ").strip()
            school_id = int(school_id) if school_id else None
            ClassroomService.update_classroom(pk, name, school_id)
        elif choice == "44":
            pk = int(input("Enter student pk: "))
            name = input("Enter new name (or leave empty): ").strip() or None
            class_id = input("Enter new class pk (or leave empty): ").strip()
            class_id = int(class_id) if class_id else None
            StudentService.update_student(pk, name, class_id)
        elif choice == "45":
            pk = int(input("Enter subject pk: "))
            name = input("Enter new name (or leave empty): ").strip() or None
            SubjectService.update_subject(pk, name)
        elif choice == "46":
            pk = int(input("Enter grade pk: "))
            score = input("Enter new score (or leave empty): ").strip()
            score = float(score) if score else None
            GradeService.update_grade(pk, score)

        elif choice == "51":
            pk = int(input("Enter area pk: "))
            AreaService.delete_area(pk)
        elif choice == "52":
            pk = int(input("Enter school pk: "))
            SchoolService.delete_school(pk)
        elif choice == "53":
            pk = int(input("Enter class pk: "))
            ClassroomService.delete_classroom(pk)
        elif choice == "54":
            pk = int(input("Enter student pk: "))
            StudentService.delete_student(pk)
        elif choice == "55":
            pk = int(input("Enter subject pk: "))
            SubjectService.delete_subject(pk)
        elif choice == "56":
            pk = int(input("Enter grade pk: "))
            GradeService.delete_grade(pk)

        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")

        input("\nPress Enter to continue...")
