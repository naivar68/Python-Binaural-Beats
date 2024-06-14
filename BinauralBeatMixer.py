import subprocess as sp
from pathlib import Path
import ffmpeg
from variables import Variables


class BinauralBeatMixer:
    def __init__(self, variables):
        self.duration = variables.duration
        self.frequency_left = variables.frequency_left
        self.frequency_right = variables.frequency_right
        self.sample_rate = variables.sample_rate
        self.video_name = variables.video_name
        self.ffmpeg_path = 'ffmpeg'

    def binaural_mixer(self):
        try:
            # Check if the binaural_beat.wav file exists
            if Path('binaural_beat.wav').exists():
                # Proceed with merging the binaural beat with the video
                input_video = ffmpeg.input(self.video_name)
                input_audio = ffmpeg.input('binaural_beat.wav')
                # Extract the original audio from the video
                original_audio = input_video.audio
                # Mix the original audio with the binaural beats
                mixed_audio = ffmpeg.filter([original_audio, input_audio], 'amix', inputs=2)
                # Combine the mixed audio with the video stream
                output = ffmpeg.output(input_video.video, mixed_audio, 'output.mp4')
                output.run()
                print("Binaural beats mixed with video successfully.")
            else:
                print("File 'binaural_beat.wav' does not exist. Please generate the binaural beat file first.")
                raise SystemExit()
        except ffmpeg.Error as e:
            print(f"An error occurred while mixing binaural beats with the video file: {e}")
            return None
