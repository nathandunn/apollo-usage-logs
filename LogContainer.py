class LogContainer:
    entries = dict({})

    def __init__(self):
        pass

    def add_entry(self, log_entry):
        if log_entry.server in self.entries:
            return
        self.entries[log_entry.server] = log_entry

    def print_data(self):
        # print str(len(self.entries))
        total_organisms = 0
        total_users = 0
        for entry_key in self.entries:
            entry = self.entries[entry_key]
            # print "num users " + str(entry.num_users)
            total_users = total_users + int(entry.num_users)
            total_organisms = total_organisms + int(entry.num_organisms)
            # print entry.server + " " + str(entry.num_organisms) + " " + str(entry.num_users)

        entry_count = len(self.entries)
        print "Num servers: " + str(entry_count)
        print "Num organisms " + str(total_organisms) + " (" + str(total_organisms / entry_count) + ")"
        print "Num users " + str(total_users) + " (" + str(total_users / entry_count) + ")"
