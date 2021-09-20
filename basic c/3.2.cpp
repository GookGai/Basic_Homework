#include<stdio.h>
int main()
{
	int a,b,c;
    printf(" *** Show a number in variety formats. ***\nEnter integer : ");
    scanf("%d",&a);
    printf("Char	-> %c\n",a);
    printf("Float	-> %.2f\n",a*1.0);
    printf("Int*2.5	-> %.4f\n",a*2.5);
    return 0;
}
