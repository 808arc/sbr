import asyncio
import librosa
#from IPython.display import Audio
import scipy.io

voice, sr=librosa. load ('/tracks/*.mp3')
sr 
#display(Audio(voice, rate=sr))

#display Audio(voice, rate=20000))

scipy. io.wavfile.write ('sbr_tracks/*.mp3', rate=20000, data=voice)