import numpy as np
from scipy.io.wavfile import write
import time
from variables import Variables



class BinauralBeatGenerator:
    def __init__(self, variables):
        self.sample_rate = variables.sample_rate
        self.duration = variables.duration
        self.frequency_left = variables.frequency_left
        self.frequency_right = variables.frequency_right
        self.video_name = variables.video_name

    def binaural_beats(self):
        # Generate time points
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)

        # Generate sine wave tones
        tone_left = np.sin(2 * np.pi * self.frequency_left * t)
        tone_right = np.sin(2 * np.pi * self.frequency_right * t)

        # Combine into a stereo signal
        stereo_tone = np.vstack((tone_left, tone_right)).T

        # Convert to 16-bit data
        stereo_tone = np.int16(stereo_tone * 32767)

        # Write to a WAV file
        write("binaural_beat.wav", self.sample_rate, stereo_tone)

        time.sleep(5)

        return 'binaural_beat.wav successfully generated.'
