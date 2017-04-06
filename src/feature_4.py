def find_block(To_log,outfile):

    feature_file = open(outfile,'w')
    for log in To_log:
        feature_file.write(str(log))

    feature_file.close()
