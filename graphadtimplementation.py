#!/usr/bin/python

class Vertex():
    def __init__(self,key):
        self.id=key
        self.connectedto={}

    def addneighbor(self,nbr,weight=0):
        self.connectedto[nbr]=weight

    def __str__(self):
        return str(self.id) + 'connectedto:' +str([x.id for x in self.connectedto])

    def getconnections(self):
        return self.connectedto.keys()

    def getId(self):
        return self.id

    def getweight(self,nbr):
        return self.connectedto[nbr]

class Graph():
    def __init__(self):
        self.vertlist={}
        self.numvertices=0

    def addvertex(self,key):
        self.numvertices=self.numvertices+1
        newvertex=Vertex(key)
        self.vertlist[key]=newvertex
        return newvertex

    def getvertex(self,n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertlist

    def addedge(self,f,t,cost=0):
        if f not in self.vertlist:
            nv=self.addvertex(f)
        if t not in self.vertlist:
            nv=self.addvertex(t)
        self.vertlist[f].addneighbor(self.vertlist[t],cost)

    def getvertices(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertlist.values())

if __name__=='__main__':
    g=Graph()
    for i in range(6):
        g.addvertex(i)

    print g.vertlist;
    g.addedge(0,1,5)
    g.addedge(0,5,2)
    g.addedge(1,2,4)
    g.addedge(2,3,9)
    g.addedge(3,4,7)
    g.addedge(4,0,1)
    g.addedge(5,4,8)
    g.addedge(5,2,1)
    for v in g:
        for w in v.getconnections():
            print "(%s,%s)"  %(v.getId(),w.getId())
