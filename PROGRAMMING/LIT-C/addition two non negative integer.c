#include"stdio.h"
main()
{
    int a,b,c;
    while(1)
    {
        printf("enter first positive number");
        scanf("%d", &a);
        if(a<1)
        {
            printf("invalid input\n");
            continue;
        }
        else
            break;
    }
    while(1)
    {
       printf("enter second positive number");
        scanf("%d", &b);
        if(b<1)
        {
            printf("invalid input\n");
            continue;
        }
        else
            break;
    }
    c = a+b;
    printf("addition result is %d",c);

}
