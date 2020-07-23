#include<stdio.h>
void change(int *a,int b);
int main()
{
    int i,a;
    printf("enter the size of array\n");
    scanf("%d",&a);
    int arr[a];
    printf("enter the value of array\n");
    for(i=0;i<a;i++)
    {
        scanf("%d",&arr[i]);
    }
    int *p=&arr;
    change(&arr,a);
     printf("the values of array are:\n");
     for(i=0;i<a;i++)
      {
            printf("%d\n",arr[i]);
      }
    return 0;
}
void change(int *p, int a)
{
    int i=0;
    for(i=0;i<a;i++)
    {
        if((*(p+i))%7==0)
        {
            *(p+i)=(*(p+i))/7;
        }
        else
        {
            *(p+i)=(*(p+i))*3;
        }
    }
}
