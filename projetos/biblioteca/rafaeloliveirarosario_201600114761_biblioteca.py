import sys

def main(args):
    # Ilustrando uso de argumentos de programa
    print("#ARGS = %i" %len((args)))
    print("PROGRAMA = %s" %(args[0]))
    print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))
    # Abrindo os arquivos
    input = open(sys.argv[1],'r')
    output = open(sys.argv[2],'w')
    # ...
    entrada = input.readlines()
    quant_de_livros = int(entrada[0])
    entrada.pop(0)
    entrada.sort()
    for livros in entrada:
        output.writelines([livros])
    # Fechando os arquivos
    input.close()
    output.close()
    #Finalizando programa

if __name__ == '__main__':
    main(sys.argv)
