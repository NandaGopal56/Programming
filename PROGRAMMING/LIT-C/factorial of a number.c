#include"stdio.h"
main()
{
    int n,f=1;
    printf("enter a  number");
    scanf("%d", &n);
     while(n>0)
    {
        f=f*n;
        n--;
    }
    printf("fatorialof this number is %d",f);
}
