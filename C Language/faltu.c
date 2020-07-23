#include<stdio.h>
#include<math.h>
int mera(int a);
int swapping(int a,int b,int c,int d);
int first(int a1,int b1);
int second(int a2,int b2);
int main()
{
    printf("enter the number:\n");
    int a,b,c,d;
    scanf("%d%d",&a,&b);
    printf("the numbers are :%d and %d\n",a,b);
    c=mera(a);
    d=mera(b);
    printf("the size of a: %d\nthe size of b: %d\n",c,d);
    int sm=swapping(a,b,c,d);
    printf("the sum is:%d\n",sm);
    b=first(sm,d);
    a=second(sm,c);
    printf("the values after reversing are :\n a=%d \n b=%d",a,b);
    return 0;
}
mera(int a)
{
    int i,sizes=0;
    for(i=0;a>0;i++)
    {
        sizes=sizes+1;
        a=a/10;
    }
  return sizes;
}
int swapping(int a,int b,int c,int d)
{
   int temp=b+(a*pow(10,d));
   return temp;
}
int first(int sm,int d)
{
    int b=sm/d;
    return b;
}
int second(int sm,int d)
{
    int a=sm%d;
}
