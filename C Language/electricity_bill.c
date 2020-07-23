#include <stdio.h>
int main()
{
    int a,b,i,p;
    float c;
    printf("enter the  no of entries");
    scanf("%d",&a);
    char str[a][20];
    int arr[a];
    for(i=0;i<a;i++)
    {
        printf("enter the %d user name:",i+1);
        scanf("%s",&str[i]);
        printf("total units consumed:");
        scanf("%d",&arr[i]);
    }
    for(i=0;i<a;i++)
    {
        p=arr[i];
        /*if(p<=100)
            {c=p*.4f;}
        else if(p<=200)
            {c=p*.5f;}
        else
            {c=p*.6f;}*/
        int f,g,h;
        ;
        g=
        printf("the %s has to pay %.2f\n",str[i],c+50);
    }
    return 0;
}
