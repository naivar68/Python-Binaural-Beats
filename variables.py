# variables.py
import os

class Variables:
    def __init__(self):
        self.video_name = ""
        self.sample_rate = None
        self.duration = None
        self.frequency_left = None
        self.frequency_right = None
        self.video_name = ""
        self.ffmpeg_path = ""
        self.frequency_left = None
        self.frequency_right = None
        self.duration = None
        self.sample_rate = None



    def name_video(self):
        self.video_name = input("Enter the name of the video file (including the file extension): ")
        if not os.path.exists(self.video_name):
            raise SystemExit("The file does not exist in this directory. Please ensure the file is in this directory.")
        elif not self.video_name.endswith(".mp4"):
            raise SystemExit("The file is not an MP4 file. Please ensure the file is an MP4 file.")
        elif os.path.exists(f"The file {self.video_name} already exists. Please rename the file or remove the existing file."):
            raise SystemExit(f"The file {self.video_name} already exists. Please rename the file or remove the existing file.")
            return self.video_name


    def interface(self):

        self.sample_rate = int(input("Sample Rate (44100 for CD-quality audio): "))
        self.duration = int(input("Duration (in seconds): "))
        self.frequency_left = int(input("Frequency for the left ear (in Hz): "))
        self.frequency_right = int(input("Frequency for the right ear (in Hz): "))
        return self.sample_rate, self.duration, self.frequency_left, self.frequency_right, self.video_name














   