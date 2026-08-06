# Function to enter marks
def get_marks():
    marks = []

    while True:
        mark = input("Enter Marks : ")

        if mark.lower() == "done":
            break

        marks.append(int(mark))

    return marks

# Function to calculate average
def average(marks):
    return sum(marks) / len(marks)

# Function to calculate grade
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Function to display result
def display(name, marks):
    avg = average(marks)
    g = grade(avg)

    print("\nStudent Name :", name)
    print("Marks        :", marks)
    print("Average      :", round(avg, 2))
    print("Grade        :", g)

# Main Function
def main():
    name = input("Enter Student Name: ")
    marks = get_marks()
    display(name, marks)

main()