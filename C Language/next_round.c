#include<stdio.h>
int main()
{
    int a,b;
    scanf("%d %d",&a,&b);
    int count=0,i,arr[a];
    for(i=0;i<a;i++)
     scanf("%d",&arr[i]);
     for(i=0;i<a;i++)
     {
         if(arr[i]==0)
         {
             continue;
         }
         if(arr[i]>=arr[b])
          {
              count++;
          }
     }
     printf("%d",count);
     return 0;
}
