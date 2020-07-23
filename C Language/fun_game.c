#include<stdio.h>
int main()
{
    int i,a=51,b=0,temp=0;
    while(a>=1)
    {
        printf("enter your choice");
        scanf("%d",&b);
        if(b<=4 && b>0)
        {
            if(b<=a)
            {
                if(a<=1)
                {
                    break;
                }
                temp=5-b;
                printf("the computer entered: %d\n",temp);
                a=a-5;
                printf("the no of balls remaining are: %d\n",a);
            }
            else
                printf("the are not sufficient balls\n");
        }
        else
            printf("please enter choice less than 4\n");
     }
printf("the last ball will be picked by the user, so computer won the game");
return 0;
}
