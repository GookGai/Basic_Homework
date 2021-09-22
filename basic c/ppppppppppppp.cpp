#include <stdio.h>
main(){
	int a,n,s,r,ans,sum=0;
	scanf("%d",&a);
	a=a-1;
	for(int i =0;i<5;i++){
		a = a+1;
		n = (a%100)%10;
		s = (a/10)%10;
		r = a/100;
		ans = a - n*100 -s*10 -r; 
		if(ans<0)
		ans = ans*-1;
		sum = sum+ans;
		printf("%d - %d%d%d = %d\n",a,n,s,r,ans);
	}
	printf("sum = %d",sum);
	
	
}
