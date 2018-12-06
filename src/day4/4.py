# for help: https://github.com/bpeebles/aoc2018/blob/master/day4/guard.py

import re
import attr
import datetime
from collections import defaultdict, Counter

# Create a guard which holds all of that guard's info
# `attr.s` is the key to trigger the attr module to do it's magic

@attr.s
class Guard:

    # I spent a long time reading the attr documentation trying to figure out what the
    # .ib() method stood for. Then I realized it was a pun and I felt dumb.
    # Create atts for the guard ID and the days each guard appears

    guard_id = attr.ib()
    days = attr.ib()
    # store all the minutes the guard is asleep
    def minutes(self):
        # Take the time input for the given day in [days]
        for time, day in self.days.items():
            # Define a var --> sleep for each day
            for sleep in day:
                # Break each sleep into minutes and calculate the difference between the two
                for minutes in range(sleep[0], sleep[1]):
                    yield minutes

    # helper function to count all minutes
    def total_asleep(self):
        # add things up by calling minutes
        # I still don't really understand this syntax
        return sum(1 for _ in self.minutes())

    # figure out which minute is slept the most by a given guard
    def most_common_minute(self):
        # use a counter for fast tallying
        count = Counter(self.minutes())

        #get the most common minute from the Counter
        return count.most_common(1)[0]

# open and sort the list
with open('input.txt') as f:
    input = f.readlines()
    sorted = sorted(input)

guards = {}

for entry in sorted:
    # get the timestring from the entry
    time_string = re.search(r'(\d+)-(\d+)-(\d+)\s(\d+)\:(\d+)', entry)

    time = datetime.datetime(year=int(time_string.group(1)), month=int(time_string.group(2)), day=int(time_string.group(3)), hour=int(time_string.group(4)), minute=int(time_string.group(5)))

    if 'Guard' in entry:
        search = re.search(r'#(\d+)', entry)
        id = search.group(1)
    elif 'falls' in entry:
        sleeping = time
    elif 'wakes' in entry:
        # print(id, time, sleeping.minute, time.minute)
        if id not in guards:
            guards[id] = Guard(guard_id=id, days=defaultdict(list))
        guards[id].days[time.date()].append((sleeping.minute, time.minute))


# part 1
most = -1
most_guard = None
for id, guard in guards.items():
    asleep = guard.total_asleep()
    if asleep > most:
        most = asleep
        most_guard = guard

print(most_guard) #3491

common_minute = most_guard.most_common_minute()
print(common_minute)
print(int(most_guard.guard_id) * common_minute[0])

#part 2
most = None
most_times = -1
sleepiest_guard = None
for id, guard in guards.items():
    min, events = guard.most_common_minute()
    if events > most_times:
        most = min
        most_times = events
        sleepiest_guard = guard.guard_id

print(most, most_times, sleepiest_guard)
print(int(sleepiest_guard) * most)
