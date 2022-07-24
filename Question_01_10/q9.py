import matplotlib.pyplot as plt
import numpy as np
import cv2
import math
from scipy.ndimage import convolve, correlate, gaussian_filter


def my_convolve(img: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    H, W, C = img.shape
    k = kernel.shape[0]

    pad = k // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float64)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float64)
    tmp = out.copy()

    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y, pad + x, c] = np.mean(tmp[y: y + k, x: x + k, c])

    out = np.clip(out, 0, 255)
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)
    return out


def median_kernel(k_size):
    return np.ones((k_size, k_size)) / (k_size ** 2)


def main():
    img = plt.imread('imori_noise.jpg')
    kernel = median_kernel(3)
    test = cv2.filter2D(img, kernel=kernel, ddepth=-1)

    out = my_convolve(img, kernel)
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    ax2.set_title('correct')
    ax1.set_title('mine')
    ax2.imshow(test)
    ax1.imshow(out)
    plt.show()


if __name__ == '__main__':
    main()
