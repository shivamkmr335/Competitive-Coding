#include<stdio.h>
int main()
{
    int i,j,r,c;
    printf("enter the rows and columns of matrices:\n");
    scanf("%d%d",&r,&c);
    int arr1[r][c],arr2[r][c],arr3[r][c];
    printf("enter the values of 1st matrix:\n");
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            printf("%d X %d :\t",i,j);
            scanf("%d",&arr1[i][j]);
        }
    }
     printf("enter the values of 2st matrix:\n");
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            printf("%d X %d :\t",i,j);
            scanf("%d",&arr2[i][j]);
        }
    }
    printf("the resultant matrix is:\n");
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            printf("%d\t",arr1[i][j]-arr2[i][j]);

        }
        printf("\n");
    }

    return 0;
}
