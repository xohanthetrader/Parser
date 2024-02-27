import sys

operations = {"+": lambda x,y : x + y,
              "*": lambda x,y : x* y}


symboltable = {}
fname = ""
if len(sys.argv) == 2:
    filename = sys.argv[1]
else :
    quit()

class Tree:
    def __init__(self,fun,l,r):
        self.r = r
        self.l = l
        self.fun = fun

class Leaf:
    def __init__(self,val):
        self.val = val

def eval(node):
    if type(node) == Tree:
        return node.fun(eval(node.l),eval(node.r))
    elif type(node) == Leaf:
        return node.val

def SymbolAnal(fname):
    st = {}
    with open(fname,"r") as f:
        for line in f:
            if "=" in line:
                symbol,computation = line.split("=")
                st[symbol.strip()] = list(reversed(computation.split()))
            else:
                st["out"] = [line]
    return st
 
def Gentree(symbols):
    prevs = []
    for i in symbols:
        try: 
            prevs.append(Leaf(int(i)))
        except:
            if i in operations:
                if len(prevs) >= 2:
                    l = prevs.pop()
                    r = prevs.pop()
                    prevs.append(Tree(operations[i],l,r))
    return prevs[-1]

def SyntaxAnal(st):
    output = st["out"].copy()
    i = 0
    while i < len(output):
        if output[i] in st:
            output[i+1:i+1] = st[output[i]].copy()
            del output[i]
        else:
            i += 1
    return(output)
    


            

symboltable = SymbolAnal(filename)
ast = SyntaxAnal(symboltable)
evalTree = Gentree(ast)
print(eval(evalTree))
