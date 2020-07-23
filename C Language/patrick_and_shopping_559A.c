#include<stdio.h>
main()
{
    int sum,i,arr[3];
    for(i=0;i<3;i++)
        scanf("%d",&arr[i]);
//arranging in ascending order
    if(arr[0]<arr[1])
    {
        arr[0]=arr[0]+arr[1];
         arr[1]=arr[0]-arr[1];
          arr[0]=arr[0]-arr[1];
    }
    if(arr[2]>(arr[0]+arr[1]))
        sum=2*(arr[0]+arr[1]);
    else if(arr[0]>(arr[1]+arr[2]))
        sum= 2*(arr[1]+arr[2]);
    else
        sum=arr[0]+arr[1]+arr[2];
    printf("%d",sum);
}
