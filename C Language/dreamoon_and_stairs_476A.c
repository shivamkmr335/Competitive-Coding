#include<stdio.h>
main()
{
    int temp1,temp2,a,b,i=0,sum =-1;
    scanf("%d",&a);
    scanf("%d",&b);
    temp1=a/2;
    temp2=a%2;
    while((i<=a)&&(temp1>=0)&&(temp2>=0))
    {
        if((temp1 + temp2)%b==0)
        {
            sum=temp1+temp2;
            break;
        }
        else
            {
                temp1 = temp1 - 1;
                temp2 = temp2 + 2;
            }
        i++;
    }

    printf("%d",sum);
}
