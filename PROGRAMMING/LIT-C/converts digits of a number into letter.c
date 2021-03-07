#include"stdio.h"
main()
{
    int n,r=0;
    printf("enter a number");
    scanf("%d",&n);
    while(n>0)
    {
        r=r*10+n%10;                     //logic to reverse a number
        n=n/10;
    }
    while(r>0)
    {
        n=r%10;
        switch(n)
        {
        case 1:
            printf("one\t");
            break;
        case 2:
            printf("two\t");
            break;
        case 3:
            printf("three\t");
            break;
        case 4:
            printf("four\t");
            break;
        case 5:
            printf("fiive\t");
            break;
        case 6:
            printf("six\t");                      //convert digits into letters
            break;
        case 7:                                    //123=one two three
            printf("seven\t");
            break;
        case 8:
            printf("eight\t");
            break;
        case 9:
            printf("nine\t");
            break;
        default:
            printf("zero\t");

        }
        r=r/10;
    }

}
