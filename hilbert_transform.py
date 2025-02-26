import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import hilbert

# Load the audio file
file_path = "sample_music.wav"   # Replace with your .wav file path
sample_rate, audio_signal = wavfile.read(file_path)

# Normalize the audio signal
if audio_signal.ndim > 1:  # If stereo, take one channel
    audio_signal = audio_signal[:, 0]
audio_signal = audio_signal / np.max(np.abs(audio_signal))  # Normalize

# Apply the Hilbert Transform
analytic_signal = hilbert(audio_signal)
envelope = np.abs(analytic_signal)  # Calculate instantaneous amplitude
instantaneous_phase = np.angle(analytic_signal)  # Calculate Instantaneous phase angle

# Generate binary data based on amplitude change sign
with open("binary_output1", "w") as f:
    signal = np.real(analytic_signal) # Analyze real and imaginary parts of analytical_signal for better randomness
    for n in range(0,len(signal)-1):
        if signal[n] < signal [n+1]:
            f.write("1")
        elif signal[n] > signal [n+1]:
            f.write("0")

with open("binary_output2", "w") as f:
    signal = np.imag(analytic_signal) # Analyze real and imaginary parts of analytical_signal for better randomness
    for n in range(0,len(signal)-1):
        if signal[n] < signal [n+1]:
            f.write("1")
        elif signal[n] > signal [n+1]:
            f.write("0")

with open("binary_output3", "w") as f:
    signal = instantaneous_phase
    for n in range(0,len(signal)-1):
        if signal[n] < signal [n+1]:
            f.write("1")
        elif signal[n] > signal [n+1]:
            f.write("0")



# Plot the results (Optional)
time = np.arange(0, len(audio_signal)) / sample_rate  # Time vector
plt.figure(figsize=(12, 10))

# Original signal
plt.subplot(4, 1, 1)
plt.plot(time, audio_signal, label="Original Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original Audio Signal")
plt.grid()
plt.legend()

# Analytic signal (real and imaginary parts)
plt.subplot(4, 1, 2)
plt.plot(time, np.real(analytic_signal), label="Real Part (Original Signal)")
plt.plot(time, np.imag(analytic_signal), label="Imaginary Part (Hilbert Transform)", linestyle='dashed')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Analytic Signal (Real and Imaginary Parts)")
plt.grid()
plt.legend()

# Envelope (Instantaneous Amplitude)
plt.subplot(4, 1, 3)
plt.plot(time, envelope, label="Envelope (Instantaneous Amplitude)", color='orange')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Envelope of the Audio Signal")
plt.grid()
plt.legend()

# Instantaneous phase angle
plt.subplot(4, 1, 4)
plt.plot(time, instantaneous_phase, label="Instantaneous Phase", color='green')
plt.xlabel("Time (s)")
plt.ylabel("Phase (radians)")
plt.title("Instantaneous Phase of the Audio Signal")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
