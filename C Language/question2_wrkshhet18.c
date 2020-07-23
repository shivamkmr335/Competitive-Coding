#include<stdio.h>
int main()
{
    int a,b,c,d;
    printf("enter the no of  rows and columns :");
    scanf("%d%d",&a,&b);
    int arr[a][b];
    printf("enter the values :");
    for(c=0;c<a;c++)
    {
        for(d=0;d<b;d++)
        {
            scanf("%d",&arr[c][d]);
        }
    }
     for(c=0;c<a;c++)
    {
        for(d=0;d<b;d++)
        {
            printf("%d",arr[c][d]);
        }
    }
    return 0;
}
