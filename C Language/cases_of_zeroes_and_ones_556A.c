#include<stdio.h>
int main()
{
    int size;
    scanf("%d",&size);
    char ch[size],c,d;
    scanf("%s",&ch)
    for(i=0;i<size;i++)
    {
        for(j=0;j<(size-2);j++)
        {
            c=ch[j];
            d=ch[j+1];
            if(c==d)
            {
                if(j==(size-2))
                {
                    ch[j]='\0';
                    ch[j+1]='\0';
                }
                else
                {
                    ch[j]=ch[j+2];
                    ch[j+1]=
                }
            }
        }
    }

}
