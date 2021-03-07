#include"stdio.h"
int addition(int);
int substraction();
int multiplication();
int division();
main()
{
    int m;
    printf("enter your choice\n");
    printf("1.addition 2.substraction 3.multiplication  4.division\n");
    scanf("%d",&m);
    switch(m)
    {
    case 1:
        printf("$$ Addition $$\n");
        addition();
        break;
    case 2:
        printf("$$ Substraction $$\n");
        substraction();
        break;
    case 3:
        printf("$$ Multiplication $$\n");
        multiplication();
        break;
    case 4:
        printf("$$ Division $$\n");
        division();
        break;
    default :
        printf("wrong choice \nenter once again");
    }
}

int addition()
{
  int x,y;
  printf("enter two numbers\n");
  scanf("%d%d",&x,&y);
  printf("result is = %d",x+y);
}

int division()
{
    int x,y,res,rem;
    scanf("%d%d",&x,&y);
    printf("result is = %d",res=x/y);
    printf("reminder is = %d",rem=x%y);
}

int substraction()
{
  int x,y;
  printf("enter two numbers");
  scanf("%d%d",&x,&y);
  printf("result is = %d",x-y);
}

int multiplication()
{
  int x,y;
  printf("enter two numbers");
  scanf("%d%d",&x,&y);
  printf("result is = %d",x*y);
}
