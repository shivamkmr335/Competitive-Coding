#include<stdio.h>
#include<string.h>
main()
{
    char str[100];
    scanf("%s",&str);
    if(strstr(str,"1111111") || strstr(str,"0000000"))
        printf("YES");
    else
        printf("NO");
}
