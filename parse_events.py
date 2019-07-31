import subprocess
import os
import sys
from LogEntry import LogEntry
from LogContainer import LogContainer

dir_path = os.path.dirname(os.path.realpath(__file__))
# print "dir path " + dir_path

date = "2019-07-30"
if len(sys.argv) > 1:
    date = sys.argv[1]

filename = "logs_for_" + date + ".txt"
log_container = LogContainer()


def grep_files():
    subprocess.call([dir_path + '/find_logs.sh', date])
    # program ="find report-logs -name " + date + " | xargs cat | grep production  | grep  running "
    # print "file written to " + filename


def parse_line(line):
    entries = line.split("&")
    # print entries
    server = entries[0].split("=")[1]
    user_count = entries[3].split("=")[1]
    organism_count = entries[4].split("=")[1].split(" ")[0]
    return server, user_count, organism_count


def parse_file():
    file_path = dir_path + "/" + filename
    fp = open(file_path, 'r')
    cnt = 1
    with open(file_path) as fp:
        line = fp.readline()
        while line:
            (server, user_count, organism_count) = parse_line(line)
            log_entry = LogEntry(server=server, num_users=user_count, num_organisms=organism_count)
            # print "log entry "
            # print log_entry.server + " " + str(log_entry.num_organisms) + " " + str(log_entry.num_users)
            log_container.add_entry(log_entry)

            # print "server: " + server
            # print "user_count: " + str(user_count)
            # print "organism_count: " + str(organism_count)

            cnt += 1
            line = fp.readline()
            # print cnt
            # if cnt > 5:
            #     break

        # cnt = 1
        # while line:
        #     print("Line {}: {}".format(cnt, line.strip()))
        #     line = fp.readline()
        #     cnt += 1

    fp.close()


# print "A"
if len(sys.argv) > 1:
    grep_files()
parse_file()
# print "B"
log_container.print_data()
# print "C"
