/*************************************************************************
    > File Name: jingdian4.c
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2016年03月24日 星期四 13时37分05秒
 ************************************************************************/
/*输入年月日，输出当前是一年当中的第几天*/
#include<stdio.h>
void main(){
	int year,month, day,leap,sum_month;
	scanf("%d%d%d",&year,&month,&day);
	switch(month){
		case 1:sum_month=0;break;
		case 2:sum_month=31;break;
		case 3:sum_month=59;break;
		case 4:sum_month=90;break;
		case 5:sum_month=120;break;
		case 6:sum_month=151;break;
		case 7:sum_month=181;break;
		case 8:sum_month=212;break;
		case 9:sum_month=243;break;
		case 10:sum_month=273;break;
		case 11:sum_month=304;break;
		case 12:sum_month=334;break;
        default:printf("data error\n");break;
	}
	sum_month=sum_month+day;
	if(year%400==0||(year%4==0&&year%100!=0)) 
	   leap=1;
	else
		leap=0;
	if (leap==1&&month>2)
		sum_month++;                  /*用leap做为标志，根据标记再做运算*/
	printf("It is the %dth day.\n",sum_month);
	
}
