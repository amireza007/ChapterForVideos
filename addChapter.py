import re
import os 

print("\nATTENTION:\n Please Take note that this script works only if you have a macOS machine and installed FFmpeg\n\n")
print("we will be changing that very soon and make it compatible with Windows OS,as well!")

print("To create a readable chapter of a video, type 1 and press enter.")
print ("To use your readable chapter file to add video chapters, type 2 and press enter")
print("To abort, type 0 and enter.")

b = True

mode = input("If you are unsure which mode to choose, type -h: ")
while b:
    print(mode)
    if mode == '-h':
        print("""###
          Mode 1 basically extracts a readable chapter txt file containing with the format like below from a video:
          h:mm:ss YOUR CHAPTER TITLE

          Mode 2 take your readable chapter txt file and attatch it to your video 
     ###""")
        mode = input("please eneter your preferred mode: ")
        print()
    elif mode == '1': 
        import getReadableChapter
        print("Done!")
        b = False
    elif mode == '2':
        import attatchChapterToVid
        # print(attatchChapterToVid.bash)
        if (input("\n\nDone!\nThere is a backup version, named v1*.mp4 \nWould you like delete the previous version of the video?\n(type 1 if so, otherwise, type something else)") == "1"):
            os.system("rm v1"+ attatchChapterToVid.vid_filename) 
        b = False

    elif mode == '0': b = False
    else: 
        print("\nNot correct input!")
        mode = input("please eneter your preferred mode: ")

