
#include"stdio.h"
int prime(int);
main()
{
    int n,x,i;
    printf("enter upper limit");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {

        x=prime(i);
        if(x==2)
           printf("%d ",i);
    }

}
int prime(int n)
{
    int i=1,c=0;
    while(i<=n)
    {
        if(n%i==0)
            c++;
        i++;
    }
    return c;
}

