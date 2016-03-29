/*************************************************************************
    > File Name: jingdian26.c
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2016年03月26日 星期六 14时15分47秒
 ************************************************************************/
/*递归求５的阶乘*/
#include<stdio.h>
long factorial(int n);

main(){
	printf("the factorial number is %ld\n",factorial(5));
}
long factorial(int n){
	long result;
	if(n==0 || n==1){
		result = 1;
	}else{	
		result = factorial(n-1) * n;  // 递归调用
	  }
    return result;
	}
