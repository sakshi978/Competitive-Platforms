#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int cnt0=0,cnt1=0,cnt2=0,cnt3=0,cnt4=0,cnt5=0,cnt6=0,cnt7=0,cnt8=0,cnt9=0;
    char s[1000];
    scanf("%[^\n]%*c", &s);
    //int n=strlen(s);

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    if((strlen(s)>=1) && (strlen(s)<=1000))
    {
       for(int i=0;i<strlen(s);i++)
        {
            if(s[i]=='0')
            {
                cnt0++;
            }
            else if(s[i]=='1')
            {
                cnt1++;
            }
            else if(s[i]=='2')
            {
                cnt2++;
            }
            else if(s[i]=='3')
            {
                cnt3++;
            }
            else if(s[i]=='4')
            {
                cnt4++;
            }
            else if(s[i]=='5')
            {
                cnt5++;
            }
            else if(s[i]=='6')
            {
                cnt6++;
            }
            else if(s[i]=='7')
            {
                cnt7++;
            }
            else if(s[i]=='8')
            {
                cnt8++;
            }
            else if(s[i]=='9')
            {
                cnt9++;
            }
        } 
    } 
    printf("%d ",cnt0);
    printf("%d ",cnt1);
    printf("%d ",cnt2);
    printf("%d ",cnt3);
    printf("%d ",cnt4);
    printf("%d ",cnt5);
    printf("%d ",cnt6);
    printf("%d ",cnt7);
    printf("%d ",cnt8);
    printf("%d ",cnt9);
    return 0;
}
