#include"stdio.h"
#include"math.h"
main()
{
    int n,r=0,p,i,m;
    printf("enter a number");
    scanf("%d", &n);
    printf("enter no of digits to be replaced by ");
    scanf("%d", &p);
    while(n>0)
    {
        r = r*10 + n%10;
        n = n/10;
    }
   for(i=0;i<p;i++)
   {
       m = (r/(int)pow(10,i))%10;
       r = r+ (9-m)*pow(10,i);
   }
    while(r>0)
    {
        n = n*10 + r%10;
        r = r/10;
    }
    printf("%d",n);
}
