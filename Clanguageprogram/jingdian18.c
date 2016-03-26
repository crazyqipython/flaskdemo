/*************************************************************************
    > File Name: jingdian18.c
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2016年03月24日 星期四 19时20分46秒
 ************************************************************************/
/*计算a aa aaa aaaa aaaaa*/
#include<stdio.h>
void main(){
	int i,j=1, count;             /*每一个变量在使用的过程中一定需要赋值。python中不赋值就会出错。c中不赋值，变量的值就是不确定的。*/
	int sum=0,element=0;
	printf("\nplease input a number and a count:");
	scanf("%d%d",&i,&count);
	printf("%d%d\n",count,i);
	while(j<=count){
		element=i+element;         
		sum=element+sum;            
		i=i*10;                      
	    ++j;
	}
	printf("%d\n",sum);
}
