class Graph:
    def __init__(self):
        self.dictionary={}

    def edge(self, node11, node22):
        trueorfalse=False
        for i in range(1, len(self.dictionary)):
            listkeys=list(self.dictionary.keys())
            node1=int(node11)
            node2=int(node22)
            if node1==listkeys[i] or node2==listkeys[i]:
                self.dictionary[node1].append(node2)
                self.dictionary[node2].append(node1)
                trueorfalse=True
                break
        lengthdictionary=len(self.dictionary)
        for i in range(1, lengthdictionary+1):
            print(i, " : ", self.dictionary[i])

    def addtodictionary(self, key, value):
        self.dictionary[key]=value

if __name__ == '__main__':
    g=Graph()
    g.addtodictionary(1, [2])
    g.addtodictionary(2, [3,4])
    g.addtodictionary(3, [1])
    g.addtodictionary(4, [2])
    g.edge(3,4)

"""
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertlist={}
        self.numverticies=0

    def addvertex(self, key):
        self.numverticies=self.numverticies+1
        newvertex=Vertex(key)
        self.vertlist[key]=newvertex
        return newvertex

    def getvertex(self, n):
        for i in self.vertlist:
            return self.vertlist[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertlist

    def addedge(self, f, t, cost=0):
        if f not in self.vertlist:
            nv=self.addvertex(f)
        if t not in self.vertlist:
            nv=self.addvertex(t)
        self.vertlist[f].addNeighbor(self.vertlist[t], cost)

    def getVerticies(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertlist.values())

if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addvertex(i)
    g.vertlist
    g.addedge(1,2)
    g.addedge(2,3)
    g.addedge(3,4)
    g.addedge(3,5)
    g.addedge(4,0)
    g.addedge(5,4)
    g.addedge(5,2)
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))

class adjacencylist(object):
    def __init__(self):
        self.emptydictionary={}

    def addtodictionary(self, x, value):
        self.emptydictionary[x]=value

    def result(self):
        for i in range(1,len(self.emptydictionary)+1):
            print(x + ":" + self.emptydictionary[i])

    def edge(self, value1, value2):
        self.emptydictionary[value1].append(value1)
        self.emptydictionary[value2].append(value2)

if __name__ == '__main__':
    graph=adjacencylist()
    graph.addtodictionary(1, [2, 4])
    graph.addtodictionary(2, [1, 3])
    graph.addtodictionary(3, [2])
    graph.addtodictionary(4, [1, 3])

class Graph:
    def nodes(main):
        list1=[]
        list1.join(main)

if __name__ == '__main__':
    g=Graph()
    print(g)
    g.nodes(1: [2])
    g.nodes(2: [1,4])
    g.nodes(3: [3])
    g.nodes(4: [2,3])
"""
