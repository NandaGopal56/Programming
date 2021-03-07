#include"stdio.h"
main()
{
    int i,j,sum=0;

    printf("enter upper and lower limits");
    scanf("%d%d",&i,&j);

    while(i<=j)
    {
        sum=sum+i;
        i++;
    }
    printf("%d",sum);
}
