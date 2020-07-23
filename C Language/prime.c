#include<stdio.h>
int main()
{
    int n=0,i=0,count =0;
    printf("enter a number");
    scanf("%d",&n);
    for(i=0;i<=5;i++)
    {
        if(5%i==0)
          {
              count=count +1;
          }
    }
    if(count ==0)
    {
        printf("prime no");
    }
    else
    {
        printf("not a prime  no");
    }
    return 0;
}
