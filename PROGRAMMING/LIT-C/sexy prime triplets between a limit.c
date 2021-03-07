#include"stdio.h"
int prime (int);
main()
{
    int x,y,i,k,l,j=0,arr[1000],counter=0;
    for(i=0;i<1000;i++)
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
   for(i=0;i<1000;i++)
   {
       for(j=i+1;j<1000;j++)
       {
           for(l=j+1;l<1000;l++)
           {
           if(arr[l]-arr[i]==12 && arr[j]-arr[i]==6)    //p,p+6,p+12
           {

               printf("(%d %d %d) ",arr[i],arr[j],arr[l]);
               counter++;

           }
           }
       }
   }
   printf("\ntotal sexy triplets are = %d",counter);
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
