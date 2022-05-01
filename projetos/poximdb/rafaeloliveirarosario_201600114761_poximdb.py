import sys
#import time

def getOp(frase):
      op = ""
      i = 0
      while frase[i] != " ":
        op = op+frase[i]
        i = i+1
      return op

def getHash(frase):
    i = (len(frase))-1
    hash = ""
    while frase[i] != " ":
        hash = frase[i]+hash
        i = i - 1
    hash = hash[:-1]
    return hash

def getElemOp(frase):
      frase = frase[7:]
      frase = frase[:-1]
      return frase

def strElements(frase):
    strElem = ""
    word = ""
    size = ""
    hash = ""
    i = 0
    while frase[i] != " ":
        word = word+frase[i]
        i = i+1
    strElem = word+":"
    i = i + 1
    while frase[i] != " ":
        size = size+frase[i]
        i = i+1
    strElem = strElem + "size=" + size
    i = i + 1
    while i<len(frase):
        hash = hash+frase[i]
        i = i + 1
    strElem = strElem + ",hash=" + hash
    return strElem

#create key
class key:
    def __init__(self, frase):
        self.frase = frase[:-1]
        self.hash = getHash(frase)

# Create a node
class BTreeNode:
  def __init__(self, leaf=False):
    self.leaf = leaf #boolean, is a leaf or not
    self.keys = []
    self.child = []

  def StrNode(self):
        res = ""
        i = 0
        while i < len(self.keys):
              res = res + strElements(self.keys[i].frase) + "\n"
              i = i+1
        return res
        
# Tree
class BTree:
  def __init__(self, order):
    self.root = BTreeNode(True)
    self.order = order

    # Insert node
  def insert(self, key):
    root = self.root
    if len(root.keys) == (2 * self.order) - 1:
      temp = BTreeNode()
      self.root = temp
      temp.child.insert(0, root)
      self.split_child(temp, 0)
      self.insert_non_full(temp, key)
    else:
      self.insert_non_full(root, key)

    # Insert nonfull
  def insert_non_full(self, BTNode, key):
    i = len(BTNode.keys) - 1
    if BTNode.leaf:
      BTNode.keys.append((None, None))
      while i >= 0 and key.hash < BTNode.keys[i].hash:
        BTNode.keys[i + 1] = BTNode.keys[i]
        i -= 1
      BTNode.keys[i + 1] = key
    else:
      while i >= 0 and key.hash < BTNode.keys[i].hash:
        i -= 1
      i += 1
      if len(BTNode.child[i].keys) == (2 * self.order) - 1:
        self.split_child(BTNode, i)
        if key.hash > BTNode.keys[i].hash:
          i += 1
      self.insert_non_full(BTNode.child[i], key)

    # Split the child
  def split_child(self, BTNode, i):
    t = self.order
    y = BTNode.child[i]
    z = BTreeNode(y.leaf)
    BTNode.child.insert(i + 1, z)
    BTNode.keys.insert(i, y.keys[t - 1])
    z.keys = y.keys[t: (2 * t) - 1]
    y.keys = y.keys[0: t - 1]
    if not y.leaf:
      z.child = y.child[t: 2 * t]
      y.child = y.child[0: t - 1]

  # Search key in the tree
  def search_key(self, hash, BTNode=None):
    if BTNode is not None:
      i = 0
      while i < len(BTNode.keys) and hash > BTNode.keys[i].hash:
        i += 1
      if i < len(BTNode.keys) and hash == BTNode.keys[i].hash:
        return BTNode
      elif BTNode.leaf:
        return None
      else:
        return self.search_key(hash, BTNode.child[i])  
    else:
      return self.search_key(hash, self.root)

  def insertOp(self, frase):
      frase = frase[7:]
      newKey = key(frase)
      self.insert(newKey)
      

  def selectOp(self, frase):
      hash = getHash(frase)
      temp = self.search_key(hash)
      if temp is not None:
            res = "["+hash+"]\n" + temp.StrNode()
            return res
      else:
            return ("["+hash+"]\n-")

def main(args):
    #start_time = time.time()
    # Ilustrando uso de argumentos de programa
    print("#ARGS = %i" %len((args)))
    print("PROGRAMA = %s" %(args[0]))
    print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))
    # Abrindo os arquivos
    input = open(sys.argv[1],'r')
    output = open(sys.argv[2],'w')
    # ...
    entrada = input.readlines()
    arvoreb = BTree(int(entrada[0]))
    quant_arquivos = int(entrada[1])
    i = 2
    while i <(quant_arquivos + 2):
        newKey = key(entrada[i])
        arvoreb.insert(newKey)
        i = i + 1
    num_op = int(entrada[i])
    i = i+1
    while i < len(entrada):
        if (getOp(entrada[i]) == "INSERT"):
            arvoreb.insertOp(entrada[i])
        else:
            output.write(arvoreb.selectOp(entrada[i]))
        i = i + 1
    # Fechando os arquivos
    input.close()
    output.close()
    #Finalizando programa
    #print("Process finished --- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main(sys.argv)
