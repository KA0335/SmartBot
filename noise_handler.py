# import matplotlib.pyplot as mplt
# from scipy.io import wavfile
import numpy as np
from scipy.io import wavfile
import soundfile as sf
from numpy import  mean
import speech_recognition as sr


import sounddevice as sd
import soundfile as sf
import time as t


n=0
while n==0:
    samplerate = 44100  # Hertz
    duration = 10  # seconds
    filename = 'noise.wav'

    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                    channels=1, blocking=True)
    sf.write(filename, mydata, samplerate)

    wav_loc = "noise.wav"
    f = sf.SoundFile('noise.wav')
    print('samples = {}'.format(len(f)))
    print('sample rate = {}'.format(f.samplerate))
    print('seconds = {}'.format(len(f) / f.samplerate))
    rate, data = wavfile.read(wav_loc)
    data = data
    threshold=10000
    count=0
    data=np.sort(data)
    data=data.tolist()
    average_of_peaks=mean(data)
    i=0
    while data[i]<0:
        data[i]=data[i]*-1
        i=i+1

    data.sort(reverse=True)
    i=0
    mod_highest=data[0]
    for i in range(50):   
        if data[i]>threshold:
            count=count+1

    if count>25:
        print('Noisy Background')
        n=0
        print('Retesting in 10 seconds')
        t.sleep(10)# Please set this value accordingly. Its the interval between next background noise testing
        
    else:
        print('We can take care of the noise')
        n=1
        
    
print('samples = {}'.format(len(f)))
print('seconds = {}'.format(len(f) / f.samplerate))
print('average peak = {}'.format(average_of_peaks))
print('highest value= {}'.format(mod_highest))


import IPython
from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf
from noisereduce.generate_noise import band_limited_noise
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import io
%matplotlib inline

samplerate = 44100  # Hertz
duration = 125
# seconds
filename = 'audio.wav'

mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                channels=1, blocking=True)
sf.write(filename, mydata, samplerate)


wav_loc = "audio.wav"
rate, data = wavfile.read(wav_loc)
data = data


IPython.display.Audio(data=data, rate=rate)

fig, ax = plt.subplots(figsize=(20,3))
ax.plot(data)

noise_len = 10 # seconds
noise = "noise.wav"
nrate, ndata= wavfile.read(noise)

fig, ax = plt.subplots(figsize=(20,3))
ax.plot(ndata)

IPython.display.Audio(data=ndata, rate=rate)

noise_reduced = nr.reduce_noise(audio_clip=data.astype('float64'),
                                noise_clip=ndata.astype('float64'),
                                prop_decrease=1.0,
                                n_std_thresh=1.25,
                                verbose=False)
								
IPython.display.Audio(data=noise_reduced, rate=nrate)

fig, ax = plt.subplots(figsize=(20,3))
ax.plot(noise_reduced)

IPython.display.Audio(data=noise_reduced, rate=rate)

f=f = sf.SoundFile('audio.wav')
print('samples = {}'.format(len(f)))
print('seconds = {}'.format(len(f) / f.samplerate))
print('average peak = {}'.format(average_of_peaks))
print('highest value= {}'.format(mod_highest))


r = sr.Recognizer()

with sr.AudioFile('audio.wav') as source:
    
    audio_text = r.listen(source)
    
    try:
        
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
     
    except:
         print('Sorry.. run again...')