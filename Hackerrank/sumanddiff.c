#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int add1(int x,int y)
{
    return x+y;
}

int sub1(int x,int y)
{
    return x-y;
}

float add2(float a,float b)
{
    return a+b;
}

float sub2(float a,float b)
{
    return a-b;
}

int main()
{
	int val1=0,val2=0;
    int ret1=0,ret2=0;
    float val3=0.0,val4=0.0;
    float ret3=0.0,ret4=0.0;
    
    //Taking input of two numbers of type int 
    scanf("%d%d",&val1,&val2);
    //Taking input of two numbers of type float
    scanf("%f%f",&val3,&val4);

    ret1=add1(val1,val2);
    ret2=sub1(val1,val2);
    printf("%d %d\n",ret1,ret2);

    ret3=add2(val3,val4);
    ret4=sub2(val3,val4);
    printf("%.1f %.1f\n",ret3,ret4);
    
    return 0;
}
