/*************************************************************************
    > File Name: jingdian24.c
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2016年03月26日 星期六 13时44分04秒
 ************************************************************************/
/*求2/1,3/2,5/3,8/5前20个数的和*/
#include<stdio.h>
main(){
	int i;
	float sn=0.00,hn,t1,t2,t3;
	for (i=1;i<=20;i++){
		if(i==1){
			t1=i+1;
			hn=(i+1)/1;
			sn=hn+sn;
		}
		
		if(i==2){
			t2=i+1;
			hn=(i+1)/2;
			sn=hn+sn;
		}
		if(i>=3){
		    t3=t1+t2;
			hn=t3/t2;
			sn=t3+sn;
			t1=t2;
			t2=t3;
	}
	}
	printf("the sum of twenty is %9.6f\n",sn);
}
