import subprocess as sp
import os
import ffmpeg
import sys
from variables import Variables

class BinauralBeatMixer:
    def __init__(self, variables):
        self.variables = Variables()
        self.duration = variables.duration
        self.frequency_left = variables.frequency_left
        self.frequency_right = variables.frequency_right
        self.sample_rate = variables.sample_rate
        self.ffmpeg_path = variables.ffmpeg_path  # Use ffmpeg_path from variables

    def binauralmixer(self):
        # Generate left tone
        try:
            sp.run("cls" if os.name == "nt" else "clear", shell=True)
            print("Mixing binaural beats with the video file.")

            command = f'{self.ffmpeg_path} -y -f lavfi -i "sine=frequency={self.variables.frequency_left}:duration={self.variables.duration}" left.wav'
            print(f"Running command: {command}")
            result = sp.run(command, shell=True, capture_output=True)
            if result.returncode != 0:
                print(f"Error running command: {result.stderr.decode()}")
                return None

            # Generate right tone
            command = f'{self.ffmpeg_path} -y -f lavfi -i "sine=frequency={self.variables.frequency_right}:duration={self.variables.duration}" right.wav'
            print(f"Running command: {command}")
            result = sp.run(command, shell=True, capture_output=True)
            if result.returncode != 0:
                print(f"Error running command: {result.stderr.decode()}")
                return None

            # Merge into stereo file
            output_file_path = os.path.join(os.getcwd(), "output.wav")
            command = f'{self.ffmpeg_path} -y -i left.wav -i right.wav -filter_complex "[0:a][1:a]amerge=inputs=2[a]" -map "[a]" {output_file_path}'
            print(f"Running command: {command}")
            result = sp.run(command, shell=True, capture_output=True)
            if result.returncode != 0:
                print(f"Error running command: {result.stderr.decode()}")
                return None

            else:
                # Remove temporary files
                os.remove('left.wav')
                os.remove('right.wav')
                print(f"Binaural beats successfully mixed with the video file. The output file is named {output_file_path}.")
                return output_file_path

        except Exception as e:
            print(f"An error occurred: {e}")
            return None