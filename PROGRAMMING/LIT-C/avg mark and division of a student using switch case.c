#include"stdio.h"
main()
{
    int math,eng,mil,geo,his,sci,avg,n;
    printf("enter your mark in math");
    scanf("%d", &math);
    printf("enter your mark in english");
    scanf("%d", &eng);
    printf("enter your mark in geography");
    scanf("%d", &geo);
    printf("enter your mark in history");
    scanf("%d", &his);
    printf("enter your mark in science");
    scanf("%d", &sci);
    printf("enter your mark in mil");
    scanf("%d", &mil);
    avg=(math+eng+mil+geo+his+sci)/6;
    printf("\n your avrage mark is %d",avg);
    n=avg/10;
    switch(n)
    {
        case 9:
        case 8:
        case 7:
        case 6:
        printf("\n first division");
        break;
        case 5:
        printf("\n second division");
        break;
        case 4:
        printf("\n third division");
        break;
        default:
        printf("\n fail");
    }
}


