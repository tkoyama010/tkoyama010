import pyaudio
import numpy as np

RATE = 44100

BPM = 100
L1 = (60 / BPM * 4)
L2,L4,L8 = (L1/2,L1/4,L1/8)

C,D,E,F,G,A,B,C2 = (
        261.626, 293.665, 329.628, 
        349.228, 391.995, 440.000,
        493.883, 523.251)

def tone(freq, length, gain):
    slen = int(length * RATE)
    t = float(freq) * np.pi * 2 / RATE
    return np.sin(np.arange(slen) * t) * gain

def play_wave(stream, samples):
    stream.write(samples.astype(np.float32).tostring())


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=RATE,
                frames_per_buffer=1024,
                output=True)

play_wave(stream, tone(C, L4, 1.0)) 
play_wave(stream, tone(D, L4, 1.0)) 
play_wave(stream, tone(E, L4, 1.0)) 
play_wave(stream, tone(F, L4, 1.0)) 
play_wave(stream, tone(E, L4, 1.0)) 
play_wave(stream, tone(D, L4, 1.0)) 
play_wave(stream, tone(C, L2, 1.0)) 
play_wave(stream, tone(E, L4, 1.0)) 
play_wave(stream, tone(F, L4, 1.0)) 
play_wave(stream, tone(G, L4, 1.0)) 
play_wave(stream, tone(A, L4, 1.0)) 
play_wave(stream, tone(G, L4, 1.0)) 
play_wave(stream, tone(F, L4, 1.0)) 
play_wave(stream, tone(E, L4, 1.0)) 
play_wave(stream, tone(C, L8, 1.0)) 
play_wave(stream, tone(C, L8, 0.0)) 
play_wave(stream, tone(C, L8, 1.0)) 
play_wave(stream, tone(C, L8, 0.0)) 
play_wave(stream, tone(C, L8, 1.0)) 
play_wave(stream, tone(C, L8, 0.0)) 
play_wave(stream, tone(C, L8, 1.0)) 
play_wave(stream, tone(C, L8, 0.0)) 
play_wave(stream, tone(C, L8, 1.0)) 
play_wave(stream, tone(C, L8, 1.0)) 
play_wave(stream, tone(D, L8, 1.0)) 
play_wave(stream, tone(D, L8, 1.0)) 
play_wave(stream, tone(E, L8, 1.0)) 
play_wave(stream, tone(E, L8, 1.0)) 
play_wave(stream, tone(F, L8, 1.0)) 
play_wave(stream, tone(F, L8, 1.0)) 
play_wave(stream, tone(E, L4, 1.0)) 
play_wave(stream, tone(D, L4, 1.0)) 
play_wave(stream, tone(C, L4, 1.0)) 
stream.close()
