#include"stdio.h"
main()
{
    int n,s=0;
    printf("enter a  number");
    scanf("%d", &n);
    while(n>0)
    {
       s=s+n%10;
       n=n/10;
    }
    printf("addition of each digits in this number is %d",s);
}
