def student_marks():
    total = 0
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        subject = input("Enter Subject {i+1} Name: ")
        marks = int(input("Enter marks for {subject}: "))
        total += marks

    print("\nTotal Marks =", total)

student_marks()