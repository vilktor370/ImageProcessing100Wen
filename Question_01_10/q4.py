import matplotlib.pyplot as plt
import numpy as np


def calc(gray: np.ndarray, th=128) -> float:
    lower = gray[gray >= th]
    upper = gray[gray < th]

    total_pixel = gray.shape[0] * gray.shape[1]
    w0 = lower.shape[0] / total_pixel
    w1 = upper.shape[0] / total_pixel

    m0 = lower.mean() if lower.shape[0] > 0 else 0
    m1 = upper.mean() if upper.shape[0] > 0 else 0

    res = (w0 * w1 * (m0 - m1) ** 2) ** 2
    return res


def main():
    img = plt.imread('imori.jpg')
    gray = (0.2126 * img[:, :, 0] + 0.7152 * img[:, :, 1] + 0.0722 * img[:, :, 2]).astype(np.uint8)
    max_th, max_val = 0, 0
    for i in range(1, 256, 1):
        sigma = calc(gray, i)
        if sigma > max_val:
            max_th = i
            max_val = sigma

    bin = np.zeros_like(gray)
    bin[gray >= max_th] = 255
    bin[gray < max_th] = 0
    plt.imshow(bin, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
