import os
import subprocess


def ffmpeg_encode(folderpath, dirname):
    os.chdir(folderpath)
    try:
        subprocess.call(['ffmpeg', '-i', f'{dirname}.mp4', '-c:v', 'libx264', '-b:v', '3M',
                        '-threads', '1', '-preset', 'superfast', f'f_{dirname}.mp4'])
        os.remove(os.path.join(folderpath, f'{dirname}.mp4'))
        print(f"Encoded {dirname}")
    except:
        print(f"Fail to encode {dirname}")
