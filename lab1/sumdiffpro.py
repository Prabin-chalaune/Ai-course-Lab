#3.WAP to calculate sum,diff,product, and quotient between two numbers using a single function.
def calculate(a,b):
    sum=a+b;
    diff=a-b;
    product=a*b;
    quotient=a/b;
    return sum, diff, product,quotient;

if __name__=="__main__":

    num1=int(input("Enter num1:"))
    num2=int(input("Enter num2:"))
    sum,diff,product,quotient=calculate(num1,num2)

    print('The sum is:',sum);
    print('The difference is:',diff);
    print('The product is:',product);
    print('The quotient is:',quotient);


