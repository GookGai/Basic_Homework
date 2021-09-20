#include <stdio.h>

int main()
{
	int i;
  printf("0123456789abcdefghij0123456789abcdefghij0123456789abcdefghij0123456789abcdefghij\n");
  for(i=0;i<4;i++){printf("%20d",1234567890);}
  for(i=0;i<4;i++){printf("%-20d",1234567890);}
  for(i=0;i<4;i++){printf("%20d",1234567890);}
  for(i=0;i<10;i++){printf("12345678");}
  printf("%9d%9d%9d%9d%9d%9d%9d%9d%16d%16d%16d%16d%16d",1,12,123,1234,12345,123456,1234567,12345678,12345678,12345678,12345678,12345678,12345678);
  
  return 0;
}

