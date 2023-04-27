import asyncio
import librosa
#from IPython.display import Audio
import scipy.io

voice, sr=librosa. load ('tracks/_crazy bounce 142 bpm prod shadoww x @808 arc.mp3')
sr 
#display(Audio(voice, rate=sr))

#display Audio(voice, rate=20000))

scipy. io.wavfile.write ('sbr_tracks/*.mp3', rate=20000, data=voice)