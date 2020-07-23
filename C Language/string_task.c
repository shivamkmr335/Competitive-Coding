#include<stdio.h>
#include<string.h>
main()
{
char a[101];
scanf("%s",&a);
strlwr(a);
int i,b=strlen(a);
for(i=0;i<b;i++)
{
    if(a[i]!='a'&& a[i]!='e'&& a[i]!='i'&& a[i]!='o'&& a[i]!='u'&& a[i]!='y')
    {
        printf(".%c",a[i]);
    }
}
}
