# Given one node, find whether another node lies in the subtree of second node

def checksubtree(tree, node1, node2 ):
    in_time = [0]*len(tree)
    out_time = [0]*len(tree)
    time = 0
    visited = [0]*len(tree)
    def dfs(node):
        nonlocal time
        visited[node] = 1
        in_time[node] = time
        time+=1
        for i in tree[node]:
            if visited[i]==0:
                dfs(i)
        out_time[node] = time
        time+=1
    dfs(0)
    if in_time[node2]>in_time[node1] and out_time[node2]<out_time[node1]:
        return True
    else:
        return False
    
checksubtree([[1],[2,3],[4],[],[]],1,4)