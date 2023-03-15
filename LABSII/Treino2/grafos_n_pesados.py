exemplo = [("OPO","LIS"),("OPO","FAO"),
 ("LIS","FAO"),("MAD","OPO"),
 ("LIS","LON"),("FRA","OPO"),
 ("LIS","NRT"),("LON","NRT"),
 ("LON","FRA"),("LIS","FRA")]

def build(arestas):
    adj = {}
    for o,d in arestas:
        if o not in adj:
            adj[o] = set()
        if d not in adj:
            adj[d] = set()
        adj[o].add(d)
        adj[d].add(o)
    return adj

print(build(exemplo))