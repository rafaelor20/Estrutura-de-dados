#include <stdio.h>
#include <stdint.h>

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



typedef struct lista {
	// Ponteiro
	elemento * L ;
} lista ;

// Função de busca sequencial em lista
elemento * bseql ( lista L , uint32_t x ) {
	// Ajustando ponteiros
	elemento * i = L .L , * r = NULL ;
	// Iterações de cabeça -> cauda
	while ( i != NULL && r == NULL ) {
		// Comparação de valor
		if (i -> E == x )
			// Atualização de referência
			r = i;
		// Próximo elemento da lista
		i = i->P;
}
// Retornando resultado
return r ;
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
