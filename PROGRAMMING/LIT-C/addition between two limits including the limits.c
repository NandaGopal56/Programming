#include"stdio.h"
main()
{
    int i=0,sum=0,a,b,j,k,arr[6]={0,0,0,0,0,0};
    printf("enter two limits\n");
    scanf("%d%d",&a,&b);
    j=a;k=b;
    while(a<=b)
    {
        arr[i]=a;
        a++;
        i++;
    }
    for(i=0;i<=5;i++)
    {
        sum=sum+arr[i];
    }
    printf("%d\n",sum);
    printf("%d",sum+j+k);
}
