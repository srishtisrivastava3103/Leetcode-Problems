

import math
def detectArbitrage(exchangeRates):
    # Write your code here.
	convertToLog(exchangeRates)
	dist = [float('inf') for i in range(len(exchangeRates))]
	dist[0] = 0
	for i in range(len(exchangeRates)-1):
		bellmanford(exchangeRates, dist)
	if bellmanford(exchangeRates, dist):
		return True
	return False

def convertToLog(exchangeRates):
	for i in range(len(exchangeRates)):
		for j in range(len(exchangeRates)):
			exchangeRates[i][j] = -math.log10(exchangeRates[i][j])

def bellmanford(mat,dist):
#     for i in range(len(mat)):
	f = 0
	for u in range(len(mat)):
		for v in range(len(mat)):
			if dist[v]>dist[u]+mat[u][v]:
				f = 1
				dist[v] = dist[u]+mat[u][v]
	if f==1:
		return True


