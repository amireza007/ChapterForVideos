# ChapterForVideos
This python program creates a readable chapter txt file, formatted as (h:mm:ss YOUR_CHAPTER_TITLE) and then attaches it to the video by using ffmpeg's ffmetadata functionality.

Before doing anything, make sure you are in **macOS** and have **python** and **FFmpeg** installed on your machine.

In order to create a beautiful, readable chapter text file, you first need to **run addChapter.py**. 
`python addChapter.py`
Then you are prompted with 3 options:
```
To create a readable chapter of a video, type 1 and press enter.
To use your readable chapter file to add video chapters, type 2 and press enter
To abort, type 0 and enter.
If you are unsure which mode to choose, type -h:
```
You need to type 1 and then press enter.\
Then you are prompted to drag your video to the terminal and hit the enter.\
Afterwards, beautiful txt file is created and located in the same directory as your video.\
The name of the txt file is the same as the video file, except that instead of between-the-words spaces, it has underscores (_)

**Attention:**
When you are editting chapter txt file, be careful to **NOT TO** write single-digit hours followed by a 0 (e.g. 03:22:1 is wrong but 3:22:1 is correct). But feel free to write single-digit minutes and seconds in any way you like. (e.g. 03:2:1 and 03:02:1 and 03:2:01 are all ok!)

Once you have finished adding your chapters to the readable txt file, in order for you to attatch it to the video, you need to run `python addChapter.py` once more and type 2. 

Then you are prompted to drag your readable txt file and then your video itself. \
The way it attaches chapters is by creating a two copies of the video (temporary and the output) and makes changes to the output and then delete the temporary file and ~~the original one and rename the output to the original video's name.~~ keep the previous version (named v1*.mp4) and let you choose to delete it (because you just might endup losing your chapters by attaching wrong chapter file to the video).

## TODO:
### Exception handling:
 The code **does not** provide any means of exception handling and you may encounter some exceptions.
### A nice and very useful UI: 
For entering h:mm:ss and chapter title 
### problem when having a single chapter:
When you add a single chapter, there would be a **default end chapter** and the position of this chapter is **BAD!** (1 sec ahead of the first chapter)
### Using python coroutines or multithreading to show the famous animation in terminals: \-|-\ 
