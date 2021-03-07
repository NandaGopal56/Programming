#include"stdio.h"
main()
{
    char c;
    printf("enter a character");
    scanf("%C", &c);
    if (c == 'a' || c == 'e'  || c == 'i' || c == 'o' || c == 'u')
        printf("vowel");
    else
        printf("not vowel");
}
