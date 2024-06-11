import subprocess

def is_ffmpeg_installed():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        return True
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    if is_ffmpeg_installed():
        print("ffmpeg is installed and accessible.")
    else:
        print("ffmpeg is not installed or not accessible.")

