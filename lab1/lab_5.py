
#5.WAP to enter the marks of 10 students and display it

def studentMarks():
    marks = [int(input(f"Enter marks for student {i + 1}: ")) for i in range(10)]
    return marks

if __name__ == "__main__":
    numbers = studentMarks()
    print("Students' marks are:", numbers)
