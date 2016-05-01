#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <time.h>
#include <string.h>

void master(FILE* fin, int numCities);
void slave();
void die (char* error);
int check_dups(int* prefix, int length);
int* addresses(int start, int length, int* prefix);

int main(int argc, char **argv) {
    //start time
    time_t start_time = time(NULL);
    
    //local variables
    int i, rank, tasks, numCities;
    
    /*Initialize MPI*/
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &tasks);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);       
    
    if (argc!=3) die("wrong number of args. Should be 2\n");
    numCities=atoi(argv[2]);

    //open file for reading
    FILE *fin = fopen(argv[1],"r");
        if(!fin){
            printf("Error: Cannot open file\n");
            exit(EXIT_FAILURE);
        }


    //master
    if (rank == 0) {
 
      master(fin, numCities);
    }
    
    //slave
    else {
      //slave();
    }
    
    /*flush and finalize*/
    fflush(stdout);
    MPI_Finalize();
    
    // Compute and output the execution time
    time_t end_time = time(NULL);
    printf("\nExecution time: %d seconds\n", (int) difftime(end_time, start_time));
    return 0;
}

void master(FILE* fin, int numCities) {

  int distance[numCities][numCities];
  printf("started master\n");
  //local var
  int k=0,l=0;
  int prefix[4]={0};

  //////////need to create a pointer to queue probably an array of prefixes
  //////////17(16)(15)(14) = 57120 permutations (do 57130) just in case
  /////////aka int queue[57130][4];


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
  
  
  addresses(0,4,prefix);
  return;


}//end master()

void slave () {

  int address[17]={0};
  MPI_Send()//request work
    MPI_Recv()//receive prefix
  addresses(4,17,address);

}

/*checks the prefixes and returns 0 if there are >1 occurence of a number in prefix*/
int check_dups(int* prefix,int length){

  int array[17]={0};
  int j=0,i=0;

  for (i=0;i<length;i++) array[prefix[i]]++; //Go through the prefix values, incrementing the element of array

  for (j=0;j<17;j++) if (array[j]>1) {return 0;} //if any element of array is >1 then it appears more than once in prefix => Bad prefix!
  return 1;

}

void die (char* error) {
  printf("%s",error);
  exit(1);
}

/*function that creates every permutation of unique integers given length and start position*/
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
      }
      return prefix;
    }
    addresses(start+1,length,prefix);
  }
  return prefix;
}

void compute_distance(int* address) { 

  static int best_distance=0; //supposed to be the shortes distance
  static address[17]={0}; //maybe change name since it is the same as argument
  int current_distance = 0;
  int i;

  distance+=[address[0]][address[1]];  
  /*
    for(i == 0; i < 16; i++) {
       current_distance+= distance[address[i]][address[i+1]]; //slaves need access to the matrix
    }
    if(current_distance < best_distance) best_distance = current_distance;
    ////////really need to change static var
   */
  /////////////////////////////
  //maybe need to either pass in distance or make distance global var
  //also we should read file outside of master so slaves will have their own copy of distance
}
