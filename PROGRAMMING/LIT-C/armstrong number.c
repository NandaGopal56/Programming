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
        s=s+r*r*r;
        n=n/10;
    }
    if(s==m)
        printf("armstrong number");
    else
        printf("not a armstrong number");
}
