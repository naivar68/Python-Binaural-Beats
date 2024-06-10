import time
import os
from scipy.io.wavfile import write
from moviepy.editor import *


class Variables:
    def __init__(self):
        self.sample_rate = None
        self.duration = None
        self.frequency_left = None
        self.frequency_right = None
        self.video_name = str





    def interface(self):

        print("Welcome to the Binaural Beat Generator!")
        print("Please enter the following values:")
        self.sample_rate = int(input("Sample Rate (44100 for CD-quality audio): "))
        self.duration = int(input("Duration (in seconds): "))
        self.frequency_left = int(input("Frequency for the left ear (in Hz): "))
        self.frequency_right = int(input("Frequency for the right ear (in Hz): "))
        time.sleep(2)
        os.system("clear") if os.name == "posix" else os.system("cls")
        # Print the values
        print("The following values have been entered:")
        print(f"Sample Rate: {self.sample_rate}")
        print(f"Duration: {self.duration}")
        print(f"Frequency Left: {self.frequency_left}")
        print(f"Frequency Right: {self.frequency_right}")
        time.sleep(2)

        return self.sample_rate, self.duration, self.frequency_left, self.frequency_right


        # Get the video file name from the user
    def video_name(self):
        video_name = input("Please enter the name of the video file (including the extension): ")
        # Check if the file exists in the directory
        if not os.path.exists(video_name):
            print("The file does not exist in this directory. Please ensure the file is in this directory.")
            exit(0)
        elif not video_name.endswith(".mp4"):
            print("The file is not an MP4 file. Please ensure the file is an MP4 file.")
            exit(0)
        elif os.path.exists(f"The file {video_name} already exists. Please rename the file or remove the existing file."):
            print(f"The file {video_name} already exists. Please rename the file or remove the existing file.")
            exit(0)


        else:
            print("The file exists in this directory. Proceeding with the Binaural Beat Generator and Mixer...")
            return str(video_name)




