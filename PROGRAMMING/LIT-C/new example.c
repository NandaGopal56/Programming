#include"stdio.h"
main()
{
    int i,j=1;
    for(i=1;i<=5;i++)
    {
        while(j<=5)
        {
            printf("%d\n",i+j);
            if(i==j)
                break;
            j++;
        }
    }
}
