#include<stdio.h>
main()
{
    long int a,b,i,j,count=0,c;
    scanf("%d %d",&a,&b);
    for(i=1;i<=a;i++)
    {
        for(j=1;j<=a;j++)
    {
        c=i*j;
            if(b==c)
            {
                count++;
            }
    }
    }
    printf("%d",count);
}
