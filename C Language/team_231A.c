#include<stdio.h>
main()
{
    int temp=0,count=0,i,j,size;
    scanf("%d",&size);
    int arr[size][3];
    for(j=0;j<size;j++)
    {
        for(i=0;i<3;i++)
        {
            scanf("%d",&arr[j][i]);
        }
    }
    for(i=0;i<size;i++)
    {
        temp=arr[i][0]+arr[i][1]+arr[i][2];
        if(temp>=2)
        {
            count=count+1;
        }
        temp=0;
    }
    printf("%d",count);
}
