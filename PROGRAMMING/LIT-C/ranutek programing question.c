#include"stdio.h"
int div(int , int);
main()
{
    int i,j,total=0;
    int index1,index2,index3,index4,final_sum;
    scanf("%d",&i);
    scanf("%d",&j);
    while(i<=j)
    {
        total=total+i;
        i++;
    }
    index1=div(1,2)+div(2,2)+div(3,2)+div(4,2)+div(5,2);
    index2=div(1,3)+div(2,3)+div(3,3)+div(4,3)+div(5,3);
    index3=div(1,4)+div(2,4)+div(3,4)+div(4,4)+div(5,4);
    index4=div(1,5)+div(2,5)+div(3,5)+div(4,5)+div(5,5);
    final_sum=total+index1+index2+index3+index4;
    printf("%d",final_sum);
}

int div(int x , int y)
{
    int z = x/y;
    return z;
}
