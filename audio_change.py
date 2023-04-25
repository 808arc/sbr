import librosa
from IPython.display import Audio
import scipy.io

voice, sr=librosa. load ('vocal copy.wav', sr=44100)

sr 

display (Audio (voice, rate=sr))

display Audio (voice, rate=20000))

scipy. io.wavfile.write ('coice.wav', rate=20000, data=voice)