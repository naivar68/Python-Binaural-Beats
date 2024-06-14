from variables import Variables
import ffmpeg
from pathlib import Path


class BinauralBeatGenerator:
    def __init__(self, variables):
        self.duration = variables.duration
        self.frequency_left = variables.frequency_left
        self.frequency_right = variables.frequency_right
        self.sample_rate = variables.sample_rate
        self.ffmpeg_path = 'ffmpeg'
        self.video_name = variables.video_name

    def binaural_beats(self):
        # Generate left tone
        try:
            if not Path('left.wav').exists():
                ffmpeg.input('anullsrc=r=44100:cl=mono', f='lavfi').output('left.wav', filter_complex=f'sine=frequency={self.frequency_left}:duration={self.duration}', ar=self.sample_rate).run()
                print("Left tone generated.")
        except ffmpeg.Error as e:
            print(f"An error occurred while generating left tone: {e}")
            return None

        # Generate right tone
        try:
            ffmpeg.input('anullsrc=r=44100:cl=mono', f='lavfi').output('right.wav', filter_complex=f'sine=frequency={self.frequency_right}:duration={self.duration}', ar=self.sample_rate).run()
            print("Right tone generated.")
        except ffmpeg.Error as e:
            print(f"An error occurred while generating right tone: {e}")
            return None

        # Combine left and right tones into a stereo file
        try:
            input1 = ffmpeg.input('left.wav')
            input2 = ffmpeg.input('right.wav')
            ffmpeg.filter([input1, input2], 'amerge', inputs=2).output('binaural_beat.wav', ac=2).run()
            print("Binaural beat stereo mixdown created.")
        except ffmpeg.Error as e:
            print(f"An error occurred while creating the stereo mixdown: {e}")
            return None

        return "Binaural beats generated successfully"


# Assuming you have a main function or similar to call the above class
if __name__ == "__main__":
    variables = Variables()
    generator = BinauralBeatGenerator(variables)
    generator.binaural_beats()
