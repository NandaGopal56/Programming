#include"stdio.h"
main()
{
    int n,l=0,s,r;
    printf("enter a  number");
    scanf("%d", &n);
    s=n;
    while(n>0)
    {
        r=n%10;
        if(l<r)
            l=r;
        if(s>r)
            s=r;
        n=n/10;
    }
    printf("addition of each digits in this number is %d",s+l);
}
