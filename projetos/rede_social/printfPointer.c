#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * ptr = "Hello World";
char * H = "H";
int size = 10;

int main(){
    for (int i = 0; i <= size; i = i+1){
        printf("%c",ptr[i]);
        }
    for (int j = 0; j<1; j++){
        ptr++;
        }
    printf("\n");
    for (int x = 0; x <= size; x = x+1){
        printf("%c",ptr[x]);
        }
    H = (char*)malloc(sizeof(H)+sizeof(ptr));
    strcat(H, ptr);
    printf("\n");
    for (int k = 0; k <= size; k = k+1){
        printf("%c",H[k]);
        }
    return 0;
}