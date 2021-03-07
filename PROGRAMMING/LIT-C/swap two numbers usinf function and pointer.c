#include"stdio.h"
void swap(int *,int*);
main()
{
    int a,b;
     printf("enter any two number");
    scanf("%d %d",&a,&b);
    swap(&a,&b);
    printf("%d %d",a,b);
}
void swap(int *p,int*q)
{
    int temp;
    temp=*p;
    *p=*q;
    *q=temp;
}
