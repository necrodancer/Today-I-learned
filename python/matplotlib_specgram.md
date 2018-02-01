# Pyplot specgram
  Specgram is a image that have time axis and frequency axis. For each time interval, Short Time Fourier Transform(STFT) is done for a time-series 1d signal. So in the image, frequency spectrum bars that are the result of each STFT are aligned with time-series. It is useful to analyze sequential data-sound,EEG,EKG, ...- as an image.<br>
  Pyplot(from matplotlib) library provides a method to make specgram for 1d signal data. Here are the document and example code.<br>
Following code was referred to the example code of specgram.
<br> **[The document of specgram](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.specgram.html)
<br> [The example code of specgram](https://matplotlib.org/examples/pylab_examples/specgram_demo.html)**
# Example code
```python
# x is 1d array signal
# Fs is sampling rate of the signal
# NFFT is the integer number, and proportional to power of 2, confirms the size of FFT or STFT.
# noverlap is the integer number that asks how many samples to overlap in doing next FFT.

# Pxx is the segments x freqs array of instantaneous power, freqs is
# the frequency vector, bins are the centers of the time bins in which
# the power is computed, and im is the matplotlib.image.AxesImage
# instance

Pxx, freqs, bins, im = plt.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
```
