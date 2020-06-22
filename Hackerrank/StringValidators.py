'''
Question:
Task
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format
A single line containing a string S.

Output Format
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

Sample Input
qA2

Sample Output
True
True
True
True
True
'''
if __name__ == '__main__':
    s = input()
    lst = list(s)
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    flag5 = False

    for i in range(len(lst)):
        if(lst[i].isalnum()):
            flag1 = True
            break
        else:
            flag1 = False

    for i in range(len(lst)):
        if(lst[i].isalpha()):
            flag2 = True
            break
        else:
            flag2 = False

    for i in range(len(lst)):
        if(lst[i].isdigit()):
            flag3 = True
            break
        else:
            flag3 = False

    for i in range(len(lst)):
        if(lst[i].islower()):
            flag4 = True
            break
        else:
            flag4 = False

    for i in range(len(lst)):
        if(lst[i].isupper()):
            flag5 = True
            break
        else:
            flag5 = False

    print(flag1)
    print(flag2)
    print(flag3)
    print(flag4)
    print(flag5)
