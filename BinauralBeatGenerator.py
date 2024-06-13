from variables import Variables
import ffmpeg
from pathlib import Path


class BinauralBeatGenerator:
    def __init__(self, variables):
        self.variables = Variables()
        self.duration = variables.duration
        self.frequency_left = variables.frequency_left
        self.frequency_right = variables.frequency_right
        self.sample_rate = variables.sample_rate
        self.ffmpeg_path = 'ffmpeg'
        self.video_name = variables.video_name

    def binaural_beats(self, variables):


# Generate left tone
        try:
            if not Path('left.wav').exists():
                ffmpeg.input(f'{self.video_name}').filter('sine',
                                                          frequency=self.frequency_left,
                                                          duration=self.duration).output('left.wav', ar=self.sample_rate).run()
                print("Left tone generated.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

        # Generate right tone
        try:
            ffmpeg.input(f'{self.video_name}').filter('sine',
                                                      frequency=self.frequency_right,
                                                      duration=self.duration).output('right.wav', ar=self.sample_rate).run()
            print("Right tone generated.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
