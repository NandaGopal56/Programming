#include"stdio.h"
#include"math.h"
main()
{
    int n,r,i=0,s=0;
    printf("enter number in binary format");
    scanf("%d", &n);
    while(n>0)
    {
        r=n%10;
        s=s+r*pow(2,i);                      //logic to covert binary to decimal
        i++;
        n=n/10;
    }
    printf("%d",s);
}
