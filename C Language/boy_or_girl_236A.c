#include<stdio.h>
main()
{
    char c[100];
    scanf("%s",&c);
    int i,j,k,l,count=0;
    i=strlen(c);
    for(j=1;j<i;j++)
    {
        for(k=(j-1);k>=0;k--)
        {
            if(c[j]==c[k])
                count++;
        }
    }
    l=i-count;
    printf("%d\n",l);
    if(l%2==0)
    printf("CHAT WITH HER!");
    else
    printf("IGNORE HIM!");
}
