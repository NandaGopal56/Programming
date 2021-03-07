#include"stdio.h"
int prime (int);
main()
{
    int x,y,i,k,j=0,arr[500000],counter=0;
    for(i=0;i<50000;i++)
    {
        arr[i]=0;
    }
    printf("enter two limits\n");
    scanf("%d%d",&x,&y);
    for(i=x;i<=y;i++)
    {
       k = prime(i);
       if(k == 1)
       {
           arr[j]=i;
           j++;
       }
    }
   for(i=0;i<10000;i++)
   {
       for(j=i+1;j<10000;j++)
       {
           if(arr[j]-arr[i]==6)
           {
               printf("(%d %d) ",arr[i],arr[j]);   //p,p+6
               counter++;
           }
       }
   }
   printf("\ntotal sexy pairs are = %d",counter);
}

int prime (int p)
{
    int i,count=0;
    for(i=1;i<=p;i++)
    {
        if(p%i==0)
        {
            count++;
        }
    }
     if(count==2)
          return 1;
        else
            return 0;
}
