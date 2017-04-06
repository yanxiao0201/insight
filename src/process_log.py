from load_data import *
from feature_1 import *
from feature_2 import *
from feature_3 import *
from feature_4 import *
import collections
import sys


if (len(sys.argv) < 6):
    print "usage: python [process_log.py] [log.txt] [hosts.txt] [resources.txt] [hours.txt] [blocked.txt]"
    sys.exit()

IP_dict = collections.Counter()
Reso_dict = collections.Counter()

visit_freq = []
visit_time = []

Block_dict = collections.Counter()
To_log = []

start_time = datetime.strptime("01/Jul/1995:00:00:00","%d/%b/%Y:%H:%M:%S")

#loading data
in_file = sys.argv[1]
print "Loading data......."
zone = load_data(IP_dict,Reso_dict,visit_freq,visit_time,Block_dict,To_log,start_time,in_file)

#feature_1
hosts_outfile = sys.argv[2]
print "Generating feature #1......"
find_topIP(IP_dict,hosts_outfile)

#feature_2
reso_outfile = sys.argv[3]
print "Generating feature #2......"
find_topResource(Reso_dict,reso_outfile)

#feature_3
hours_outfile = sys.argv[4]
print "Generating feature #3......"
find_topHour(visit_time,visit_freq,start_time,zone,hours_outfile)

#feature_4
blocked_outfile = sys.argv[5]
print "Generating feature #4......"
find_block(To_log,blocked_outfile)
