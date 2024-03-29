
#6.WAP to calculate the factorial of input number
def factorial(n):
    if n==0 or n==1:
        return 1;
    else:
        return n*factorial(n-1);


if __name__ == "__main__":
    num=int(input("Enter a number:"))
    result=factorial(num);
    print(f"The factorial of {num} is: {result}")
