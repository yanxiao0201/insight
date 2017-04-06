import collections

def find_topResource(Reso_dict,outfile):

    top_10 = Reso_dict.most_common(10)

    feature_file = open(outfile,'w')

    for item in top_10:
        feature_file.write(str(item[0]) + "\n")

    feature_file.close()


