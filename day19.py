'''
University management system using oops:
'''

class person:
    university_name = "codegnan university"

    def __init__(self, name, age, id_no):
        self.name = name
        self.age = age
        self.id_no = id_no

    def display_info(self):
        pass

class student(person):
     student_count = 0

     def __init__(self, name, age, gender, id_no, course, year):
        
        super().__init__(name, age, id_no)
        self.gender = gender
        self.course = course
        self.year = year
        student.student_count += 1

     def display_info(self):
         print(f"Name : {self.name} \nAge : {self.age} \nID_NO: {self.id_no} \nGender : {self.gender} \nCourse: {self.course} \nYear: {self.year}")
         
class faculty(person):
    faculty_count = 0
    def __init__(self, name, age, id_no, gender, edu_):
        super().__init__(name, age, id_no)
        self.gender = gender
        self.edu_ = edu_
        faculty.faculty_count += 1

    def display_info(self):
         print(f"Name : {self.name} \nAge : {self.age} \nID_NO: {self.id_no} \nGender : {self.gender} \nEducation: {self.edu_}")

class helper(person):
    helper_count = 0
    def __init__(self, name, age, id_no, gender,phone_num):
        super().__init__(name, age, id_no)
        self.gender = gender
        self.phone_num= phone_num
        helper.helper_count += 1

    def display_info(self):
         print(f"Name : {self.name} \nAge : {self.age} \nID_NO: {self.id_no} \nGender : {self.gender} \nPhone num: {self.phone_num}")



class watchmen(person):
    watchmen_count = 0
    def __init__(self, name, age, id_no, gender,phone_num):
        super().__init__(name, age, id_no)
        self.gender = gender
        self.phone_num= phone_num
        watchmen.watchmen_count += 1

    def display_info(self):
         print(f"Name : {self.name} \nAge : {self.age} \nID_NO: {self.id_no} \nGender : {self.gender} \nPhone num: {self.phone_num}")


class driver(person):
    driver_count = 0
    def __init__(self, name, age, id_no, gender,phone_num, salary,skills):
        super().__init__(name, age, id_no)
        self.gender = gender
        self.salary = salary
        self.skills = skills
        self.phone_num= phone_num
        driver.driver_count += 1

    def display_info(self):
         print(f"Name : {self.name} \nAge : {self.age} \nID_NO: {self.id_no} \nGender : {self.gender} \nsalary: {self.salary} \nskills: {self.skills} \nPhone num: {self.phone_num}")    
         
         
         
        
print("\n----- studenr details -----")
s1 = student("Sravya", 20, 400, "Female", "B.Tech", 3)
s1.display_info()

print("\n----- faculty details -----")
f1 = faculty("Rajan", 35, 201, "Male", "phd")
f1.display_info()

print("\n----- helper details -----")
h1 = helper("rani", 45, "Female", 234, 1234567890)
h2 = helper("roja", 44, "Female", 235, 987654321)
h1.display_info()
h2.display_info()

print("\n----- watchmen details -----")
w1 = watchmen("rajesh", 45, "Male", 123, 1234567890)
w2 = watchmen("ramu", 44, "Male", 124, 987654321)
w1.display_info()
w2.display_info()

print("\n----- driver details -----")
d1 = driver("rajesh", 45, "Male", 123, 20000, "driving skills", 1234567890)
d1.display_info()


print("\n----- counts -----")
print("Total Students:", student.student_count)
print("Total Faculty:", faculty.faculty_count)
print("Total helper:", helper.helper_count)
print("Total watchmen:", watchmen.watchmen_count)
print("Total driver:", driver.driver_count)
