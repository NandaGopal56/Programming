#include"stdio.h"
int fact (int m);
main()
{
    int i,n,x;
    printf("enter a number");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        x=fact(i);
        printf("%d \n",x);
    }

}

int fact(int m)
{
    int f=1,j;
    for(j=1;j<=m;j++)
    {
        f=f*j;
    }
    return f;
}
