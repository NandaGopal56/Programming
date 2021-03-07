#include"stdio.h"
#include"math.h"
main()
{
    int i,n,s1=0,s2=0;
    for(i=0;i<=100;i++)
    {
        n=i;
        while(n>0)
        {
            s1=s1+n%10;
            n=n/10;
        }
        n=pow(i,2);
        while(n>0)
        {
            s2=s2+n%10;
            n=n/10;
        }
        if(pow(s1,2)==s2)
            printf("%d\n",i);

        s1=0;
        s2=0;

    }
}
