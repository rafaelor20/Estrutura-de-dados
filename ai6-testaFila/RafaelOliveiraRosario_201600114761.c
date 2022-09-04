/* 
 * Universidade Federal de Sergipe
 * Centro de Ciência Exatas e Tecnologia
 * Departamento de Computação
 * 
 * Disciplina: Estruturas de Dados
 * Professora: Kenia Kodel
 * 
 * Objetivo Didático: Aplicação de fila.
 * 
 * Objetivos: Operador de uma agência de taxis, contendo 10 taxis.
 *            O sistema deve agendar qual taxi atente à próxima chamada.
 *            Sendo formada uma fila de taxistas e havendo uma chamada, o 
 *            primeiro da fila atende. E quando um taxiste chega para trabalhar ou
 *            finaliza uma corrida, deve ser inserido no final da fila.
 * */
 
#include <stdio.h>
#include <stdlib.h>  //usado system
#include <ctype.h>   //usado toupper
#include <string.h>  //usado strcmp

typedef char Str20[20];
int L[] = {1,2,3,4,5,6,7,8};
int quant_chamados = 0;
struct Reg{
	Str20 Taxista; //nome
	void *Prox;
  };
  
typedef struct Reg TpReg;
Str20 T;

TpReg *Inicio,*Fim=NULL;
TpReg *Aux;

int Opcao;

//Insere registro do taxista no fim da fila
void EmFila(Str20 S){
  Aux=(TpReg *) malloc(sizeof(TpReg));
  strcpy(Aux->Taxista,S);
  Aux->Prox=NULL;
  if ((Inicio==NULL) && (Fim==NULL)){
    Inicio=Aux;
	}
  else{
    Fim->Prox = Aux;
	}
  Fim = Aux;
}

//Verifica se há clientes esperando por taxistas
//Se houver, o primeiro sera removido
void olhaFila(){
  Aux=(TpReg *) malloc(sizeof(TpReg));
  while (quant_chamados > 0){
    if (Inicio == NULL){
      //free(Aux);
      break;
    }
    else{
      Remover();
      quant_chamados = quant_chamados - 1;
    }
  }
}

//Para incluir taxista.
void Incluir() {
  char R;
  do{
    //system("cls");
    printf("*** Chegada de Taxista ***\n\n");
    printf("Nome do Taxista: ");
    scanf("%s",T);
    fflush(stdin);
    //inclusao da taxista na fila
    EmFila(T);
    olhaFila();
    printf("\nOutro taxista? S/N\n");
    scanf(" %c", &R);
    fflush(stdin);
    R=toupper(R);}
  while (R =='S');
}

//atende a chamada do usuario por taxistas
void atendeChamada(){
  char R = 'S';
  while (R =='S'){
    Remover();
    printf("Efetuar novo atendimento? S/N \n");
    scanf(" %c",&R);
    fflush(stdin);
    R=toupper(R);
  }
}

//Remove o primeiro taxista da lista
void Remover(){
    if ((Inicio==NULL) && (Fim==NULL)){
      printf("Lista de Taxistas Vazia\n\n");
      quant_chamados = quant_chamados + 1;
      //system("pause");
    }
    else{
      printf("Taxista: ");
      printf("%s \n\n", Inicio->Taxista);
      if (Inicio == Fim){
        Aux = Inicio;
        Inicio = NULL;
        Fim = NULL;
        free(Aux);
      }
      else {
        Aux = Inicio;
        Inicio=Inicio->Prox;
        free(Aux);
      }
      if (Inicio==NULL){
        Fim=NULL;
      }
    }
}

//Mostra a lista de taxistas a espera de uma chamada
void LTodos(int K[]) {
  //system("cls");
  printf("\nFila de clientes: ");
  printf("%d\n\n", quant_chamados);
  printf("***Fila de Taxistas***\n\n");
  if (Inicio!= NULL){
	  Aux = Inicio;
	  do{
	    printf("%s, ", Aux->Taxista);
	    Aux=Aux->Prox;}
	  while (Aux!=NULL);
  }
  else
    printf("Fila de taxistas vazia\n");  
  //system("pause");
  }

int main(){
  do{ 
	  //system("cls");
    printf("\n\n> > > Charme Taxis < < < \n\n");
    if (Inicio!= NULL){
	    Aux = Inicio;
	    do{
	      printf("%s ",Aux->Taxista);
	      Aux=Aux->Prox;}
	    while (Aux!=NULL);
    }
    printf("\n\nQue deseja fazer? \n\n");
    printf("1 - Chegada de Taxista \n"); 
    printf("2 - Chamada de Cliente \n"); //taxista é removido da fila
    printf("3 - Listar Taxistas \n");
    printf("4 - Sair \n\n");
    printf("Opcao: ");
    scanf("%d",&Opcao);
    fflush(stdin);
    switch (Opcao){
      case 1: Incluir(); break;
      case 2: atendeChamada(); break;
      case 3: LTodos(L); break;}}
  while (Opcao != 4);
  return 0;}
