import os

def dumpmeta(path, beautiful_directory):
    """this function dumps the FFMETADATAFILE.txt of a movie file """
    # os.chdir(env_directory)
    base = os.path.basename(path)    
    bash = "ffmpeg -hide_banner -loglevel quiet -i " + path + " -f ffmetadata " + beautiful_directory + "/FFMETADATAFILE.txt"    
    os.system(bash)
