#include<stdio.h>
main()
{
    int a,j,i=0,count;
    scanf("%d",&a);
    int b[a];
    scanf("%d",&b);
    j=a-1;
    while(b[i]!=0)
        i++;
    while(b[j]!=0)
        j--;
    count=j-i;
    printf("%d",count);
}
