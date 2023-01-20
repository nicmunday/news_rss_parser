#!/usr/bin/env python3
from imports import newsprocessor
import sys
import datetime

stories = []
    ############ DEALING WITH PASSED IN (SYS.ARGS) ARGS -n, -l, -s, -t, -nt, int(start) int(end)##########
nflag = False
lflag = False
sflag = False
tflag = False
ntflag = False

if "-n" in sys.argv:
    sys.argv.pop(sys.argv.index("-n"))
    nflag = True
if "-t" in sys.argv:
    sys.argv.pop(sys.argv.index("-t"))
    tflag = True
if "-nt" in sys.argv:
    sys.argv.pop(sys.argv.index("-nt"))
    ntflag = True



    #######   THESE ONES ONLY AFFECT OUTPUT, NOT SEARCHING (I.E. SAME NUM STORIES BUT WITH LINKS#######
if "-l" in sys.argv:
    sys.argv.pop(sys.argv.index("-l"))
    lflag = True
if "-s" in sys.argv:
    sys.argv.pop(sys.argv.index("-s"))
    sflag = True
###########DECIDE WHICH METHOD TO CALL BASED ON USER ARGUMENTS PASSED WITH STARTUP #########

my_news = newsprocessor.NewsProcessor()


if len(sys.argv) > 1:
    if len(sys.argv) == 2:
        stories = my_news.stories_in_range(1, int(sys.argv[1]))
    elif len(sys.argv) == 3:
        stories = my_news.stories_in_range(int(sys.argv[1]), int(sys.argv[2]))
else:
    stories = my_news.all_stories()

if nflag:
    stories = my_news.new_stories(stories)


if tflag:
    stories = my_news.today_stories(stories)

if ntflag:
    stories = my_news.not_today_stories(stories)


print("\n")

for story in stories:
    print(story["story"])
    if lflag:
        print(story["link"])
    if sflag:
        print(story["summary"])
    print(story["pub_string"])

if(len(stories)) > 0:

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f" {len(stories)} stories  ||| {my_news.final_string}")

else:
    print("                    There Are Currently No Stories To Display\n\n")

with open("/home/nic/bin/imports/text_files/newsaccessed.txt", "w") as writer:
    writer.write(str(datetime.datetime.now()))
