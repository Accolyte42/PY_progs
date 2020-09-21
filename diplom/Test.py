import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import xlwt

import librosa as lr

data_dir = "./Ado/set_a"
audio_file = glob(data_dir + '/*.wav')
print(len(audio_file))

# sfreq - это частота дискретизации. 22050 Гц
# audio - это sampling rate или что-то типа массива всех Дб
# .load - это получение массива дискретных точек
# time - это время))
audio, sfreq = lr.load(audio_file[8])
time = np.arange(0, len(audio)) / sfreq
print(time)
print(sfreq)

fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='Time(s)', ylabel='Sound Amplitude')
plt.show()
print(type(time), type(audio))

time1 = []
audio1 = []
for i in range(len(audio)):
    time1.append(float(time[i]))
    audio1.append(float(audio[i]))
print(len(audio), type(time1), type(audio1))

Signal_book = xlwt.Workbook()
sheet1 = Signal_book.add_sheet("Sheet_1")
sheet1.write(0, 0, time1[0])
sheet1.write(0, 1, audio1[0])

Signal_book.save("Signal_Table.xls")




