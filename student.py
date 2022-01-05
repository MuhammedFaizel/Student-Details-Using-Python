class Student:
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    def add(self, Name, Rollno, mark1, mark2):
        std = Student(Name, Rollno, mark1, mark2)
        ls.append(std)

    def display(self, std):
        print("Name: ", std.name)
        print(f"Rollno:  {std.rollno}")
        print(f"Mark1:  {std.m1}")
        print(f"Mark2:  {std.m2}")
        print("\n")

    def search(self, rn):
        for i in range(ls.__len__()):
            if ls[i].rollno == rn:
                return i

    def update(self, rn, No, New_Name):
        i = obj.search(rn)
        roll = No
        n = New_Name
        ls[i].rollno = roll
        ls[i].name = n


ls = []
obj = Student("", 0, 0, 0)

while True:
    print("\nOperations")
    print("\n1. Add Student \n2. Display \n3. Search \n4. Update \n5. exit")
    print("\n")
    ch = int(input("Enter your operation: "))

    if ch == 1:
        s = int(input("How many Students have to be added: "))
        for i in range(s):
            n = input("Enter name: ")
            r = int(input("Enter the roll number: "))
            m_1 = int(input("Enter mark 1: "))
            m_2 = int(input("Enter mark 2: "))
            print("\n")
            obj.add(n, r, m_1, m_2)

    elif ch == 2:
        print("\nList of Students\n")
        for i in range(ls.__len__()):
            obj.display(ls[i])

    elif ch == 3:
        a = int(input("Enter the rollno of student you have to search: "))
        s = obj.search(a)
        print(s)
        obj.display(ls[s])

    elif ch == 4:
        n = int(input("Enter the rollno of student you hsve to update: "))
        nr = int(input("Enter the new roll number: "))
        nn = input("Enter the new name: ")
        obj.update(n, nr, nn)

        print("\nAfter updation\n")
        for i in range(ls.__len__()):
            obj.display(ls[i])

    elif ch == 5:
        break

    else:
        print("INvalid option")
        continue
    continue_next = input("Do you want to continue(Y/N): ").lower()
    if continue_next not in ["y", "yes"]:
        break

print("Thank you")
