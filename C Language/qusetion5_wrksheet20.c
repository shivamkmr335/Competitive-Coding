#include<stdio.h>
void exchange(int *p,int a);
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
    exchange(&arr,a);
    printf("the values of array are:\n");
     for(i=0;i<a;i++)
      {
            printf("%d\n",arr[i]);
      }
return 0;
}
void exchange(int *p,int a)
{
    int c=a/2,i,d;
    for(i=0;i<=c;i++)
    {
        printf("....%d....",i);
        d= *((p+c)+i+1);
        *((p+c)+i+1)=*(p+i);
        *(p+i)=d;
    }

}
