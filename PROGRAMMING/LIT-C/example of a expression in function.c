#include"stdio.h"
int sum(int,int);
int mul(int,int);
int div(int,int);
main()
{
    int x;
    x=sum(mul(5,9),div(8,2));
    printf("%d",x);
}
int sum(int a,int b)
{
    int c=a+b;
    return c;
}
int mul(int a,int b)
{
    int c=a*b;
    return c;
}
int div(int a,int b)
{
    int c=a/b;
    return c;
}
