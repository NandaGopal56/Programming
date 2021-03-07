#include"stdio.h"
main()
{
    int i,j,limit;
    int *prime;
    printf("enter the limit :\n");
    scanf("%d",&limit);
    prime = malloc(sizeof(int) * limit);
    for(i=2;i<limit;i++)
    {
        prime[i]=1;
    }

    for(i=2;i<limit;i++)
    {
        if(prime[i])
        {
            for(j=i*i;j<limit;j=j+i)
            {
                prime[j]=0;
            }
        }
    }

    for(i=2;i<limit;i++)
    {
        if(prime[i])
            printf("%d ",i);
    }
}
