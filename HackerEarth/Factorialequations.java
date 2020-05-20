/*
Question:
You are given two numbers X and N . Your task is to find the last digit of the following equation: 
X^((N!)mod10)

Input format
The first line contains two integers  and .

Output format
Print the last digit of the given equation.

Constraints
1<=X<=10^9
0<=N<=10^18

SAMPLE INPUT 
5 2
SAMPLE OUTPUT 
5
Explanation
factorial of (2) is 2*1=2  ,So 5^2=25 the last digit in 25 is 5
*/
import java.lang.*;
import java.util.*;
import java.lang.Math;

class TestClass {
    public static long factorial(long N)
    {
        long fact=1;
        if(N==0 || N==1)
        {
            fact=1;
        }
        else
        {
            fact=N*factorial(N-1);
        }
        return fact;
    }
    public static long Calculation(long X,long N)
    {
        long rfact = factorial(N);
        long equ = rfact%10;
        
        long res = 1;
        while(equ!=0)
        {
            res = res*X;
            equ--;
        }
        return res%10;
    }
    public static void main(String args[] ) throws Exception {
        
        Scanner sobj = new Scanner(System.in);
        long X = sobj.nextLong();
        if((X<1) || (X>1000000000))
        {
            return;
        }
        long N = sobj.nextLong();
        if((N<0) && (N>1000000000))
        {
            return;
        }
        long result = Calculation(X,N);
        System.out.println(result);

    }
}
