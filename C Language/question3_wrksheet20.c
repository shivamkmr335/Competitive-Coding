#include<stdio.h>
void prod(int *p);
int main()
{
    int i,a,b;
    int arr[5][5]={{1,2,3,4,5},{6,7,8,9,1},{1,2,34,5,6},{1,3,46,7,8},{5,6,7,8,9}};
    int *p=&arr[5][5];
    prod(&arr);
    prod(p);
    return 0;
}
void prod(int *p)
{
    int i=0,c;
    for(i=0;i<5;i++)
    {
        int c=(*p)*(*(p+1))*(*(p+2))*(*(p+3))*(*(p+4));
        printf("%d\n",c);
        p=p+5;
    }
}
