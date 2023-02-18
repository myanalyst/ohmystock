import numpy as np

def get_support_by_big_vols(data, vols):
    #find the largest volume
    v1 = []
    for d in data:
        v1.append(d[6]) 
    v2 = np.sort(np.array(v1))[-vols:]
    
    
    v3 = []
    for v in v2:
        avgp = 0
        i = 0
        for d in data:
            if v == d[6]:
                v3.append((d[1],_get_avg_price(data[i:])))
            i = i + 1
                
    return v3

#avgp: the price started from
#data: data set
def _get_avg_price(data):
    avgp = 0
    for d in data:
        avgp = avgp + d[5]
    return round(avgp/len(data),2)
