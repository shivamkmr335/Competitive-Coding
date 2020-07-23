#include<stdio.h>
main()
{
    int no,curr,req;
    scanf("%d%d%d",&no,&curr,&req);
    int i,temp1,temp2,count=0,temp;
    for(i=0;i<no;i++)
    {
        temp1=curr%10;
        temp2=req%10;
        curr=curr/10;
        req=req/10;
        if(temp1>temp2)
            temp=temp1-temp2;
        else
            temp=temp2-temp1;
        if(temp>5)
            count=count+(10-temp);
        else
            count=count+temp;
    }
    printf("%d",count);
}

