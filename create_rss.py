# Goes through a markdown file containing links to blog entries
# and creates an RSS feed file out of them
# The markdown is expected to be formatted as follows:
#
# * 2017-11-11 ["Haba-IPA", the beer documentary](./blog_habaipa.html)
# * 2014-02-24 [Generation of Procedural Worlds using OpenCL](./blog_proceduralis.html)
# * 2013-07-05 [Parallax Scrolling with SFML](./blog_parallax.html)
#
# Usage: python ./create_rss bloglist.md rss.xml
#

import sys
from datetime import datetime

days_of_week = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ]
months = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]

header = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
<atom:link href="https://jessekaukonen.net/rss.xml" rel="self" type="application/rss+xml" />
<title>Jesse Kaukonen</title>
<link>https://jessekaukonen.net</link>
<description>Jesse Kaukonen</description>
"""

footer = """</channel>
</rss>"""

# RFC822 date is formatted as such:
# Sat, 07 Sep 2002 9:42:31 GMT
def dateToRFC822(dateobj):
    day_of_week = days_of_week[dateobj.weekday()]
    month = months[dateobj.month]
    day = dateobj.day
    daystr = str(day)
    if day < 10:
        daystr = "0" + str(day)
    year = dateobj.year

    pubdate = day_of_week + ", " + daystr + " " + month + " " + str(year) + " 00:00:00 GMT"
    return pubdate

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ./create_rss ./input.md ./out.rss")
        sys.exit(1)

    inf = sys.argv[1]
    outf = sys.argv[2]

    content = []
    serverurl = "https://jessekaukonen.net/"

    try:
        with open(inf) as f:
            data = f.readlines()
            for l in data:
                parts = l.strip("\n").split("[")
                if len(parts) != 2:
                    print("Incorrect formatting for link: " + str(parts) + ", expected: \"* YYYY-MM-DD [title](./foo.html)\"")
                    continue

                # The strings are formatted like so:
                # * 2017-11-02 [some title](./somearticle.html)
                datestr = parts[0].strip("*").strip()
                title = parts[1].split("]")[0]
                url = parts[1].split("]")[1].strip("(").strip(")")
                url = serverurl + url

                try:
                    dateobj = datetime.strptime(datestr, "%Y-%m-%d")
                    pubdate = dateToRFC822(dateobj)
                except Exception as e:
                    print("Error converting date to RFC822: " + str(e) + ", date was: " + str(datestr))
                    continue

                itemstr = "<item>\n"
                itemstr += "\t<title>" + title + "</title>\n"
                itemstr += "\t<link>" + url + "</link>\n"
                itemstr += "\t<guid>" + url + "</guid>\n"
                itemstr += "\t<pubDate>" + pubdate + "</pubDate>\n"
                itemstr += "\t<description>" + title + ": " + url + "</description>\n"
                itemstr += "</item>\n"
                content.append(itemstr)
        f.close()
    except Exception as e:
        print("Error reading input file: " + str(inf) + ": " + str(e))
        sys.exit(1)

    try:
        rss = header
        for c in content:
            rss += c
        rss += footer
    except Exception as e:
        print("Exception forming rss: " + str(e))
        sys.exit(1)

    try:
        f = open(outf, "w")
        f.write(rss)
        f.close()
    except Exception as e:
        print("Exception writing output to file " + outf + ": " + str(e))
        sys.exit(1)


    
