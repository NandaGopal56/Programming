#include"stdio.h"
main()
{
    int x;
    printf("enter number between 1 to 5\n");
    scanf("%d",&x);
    switch(x)
    {

case 1:
    printf("one");

case 1:                       //duplicate case is not allowed
    printf("one");

case 3:
    printf("three");

case 4:
    printf("four");

case 5:
    printf("five");

    }
}


