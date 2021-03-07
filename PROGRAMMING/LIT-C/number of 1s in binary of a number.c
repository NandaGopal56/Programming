#include"stdio.h"
main()
{
    int n,c=0;
    printf("enter a number");
    scanf("%d", &n);
    while(n>0)
    {
        c++;
        n=n&n-1;
    }
    printf("number of one's in binary of this number is %d",c);
}
