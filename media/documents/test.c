#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int check_dups(int* prefix, int length);
int* addresses(int start, int length, int* prefix);

int total;


int main(int argc, char **argv) {
  int numCities;

  //////////need to create a pointer to queue probably an array of prefixes
  //////////17(16)(15)(14) = 56120 permutations (do 56500) just in case
  /////////aka int queue[56500][4];
  FILE *fin = fopen(argv[1], "r");
  numCities = atoi(argv[2]);
  int distance[numCities][numCities];
  //local var
  total = 0;
  int k=0,l=0;
  int prefix[4]={0};
  char dummy[3];
  fread(dummy,sizeof(char),3,fin); //Throw away the first 3 spaces so as to not confuse strtok
  int i=0,j=0;
  char buff[87];
  for (j=0;j<numCities;j++){ //iterate on rows
    //format how to read in the file. First line is handled specially because extra 0s
    char tmpBuff[10];
    sprintf(tmpBuff,"%%%ic", j==0 ? 83 : 86);
    
    fscanf(fin,tmpBuff,buff);//read the line
    distance[j][0]=atoi(strtok(&buff[0]," ")); //save into array
    for (i=1;i<numCities;i++) {
      distance[j][i]=atoi(strtok(NULL," "));//read subsequent lines into array
    }
  }
  
  addresses(0,4, prefix);
  printf("total is %d\n", total);
  return 0;
}

/*checks the prefixes and returns 0 if there are >1 occurence of a number in prefix*/
int check_dups(int* prefix,int length){

  int array[17]={0};
  int j=0,i=0;

  for (i=0;i<length;i++) array[prefix[i]]++; //Go through the prefix values, incrementing the element of array

  for (j=0;j<17;j++) if (array[j]>1) {return 0;} //if any element of array is >1 then it appears more than once in prefix => Bad prefix!
  return 1;

}


int* addresses(int start,int length,int* prefix){  
  /////////////////need to pass in pointer to queue and maybe rank

  //int prefix[length];
  int j;
  //for (i=start;i<length;i++){
  for (j=0;j<17;j++){
    //if (check_dups(prefix))
    prefix[start]=j;
    if (start==length) {
      if (check_dups(prefix,length)) {
	printf("%i %i %i %i\n",prefix[0],prefix[1],prefix[2],prefix[3]);
	total++;
      }
      return prefix;
    }
    addresses(start+1,length,prefix);
  }
  return prefix;
}
