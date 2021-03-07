#include"stdio.h"
main()
{
    int i=1;
    while(i<=5)
    {
        printf("hello\n");
        break;                     //break statement transfer the control just outside the current loop
        printf("bye\n");
        i++;
    }
    printf("good bye\n");
}
