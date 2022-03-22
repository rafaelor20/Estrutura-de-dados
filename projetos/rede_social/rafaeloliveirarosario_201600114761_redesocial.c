#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

char* ok = "[ OK  ] ";
char* error = "[ERROR] ";

struct node {
   char *data;
   struct node *next;
   struct node *previous;
};

struct list {
   struct node *noo;
};

struct node *head = NULL;
struct node *current = NULL;

//is list empty
bool isEmpty() {
   return head == NULL;
}

int length() {
   int length = 0;
   struct node *current;
   struct node *last = head->previous;

   if(head == NULL){
      return length;
   }

   for(current = head; current != last; current = current->next) {
      length++;
   }
	length++;
   return length;
}

//find a link with given key
struct node* find(char *data) {

   //start from the first link
   struct node* current = head;

   //if list is empty
   if(head == NULL) {
      return NULL;
   }

   //navigate through list
   while(current->data != data) {
	
      //if it is last node
      if(current->next == NULL) {
         return NULL;
      } else {
         //go to next link
         current = current->next;
      }
   }      
	
   //if data found, return the current Link
   return current;
}

//insert link at the last location
void insertLast(char *data) {
   //create a link
   struct node *link = (struct node*) malloc(sizeof(struct node));
   link->data = data;

   if (find(data) == NULL) {
      if (head == NULL){
         head = link;
         head->next = link;
         head->previous = link;
      } 
      else {
         struct node *last = head->previous;
         struct node *current = head;

         //point last node to new last node
         last->next = link;
   
         //put new node in last position
         link->previous = last;

         //point new node to first node
         link->next = head;
	
         //point first to new last node
         head->previous = link;
      }
   }
}

//delete a link with given key
struct node* delete(char *data) {
	
   //if list is empty
   if(current == NULL) {
      return NULL;
   }

   //start from the first link
   struct node* current = head;
   //struct node* previous = NULL;

   //navigate through list
   struct node *last = head->previous;
   while(current->data != data) {
      //if it is last node
      if(current->next == head) {
         return NULL;
      } else {
         current = current -> next;
      }
   }

   //found a match, update the link
   struct node *temp = current -> previous;
   temp->next = current->next;
   temp = current->next;
   temp->previous = current->previous;
   return current; 
}

char* show(struct node* node){
   if (find(node->data) == NULL ){
      return NULL;
   } else {
      struct node *previousP = node->previous;
      struct node *nextP = node->next;
      char* previous = strcat(previousP->data,"<-");
      char* next = strcat(nextP->data,"->");
      char* retorno = strcat(strcat(previous,node->data),next);
      return retorno;
   }
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

   char* readline;
   char* writeline;
   struct list lista;
   lista.noo = head;
   int i;

   for(int i = 0; i < argc; i++){
      fgets(readline, 50, input);
      if (readline[0] == 'A'){
         for(i = 0; i < 4; i++ ){
            readline++;
         }
         insertLast(readline);
      } else if(readline[0] == 'R'){
         for(i = 0; i < 7; i++ ){
            readline++;
         }
         delete(readline);
      } else {
         for(i = 0; i < 5; i++ ){
            readline++;
         }
         show(find(readline));
      }


   }

	// Fechando arquivos
	fclose(input);
	fclose(output);
	// Finalizando programa
	return 0;
}