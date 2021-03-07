#include"stdio.h"
main()
{
    int a,b,temp;
    printf("enter amy two number");
    scanf("%d %d",&a ,&b);
    temp=a;
    a=b;
    b=temp;
    printf("%d %d",a,b);
}
