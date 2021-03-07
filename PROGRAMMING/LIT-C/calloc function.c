#include"stdio.h"
#include"stdlib.h"
main()
{
    int *ptr;
    int  i,n;

    printf("enter the limit of the array:\n");
    scanf("%d",&n);

    ptr=(int*)calloc(n,sizeof(int));

    if(ptr==NULL)
    {
        printf("memory not created:\n");
        exit(0);
    }

    else
    {
        printf("enter elements to the array:\n");
        for(i=0;i<n;i++)
            scanf("%d",&ptr[i]);

        printf("the elements in the array are:\n");
        for(i=0;i<n;i++)
            printf("%d ",ptr[i]);
    }
}
