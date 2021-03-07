#include"stdio.h"
main()
{
    int i=1;
    while(i<=5)
    {
        printf("hello\n");
       continue;                         //continue statement transfer the control again to the beginning of he current loop
        printf("bye\n");
        i++;
    }
    printf("good bye\n");
}
                                        //the output will print "hello" infinite times
