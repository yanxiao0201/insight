import collections
import heapq

def find_topIP(IP_dict,outfile):


    heap = []

    for ip in IP_dict:
        freq = IP_dict[ip]

        if len(heap) < 10:
            heapq.heappush(heap,(freq,ip))
        elif freq > heap[0][0]:
            heapq.heappushpop(heap,(freq,ip))


    top_10 = []
    while len(heap)!= 0:
        data = heapq.heappop(heap)
        top_10.insert(0,data)


    #alternative method
    #top_10 = IP_dict.most_common(10)

    feature_file = open(outfile,'w')

    for item in top_10:
        feature_file.write(str(item[1]) + "," + str(item[0]) + "\n")

    feature_file.close()
