
#include"stdio.h"
main()
{
    int n,s=0;
    printf("enter a number");
    scanf("%d",&n);
    while(n>0)
    {
        s=s*10+n%10;                     //logic to reverse a number
        n=n/10;
    }
    printf("%d",s);

}
