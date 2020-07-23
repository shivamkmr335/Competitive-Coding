#include<stdio.h>
int main()
{
    int a,i;
    printf("enter the value of n:\n");
    scanf("%d",&a);
    float f=1.0f;
    printf("1");
    for(i=2;i<=a;i++)
    {
        printf(" + 1/%d ",i);

        f=f + (1.0f/i);
    }
    printf(" = %0.2f",f);
    return 0;
}
