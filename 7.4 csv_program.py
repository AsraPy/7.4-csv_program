import csv
file_path = "students.csv"
def add_student():
    name = input("نام: ")
    age = input("سن: ")
    grade = input("نمره: ")
    with open(file_path,"a",newline="",encoding="utf-8")as file:
        writer = csv.writer(file)
        writer.writerow([name,age,grade])
        
def show_students():
    with open(file_path,"r",encoding="utf-8")as file:
        reader = csv.reader(file)
        print("\nليست دانش اموزان:")
        for row in reader:
            print(row)
            
while True:
    print("\n1.افزودن دانش اموز")
    print("2.نمايش دانش اموزان")
    print("3.خروج")
    
    choice = input("انتخاب: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        break
    else:
        print("گزينه نامعتبر")
    
