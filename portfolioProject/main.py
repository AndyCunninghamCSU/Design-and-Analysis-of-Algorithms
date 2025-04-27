# Main.py

# Andrew Cunningham
# CSC506 Portfolio Project

# Implements DTW and backtracking to predict failure criteria on
# simulated healthy and faulted core ex-core neutron flux

from signal_generation import generate_signal, apply_FFT
from plot_data import plot_healthy_faulted
from dtw import dtw
from backtracking import backtrack
show_plots = True

import numpy as np


# Parameters for a healthy core
freqs = [8, 15, 26]  # Hz
amplitudes = [1 for _ in freqs] # all the aplitudes are 1 for healthy core
sample_rate = 1000          # Hz
duration = 1.0              # Second

# Generate healthy signal
signal_healthy, t_healthy = generate_signal(freqs, amplitudes, sample_rate, duration)

# Parameters for faulted core

freqs_faulted = freqs
freqs_faulted.append(250)
amplitudes_faulted = [1, 1, 5, 10]

# generate faulted signal
signal_faulted, t_faulted = generate_signal(freqs_faulted, amplitudes_faulted, sample_rate, duration)

# Apply FFT
freqs_healthy_FFT, mag_healthy_FFT = apply_FFT(signal_healthy, sample_rate)
freqs_faulted_FFT, mag_faulted_FFT = apply_FFT(signal_faulted, sample_rate)

# Apply DTW
dtw_matrix = dtw(mag_healthy_FFT, mag_faulted_FFT)

# Apply Backtracking
optimal_path = backtrack(dtw_matrix)

if show_plots:
    plot_healthy_faulted(t_healthy, signal_healthy, freqs_healthy_FFT, mag_healthy_FFT,
                         t_faulted, signal_faulted, freqs_faulted_FFT, mag_faulted_FFT,
                         dtw_matrix, optimal_path)

