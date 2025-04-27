# plot_data.py

# Andrew Cunningham
# CSC506 Portfolio Project

# contains all of the plotting functions to visualize data

import matplotlib.pyplot as plt

def plot_healthy_faulted(t_healthy, signal_healthy, freqs_healthy_FFT, mag_healthy_FFT,
                         t_faulted, signal_faulted, freqs_faulted_FFT, mag_faulted_FFT,
                         dtw_matrix, optimal_path):
    # Plot in 2x3 grid: 
    # Healthy (top left), Healthy FFT (middle left), DTW Heatmap (bottom left)
    # Faulted (top right), Faulted FFT (bottom right), optim

    plt.figure(figsize=(12, 9))

    # Top left - Healthy signal
    plt.subplot(3, 2, 1)
    plt.plot(t_healthy, signal_healthy)
    plt.title("Healthy Core Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Flux")
    plt.grid(True)

    # Middle left - Healthy FFT
    plt.subplot(3, 2, 3)
    plt.plot(freqs_healthy_FFT, mag_healthy_FFT)
    plt.title("Healthy FFT")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)

    # Bottom left - DTW Heatmap with Optimal Path
    plt.subplot(3, 2, 5)
    plt.imshow(dtw_matrix[1:, 1:])
    i_vals, j_vals = zip(*optimal_path)
    plt.plot(j_vals, i_vals, color='white', linewidth=1.5, label='Warping Path')
    plt.colorbar(label='Cumulative Cost')
    plt.title("DTW Cost Matrix with Warping Path")
    plt.xlabel("Faulted FFT Index")
    plt.ylabel("Healthy FFT Index")
    plt.legend()

    # Top right - Faulted signal
    plt.subplot(3, 2, 2)
    plt.plot(t_faulted, signal_faulted)
    plt.title("Faulted Core Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Flux")
    plt.grid(True)

    # Bottom right - Faulted FFT
    plt.subplot(3, 2, 4)
    plt.plot(freqs_faulted_FFT, mag_faulted_FFT)
    plt.title("Faulted FFT")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)

    plt.tight_layout()
    plt.show()