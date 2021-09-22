#include <stdio.h>
main(){
	int a,b,max;
	scanf("%d",&a);
	max = 65+a;
	for(int j = 0;j<a;j++){
		for(int i = 0;i<a;i++){
			b = 65+i+j;
			if(b>=max){
				for(int k = 0;k<5-i;k++){
					printf("%c",65+k);
				}
			break;
			}
			else{
				printf("%c",b);
			}
			
		}
		printf("\n");
	}
	
}
