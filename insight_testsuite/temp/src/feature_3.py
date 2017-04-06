from datetime import datetime,timedelta
import collections

#visit_time: timestamp
#visit_freq: nums

def find_topHour(visit_time,visit_freq,start_time,zone,outfile):

    Re_dict = collections.Counter()

    rolling_start = visit_time[0]
    rolling_end = visit_time[-1]

    tmp_start = 0
    tmp_end = 0

    tmp_sum = 0

    for i in xrange(len(visit_time)):
        if visit_time[i] < rolling_start + 3600: # within one hour
            tmp_sum += visit_freq[i]
            tmp_end += 1
        else:
            break


    Re_dict[rolling_start] = tmp_sum
    rolling_start += 1

    while rolling_start <= rolling_end:
        if tmp_end < len(visit_time):
            if visit_time[tmp_end] < rolling_start + 3600:
                tmp_sum += visit_freq[tmp_end]
                tmp_end += 1


        if visit_time[tmp_start] < rolling_start:
            tmp_sum -= visit_freq[tmp_start]
            tmp_start += 1

        Re_dict[rolling_start] = tmp_sum
        rolling_start +=1


    top_10 = Re_dict.most_common(10)

    feature_file = open(outfile,'w')

    for item in top_10:

        delta = timedelta(seconds = (item[0]%(3600*24)),days = (item[0]/(3600*24)))
        right_time = delta + start_time

        print_time = right_time.strftime("%d/%b/%Y:%H:%M:%S")

        feature_file.write(print_time + " " + zone + "," + str(item[1]) + "\n")


    feature_file.close()









