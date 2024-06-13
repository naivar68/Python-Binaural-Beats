# variables.py
import os
import sys
from pathlib import Path



class Variables:
    def __init__(self):
        self.sample_rate = None
        self.duration = None
        self.frequency_left = None
        self.frequency_right = None
        self.video_name = ""
        self.ffmpeg_path = ""



    def name_video(self):
        self.video_name = input("Enter the name of the video file (including the file extension): ")
        if not Path(self.video_name).exists():
            raise SystemExit("The file does not exist in this directory. Please ensure the file is in this directory.")
        elif not self.video_name.endswith(".mp4"):
            raise SystemExit("The file is not an MP4 file. Please ensure the file is an MP4 file.")
        elif Path(f"The file {self.video_name}").exists():
            raise SystemExit(f"The file {self.video_name} already exists. Please rename the file or remove the existing file.")
        return self.video_name



    def command_exists(command):
        try:
            os.system(f"where {command}")
            return True
        except FileNotFoundError:
            return False

    def is_ffmpeg_installed():
        try:
            ffmpeg = os.system("where ffmpeg")
            if ffmpeg == 0:
                ffmpeg_path = "ffmpeg"
                return ffmpeg_path
        except FileNotFoundError:
            return False





            return True
        except FileNotFoundError:
            return False



    def interface(self):
        try:
            self.sample_rate = int(input("Sample Rate (44100 for CD-quality audio): "))
            self.duration = int(input("Duration (in seconds): "))
            self.frequency_left = int(input("Frequency for the left ear (in Hz): "))
            self.frequency_right = int(input("Frequency for the right ear (in Hz): "))
        except ValueError:
            print("Error: Sample rate, duration, and frequencies must be integers.")
            sys.exit()

        # Check if the values are correctly set
        if not all([self.sample_rate, self.duration, self.frequency_left, self.frequency_right]):
            print("Error: All values must be set and non-zero.")
            sys.exit()

        return self.sample_rate, self.duration, self.frequency_left, self.frequency_right, self.video_name














