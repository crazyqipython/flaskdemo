//this is mini five link game,three link//
#include<stdio.h>
#include<string.h>

enum{NOUGHTS,CROSSES,BORDER,EMPTY};
//enum{HUMANWIN,COMPWIN,DRAW};

const int InMiddle=4;                     //Getnextbest function use.
const int Corners[4] = {0,2,6,8};
const int Directions[4]={1,5,4,6};       //four directions condition.
const int ConverTo25[9]={
	6, 7,8,
	11,12,13,
	16,17,18,
};                                         /*use the array to convert the*/ 

int GetNumForDir(int startSq, const int dir, const int *board, const int us){
	int found=0;
	while (board[startSq]!=BORDER){
		if(board[startSq] !=us){
			break;
		}
		found++;
		startSq+=dir;
	}
	return found;
}
 
int FindThreeInARow(const int *board, const int ourindex, const int us){

	int DirIndex =0;
	int Dir=0;
	int threeCount =1;                                                               //itself is one.

	for (DirIndex = 0; DirIndex<4; ++DirIndex){
		Dir = Directions[DirIndex];                                                  //get one direction in four directions in one loop
		threeCount+=GetNumForDir(ourindex+Dir,Dir, board,us);                       //positive direction call getnumfor dir ourindex+dir \
		                                                                                is the next elment.
		threeCount+=GetNumForDir(ourindex+Dir*-1,Dir*-1,board,us);                  //call function by negitive direction.
		if (threeCount ==3){
            break;
		}
		threeCount=1;
	}
	return threeCount;
}

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

int GetNextBest(const int *board){

	int ourMove=ConverTo25[InMiddle];
	if (board[ourMove]==EMPTY) {
		return ourMove;
	}
	int index=0;
	ourMove=-1;

	for (index=0; index<4; index++){
		ourMove=ConverTo25[Corners[index]];
		if(board[ourMove] == EMPTY)
			break;
		ourMove = -1;
	}
	return ourMove;
}

int GetWinningMove(int *board,const int side) {
	
	int ourMove=-1;
	int winFound =0;
	int index=0;

	for (index=0; index<9; ++index) {
		if ( board[ConverTo25[index]]==EMPTY){
			ourMove=ConverTo25[index];
			board[ourMove]=side;                                       //find a available move and take to the FindThreeInARow fuction.

			if (FindThreeInARow(board,ourMove, side)==3){
				winFound =1;
			}
			board[ourMove]=EMPTY;                                    //rewrite to empty.
			if (winFound==1) {
				break;
			}
			ourMove=-1;
		}
	}
	return ourMove;
}

/*computermove when the square is empty then input the number*/
int GetComputerMove(int *board,const int side) {                     //take two agruments
	int index=0;
	int numFree=0;
	int availableMoves[9];
	int randMove = 0;

	randMove=GetWinningMove(board,side);                                   //call the getwinningmove function.
	if(randMove !=-1){
		return randMove;
	}

	randMove = GetWinningMove(board,side^1);          //block human winning\
			                                            move
	if(randMove!=-1){
		return randMove;
	}

	randMove=GetNextBest(board);
	if(randMove!=-1){
		return randMove;
	}

	randMove=0;
	for (index=0; index < 9; ++index){
		if ( board[ConverTo25[index]]==EMPTY){
			availableMoves[numFree++] = ConverTo25[index]; //first assain 0
		}
	//InitialiseBoard(&board[0]);              /*call the initialise board*/
	//PrintBoard(&board[0]);                   /*call the printboard*/

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
			LastMoveMade=GetComputerMove(&board[0],Side);
			MakeMove(&board[0],LastMoveMade,Side);
			Side=NOUGHTS;
			PrintBoard(&board[0]);            /*reprint the board by new va\
											   lue*/
		}
		
		//if three in a row  game is over
		if (FindThreeInARow(board,LastMoveMade,Side^1)==3){
			printf("Game over!");
			GameOver=1;
			if (Side==NOUGHTS) {
				printf("Computer Win\n");
			}else{
				printf("Human Wins\n");
			}
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
