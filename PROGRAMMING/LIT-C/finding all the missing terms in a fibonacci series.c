#include"stdio.h"
main()
{
    int a=0,b=1,c,i;
    do
    {
        c=a+b;
        a=b;
        b=c;
        for(i=a+1;i<b;i++)
            printf("%d\n",i);

    }
      while(c<20);
}
