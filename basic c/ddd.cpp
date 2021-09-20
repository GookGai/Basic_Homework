#include <stdio.h>

int main() {
   int b,min=99999999,i=1;
   while (1)
    { 	
		printf("Enter number :");
       	scanf("%d",&b);
       	i++;
       	if (b<min){
       		if(b<0&&b%2==0)
       			break;
	   	min=b;
		}
	   	printf("Min = %d\n",min);	
   }
   printf("Min = %d\n",b);
   printf("---Data Complete---\n");
	printf("All numbers = %d",i);
   return 0;
}
