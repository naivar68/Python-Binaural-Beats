# Binaural Beat Generator and Mixer

This project is a Binaural Beat Generator and Mixer that creates binaural beats and mixes them with a video file. The resulting output is a video file with the generated binaural beats as audio.

## Features

- Generate binaural beats with customizable frequencies for the left and right ears.
- Mix the generated binaural beats with an existing video file.
- Output the final video with the mixed audio.

## Requirements

- Python 3.6+
- `ffmpeg` installed and accessible via the command line
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/BinauralBeatGenerator.git
    cd BinauralBeatGenerator
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure `ffmpeg` is installed and accessible from the command line. You can check this by running:
    ```bash
    ffmpeg -version
    ```
   If `ffmpeg` is not installed, you can download and install it from [FFmpeg.org](https://ffmpeg.org/download.html).

## Usage

1. Place the video file you want to mix the binaural beats with in the same directory as the script.
2. Run the main script:
    ```bash
    python main.py
    ```

3. Follow the prompts to input the necessary parameters:
    - Sample rate (e.g., `44100` for CD-quality audio)
    - Duration of the binaural beats (in seconds)
    - Frequency for the left ear (in Hz)
    - Frequency for the right ear (in Hz)
    - Name of the video file (including the file extension, e.g., `video.mp4`)

4. The script will generate the binaural beats and mix them with the provided video file, producing an output file named `output.mp4`.

## Project Structure

- `main.py`: The main script that orchestrates the process.
- `BinauralBeatGenerator.py`: Contains the `BinauralBeatGenerator` class responsible for generating the binaural beats.
- `BinauralBeatMixer.py`: Contains the `BinauralBeatMixer` class responsible for mixing the binaural beats with the video.
- `variables.py`: Contains the `Variables` class for handling user inputs and configurations.

## Example

Here is an example of how to use the script:

```bash
$ python main.py
