# https://www.codechef.com/problems/PD31

import collections
n, m = [int(x) for x in input().split()]
adj = collections.defaultdict(list)
for i in range(m):
    u,v = [int(x) for x in input().split()]
    adj[u].append(v)
if m!=n-1:
    print("NO")
visited = [0]*(n+1)
visited[0] = 1
def dfs(node):
    visited[node] = 1
    for i in adj[node]:
        if visited[i] == 0:
            dfs(i)
c = 0
for i in range(len(visited)):
    if visited[i]==0:
        dfs(i)
        c+=1
if c!=1:
    print("NO")
print("YES")
    