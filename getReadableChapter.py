import re, os
from dumpmeta import dumpmeta

text=""

inpt = input('please drag (or paste the path WITH all scaping \\) your video here to produce a readlbe chapter txt file:')
beautiful_directory = inpt.replace(os.path.basename(inpt), '')
file_directory = beautiful_directory.replace('\\', '')

os.chdir(file_directory)    #Setting up the environment
dumpmeta(inpt, beautiful_directory)
filename = os.path.basename(inpt).replace('\\', '')

filename = filename.strip()

with open('FFMETADATAFILE.txt', 'r') as f:
    for line in f:
        start=0
        end = 0
        s= re.search(r"\bSTART=(\d+)", line)
        ch = re.search(r"\btitle=(.*)", line)
        if s is not None: 
            start = int(s.group(1))/1000
            if start >= 10000: start = start /10000
            hrs = int(start/3600)
            start -= hrs * 3600 
            minutes = int(start/60)
            if minutes < 10: 
                start -= minutes * 60
                minutes = "0" + str(minutes)
            else: start -= minutes * 60
            seconds  = int(start)
            if seconds < 10: seconds = "0" + str(seconds) 
            text+= f"{hrs}:{minutes}:{seconds}"
        if ch is not None:
            text+=f" {ch.group(1)}\n"
    f.close()
text.rstrip()
filename = filename.replace(".mp4", ".txt")
name_of_txt_file = filename.replace(' ', '_')
f = open(name_of_txt_file, 'w')
f.write(text)
f.close()
print('Readable chapter txt file is created in the same directory as your video')


