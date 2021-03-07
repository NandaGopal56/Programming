#include"stdio.h"
main()
{
    int x=2;
    switch(x)
    {

        case 1:
        printf("one");
        case 2:
        printf("\ntwo");
        case 3:
        printf("\nthree");
        default:
            printf("\nnone");          //as there is no break so it will print all after match case
    }
}
