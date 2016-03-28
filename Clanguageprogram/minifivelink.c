//this is mini five link game,three link//
#include<stdio.h>
#include<string.h>

enum{NOUGHTS,CROSSES,BORDER,EMPTY};
enum{HUMANWIN,COMPWIN,DRAW};

const int ConverTo25[9]={
	6, 7,8,
	11,12,13,
	16,17,18,
};                                         /*use the array to convert the*/ 

/*initial the 5*5 board*/
void InitialiseBoard(int *board){
       int index;

	   for (index=0;index<25;++index){
		   board[index]=BORDER;
	   }
	   
	   for (index=0;index<9;++index){
		   board[ConverTo25[index]]=EMPTY; /*use the array ConverTo25 inser\
											 t EMPTTY in board[6~15]*/
	   }
} 

/*print the format board*/
void PrintBoard(const int *board){
	int index=0;
	char pceChars[] = "OX|-";
	printf("\n\nBoard:\n");
	for (index=0;index<9;++index){
		if(index!=0 && index%3==0){
			printf("\n\n");
		}
		printf("%4c",pceChars[board[ConverTo25[index]]]); /*input the char*/

	}
	printf("\n");
}

/*a function if the 3*3 board is empty*/
int HasEmpty(const int *board) {
	int index=0;

	for (index=0; index < 9; ++index){
		if (board[ConverTo25[index]]==EMPTY)
			return 1;
		}
	return 0;
	}

/* take sq agrument as index and insert side of NOUGHTS or CROSSES*/
void MakeMove(int *board, const int sq, const side){
	board[sq]=side;
}

/*computermove when the square is empty then input the number*/
int GetComputerMove(const int *board) {
	int index=0;
	int numFree=0;
	int availableMoves[9];
	int randMove = 0;

	for (index=0; index < 9; ++index){
		if ( board[ConverTo25[index]]==EMPTY){
			availableMoves[numFree++] = ConverTo25[index]; //first assain 0
		}
	}

	randMove = (rand() % numFree);                          //rand move generate 0~numfree.
	return availableMoves[randMove];             
}

int GetHumanMove(const int *board) {

	char userInput[4];                      /*define a four lenth char arr\
											  ay store the user input*/
	int moveOk=0;
	int move=-1;

	while(moveOk==0) {

		printf("Please enter a move from 1 to 9:");
		fgets(userInput, 3, stdin);
		fflush(stdin);                       /*delete the cathe value*/

		if(strlen(userInput) != 2){
			printf("Invalid strlen()\n");
			continue;
		}

		if ( sscanf(userInput, "%d", &move) !=1) {
			move = -1;
			printf("Invalid sscanf()\n");
			continue;
		}

		if (move < 1 || move >9 ) {
			move = -1;
			printf("invalid range\n");
			continue;                   
		}                                //three if conditions to take a p\
		                                   proper input.

		move--;                          //because the array start form o*/

	    if ( board[ConverTo25[move]]!=EMPTY) {
			move=-1;
			printf("Square not available\n");
			continue;
		}                                   //if the board is empty
		moveOk=1;
	}
	printf("Making move...%d\n",(move+1));
	return ConverTo25[move];
}

/*the game start here*/
void RunGame(){
                                            
	int GameOver=0;
	int Side = NOUGHTS; 
	int LastMoveMade=0;
	int board[25];                           /*define a board array*/ 

	InitialiseBoard(&board[0]);              /*call the initialise board*/
	PrintBoard(&board[0]);                   /*call the printboard*/

	while(!GameOver){                        /*make move side by side unti\
											   the gameover*/
		if(Side==NOUGHTS){
			LastMoveMade = GetHumanMove(&board[0]);
			MakeMove(&board[0],LastMoveMade,Side);
			Side=CROSSES;
		}else{
			LastMoveMade=GetComputerMove(&board[0]);
			MakeMove(&board[0],LastMoveMade,Side);
			Side=NOUGHTS;
			PrintBoard(&board[0]);            /*reprint the board by new va\
											   lue*/
		}
		if(!HasEmpty(board)) {
			printf("Game over!\n");
			GameOver=1;
			printf("It's a draw\n");
		}
	}
}

int main(){

	srand(time(NULL));                     /*generate a seed rand use time\
											 tamp*/
	RunGame();

	return 0;
}
