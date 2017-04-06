
from datetime import datetime,timedelta



def load_data(IP_dict,Reso_dict,visit_freq,visit_time,Block_dict,To_log,start_time,filename):

    fileinput = open(filename,'r')

    i = 0

    zone = ""

    for line in fileinput:
        data = line.split()

        IP_dict[data[0]] = IP_dict.get(data[0],0) + 1

        if data[-1] != '-':
            byte = int(data[-1])
        else:
            byte = 0
        Reso_dict[data[6]] = Reso_dict.get(data[6],0) + byte

        newzone = data[4].strip(']')
        if newzone != zone:
            #print "The new timezone is {}".format(newzone)
            zone = newzone

        time = data[3].strip('[')
        datetime_object = datetime.strptime(time, "%d/%b/%Y:%H:%M:%S")

        seconds = int((datetime_object - start_time).total_seconds())

        if visit_time == [] :
            visit_time.append(seconds)
            visit_freq.append(1)
        elif (seconds == visit_time[-1]):
            visit_freq[-1] += 1
        else:
            visit_time.append(seconds)
            visit_freq.append(1)

        if data[0] in Block_dict and len(Block_dict[data[0]]) == 3:# has three unsuccessfull login
            tmp = Block_dict[data[0]]
            if (seconds - tmp[-1]) <= 300:# within 5min
                To_log.append(line)
            else:# already 5min
                Block_dict.pop(data[0])

        elif "login" in data[-4]:
            if data[-2][0] == "2":# if it is successful
                if data[0] in Block_dict:# restart counting
                    Block_dict.pop(data[0])
            elif data[-2][0] == "4":# if it is not successful
                if data[0] not in Block_dict:# start counting
                    Block_dict[data[0]] = [seconds]
                else: #if within 20s, then count ++, else, restart counting
                    tmp = Block_dict[data[0]]
                    if (seconds - tmp[-1]) > 20:# if > 20s later than the last one, then restart
                        tmp = [seconds]
                    elif (seconds - tmp[0]) > 20:# if > 20s later than the first one, then pop first one and add the current one
                        tmp.pop(0)
                        tmp.append(seconds)
                    else:# if within 20s of the previous two, add the current one. Now the list has a length 3 and it will go to the very first "if" clause
                        tmp.append(seconds)

        i += 1
        if i % 100000 == 0:
            print "Loading data # {}".format(i)

    fileinput.close()
    return zone
