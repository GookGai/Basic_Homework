#include<stdio.h>
int main()
{
	unsigned long a;
    printf(" *** Display integer in different styles ***\nEnter an integer : ");
    scanf("%ld",&a);
    printf("Your number : %ld \n",a);
	printf("variable size = %d bytes\n",sizeof(a));
	printf("last 3 digits : %ld \n",(a%1000)); 
	printf("next 3 digits : %ld \n",(a/1000)%1000);
	printf("next 3 digits : %ld \n",(a/1000000)%1000);
	printf("next 3 digits : %3ld \n",(a/1000000000)%1000);
	printf("comma format  : %ld,%ld,%ld,%ld \n",(a/1000000000)%1000,(a/1000000)%1000,(a/1000)%1000,(a%1000));
    return 0;
}
