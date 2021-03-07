#include"math.h"
#include"stdio.h"
main()
{
    int i,j,k,n;
    for(i=1;i<=3;i++)
    {
        for(j=1;j<=3;j++)
        {
            for(k=1;k<=3;k++)
            {
                if(i!=j && i!=k && j!=k)
                {
                    n=i*pow(10,2) + j*pow(10,1) + k*pow(10,0);
                    printf("%d\n",n);
                }
            }
        }

    }
}
