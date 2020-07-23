#include<stdio.h>
int main()
{
    int ascii,choice=0;
    char input;
    printf("enter 1 to enter ASCII or 2 to enter character:\n");
    scanf("%d",&choice);
    if(choice == 1)
    {
        printf("enter the ascii value:\n");
        scanf("%d",&ascii);
        printf("the char value of %d is  %c\n",ascii,ascii);
    }
    if(choice == 2)
    {
        printf("enter the char value:");
        scanf(" %c",&input);
        printf("the ascii value of %c is %d\n",input,input);
    }

    return 0;
}
