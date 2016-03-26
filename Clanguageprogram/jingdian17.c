/*************************************************************************
    > File Name: jingdian17.c
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2016年03月24日 星期四 20时23分05秒
 ************************************************************************/

#include<stdio.h>
main(){
	char c;
	int leters=0,space=0,digit=0,others=0;
	printf("enter a string:");
	while(c=getchar()!='\n'){
		if ((c>='a'&&c<='z')||(c>='A'&&c<='Z'))
			++leters;
		else if (c==' ')
			++space;
		else if(c>='0'&&c<='9')
			++digit;
		else
			++others;
	}
	printf("all in all:char=%d space=%d digit=%d others=%d\n",leters,
			space,digit,others);
}
