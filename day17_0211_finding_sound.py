import winsound
import time

""" Parameter of winsound.Beep(frequency, duration) """

def test_play_sound():
    for n in range(37, 21000, 10):
        winsound.Beep(n, 200)
# test_play_sound()

def teen_bell():
    for n in range(50, 21000, 500):
        print('Frequency : {}\n'.format(n))
        winsound.Beep(n, 1000)
# teen_bell()

scales = {'C':(65.406, 130.81, 261.63, 523.25, 1046.5, 2093.0),
         'C#':(69.296, 138.59, 277.18, 554.37, 1108.7, 2217.5),
         'D':(73.416, 146.83, 293.67, 587.33, 1174.7, 2349.3),
         'D#':(77.782, 155.56, 311.13, 622.25, 1244.5, 2489.0),
         'E':(82.407, 164.81, 329.63, 659.26, 1318.5, 2637.0),
         'F':(87.307, 174.61, 349.23, 698.46, 1396.9, 2793.0),
         'F#':(92.499, 185.00, 369.99, 739.99, 1480.0, 2960.0),
         'G':(97.999, 196.00, 392.00, 783.99, 1568.0, 3136.0),
         'G#':(103.83, 207.65, 415.30, 830.61, 1661.2, 3322.4),
         'A':(110.00, 220.00, 440.00, 880.00, 1760.00, 3520.0),
         'A#':(116.54, 233.08, 466.16, 932.33, 1864.7, 3729.3),
         'B':(123.47, 246.94, 493.88, 987.77, 1975.5, 3951.1),
         '-':(32700)}

def play_sound(scale, octave, time, tempo):
    winsound.Beep(int(scales[scale][octave-1]), time*tempo)

def set_tempo():
    return int(input('speed = '))

def input_notes():
    return input('notes : ').split(' ')
tempo = set_tempo()
input_notes()
play_notes()
