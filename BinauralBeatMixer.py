import subprocess as sp
from pathlib import Path
import ffmpeg
from variables import Variables
import sqlite3


class BinauralBeatMixer:
    def __init__(self, variables):
        self.duration = variables.duration
        self.frequency_left = variables.frequency_left
        self.frequency_right = variables.frequency_right
        self.sample_rate = variables.sample_rate
        self.video_name = variables.video_name
        self.output_file = variables.output_file
        self.ffmpeg_path = 'ffmpeg'
        self.db_path = 'binaural_beats.db'

    def binaural_mixer(self):
        try:
            if Path('binaural_beat.wav').exists():
                input_video = ffmpeg.input(self.video_name)
                input_audio = ffmpeg.input('binaural_beat.wav')
                original_audio = input_video.audio
                mixed_audio = ffmpeg.filter([original_audio, input_audio], 'amix', inputs=2)
                output = ffmpeg.output(input_video.video, mixed_audio, self.output_file)
                output.run()
                print(f"Binaural beats mixed with video successfully. The output file is named {self.output_file}.")
                self.save_to_db(self.output_file)
            else:
                print("File 'binaural_beat.wav' does not exist. Please generate the binaural beat file first.")
                raise SystemExit()
        except ffmpeg.Error as e:
            print(f"An error occurred while mixing binaural beats with the video file: {e}")
            return None

    def save_to_db(self, output_file):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS videos (
                    id INTEGER PRIMARY KEY,
                    filename TEXT,
                    file BLOB
                )
            ''')
            with open(output_file, 'rb') as file:
                blob = file.read()
            cursor.execute('INSERT INTO videos (filename, file) VALUES (?, ?)', (self.video_name, sqlite3.Binary(blob)))
            conn.commit()
            conn.close()
            print("Output file saved to database successfully.")

        except sqlite3.Error as e:
            print(f"An error occurred while saving the output file to the database: {e}")








