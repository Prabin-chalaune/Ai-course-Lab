
#1.WAP to check if an input number is odd or even

def oddeven(n):
    if n%2==0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")

if __name__== "__main__":
    num=int(input('Enter a number:'));
    oddeven(num);
