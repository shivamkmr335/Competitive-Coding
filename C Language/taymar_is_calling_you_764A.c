#include<stdio.h>
main()
{
    int a,b,c,l=1;
    scanf("%d %d %d",&a,&b,&c);
    while(l%a!=0 || l%b!=0)
        l++;
    l=c/l;
    printf("%d",l);
}
