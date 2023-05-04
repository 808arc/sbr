import librosa
import os
import scipy.io

# Get a list of all the MP3 files in the tracks directory
mp3_files = [file for file in os.listdir('tracks') if file.endswith('.mp3')]


# Loop over the MP3 files and load each one with librosa.load()
for mp3_file in mp3_files:
    file_path = os.path.join('tracks', mp3_file)
    voice, sr = librosa.load(file_path)
    print(f'{mp3_file}: {sr} Hz')
    scipy.io.wavfile.write('sbr_tracks/(SLOWED AND REVERB)' + mp3_file[:-4] + '.mp3', rate=15000, data=voice)

#voice, sr=librosa. load ('tracks/_crazy bounce 142 bpm prod shadoww x @808 arc.mp3')
#sr 




    
    