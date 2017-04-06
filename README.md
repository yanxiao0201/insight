# Insight Data Engineering Code Challenge

# Challenge Summary

Picture yourself as a backend engineer for a NASA fan website that generates a large amount of Internet traffic data. Your challenge is to perform basic analytics on the server log file, provide useful metrics, and implement basic security measures. 

The desired features are described below: 

### Feature 1: 
List the top 10 most active host/IP addresses that have accessed the site.

### Feature 2: 
Identify the 10 resources that consume the most bandwidth on the site

### Feature 3:
List the top 10 busiest (or most frequently visited) 60-minute periods 

### Feature 4: 
Detect patterns of three failed login attempts from the same IP address over 20 seconds so that all further attempts to the site can be blocked for 5 minutes. Log those possible security breaches.


# Solution Summary

This solution is implemented and tested in Python 2.7.2+ (default, Oct  4 2011, 20:03:08) [GCC 4.6.1] on linux2. 
The python modules used are all common modules: collections,sys,heapq and datetime. No addtional modules are needed.

# Source Files

All source files are placed in the "/insight/src" path
process_log.py: the main file to run. Each feature is constructed as the result of a function. If one desired to skip certain step, comment the related function. Each function is independent with each other. However, the function "load_data" should always be run first.

load_data.py: the source file for loading the data from the input, processing the data for all of the four features.

feature_1.py: the source file for the function "find_topIP", used to generate top 10 most active IP

feature_2.py：the source file for the function "find_topResource", used to generate top 10 resources

feature_3.py: the source file for the function "find_topHour", used to generate top 10 busiest 60-minutes periods

feature_4.py: the source file for the function "find_block", used to generate a list of log entries that should be blocked

# Program Executing

The program can be executed in one of the following two ways:

1) Run "/insight/run.sh" file in the terminal. The input file need to be placed in the "/insight/log_input" and need to be named "log.txt". The output for each feature will be placed in "/insight/log_output" and in "txt" format.
2) Run: "python [process_log.py] [log.txt] [hosts.txt] [resources.txt] [hours.txt] [blocked.txt]". If not enought arguments are given, a warning message will show up.

# Additional notes

To find top_10, both a heap constructed from "heapq.py" and "collections.Counter.most_common" method have been used to compare the efficiency





