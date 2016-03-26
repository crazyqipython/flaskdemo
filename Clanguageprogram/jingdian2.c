/*************************************************************************
    > File Name: jingdian2.c
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2016年03月23日 星期三 21时42分23秒
 ************************************************************************/
/*求利润提成低于１０万元，低于２０万元，低于４０万元*/
#include<stdio.h>
void main(){
	long int i;
	int bonus1,bonus2,bonus4,bonus6,bonus100,bonus;
	scanf("%ld",&i);
	bonus1=100000*0.1;
	bonus2=bonus1+100000*0.75;
	bonus4=bonus2+200000*0.5;
	bonus6=bonus4+200000*0.3;
	bonus100=bonus6+400000*0.15;
	if(i<100000){
		bonus=i*0.1;
	}
	if(i<200000)
		bonus=(i-100000)*0.1+bonus1;
	if(i<400000)
		bonus=(i-200000)*0.05+bonus2;
	if(i<600000)
		bonus=(i-400000)*0.03+bonus4;
	if(i<1000000)
		bonus=(1000000-600000)*0.015+bonus6;
    else	
		bonus=bonus100+(i-1000000)*0.01;
    printf("bonus=%d\n",bonus);
}
