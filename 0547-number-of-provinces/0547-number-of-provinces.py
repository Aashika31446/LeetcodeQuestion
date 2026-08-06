class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        marked=[0]*len(isConnected[0])
        provinces=[0]*len(isConnected[0])
        c=0
        queue=[]
        for i in range (len(isConnected[0])):
            if not marked[i]:
                c+=1
                queue.append(i)
            while queue:
                x=queue.pop(0)
                marked[x]=1
                provinces[x]=c
                for y in range (len(isConnected [0])):
                    if(x!=y and marked[y]!=1 and isConnected [x][y]==1):
                        marked[y]=1
                        provinces[y]=c
                        queue.append(y)
        return c



        