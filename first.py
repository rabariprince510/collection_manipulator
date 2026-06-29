
students = []
subjects_set = set()

print("=" * 50)
print("Welcome to the student data organizer!")
print("=" * 50)
    
while True:    

    print("Select an option: ")
    print("1.Add student")
    print("2.Display All students")
    print("3.update student information")
    print("4.Delete student")
    print("5.Display subjects offered")
    print("6.Exit")

    choice = input("Enter your choice: ")

    match choice:        
        case "1":
            print("=" * 50)
            print("Enter student details: ")
            print("=" * 50)
            student_id = int(input("Enter student ID: "))
            name = str(input("Enter Name: "))
            age = int(input("Enter age: "))
            grade = str(input("Enter Grade: "))
            dob = str(input("Enter your date of birth: "))
                        
            print("Enter three subjects")

            s1 = input("subject1: ")
            s2 = input("subject2: ")
            s3 = input("subject3: ")
                        
            sub = {s1,s2,s3}
                        
            subjects_set.update(sub)
            details = (student_id,dob)
            info = {"id": student_id,"name": name,"age": age,"grade": grade,"dob": dob, "subjects": list(sub),"details": details}
                        
            students.append(info)
            print("Student added successfully!")
        case "2":
            print("=" * 50)
            print("2.Display All students")
            print("=" * 50)
            if len(students) == 0:                
                print("No records found.")
            else:                
                for i in students:                    
                    print("student_id : ", i["id"])
                    print("name : ", i["name"])
                    print("age : ", i["age"])
                    print("grade : ", i["grade"])
                    print("dob : ", i["dob"])
                    print("subjects : ", i["subjects"])
        case "3":
            print("=" * 50)
            print("3.Update student information")
            print("=" * 50)
            student_id = int(input("Enter student ID : "))
            found = False

            for i in students:                
                if i["id"] == student_id:                    
                    found = True
                    print("1. update age")
                    print("2. update grade")
                    print("3. update subjects")

                    ch = (input("Enter choice : "))

                    match ch:                        
                        case "1":
                            i["age"] = int(input("New Age : "))
                            print("Age updated.")
                        case "2":
                            i["grade"] = input("New grade : ")
                            print("Grade updated.")
                        case "3":
                            print("Enter three subjects")

                            s1 = input("subject1: ")
                            s2 = input("subject2: ")
                            s3 = input("subject3: ")

                            sub = {s1,s2,s3}

                            i["subjects"] = list(sub)
                            subjects_set.update(sub)

                            print("Subjects updated.")

                if found == False:                    
                    print("Student not found.")
               
        case "4":
            print("=" * 50)
            print("4.Delete student")
            print("=" * 50)
            student_id = int(input("Enter student ID : "))
            found = False
            delete_index = -1           

            for i in range(len(students)):                
                if students[i]["details"][0] == student_id:
                    delete_index = i                
                    found = True
                    break
            if found:                
                del students[delete_index]
                print("student deleted")
            else:
                print("student not found.")
             
        case "5":
            print("=" * 50)
            print("5.Subject offered")
            print("=" * 50)
            if len(subjects_set) == 0:                
                print("No subjects available.")
            else:
                print("subject offered : ")

                for i in subjects_set:                    
                    print(i)

        case "6":            
            print("Thank you for using student data organizer.")
            break













                









                    
                
