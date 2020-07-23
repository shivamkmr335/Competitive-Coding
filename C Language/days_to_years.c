#include<stdio.h>
int main()
{
    int a,b,c;
    printf("enter the no of days");
    scanf("%d",&a);
    b=a/365;
    a=a%365;
    c=a/7;
    a=a%7;
    printf("the given has %d years %d weeks and %d days",b,c,a);
    return 0;
}
