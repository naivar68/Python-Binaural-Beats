from variables import Variables
import ffmpeg
from pathlib import Path
import os


class BinauralBeatGenerator:
    def __init__(self, variables):
        self.duration = variables.duration
        self.frequency_left = variables.frequency_left
        self.frequency_right = variables.frequency_right
        self.sample_rate = variables.sample_rate
        self.volume = variables.volume
        self.frequency_transition = variables.frequency_transition
        self.ffmpeg_path = 'ffmpeg'
        self.video_name = variables.video_name

    def generate_tone(self, frequency, duration, output_file):
        try:
            ffmpeg.input('anullsrc=r=44100:cl=mono', f='lavfi').output(output_file, filter_complex=f'sine=frequency={frequency}:duration={duration}', ar=self.sample_rate).run()
            print(f"Tone generated for {output_file}.")
        except ffmpeg.Error as e:
            print(f"An error occurred while generating tone for {output_file}: {e}")
            return None

    def concatenate_segments(self, segments, output_file):
        try:
            inputs = [ffmpeg.input(segment) for segment in segments]
            ffmpeg.concat(*inputs, v=0, a=1).output(output_file).run()
            print(f"Segments concatenated into {output_file}.")
        except ffmpeg.Error as e:
            print(f"An error occurred while concatenating segments: {e}")
            return None

    def binaural_beats(self):
        left_segments = []
        right_segments = []

        if self.frequency_transition:
            step_duration = self.duration / len(self.frequency_transition["left"])
            for i, freq in enumerate(self.frequency_transition["left"]):
                segment_file = f"left_{i}.wav"
                self.generate_tone(freq, step_duration, segment_file)
                left_segments.append(segment_file)

            for i, freq in enumerate(self.frequency_transition["right"]):
                segment_file = f"right_{i}.wav"
                self.generate_tone(freq, step_duration, segment_file)
                right_segments.append(segment_file)

            self.concatenate_segments(left_segments, 'left.wav')
            self.concatenate_segments(right_segments, 'right.wav')
        else:
            self.generate_tone(self.frequency_left, self.duration, 'left.wav')
            self.generate_tone(self.frequency_right, self.duration, 'right.wav')

        try:
            input1 = ffmpeg.input('left.wav')
            input2 = ffmpeg.input('right.wav')
            combined = ffmpeg.filter([input1, input2], 'amerge', inputs=2)
            if self.volume:
                combined = combined.filter('volume', volume=self.volume)
            combined.output('binaural_beat.wav', ac=2).run()
            print("Binaural beat stereo mixdown created.")
        except ffmpeg.Error as e:
            print(f"An error occurred while creating the stereo mixdown: {e}")
            return None

        return "Binaural beats generated successfully"

    @staticmethod
    def clean_temp_files():
        try:
            temp_files = [f for f in os.path('.') if f.startswith('left_') or f.startswith('right_') or f in ['left.wav', 'right.wav']]
            for temp_file in temp_files:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            print("Temporary files cleaned up.")
        except Exception as e:
            print(f"An error occurred while cleaning up temporary files: {e}")

