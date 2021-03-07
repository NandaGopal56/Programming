#include"stdio.h"
int fact(int);
main()
{
    int x,i;
    float n=0;
    printf("enter maximum limit of the sequence");
    scanf("%d", &x);
    for(i=1;i<=x;i++)
    {
       n=n+(float)i/fact(i);
    }

    printf("%f",n);
}
int fact(int x)
{

    int f=1;
    while(x>0)
    {
        f=f*x;
        x--;
    }
    return f;
}

