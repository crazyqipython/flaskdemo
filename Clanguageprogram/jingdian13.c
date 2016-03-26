/*************************************************************************
    > File Name: jingdian13.c
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2016年03月24日 星期四 16时12分30秒
 ************************************************************************/
/*打印水仙花数即每一位数的三位数立方和等于自身*/
#include<stdio.h>
void main(){
	int i,hun,tenth,oneth;
	for (i=100;i<1000;i++){
		hun=i/100;
		tenth=(i%100)/10;
		oneth=i%10;
		if (i==(hun*hun*hun+tenth*tenth*tenth+oneth*oneth*oneth))
			printf("%d\n",i);
	}
}
