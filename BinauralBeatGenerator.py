import ffmpeg
import subprocess as sp
import os
import sys
from variables import Variables



class BinauralBeatGenerator:
    def __init__(self, variables):
        self.duration = variables.duration
        self.frequency_left = variables.frequency_left
        self.frequency_right = variables.frequency_right
        self.sample_rate = variables.sample_rate
        self.ffmpeg_path = 'ffmpeg'

    def binaural_beats(self, variables):
        # Generate left tone
        command = f'{self.ffmpeg_path} -y -f lavfi -i "sine=frequency={variables.frequency_left}:duration={variables.duration}" left.wav'
        print(f"Running command: {command}")
        result = sp.run(command, shell=True, capture_output=True)
        if result.returncode != 0:
            print(f"Error running command: {result.stderr.decode()}")
            return None

        # Generate right tone
        command = f'{self.ffmpeg_path} -y -f lavfi -i "sine=frequency={variables.frequency_right}:duration={variables.duration}" right.wav'
        print(f"Running command: {command}")
        result = sp.run(command, shell=True, capture_output=True)
        if result.returncode != 0:
            print(f"Error running command: {result.stderr.decode()}")
            return None
        else:
            print("Binaural beats successfully generated.")
            return "left.wav", "right.wav"