from BinauralBeatGenerator import BinauralBeatGenerator
from BinauralBeatMixer import BinauralBeatMixer
from variables import Variables
import subprocess as sp
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
    if sp.run(["ffmpeg", "-version"], stdout=sp.DEVNULL, stderr=sp.STDOUT).returncode != 0:
        print("ffmpeg is not installed or not accessible.")
        raise SystemExit()

    start = input("Press Enter to start the process, or press 'q' to quit: ")
    if start == "":
        sp.run("cls" if os.name == "nt" else "clear", shell=True)
        variables = Variables()
        variables.name_video()
        variables.interface()
    elif start.lower() == "q":
        print("Goodbye!")
        sys.exit()
    else:
        print("Invalid input. Please press Enter to start the process, or press 'q' to quit.")
        raise SystemExit()

    try:
        query = input("Would you like to generate binaural beats? (y/n): ")
        result = None
        if query.lower() == "y":
            binaural_beat_generator = BinauralBeatGenerator(variables)
            result = binaural_beat_generator.binaural_beats()
        if result is None:
            print("Error generating binaural beats.")
            raise SystemExit()
        else:
            print("Binaural beats successfully generated.")
            print("Ready to mix the binaural beats with the video file.")
            print("The output file is named binaural_beat.wav.")

        query = input("Would you like to mix the binaural beats with the video file? (y/n): ")
        result = None
        if query.lower() == "y":
            binaural_beat_mixer = BinauralBeatMixer(variables)
            result = binaural_beat_mixer.binaural_mixer()
        if result is None:
            print("Error mixing binaural beats.")
            raise SystemExit()
        else:
            print(f"Binaural beats successfully mixed. The output file is named {variables.output_file}.")

            # Query the user about saving to the database
            save_query = input(f"Would you like to save the {variables.output_file} file to the database? (y/n): ")
            if save_query.lower() == "y":
                binaural_beat_mixer.save_to_db(variables.output_file)
                print("The output file has been saved to the database.")
            else:
                print("The output file was not saved to the database.")

            print("Thank you for using the Binaural Beat Generator and Mixer.")
            print("Goodbye!")
            raise SystemExit()
    finally:
        # Clean up temporary files
        binaural_beat_generator.clean_temp_files()

if __name__ == "__main__":
    main()
