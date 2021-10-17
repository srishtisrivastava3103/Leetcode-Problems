

def diskStacking(disks):
    # Write your code here.
    disks = sorted(disks,key = lambda x:x[2])
    sequences = [None for i in disks]
    maxHeightIdx = 0
    heights = [disk[2] for disk in disks]
    for i in range(1,len(disks)):
        for j in range(0,i):
            if disks[j][0]<disks[i][0] and disks[j][1]<disks[i][1] and disks[j][2]<disks[i][2]:
                if heights[i]<=disks[i][2]+heights[j]:
                    heights[i] = disks[i][2]+heights[j]
                    sequences[i] = j
        if heights[i]>=heights[maxHeightIdx]:
            maxHeightIdx = i
    res = []
    while maxHeightIdx is not None:
        res.append(disks[maxHeightIdx])
        maxHeightIdx = sequences[maxHeightIdx]
    return list(reversed(res))
        
	

