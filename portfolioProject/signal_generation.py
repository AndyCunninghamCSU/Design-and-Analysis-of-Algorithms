# signal_generation.py

# Andrew Cunningham
# CSC506 Portfolio Milestone


# Generate sinusoidal functions to simulate nuclear reactor core ex-core neutron flux 
# Implements FFT to analyze the signal data

import numpy as np


def generate_signal(freqs, amplitudes, rate, duration, noise = 0.1):
    '''generates a simple sine wave that's translated to be above the horizontal axis
        returns the signal and time matricies'''

    # generate the baseline signal
    t = np.linspace(0, duration, int(rate * duration))
    signal = sum(a * np.sin(2 * np.pi * f * t) for f, a in zip(freqs, amplitudes))
    
    # add noise
    noise = np.random.normal(0, noise, len(t))
    signal += noise

    # shift the signal so that there is no negative flux
    signal -= np.min(signal)

    return signal, t

def apply_FFT(signals, sample_rate):
    '''applies FFT to signal and sample_rate
    returns frequency and magnitude data'''
    # Apply FFT to healthy
    signals = signals - np.mean(signals)
    fft_result = np.fft.fft(signals)
    magnitude = np.abs(fft_result) / len(signals)  # Normalize
    freqs = np.fft.fftfreq(len(signals), d=1/sample_rate)
    # Take only positive frequencies
    half_n = len(signals) // 2
    freqs = freqs[:half_n]
    # also eliminate the spike at 0
    magnitude = magnitude[:half_n]

    return freqs, magnitude


