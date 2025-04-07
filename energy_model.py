def calculate_energy(burst_time, frequency):
    freq_map = {'low': 1, 'medium': 2, 'high': 3}
    f = freq_map.get(frequency, 1)
    return burst_time * f