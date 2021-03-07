#include"stdio.h"
int fact(int);
main()
{
    int n,x;
    printf("enter a number");
    scanf("%d",&n);
    x=fact(n);
    printf("%d",x);
}
int fact(int n)
{
    int f=1;
    while(n>0)
    {
        f=f*n;
        n--;
    }
    return f;
}

