import collections

def find_topIP(IP_dict,outfile):

    top_10 = IP_dict.most_common(10)

    feature_file = open(outfile,'w')

    for item in top_10:
        feature_file.write(str(item[0]) + "," + str(item[1]) + "\n")

    feature_file.close()


