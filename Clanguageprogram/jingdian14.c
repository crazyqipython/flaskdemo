/*************************************************************************
    > File Name: jingdian14.c
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2016年03月24日 星期四 16时30分04秒
 ************************************************************************/
/*将一个数因数分解*/
#include<stdio.h>
void main(){
	int i,j;
	scanf("%d",&i);
	for (j=2;j<=i;j++){
		while(i!=j){
		if(i%j==0){
			printf("%d*",j);
			i=i/j;
		}
		else
			break;
		}
	}
	printf("%d\n",i);     /*最后一个因子还没有赋值*/
}

