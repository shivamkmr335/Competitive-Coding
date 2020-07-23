#include<stdio.h>
main()
{
    int t1,t2,t3,t4,m,n,count=0;
    scanf("%d %d",&m,&n);
    t1=m%2;
    t2=m/2;
    t3=n%2;
    t3=n/2;
    if(t1==0)
        count=t2*n;
    else if(t3==0)
        count=t4*m;
    else
    {
    count=(t2*n) + (n/2);
    }
    printf("%d",count);
}
