import sys
import time

def separa_info(word):
    word = str(word)
    #print(word)
    atr = word.split(" ")
    return atr

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        self.perm = None
        self.size = None
        self.pos = None

    def setAtr(self, word):
        atr = separa_info(word)
        data = atr[0]
        perm = atr[1]
        size = atr[2]
        data = data[2:]
        perm = perm[1:]
        size = size[1:]
        data = data[:-2]
        perm = perm[:-2]
        size = size[:-4]
        self.data = data
        self.perm = perm
        self.size = size

    def updateNode(self, perm, size, pos):
        #perm = perm[1:]
        #size = size[1:]
        #perm = perm[:-2]
        #size = size[:-4]
        self.perm = perm
        self.size = size
        self.pos = pos

    def updateTreePos(self, pos):
        if self.pos != None:
            if self.pos > pos:
                self.pos = (self.pos)-1
        if self.left != None:
            self.left.updateTreePos(pos)
        if self.right != None:
            self.right.updateTreePos(pos)

    def bigPos(self, pos):
        if self.pos > pos:
            pos = self.pos
        if self.left != None:
            if self.left.bigPos(pos) > pos:
                pos = self.left.bigPos(pos)
        if self.right != None:
            if self.right.bigPos(pos) > pos:
                self.right.bigPos(pos)
        return pos

    def setPos(self, pos):
        self.pos = pos

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
            return self
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
        node_found = self.findData(node)
        if node_found != None:
            if node_found.perm == "rw":
                self.updateTreePos(node_found.pos)
                node.pos = (self.bigPos(self.pos))+1
                node_found.updateNode(node.perm, node.size, node.pos)
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

    #Inorder traversal
    # left -> root -> right
    def InOrderTraversal(self, root):
        res = []
        if root:
            res = self.InOrderTraversal(root.left)
            res.append(root)
            res = res + self.InOrderTraversal(root.right)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def PreOrderTraversal(self, root):
        res = []
        if root:
            res.append(root)
            res = res + self.PreOrderTraversal(root.left)
            res = res + self.PreOrderTraversal(root.right)
        return res

    # Postorder traversal
    # Left ->Right -> Root
    def PostOrderTraversal(self, root):
        res = []
        if root:
            res = self.PostOrderTraversal(root.left)
            res = res + self.PostOrderTraversal(root.right)
            res.append(root)
        return res

    def nodeToString(self):
        self.pos = str(self.pos)
        frase = str(self.pos)+" "+self.data+" "+self.perm+" "+self.size+" bytes\n"
        return frase

def main(args):
    # Ilustrando uso de argumentos de programa
    start_time = time.time()
    print("#ARGS = %i" %len((args)))
    print("PROGRAMA = %s" %(args[0]))
    print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))
    # Abrindo os arquivos
    input = open(sys.argv[1],'r')
    output = open(sys.argv[2],'w')
    # ...
    entrada = input.readlines()
    root = Node()
    root.setPos(1)
    root.setAtr(separa_info(entrada[1]))
    i = 2
    while i < len(entrada):
        newNode = Node()
        newNode.setPos(i)
        newNode.setAtr(separa_info(entrada[i]))
        root.insert(newNode)
        i = i+1
    
    output.write("EPD:\n")
    EPD = root.InOrderTraversal(root)
    i = 0
    while i < len(EPD):
        output.writelines(EPD[i].nodeToString())
        i = i+1

    output.write("PED:\n")
    PED = root.PreOrderTraversal(root)
    i = 0
    while i < len(PED):
        output.writelines(PED[i].nodeToString())
        i = i+1
    
    output.write("EDP:\n")
    EDP = root.PostOrderTraversal(root)
    i = 0
    while i < len(EDP):
        output.writelines(EDP[i].nodeToString())
        i = i+1

    # Fechando os arquivos
    input.close()
    output.close()
    #Finalizando programa
    print("Process finished --- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main(sys.argv)
