/*************************************************************************
    > File Name: ./jingdian15.c
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2016年03月24日 星期四 21时37分38秒
 ************************************************************************/
/*三目运算符的运用*/
#include<stdio.h>
main(){
	int score;
	char grade;
	printf("enter a 分数\n");
	scanf("%d",&score);
    grade=score>=90?'A':(score>=60?'B':'C');
	printf("%d belongs to %c\n",score,grade);
}
