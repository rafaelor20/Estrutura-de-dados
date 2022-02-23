#include <stdlib.h>
#include <stdio.h>
 
int main () {
int *p = 0x5DC;//1500
printf ("p = %d\n", p);
p++; //incremento
printf ("p = %d\n", p);//1504
p = p + 15; //soma
printf ("p = %d\n", p);//1564
p = p - 2;  //subtração
printf ("p=%d\n", p);//1556
 
system("pause");
return 0;
}