#include <stdio.h>

int main() {
    int x,y;
    printf("Qual a coordenada x?\n");
    scanf("%i",&x);
    printf("Qual a coordenada y?\n");
    scanf("%i",&y);
    if (x < 0){
        if (y < 0){
            printf("O ponto está no 3º quadrante.\n");
        }
        else{
            printf("O ponto está no 2º quadrante.\n");
        }
    }
    else{
        if (y < 0){
            printf("O ponto está no 4º quadrante.\n");
        }
        else{
            printf("O ponto está no 1º quadrante.\n");
            }
    }
    return 0;
}