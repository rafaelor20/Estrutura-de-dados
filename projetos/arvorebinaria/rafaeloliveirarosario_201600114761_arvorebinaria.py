from asyncio.windows_events import NULL
from math import perm
import sys

def separa_info(word):
    word = str(word)
    atr = word.split(" ")
    return atr


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        self.perm = None
        self.size = None

    def setAtr(self, word):
        atr = separa_info(word)
        self.data = atr[0]
        self.perm = atr[1]
        self.size = atr[2]

    def updateNode(self, perm, size):
        self.perm = perm
        self.size = (size)


    #reescrever
    def p_rewrite(self):
        if self.perm == "rw":
            return True
        else:
            return False

    #find data
    def findData(self, node):
        if (self.data == None):
            return None
        elif (self.data == node.data):
            return node
        elif (self.left != None):
            if (self.data > node.data):
                self.left.findData(node)
        elif (self.right != None):
            if (self.data < node.data):
                self.right.findData(node)
        else:
            return None

    # Insert Node
    def insert(self, node):
        data_aux = self.findData(node)
        if data_aux != None:
            if data_aux.perm == "rw":
                data_aux.updateAtr(node.perm, node.size)
        else:
            self.insert_aux(node)

    def insert_aux(self, node):
        if self.data == None:
            self = node
        elif self.data > node.data:
            if self.left is None:
                self.left = node
            else:
                self.left.insert_aux(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert_aux(node)

    # Print the Tree               
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    #Inorder traversal
    # left -> root -> right
    def InOrderTraversal(self, root):
        res = []
        if root:
            res = self.InOrderTraversal(root)
            res.append(root.data)
            res = res + self.InOrderTraversal(root)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def PreOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    # Postorder traversal
    # Left ->Right -> Root
    def PostOrderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

    def nodeToString(self):
        frase = " "+str(self.nome)+" "+str(self.perm)+" "+str(self.size)+" bytes"
        return frase

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
    q_arquivos = entrada[0]
    quant_elem = 0
    root = Node()
    root.setAtr(separa_info(entrada[1]))

    lista_nos = []
    i = 2
    while i < len(entrada):
        newNode = Node()
        newNode.setAtr(separa_info(entrada[i]))
        root.insert(newNode)
        i = i+1

    output.write("EPD:")
    EPD = root.InOrderTraversal(root)
    i = 0
    while i < len(EPD):
        output.writelines(EPD[i])
        i = i+1

    output.write("PED:")
    PED = root.PreOrderTraversal(root)
    i = 0
    while i < len(PED):
        output.writelines(PED[i])
        i = i+1
    
    output.write("EDP:")
    EDP = root.PostOrderTraversal(root)
    i = 0
    while i < len(EDP):
        output.writelines(EDP[i])
        i = i+1
    # Fechando os arquivos
    input.close()
    output.close()
    #Finalizando programa

if __name__ == '__main__':
    main(sys.argv)
