import wave
import struct
import numpy as np
import matplotlib.pyplot as plt	

sound_file = wave.open('Audio_1.wav', 'r') 
file_length = sound_file.getnframes()
print file_length
sound = np.zeros(file_length)
#print sound
for i in range(file_length):
    data = sound_file.readframes(1)
    data = struct.unpack("<h", data)
    sound[i] = int(data[0])
sound = np.divide(sound, float(2**15))
print sound
Ap = np.pad(sound, (0,int(np.ceil(len(sound) / 11874.)) * 11874 - len(sound)), 'constant', constant_values=0)
Apr = Ap.reshape((len(Ap) // 11874, 11874))
print Apr
Apr.shape
print Apr.shape
array1=(Apr ** 2).sum(axis=1)
print array1
#print len(array1)
threshold =4700
result= np.array(filter(lambda x: x>= threshold, array1))
print result 

print len(result)
print np.where(array1>4700)
#print array1.shape
#print result.shape
#print sound.shape
#print Apr.shape
#fftoutput=np.fft.fft(result)
#print fftoutput
#print np.argsort(fftoutput)
