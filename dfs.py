# Depth first traversal of undirected unweighted graph
n,root=map(int,input().split())
l=[]
l.append(0)
for i in range(0,n):
    x=list(map(int,input().split()))
    l.append(x)
stack=[]
stack.append(root)
result=[]
result.append(root)
var=stack[-1]
while(1):
    flag=0
    for j in range(0,n):
        if((l[var][j]==1)and((j+1)not in result)):
            flag=1
            stack.append(j+1)
            result.append(j+1)
            break
    if(len(stack)==0):
        break
    if(flag==1):
        var=stack[-1]
    else:
        stack.pop()
        if(len(stack)==0):
            break
        var=stack.pop()
print(*result)
