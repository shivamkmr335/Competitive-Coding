#include<stdio.h>
main()
{
    int count=0,a,i;
    scanf("%d",&a);
    char st[a];
    scanf("%s",&st);
    for(i=0;i<(a-1);i++)
    {
        if(st[i]==st[i+1])
            count++;
    }
    printf("%d",count);
}
