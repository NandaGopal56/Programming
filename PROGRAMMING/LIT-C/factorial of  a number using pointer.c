#include"stdio.h"
main()
{
    int n,f=1;
    int *p=&n ,*q=&f;
    printf("enter a number");
    scanf("%d",p);
    while(*p>0)
    {
        *q=*q * *p;
        (*q)--;
    }
    printf("%d",*q);
}
