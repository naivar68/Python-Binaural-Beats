# main.py
from BinauralBeatGenerator import BinauralBeatGenerator
from BinauralBeatMixer import BinauralBeatMixer
from variables import Variables
import subprocess as sp
import ffmpeg
import os
import sys

def main():

    sp.run("python testing.py", shell=True)
    sp.run("cls" if os.name == "nt" else "clear", shell=True)
    print('''
          Binaural Beat Generator
          -----------------------
          This is a Binaural Beat Generator and MIXER to take the beats and mix them with a video file.
          You need to install the requirements in requirements.txt, FFMPEG if not installed
          and also name the MP4 file you want to mix the beats with. Please ensure the video file is in the same directory as this program.
          The video file must be an MP4 file. The video file must be named with the extension.

          ''')
    # Check if ffmpeg is installed
    if not sp.run(["ffmpeg", "-version"], stdout=sp.DEVNULL, stderr=sp.STDOUT).returncode == 0:
        print("ffmpeg is not installed or not accessible.")
        raise SystemExit()

    start = input("Press Enter to start the process.")
    if start == "":
        sp.run("cls" if os.name == "nt" else "clear", shell=True)
        variables = Variables()
        variables.name_video()
        variables.interface()

    else:
        raise SystemExit()

    # Create an instance of BinauralBeatGenerator and call the methods
    print()
    query = input("Would you like to generate binaural beats? (y/n): ")
    result = None
    if query == "y":
        binaural_beat_generator = BinauralBeatGenerator(variables)
        result = binaural_beat_generator.binaural_beats(variables)
    if result is None:
        print("Error generating binaural beats.")
        sys.exit()
    else:
        print("Binaural beats successfully generated.")
        print("Ready to mix the binaural beats with the video file.")
        print("The output file is named binaural_beat.wav.")

    # Create an instance of BinauralBeatMixer and call the methods
    query = input("Would you like to mix the binaural beats with the video file? (y/n): ")
    result = None
    if query == "y":
        binaural_beat_mixer = BinauralBeatMixer(variables)
        result = binaural_beat_mixer.binauralmixer(variables)
    if result is None:
        print("Error mixing binaural beats.")
        sys.exit()
    else:
        print("Binaural beats successfully mixed.")
        print("Ready to mix the binaural beats with the video file.")
        print("The output file is named output.wav.")
        print("Thank you for using the Binaural Beat Generator and Mixer.")
        print("Goodbye!")
        sys.exit()

if __name__ == "__main__":
    main()