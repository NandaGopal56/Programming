#include"stdio.h"
int bbsr(int);
main()
{
    bbsr(3);
}
int bbsr(int n)
{
    if(n>0)
    {
        bbsr(n-1);
         bbsr(n-1);
         printf("%d ",n);
    }
}
