'''
Question:
You are given a function f(x)=x^2. You are also given K lists. The ith list consists of Ni elements.

You have to pick one element from each list so that the value from the equation below is maximized:
S=(f(x1)+f(x2)+...+f(xk))%M

Xi denotes the element picked from the ith list . Find the maximized value Smax obtained.

% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format
The first line contains  space separated integers K and M.
The next K lines each contains an integer Ni, denoting the number of elements in the ith list, followed by Ni space separated integers denoting the elements in the list.

Output Format
Output a single integer denoting the value Smax.

Sample Input
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Sample Output
206

Explanation
Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum S value equal to (5^2+9^2+10^2)% 1000= 206.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

def fofx(tup,M):
    lst6 = list()
    res1 = 0
    lst4 = list(tup)
    for i in range(len(lst4)):
        lst6 = lst4[i]
        res1 = res1 + (lst6*lst6)

    return res1%M

def main():
    K, M = map(int,input().split())
    res = 0
    res1 = 0
    lst2 = list()
    lst5 = list()

    for i in range(K):
        lst1 = list(map(int,input().split()))
        lst1.remove(lst1[0])
        lst2.append(lst1)

    lst3 = list(product(*lst2))

    for i in range(len(lst3)):
        res2 = fofx(lst3[i],M)
        lst5.append(res2)

    print(max(lst5))

if __name__=="__main__":
    main()

