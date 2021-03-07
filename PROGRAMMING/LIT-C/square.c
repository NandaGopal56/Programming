#include<stdio.h>
int square(int x);
main()
{
    int m,n;
    printf("enter a number");
    scanf("%d",&m);
    n=square(m);
    printf("%d",n);


}
int square(int z )
{
    return z*z;

}

