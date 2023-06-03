import numpy as np
def samplePoints(count, d):
    points = np.random.uniform(-1, 1, (count, d))
    radii = np.sqrt(np.sum(points * points, axis = 1, keepdims = True))
    inner = points[radii[:, 0] <= 1]
    outer = points[radii[:, 0] > 0]
    return inner, outer

ratio_sample_size = 10**5

def volumeRatio(d):
    inner, outer = samplePoints(ratio_sample_size, d)
    return inner.shape[0] / ratio_sample_size

dims = np.arange(1, 50)
ratios = np.vectorize(volumeRatio)(dims)

import matplotlib.pyplot as plt
plt.plot(dims, ratios)