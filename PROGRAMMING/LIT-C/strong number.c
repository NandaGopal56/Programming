#include"stdio.h"
main()
{
    int n,s=0,r,m;
    printf("enter a  number");
    scanf("%d", &n);
    m=n;
    while(n>0)
    {
        r=n%10;
        s=s+fact(r);
        n=n/10;
    }
    if(s==m)
        printf("strong number");
    else
        printf("not a stong number");
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
