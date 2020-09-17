from queue import Queue
adj_list = {
    "A":["B", "X"],
    "B":["A","X","Z"],
    "X":["A","B","Y"],
    "Y":["X","Z"],
    "Z":["B","Y"]
}

visited = {}
parent = {}
level = {}
output_list = []
queue = Queue()

for node in adj_list.keys():
    visited[node]= False
    parent[node]=None
    level[node]=-1

source_node = "A"
visited[source_node]=True
level[source_node]=0
queue.put(source_node)

while not queue.empty():
    p = queue.get()
    output_list.append(p)
    for v in adj_list[p]:
        if not visited[v]:
            visited[v]=True
            parent[v]= p
            level[v]=level[p]+1
            queue.put(v)

print(output_list)
print(level)
print(parent)

f = "Z"
path=[]
while f is not None:
    path.append(f)
    f = parent[f]
path.reverse()
print(path)