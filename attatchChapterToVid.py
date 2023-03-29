import re
import os
from dumpmeta import dumpmeta
chapters = list()
inpttxt = input("please drag your readable chapter file to create video chapters:")
inptvid = input("please drag your videos as well:")

beautiful_directory_for_vid = inptvid.replace(os.path.basename(inptvid), '')
beautiful_directory_for_txt = inpttxt.replace(os.path.basename(inpttxt), '')
dumpmeta(inptvid, beautiful_directory_for_txt)

txt_directory = beautiful_directory_for_txt.replace('\\', '')
os.chdir(txt_directory)
txt_filename = os.path.basename(inpttxt).replace('\\', '')
txt_filename = txt_filename.strip()

with open(txt_filename, 'r') as f:
    for line in f:
        x = re.match(r"(\d):(\d{2}):(\d{2}) (.*)", line)
        if x is None: x = re.match(r"(\d):(\d{2}):(\d{1}) (.*)", line)
        elif x is None: x = re.match(r"(\d):(\d{1}):(\d{1}) (.*)", line)
        elif x is None: x = re.match(r"(\d):(\d{1}):(\d{2}) (.*)", line)
        if x is not None:
            hrs = int(x.group(1))
            mins = int(x.group(2))
            secs = int(x.group(3))
            title = x.group(4)
            minutes = (hrs * 60) + mins
            seconds = secs + (minutes * 60)
            timestamp = (seconds * 1000)
            chap = {
                "title": title,
                "startTime": timestamp
            }
            chapters.append(chap)
text=""
with open('./FFMETADATAFILE.txt', 'r') as f:
    #neat technique right?
    head  = [next(f) for x in range (5)]
    for i in range(len(head)):
        text += head[i]
    f.close()  # for line in f:
         
    #     text += line 
for i in range(len(chapters)):
    chap = chapters[i]
    title = chap['title']
    start = chap['startTime']
    if i == len(chapters) - 1: end = chapters[i]['startTime'] + 1000

    else: end = chapters[i+1]['startTime']-1
    text += f"""[CHAPTER]
TIMEBASE=1/1000
START={start}
END={end}
title={title}
"""
    if len(chapters) == 1: 
        start = start + 1
        end = end + 1
        title = "Default END"
        text += f"""
[CHAPTER]
TIMEBASE=1/1000
START={start}
END={end}
title={title} 
"""
with open("./FFMETADATAFILE.txt", "w") as myfile:
    myfile.write(text)
    myfile.close()


vid_directory = beautiful_directory_for_vid.replace('\\', '')
os.chdir(vid_directory)
# vid_filename = os.path.basename(inptvid).replace('\\', '')
# vid_filename = vid_filename.strip()
vid_filename = os.path.basename(inptvid)
bash = "ffmpeg -i " + inptvid  + " -map_chapters -1 -c copy temp.mp4 && ffmpeg -i temp.mp4 -i " + beautiful_directory_for_txt+"FFMETADATAFILE.txt -map_metadata 1 -codec copy ./v2" + vid_filename + " && rm temp.mp4 " + vid_filename + " && mv v2"+ vid_filename + " " + vid_filename
os.system(bash)
