from BinauralBeatGenerator import BinauralBeatGenerator
from BinauralBeatMixer import BinauralBeatMixer
import os
import time
from variables import Variables



def main():
    # Clear the screen and welcome the user with important information
    os.system("cls") if os.name == "nt" else os.system("clear")
    print("Welcome to the Binaural Beat Generator and Mixer!\n")
    print("You need to have an MP4 file in the same directory as this script to proceed.\n")
    print("You will need to add the file extension to the file name.\n")
    print("If the file does not exist, or is NOT an MP$ file, the program will exit.\n")
    variables = Variables()
    variables.interface()
    variables.video_name()

    time.sleep(2)




    # Generate the binaural beat
    print("Press 'Enter' to continue...")
    input()
    os.system("cls") if os.name == "nt" else os.system("clear")
    print("Generating the binaural beat...")
    time.sleep(2)
    BinauralBeatGenerator(variables).binaural_beats()
    time.sleep(2)
    print("Binaural beat successfully generated.")
    time.sleep(2)
    print("Press 'Enter' to continue...")
    input()
    os.system("cls") if os.name == "nt" else os.system("clear")

    print("Generating the background music...")
    time.sleep(2)
    BinauralBeatMixer(variables).binauralmixer()
    time.sleep(2)
    print("Background music successfully generated.")
    print("The completed file is in this directory. Please remove it if you wish to generate a new file.")
    print("Thank you for using the Binaural Beat Generator and Mixer!")
    time.sleep(2)
    exit(0)

if __name__ == "__main__":
    main()

