#include<stdio.h>

int main() {
	int i;
	printf("Hello, world!\n");
    printf("Hello, Ladkrabang\n");
    printf("Hello, Computer Programming\n");
    printf("one\ttwo\tthree\tfour\tfive\tHallelujah\n");
    for(i =0;i<10;i++){
    	if(i<5){
    		printf("%-16s","12345678");	
		}
    	else{
    		printf("%16s","12345678");
		}
	}



    return 0;

}
