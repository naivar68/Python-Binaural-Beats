import subprocess as sp
from pathlib import Path
import ffmpeg
from variables import Variables


class BinauralBeatMixer:
    def __init__(self, variables):
        self.variables = Variables()
        self.duration = variables.duration
        self.frequency_left = variables.frequency_left
        self.frequency_right = variables.frequency_right
        self.sample_rate = variables.sample_rate
        self.video_name = variables.video_name
        self.ffmpeg_path = 'ffmpeg'


    def binauralmixer(self):
        # Generate left tone
        try:
            video_name = self.variables.video_name
            if not Path('binaural_beat.wav').exists():
                ffmpeg.input(f'{video_name}.mp4').input('binaural_beat.wav').output('output.mp4').run()
            elif Path('binaural_beat.wav').exists():
                print("File already exists. Please start again.")
                raise SystemExit()
            else:
                print("Error mixing binaural beats with the video file.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None





