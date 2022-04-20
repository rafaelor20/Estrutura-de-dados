import sys

def getWord(frase):
    temp = frase.split(" ")
    word = temp[0]
    return word

def getLSino(frase):
    sino = frase.split(" ")
    sino.pop(0)
    sino.pop(1)
    return sino

def getSino(lista):
    espaco = " "
    frase = espaco.join(lista)
    return frase

class treeNode(object):
    def __init__(self, value):
        self.value = value
        self.sino = []
        self.l = None
        self.r = None
        self.h = 1

    def getValue(self):
        return self.value

    def setSino(self, sino):
        self.sino = sino
        
    def getSino(self):
        return self.sino

class AVLTree(object):

    def insert(self, root, key):

        if not root:
            return treeNode(key)
        elif key < root.value:
            root.l = self.insert(root.l, key)
        else:
            root.r = self.insert(root.r, key)

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
            
        self.preOrder(root.l)
        self.preOrder(root.r)
        
    def buscaWord(self, word):
        caminho = []
        if self == None:
            return [caminho,[]]
       # elif self.value

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
    quant_palavras = int(entrada[0])
    Tree = AVLTree()
    i = 1
    while i <= quant_palavras:
        root = None
        root.setSino(getLSino(entrada[i]))
        Tree.insert(root, getWord(entrada[i]))
        i = i+1

    
    
    # Fechando os arquivos
    input.close()
    output.close()
    #Finalizando programa

if __name__ == '__main__':
    main(sys.argv)
