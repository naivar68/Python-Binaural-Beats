import numpy as np
from scipy.io.wavfile import write
from moviepy.editor import *
from variables import Variables

variables = Variables()


class BinauralBeatMixer:
    def __init__(self, variables):
        self.sample_rate = variables.sample_rate
        self.duration = variables.duration
        self.frequency_left = variables.frequency_left
        self.frequency_right = variables.frequency_right
        self.Video = variables.video_name



    def binauralmixer(self):

        # Generate time points
        t = np.linspace(0, self.variables.duration, int(self.variables.sample_rate * self.variables.duration), endpoint=False)
        # Generate sine wave tones
        tone_left = np.sin(2 * np.pi * self.variables.frequency_left * t)
        tone_right = np.sin(2 * np.pi * self.variables.frequency_right * t)

        # Combine into a stereo signal
        stereo_tone = np.vstack((tone_left, tone_right)).T

        # Convert to 16-bit data
        stereo_tone = np.int16(stereo_tone * 32767)

        # Mix the audio data
        mixed = tone_left + tone_right

        # Write the mixed audio back to a temporary WAV file
        write("temp_mixed.wav", self.variables.sample_rate, mixed.astype(np.int16))


        # Combine the mixed audio with the original video (without audio)
        final_clip = VideoFileClip(self.Video).set_audio(AudioFileClip("temp_mixed.wav"))

        # Save the final video with the binaural beat added to the background music
        final_clip.write_videofile("final_output.mp4")

        return "final_output.mp4"