#include <stdio.h>
int main()
{
    int n,m,a;
    if(a<1000000000 && a>0)
    {
    scanf("%d%d%d",&m,&n,&a);
    printf("%d%d",m*n,a*a);
    int c=(n*m)/(a*a);
    printf("%d",a);
    }
    return 0;
}
