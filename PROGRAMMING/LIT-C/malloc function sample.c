#include"stdio.h"
main()
{
    //this pointer will hold the address of the block created
    int *ptr;
    int n,i,sum=0;

    //get no of elements for the array

    printf("enter no of elements for the array:\n");
    scanf("%d",&n);

    //dynamically allocate memory using malloc
    ptr=(int*)malloc(n*sizeof(int));

    //check if the memory has been successfull allocated by malloc or not
    if(ptr==NULL)
    {
        printf("memory not allocated:\n");
        exit(0);
    }

    else
    {
        printf("memory has been successfully created:\n");
        printf("enter elements to the array:\n");
        for(i=0;i<n;i++)
        {
            scanf("%d ",&ptr[i]);
        }

        printf("the elements are:\n");
        for(i=0;i<n;i++)
        {
            printf("%d ",ptr[i]);
        }
    }




}
