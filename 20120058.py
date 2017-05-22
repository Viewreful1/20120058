from Queue import Queue
 
ans = ''
visit = [0 for i in range(1002)]
def bfs(adj, i):
    global ans
    ans=''
    visit = [0 for k in range(1002)]
    q = Queue()
    visit[i] = 1
    q.put(i)
    ans += str(i) + ' '
    while q.empty()==False:
        cur = q.get()
        for j in adj[cur]:
            if visit[j]==0:
                visit[j]=1
                q.put(j)
                ans += str(j) + ' '
    return
 
def dfs(adj, i):
    global ans
    global visit
    if(visit[i]==0):
        ans += str(i) + ' '
    visit[i] = 1
    for j in adj[i]:
        if (visit[j]==0):
            dfs(adj, j)
    return
 
adj = [list() for i in range(1002)]
inp = map(int,raw_input().split())
n = inp[0]
m = inp[1]
v = inp[2]
 
for i in range(m):
    inp = map(int, raw_input().split())
    adj[inp[0]].append(inp[1])
    adj[inp[1]].append(inp[0])
 
 
for i in range(n+1):
    adj[i].sort()
 
 
ans = ''
#visit = [0 for i in range(1002)]
dfs(adj, v)
print ans
bfs(adj, v)
print ans