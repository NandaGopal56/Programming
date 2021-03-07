#include"stdio.h"
main()
{
    int n,s=0,r;
    printf("enter a number");
    scanf("%d",&n);
    while(n>0)
    {
        r=n;
        while(r>0)
        {
            s=s+r%10;
            r=r/10;
        }
        if(s<10)
            break;
        n=s;
        s=0;
    }
    printf("%d",s);
}
