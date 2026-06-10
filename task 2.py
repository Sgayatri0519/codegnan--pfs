class Person:
    college_name = "andhra unversity College"

    def __init__(self, name, age, id_no):
        self.name = name
        self.age = age
        self.id_no = id_no

    def display_common_details(self):
        print(f"College Name : {self.college_name}")
        print(f"Name         : {self.name}")
        print(f"Age          : {self.age}")
        print(f"ID Number    : {self.id_no}")


class Student(Person):
    def __init__(self, name, age, id_no, course):
        super().__init__(name, age, id_no)
        self.course = course

    def display(self):
        self.display_common_details()
        print(f"Course       : {self.course}")


class TeachingStaff(Person):
    def __init__(self, name, age, id_no, subject):
        super().__init__(name, age, id_no)
        self.subject = subject

    def display(self):
        self.display_common_details()
        print(f"Subject      : {self.subject}")


class NonTeachingStaff(Person):
    def __init__(self, name, age, id_no, department):
        super().__init__(name, age, id_no)
        self.department = department

    def display(self):
        self.display_common_details()
        print(f"Department   : {self.department}")


class Driver(Person):
    def __init__(self, name, age, id_no, vehicle):
        super().__init__(name, age, id_no)
        self.vehicle = vehicle

    def display(self):
        self.display_common_details()
        print(f"Vehicle      : {self.vehicle}")


class Cleaner(Person):
    def __init__(self, name, age, id_no, area):
        super().__init__(name, age, id_no)
        self.area = area

    def display(self):
        self.display_common_details()
        print(f"Cleaning Area: {self.area}")


class Warden(Person):
    def __init__(self, name, age, id_no, hostel):
        super().__init__(name, age, id_no)
        self.hostel = hostel

    def display(self):
        self.display_common_details()
        print(f"Hostel       : {self.hostel}")


# Creating Objects

s1 = Student("Sai", 20, 101, "B.Tech")
t1 = TeachingStaff("Pavan", 35, 201, "Python")
n1 = NonTeachingStaff("Keerthi", 40, 301, "Administration")
d1 = Driver("Vamsi", 45, 401, "College Bus")
c1 = Cleaner("Gayathri", 38, 501, "Block A")
w1 = Warden("mani", 50, 601, "Boys Hostel")

# Display Details

print("\n----- Student Details -----")
s1.display()

print("\n----- Teaching Staff Details -----")
t1.display()

print("\n----- Non-Teaching Staff Details -----")
n1.display()

print("\n----- Driver Details -----")
d1.display()

print("\n----- Cleaner Details -----")
c1.display()

print("\n----- Warden Details -----")
w1.display()
