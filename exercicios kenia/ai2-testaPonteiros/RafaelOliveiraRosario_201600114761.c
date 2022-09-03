#include <stdio.h>
#include <stdlib.h> //usado malloc
#include <string.h> //usado strcpy 
#include <ctype.h> //usado toupper

 struct tipo{
	  char Palavra[20];
	  void *ProxDesordenado;
      void *ProxOrdenado; 
  };
  typedef struct tipo TIPO;
  
  TIPO *Inicio, *Fim, *Auxiliar, *Atual, *Anterior; //Estrutura ordenada
  TIPO *Primeiro, *Final, *Ajudante; //Estrutura desordenada

  char P[20],R='S';

  void desordenado(){
    Ajudante=(TIPO *) malloc(sizeof(TIPO));
    strcpy(Ajudante->Palavra,P);
    Ajudante->ProxDesordenado = NULL;
    if (Primeiro == NULL){ //primeiro elemento da estrutura
      Primeiro = Ajudante;
      Final = Ajudante;}
    else{//insere no fim
        Final->ProxDesordenado = Ajudante;
        Final = Ajudante;}
    
	printf("\n Palavras desordenadas: "); 
    Ajudante=Primeiro;; 
    while (Ajudante!=NULL){
      printf(" %s ",Ajudante->Palavra);
      Ajudante= Ajudante->ProxDesordenado; }
  }
  
  void ordena(){  
    Auxiliar=(TIPO *) malloc(sizeof(TIPO));
    strcpy(Auxiliar->Palavra,P);
    Auxiliar->ProxOrdenado = NULL;
    if (Inicio == NULL){ //primeiro elemento da estrutura
      Inicio = Auxiliar;
      Fim = Auxiliar;}
    else
      if (strcmp(P,Inicio->Palavra)<=0){ //insere no inicio
		Auxiliar->ProxOrdenado = Inicio;
		Inicio = Auxiliar;}
	  else
	    if (strcmp(P,Fim->Palavra)>=0){ //insere no fim
		  Fim->ProxOrdenado = Auxiliar;
		  Fim = Auxiliar;}
		else{ //insere no meio - antes do primeiro maior
		  Atual = Inicio->ProxOrdenado;
		  Anterior = Inicio;
		  while (strcmp(Atual->Palavra,Auxiliar->Palavra)<0){
		    Anterior = Atual;
		    Atual = Atual->ProxOrdenado;}
		  Anterior->ProxOrdenado = Auxiliar;
		  Auxiliar->ProxOrdenado = Atual;}
    
    printf("\n Palavras ordenadas: "); 
    Auxiliar=Inicio; 
    while (Auxiliar!=NULL){
      printf(" %s ",Auxiliar->Palavra);
      Auxiliar= Auxiliar->ProxOrdenado; }
}

int main(){

  Inicio=NULL;
  while (R=='S'){
    printf("\n > > > ORDENA PALAVRAS < < < \n");
    printf("\n\n Qual palavra deseja inserir? ");
    scanf(" %s",P);  
    ordena();
    desordenado();
    printf("\n\n Digite S se deseja continuar: ");
    scanf(" %c",&R);
    R = toupper(R); }
   return 0;
}