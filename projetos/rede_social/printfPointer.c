#include <stdio.h>
#include <string.h>

char * ptr = "Hello World";
int size = 10;

int main(){
    for (int i = 0; i <= size; i = i+1)
        printf("%c",ptr[i]);
    for (int j = 0; j<1; j++){
        ptr++;
    }
    printf("\n");
    for (int i = 0; i <= size; i = i+1)
        printf("%c",ptr[i]);
    return 0;
}