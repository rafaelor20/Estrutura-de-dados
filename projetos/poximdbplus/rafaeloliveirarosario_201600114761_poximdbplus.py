import sys

def getOp(frase):
      op = ""
      i = 0
      while frase[i] != " ":
        op = op+frase[i]
        i = i+1
      return op

def getWord(frase):
    i = 0
    word = ""
    while frase[i] != " ":
        word = word+frase[i]
        i = i+1
    return word

def getSize(frase):
    i = 0
    word = ""
    while frase[i] != " ":
        word = word+frase[i]
        i = i+1
    size = int(frase[i+1])
    return size

def getHash(frase):
    i = 0
    count = 0
    hash = ""
    while frase[i] != " ":
        i = i+1
    i = i+1
    while frase[i] != " ":
        i = i+1
    i = i+1
    while i<len(frase):
        hash = hash+frase[i]
    return hash

def getElements(frase):
    lista = []
    word = ""
    size = ""
    hash = ""
    i = 0
    while frase[i] != " ":
        word = word+frase[i]
        i = i+1
    lista[0] = word
    i = i + 1
    while frase[i] != " ":
        size = size+frase[i]
        i = i+1
    lista[1] = size
    i = i + 1
    while i<len(frase):
        hash = hash+frase[i]
    lista[2] = hash
    return lista

def main(args):
    # Ilustrando uso de argumentos de programa
    print("#ARGS = %i" %len((args)))
    print("PROGRAMA = %s" %(args[0]))
    print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))
    # Abrindo os arquivos
    input = open(sys.argv[1],'r')
    output = open(sys.argv[2],'w')
    # ...
    # Fechando os arquivos
    input.close()
    output.close()
    #Finalizando programa

if __name__ == '__main__':
    main(sys.argv)
