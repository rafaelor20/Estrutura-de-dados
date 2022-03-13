#include <stdio.h>
#include <stdbool.h>

// Estrutura de elemento
typedef struct elemento {
	// Valor
	char * E ;
	// Ponteiro para anterior
	elemento * A ;
	// Ponteiro para próximo
	elemento * P ;
} elemento ;

// Estrutura de lista
typedef struct lista {
	// Ponteiro
	elemento * L ;
} lista ;

//tem_item
bool temItem(elemento e, lista l){
	
}



int main(int argc, char* argv[]) {
	// Ilustrando uso de argumentos de programa
	printf("#ARGS = %i\n", argc);
	printf("PROGRAMA = %s\n", argv[0]);
	printf("ARG1 = %s, ARG2 = %s\n", argv[1], argv[2]);
	// Abrindo arquivos
	FILE* input = fopen(argv[1], "r");
	FILE* output = fopen(argv[2], "w");
	// ...
	// Fechando arquivos
	fclose(input);
	fclose(output);
	// Finalizando programa
	return 0;
}
