
#2. WAP to input percentage & display division
def checker(mark):
    if (mark>=80):
        print('Distinction');
    elif(mark>=65):
        print('First Division');
    elif(mark>=55):
        print('Second Division');

    elif(mark>=40):
        print('Third Division');
    elif(mark<40):
        print('Fail');


if __name__=="__main__":
    marks=int(input("Enter your marks:"));
    checker(marks);