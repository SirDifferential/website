import sys
import os
from dateutil.parser import parse

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python sort_entries.py file.md"
        sys.exit(0)

    filename = sys.argv[1]
    entries = []
    try:
        f = open(filename)
        for line in f:
            data = line.split("[")
            entry = dict()
            entry["date"] = data[0][2:].replace(" ", "")
            entry["data"] = data[1][1:]
            entries.append(entry)
    except Exception as e:
        print "Failed parsing: " + str(e)
        sys.exit(1)

    entries_sort = []
    for e in entries:
        d = parse(e["date"])
        entry = dict()
        entry["date"] = d
        entry["data"] = e["data"]
        entries_sort.append(entry)

    newlist = sorted(entries_sort, key=lambda k: k['date'])[::-1]

    os.remove(filename)
    f = open(filename, "w+")

    for e in newlist:
        d = e["date"].strftime('%Y-%m-%d')
        f.write("* " + d + " [" + e["data"])

    sys.exit(0)

