import sys
import random

def cod_livro(word):
    i = 0
    num = ""
    while i < 13:
        num = num + word[i]
        i = i+1
    num = int(num)
    return num

def cods_livros(words):
    i = 0
    nums = []
    while i < len(words):
        nums.append(cod_livro(words[i]))
        i = i+1
    return nums

def autor_livro(word):
    autor = ""
    i = 0
    while (word[i] != " "):
        i = i+1
    i = i+1
    while (word[i] != "&"):
        autor = autor+word[i]
        i=i+1
    return autor

def autores_livros(words):
    autores = []
    i = 0
    while i < len(words):
        autores.append(autor_livro(words[i]))
        i = i+1
    return autores

def nome_livro(word):
    divisao = word.split("&")
    livro = divisao[1]
    return livro

def nomes_livros(words):
    livros = []
    i = 0
    while i < len(words):
        livros.append(nome_livro(words[i]))
        i = i+1
    return livros

def binary_search_ite(lista, num):
    num = int(num)
    tentativas = 0
    esquerda = 0
    direita = (len(lista)) - 1
    meio = (esquerda + direita) // 2
    aux_num = lista[meio]
    while (direita >= esquerda and num != aux_num):
        tentativas = tentativas + 1
        aux_num = lista[meio]
        if aux_num > num:
            direita = meio - 1
        else:
            esquerda = meio + 1
        meio = (esquerda + direita) // 2
    if num == aux_num:
        return (tentativas, True, meio)
    else:
        return (tentativas, False, -1)
          
def busca_interpolacao(lista, x):
    x = int(x)
    i = 0
    j = len(lista) - 1
    tentativas = 0
    while i <= j:
        tentativas = tentativas + 1
        m = i + ((lista[j] - lista[i]) % (j - i + 1))
        if x == lista[m]:
            return (i,True,m)
        else:
            if x < lista[m]:
                j = m - 1
            else:
                i = m + 1
    return (tentativas,False,-1)

def string_busca(busca,lista_num):
    BB = binary_search_ite(lista_num, busca)
    BI = busca_interpolacao(lista_num, busca)
    return [BB,BI]

def string_escrita(entrada,lista_livros):
    lista_cods = cods_livros(lista_livros)
    resultado = string_busca(entrada,lista_cods)
    
    if (resultado[0][1] == True):
        livro = lista_livros[(resultado[0][2])]
        autor = autor_livro(livro)
        nome = nome_livro(livro)
        escrita = "["+entrada+"]"+"B="+tbb+",I="+tbi+":Author:"+autor+",Title:"+nome
        return escrita
    else:
        escrita = "["+entrada+"]"+"B="+tbb+",I="+tbi+":"+"ISBN NOT FOUND\n"
        return escrita

def contagem_p(x, y, c):
    if x > y:
        c[1] = c[1] + 1
    else:
        c[0] = c[0] + 1
    return c



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
    lista_livros = []
    i = 1
    while i <= quant_de_livros:
        lista_livros.append(entrada[i])
        i = i+1
    quant_de_buscas = entrada[i]
    i = i+1
    lista_livros.sort()
    pontos = [0,0]
    while i < (len(entrada)):
        resultado = string_busca(entrada[i], lista_livros)
        tbb = str(resultado[0][0])
        tbi = str(resultado[1][0])
        escrita = string_escrita(entrada[i], lista_livros)
        contagem_p(,,pontos)
        output.write(escrita)
        i = i+1
    # Fechando os arquivos
    input.close()
    output.close()
    #Finalizando programa

if __name__ == '__main__':
    main(sys.argv)
