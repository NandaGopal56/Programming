#include"stdio.h"
int reverse(int);
main()
{
    int n,x;
    printf("enter a number");
    scanf("%d",&n);
    x=reverse(n);
    printf("%d",x);
}
int reverse(int n)
{
    int r=0;
    while(n>0)
    {
        r=r*10 + n%10;
        n=n/10;
    }
    return r;
}


