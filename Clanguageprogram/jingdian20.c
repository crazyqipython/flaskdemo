/*************************************************************************
    > File Name: jingdian20.c
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2016年03月26日 星期六 09时28分23秒
 ************************************************************************/
/*一个球从100米落下，每次回弹前一次的一半，求第10次弹多高*/
#include<stdio.h>
main(){
	float sn=100.0,hn=sn/2;
	int i;
	for (i=2;i<=10;i++){
		sn=sn +2*hn;
		hn=hn/2;
	}
	printf("第10次弹%f\n",hn);
	printf("总共弹%f\n",sn+hn);
}

