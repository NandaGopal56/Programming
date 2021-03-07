
#include"stdio.h"
int powerof2(int);
main()
{
    int n,x,i;
    printf("enter upper limit");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {

        x=powerof2(i);
        if(x==0)
           printf("%d ",i);
    }

}
int powerof2(int n)
{
    return n&n-1;
}
