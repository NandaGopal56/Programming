#include"stdio.h"
main()
{
    int n,r=0;
    int *p=&n ,*q=&r;
    printf("enter a number");
    scanf("%d",p);
    while(*p>0)
    {
       *q=*q *10+ *p%10;
       *p=*p/10;
    }
    printf("%d",*q);
}
