#include<stdio.h>
int main()
{
   int count=0,i,j,k,sum;
    prntf("enter a number");
    scanf("%d",&k);
    for(i=1;i<=k;i++)
    {
        if(k%i==0)
            count++;
    }
    if(count==2)
    {
        printf("prime no");
    }

    return 0;
}

