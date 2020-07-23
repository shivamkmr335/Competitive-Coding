#include<stdio.h>
main()
{
    int a,b,i,j,count=0;
    scanf("%d%d",&a,&b);
    int arr[a][a];
    for(i=1;i<=a;i++)
    {
        for(j=1;j<=a;j++)
        {
            arr[i-1][j-1]=i*j;
            if((arr[i-1][j-1])==b)
                count++;
        }
    }
    printf("%d",count);
}
