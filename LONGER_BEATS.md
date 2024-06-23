To create a 30-minute binaural beats production that transitions from beta frequency to deep theta frequency and then back to beta frequency, you'll need to design a script that generates and modulates these frequencies over the specified time frame. Additionally, you'll need to handle the merging of the audio with an MP4 video file.

Given the provided files, I'll outline a plan and provide an updated version of the script to achieve your goals:

1. **Generate Binaural Beats**: Generate binaural beats that transition as specified.
2. **Merge Audio with Video**: Merge the generated audio with an MP4 video file.

Let's break down the tasks:

### Task 1: Generate Binaural Beats

We'll use the `BinauralBeatGenerator.py` and `BinauralBeatMixer.py` scripts to create and modulate the binaural beats. Here's a script that modifies your existing code to create the desired transitions.

#### Updated `BinauralBeatGenerator.py`:
```python
import numpy as np
from scipy.io.wavfile import write

def generate_tone(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * frequency * t)

def generate_binaural_beat(base_freq, beat_freq, duration, sample_rate=44100):
    left_tone = generate_tone(base_freq, duration, sample_rate)
    right_tone = generate_tone(base_freq + beat_freq, duration, sample_rate)
    return np.vstack((left_tone, right_tone)).T

def create_binaural_transition(start_freq, end_freq, duration, sample_rate=44100):
    transition_duration = duration // 2
    frequencies = np.linspace(start_freq, end_freq, transition_duration * sample_rate)
    left_channel = np.sin(2 * np.pi * frequencies * np.arange(transition_duration * sample_rate) / sample_rate)
    right_channel = np.sin(2 * np.pi * (frequencies + 0.1) * np.arange(transition_duration * sample_rate) / sample_rate)
    return np.vstack((left_channel, right_channel)).T

def generate_binaural_beats_production(output_file, sample_rate=44100):
    beta_freq = 20  # Beta frequency around 20 Hz
    theta_freq = 4   # Theta frequency around 4 Hz
    
    total_duration = 30 * 60  # 30 minutes
    transition_duration = total_duration // 6  # 5 minutes for each transition

    # Generate the start in beta frequency
    start_beats = generate_binaural_beat(200, beta_freq, transition_duration, sample_rate)
    
    # Transition from beta to theta
    transition_down = create_binaural_transition(beta_freq, theta_freq, transition_duration, sample_rate)
    
    # Main part in deep theta frequency
    theta_beats = generate_binaural_beat(200, theta_freq, total_duration - 2 * transition_duration, sample_rate)
    
    # Transition from theta to beta
    transition_up = create_binaural_transition(theta_freq, beta_freq, transition_duration, sample_rate)
    
    # Combine all parts
    full_beat = np.concatenate((start_beats, transition_down, theta_beats, transition_up))
    
    # Write to file
    write(output_file, sample_rate, (full_beat * 32767).astype(np.int16))

if __name__ == "__main__":
    output_file = "binaural_beats.wav"
    generate_binaural_beats_production(output_file)
```

### Task 2: Merge Audio with Video

Next, we need to merge the generated binaural beats audio with an MP4 video file. We can use `ffmpeg` for this task. We'll modify the `main.py` to handle this step.

#### Updated `main.py`:
```python
import subprocess
import os

def merge_audio_video(audio_file, video_file, output_file):
    command = [
        'ffmpeg',
        '-i', video_file,
        '-i', audio_file,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-strict', 'experimental',
        output_file
    ]
    subprocess.run(command, check=True)

if __name__ == "__main__":
    audio_file = "binaural_beats.wav"
    video_file = "input_video.mp4"  # Replace with your video file path
    output_file = "final_output.mp4"
    
    # Ensure audio file is generated first
    if not os.path.exists(audio_file):
        print(f"Error: Audio file {audio_file} does not exist.")
    elif not os.path.exists(video_file):
        print(f"Error: Video file {video_file} does not exist.")
    else:
        merge_audio_video(audio_file, video_file, output_file)
        print(f"Successfully merged audio and video into {output_file}.")
```

### How to Run

1. **Generate Binaural Beats**: Run `BinauralBeatGenerator.py` to generate the `binaural_beats.wav` file.
   ```sh
   python BinauralBeatGenerator.py
   ```

2. **Merge Audio with Video**: Run `main.py` to merge the generated audio with your video file.
   ```sh
   python main.py
   ```

Ensure you have `ffmpeg` installed on your system to handle the audio-video merging. You can install it via most package managers or download it from the [official site](https://ffmpeg.org/download.html).

Feel free to ask if you need any more help or modifications!
