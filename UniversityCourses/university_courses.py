class Student:
    def __init__(self, id, name, course_count, courses):
        self.id = id
        self.name = name
        self.course_count = course_count
        self.courses = courses

class Course:
    def __init__(self, id, name, prereq_count, prereq_ids):
        self.id = id
        self.name = name
        self.prereq_count = prereq_count
        self.prereq_ids = prereq_ids

    #Check if the student can enroll in the course
    def can_enroll(self, student):
        for prereq_id in self.prereq_ids:
            has_prereq = False
            for course_id in student.courses:
                if course_id == prereq_id:
                    has_prereq = True
                    break
            if not has_prereq:
                return False
        return True

def main():
    #Initialize the list of courses
    courses = [
        Course(0, "Intro to Programming", 0, [-1]),
        Course(1, "Data Structures", 1, [0]),
        Course(2, "Algorithms", 1, [1]),
        Course(3, "Database Management", 1, [0]),
        Course(4, "Web Development", 1, [0]),
        Course(5, "Operating Systems", 2, [1, 2]),
        Course(6, "Computer Networks", 2, [1, 5]),
        Course(7, "Software Engineering", 2, [1, 2]),
        Course(8, "Machine Learning", 2, [1, 2]),
        Course(9, "Distributed Systems", 1, [5]),
        Course(10, "Cybersecurity", 2, [2, 3]),
        Course(11, "Cloud Computing", 2, [2, 3]),
        Course(12, "Mobile App Development", 1, [4]),
        Course(13, "Game Development", 1, [0]),
        Course(14, "Artificial Intelligence", 2, [2, 8]),
        Course(15, "Big Data Analytics", 2, [2, 3]),
        Course(16, "Blockchain Technology", 2, [2, 3]),
        Course(17, "UI/UX Design", 1, [14]),
        Course(18, "Embedded Systems", 2, [1, 5]),
        Course(19, "Computer Graphics", 1, [0])
    ]

    #Initialize a student
    student = Student(1, "John Doe", 5, [0, 1, 2, 3, 4])

    #Define the target courses the student wants to enroll in
    target_courses = [
        courses[13],  # Game Development
        courses[16],  # Blockchain Technology
        courses[17],  # UI/UX Design (student cannot enroll)
        courses[18]   # Embedded Systems
    ]

    #Print the enrollment status for each target course
    print("Enrollment status for " + student.name + ": ")
    for i in range(4):
        if target_courses[i].can_enroll(student):
            print("- Can enroll in " + target_courses[i].name)
        else:
            print("- Cannot enroll in " + target_courses[i].name 
                  + " due to missing prerequisites.")

if __name__ == "__main__":
    main()
