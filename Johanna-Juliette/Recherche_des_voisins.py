G = { "A":[("B",10),("C",5)],
      "B":[("C",10)],
      "C":[("A",5),("B",10)]}

print(G.keys)
print(G["A"])

for C in G["A"]:
         "C"[0]


def voisins (G,S):
    L=[]
    for C in G[S]:
        L.append(C[0])

    return L
print(voisins(G,"C"))


def vv (G,A):
    L=voisins(G,A)
    L2=[]
    for i in L :
        L2.append(C)
        L2 + voisins(G,i)

    return L2
print(vv(G,"C"))





