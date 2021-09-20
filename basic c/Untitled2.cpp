#include <stdio.h>

int main() {
	int b;
	printf("Enter number :");
    scanf("%d",&b);
    for(int j=0;j<b;j++){
    	for(int i=0;i<b-j;i++)
    	printf(" ");
		for(int k=0;k<j*2+1;k++)
		printf("*")	;
		printf("\n");
	}
    
    return 0;
}
