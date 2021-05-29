# Cycle Detection Algorithm using Union Find Algorithm with given list of edges.

def unionFind():
    parent = [-1]*5
    def findparent(node):
        if parent[node]==-1:
            return node
        else:
            return findparent(parent[node])
    def union(x,y):
            parent[x] = y
    def checkcycle(edges):
        for u,v in edges:
            x = findparent(u)
            y =findparent(v)
            if x==y:
                return True
            else:
                union(x,y)
        return False
    return checkcycle([[1,2],[2,3],[2,4],[3,4],[4,5]])
unionFind()