#include<stdio.h>
int main()
{
    int i,a;
    printf("enter the size of array\n");
    scanf("%d",&a);
    int arr[a];
    printf("enter the value of array\n");
    for(i=0;i<a;i++)
    {
        scanf("%d",&arr[a-(1+i)]);
    }
    printf("the values of array are:\n");
     for(i=0;i<a;i++)
      {
            printf("%d\n",arr[i]);
      }
    return 0;
}
