import sys
import time

class treeNode(object):
    def __init__(self, value, sino):
        self.value = value
        self.sino = sino
        self.l = None
        self.r = None
        self.h = 1

    def setSino (self, sino):
        self.sino = sino

class AVLTree(object):

    def insert(self, root, key, sino):

        if not root:
            return treeNode(key, sino)
        elif key < root.value:
            root.l = self.insert(root.l, key, sino)
        else:
            root.r = self.insert(root.r, key, sino)

        root.h = 1 + max(self.getHeight(root.l),self.getHeight(root.r))

        b = self.getBal(root)

        if b > 1 and key < root.l.value:
            return self.rRotate(root)

        if b < -1 and key > root.r.value:
            return self.lRotate(root)

        if b > 1 and key > root.l.value:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)

        if b < -1 and key < root.r.value:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)

        return root

    def lRotate(self, z):

        y = z.r
        T2 = y.l

        y.l = z
        z.r = T2

        z.h = 1 + max(self.getHeight(z.l),self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),self.getHeight(y.r))

        return y

    def rRotate(self, z):

        y = z.l
        T3 = y.r

        y.r = z
        z.l = T3

        z.h = 1 + max(self.getHeight(z.l),self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),self.getHeight(y.r))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.h

    def getBal(self, root):
        if not root:
            return 0

        return self.getHeight(root.l) - self.getHeight(root.r)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.value), end="")
        self.preOrder(root.l)
        self.preOrder(root.r)

    def buscador(self, root, value, caminho, output):
        if not root:
            caminho = caminho + "->?]"
            caminho = "[" + caminho[2:]
            resultado = caminho + "\n" + "-\n"
            output.writelines(resultado)
        elif root.value == value:
            caminho = caminho + "->" + value + "]"
            caminho = "[" + caminho[2:]
            resultado = caminho + "\n" + root.sino + "\n"
            output.writelines(resultado)
        elif root.value > value:
            caminho = caminho + "->" + root.value
            self.buscador(root.l, value, caminho, output)
        elif root.value < value:
            caminho = caminho + "->" + root.value
            self.buscador(root.r, value, caminho, output)

def get_Word(frase):
    i = 0
    word = ""
    while frase[i] != " ":
        word = word+frase[i]
        i = i+1
    return word

def get_Sino(frase):
    i = 0
    while frase[i] != " ":
        i = i+1
    frase = frase[(i+3):]
    frase = frase[:-1]
    i = 0
    sino = ""
    while i < len(frase):
        if frase[i] == " ":
            sino = sino + ","
        else:
            sino = sino + frase[i]
        i = i+1
    #if sino[-1] == "\n":
    #    sino = sino [:-1]
    return sino

def main(args):

    start_time = time.time()

    # Ilustrando uso de argumentos de programa
    print("#ARGS = %i" %len((args)))
    print("PROGRAMA = %s" %(args[0]))
    print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))
    # Abrindo os arquivos
    input = open(sys.argv[1],'r')
    output = open(sys.argv[2],'w')
    # ...
    entrada = input.readlines()
    quant_palavras = int(entrada[0])
    Tree = AVLTree()
    root = None
    i = 1
    while i <= quant_palavras:
        value = get_Word(entrada[i])
        sino = get_Sino(entrada[i])
        print("linha: "+str(i))
        root = Tree.insert(root, value, sino)
        i = i+1
    i = i+1
    saida = ""
    while i < len(entrada):
        busca = entrada[i]
        busca = busca[:-1]
        print("busca: "+busca)
        print("linha: "+i)
        Tree.buscador(root, busca, "", output)
        i = i+1
    
    # Fechando os arquivos
    input.close()
    output.close()
    #Finalizando programa

    print("Process finished --- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main(sys.argv)
