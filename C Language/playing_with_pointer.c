#include<stdio.h>
int swap(int a1,int b1);
int size(int a2);
int main()
{
    int a,b,c,d;
    printf("enter the numbers");
    scanf("%d%d",&a,&b);
     c=size(a);
     d=size(b);
    //swap(a,b);
    printf("%d and %d",c,d);
    return 0;
}
int swap(int c,int d)
{
    int e,f;
    printf("%d and %d",e,f);

}
int size(int a2)
{
    int i=0,temp=0;
    for(i=0;a2>=0;i++)
    {
       a2=a2/10;
       temp++;
    }
    return temp;
}
