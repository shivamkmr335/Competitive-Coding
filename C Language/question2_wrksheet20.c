#include<stdio.h>
int main()
{
    int i,a;
    printf("enter the size of array:\n");
    scanf("%d",&a);
    int arr[a];
    printf("enter the value of array\n");
    for(i=0;i<a;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=0;i<a;i++)
    {
        if(arr[i]%2==0)
            arr[i]=arr[i]/2;
        else
            arr[i]=arr[i]*2;
    }
     printf("the values of array are:\n");
     for(i=0;i<a;i++)
      {
            printf("%d\n",arr[i]);
      }
return 0;
}
