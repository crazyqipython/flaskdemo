/*************************************************************************
    > File Name: jingdian16.c
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2016年03月24日 星期四 21时48分18秒
 ************************************************************************/
/*求最大公约数和最小公倍数*/
#include<stdio.h>
void main(){
	int a,lnum,bnum,temp,b;
    scanf("%d %d",&a,&b);
    if (a>b){
		temp=a;
		a=b;
		b=temp;
	}
	lnum=a;
	bnum=b;
	while(a!=0){
		temp=b%a;
		b=a;
		a=temp;               /*the bigest commondivisor*/
	}
	printf("the commondivisor is %d\n",b);
	printf("the 公倍数为：%d\n",b*(lnum/b)*(bnum/b));
}

