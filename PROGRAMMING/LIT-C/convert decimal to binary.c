#include"stdio.h"
#include"math.h"
main()
{
    int n,s,r,i=-1;
     printf("enter number in binary format");
    scanf("%d", &n);
    s=log(n)/log(2)+1;                          //(log n,base 2)+1
    int X[s];
    while(n>0)
    {
        r=n%2;
        i++;
        X[i]=r;
        n=n/2;
    }
    while(i>=0)
    {
        printf("%d",X[i]);
        i--;
    }
}
