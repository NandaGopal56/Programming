#include"stdio.h"
#include"stdlib.h"
main()
{
    int i,j;
    scanf("%d%d",&i,&j);
    div_t output;
   output = div(i, j);

    printf("%d",output.quot);
}
