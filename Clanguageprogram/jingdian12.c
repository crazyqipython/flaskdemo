/*************************************************************************
    > File Name: jingdian12.c
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2016年03月24日 星期四 15时23分22秒
 ************************************************************************/
/*计算１０１～200的素数*/
#include<stdio.h>
#include<math.h>
void main(){
	int i,j,flag=1;
	for (i=101;i<200;i++){
		for (j=2;j<=sqrt(i);j++){
			if(i%j==0){
			    flag=0;
			    break;
			}
		}
		if (flag)
		    printf("%d\n",i);
		flag=1;

	}
}
