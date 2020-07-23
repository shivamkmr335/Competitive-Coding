#include<stdio.h>
int main()
{
    char a,b;
    int c=0;
    char str[100];
    scanf("%s",&str);
    int len=strlen(str);
    for(a=0;a<(len-7);a++)
    {
        if(str[a]==str[a+1] && str[a]==str[a+2] && str[a]==str[a+3] && str[a]==str[a+4] && str[a]==str[a+5] && str[a]==str[a+6] )
        {
            printf("YES");
            c=5;
            break;
        }
    }
    if(c!=5)
    {
        printf("NO");
    }
}
